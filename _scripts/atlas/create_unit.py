#!/usr/bin/env python3
"""Create a new Unit in Atlas (course Bible 9 Foundations) and fill its 4 free-text
fields, all in the persistent watchable Chrome (:9222).

Reads the unit name from the data-model file's H1 (`# Rubicon Atlas — Unit NN: Title`)
and the field content via fill_unit's parser. Leaves dates at the placeholder default
(2026-27 week dates aren't exposed until after Aug 1, 2026) and Draft unchecked, matching
unit 01. Prints the new unit_id parsed from the resulting /unit-planner/<id> URL.

Usage:
    create_unit.py <unit_md_path> [--no-fill] [--dry-run]
"""
import re, sys, pathlib
from playwright.sync_api import sync_playwright
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from session import attach
from fill_unit import FIELDS, section_text, parse_blocks, fill_field

ANCHOR_UNIT = "2224"  # any existing unit; we click its "Add New Unit"
BASE = "https://watersprings.rubiconatlas.org"

def unit_name(md: str) -> str:
    m = re.search(r"^#\s+Rubicon Atlas — Unit\s+(.+?)\s*$", md, re.M)
    if not m:
        raise SystemExit("Could not parse unit name from H1")
    return m.group(1).strip()

def main():
    if len(sys.argv) < 2:
        print("Usage: create_unit.py <unit_md_path> [--no-fill] [--dry-run]"); sys.exit(1)
    md_path = pathlib.Path(sys.argv[1])
    no_fill = "--no-fill" in sys.argv
    dry = "--dry-run" in sys.argv
    md = md_path.read_text()
    name = unit_name(md)
    plan = {label: parse_blocks(section_text(md, n)) for label, n in FIELDS.items()}
    print(f"Unit name: {name!r}")
    for label, blocks in plan.items():
        print(f"  {label}: {len(blocks)} block(s)")
    if dry:
        print("[dry-run] not creating."); return

    with sync_playwright() as p:
        b, ctx, pg = attach(p)
        pg.bring_to_front()
        pg.goto(f"{BASE}/develop/unit-planner/{ANCHOR_UNIT}", wait_until="networkidle")
        pg.wait_for_timeout(1500)
        pg.get_by_role("button", name="Add New Unit").first.click()
        pg.wait_for_selector("#unit-form-input-name", timeout=15000)
        pg.wait_for_timeout(800)
        pg.fill("#unit-form-input-name", name)
        pg.wait_for_timeout(400)
        save = pg.locator("#unit-form-button-save")
        if save.is_disabled():
            # ensure a color is chosen (Color is required); click first swatch
            try:
                pg.locator("[id^='unit-form'] .color, .unit-color, [class*='color'] button").first.click()
            except Exception:
                pass
            pg.wait_for_timeout(400)
        if save.is_disabled():
            pg.screenshot(path=str(pathlib.Path(__file__).parent/"probe-output"/"create-blocked.png"))
            print("! Save still disabled — see probe-output/create-blocked.png"); b.close(); sys.exit(2)
        save.click()
        # wait for navigation to the new unit's planner
        pg.wait_for_url(re.compile(r"/develop/unit-planner/\d+(?!.*addUnit)"), timeout=20000)
        pg.wait_for_timeout(2500)
        m = re.search(r"/unit-planner/(\d+)", pg.url)
        uid = m.group(1) if m else "?"
        print(f"CREATED {name!r} -> unit_id={uid}  ({pg.url})")

        if not no_fill and uid != "?":
            pg.goto(f"{BASE}/develop/unit-planner/{uid}", wait_until="networkidle")
            pg.wait_for_timeout(2500)
            for label, blocks in plan.items():
                if blocks: fill_field(pg, label, blocks)
        b.close()
    print("Done." if no_fill else "Done (created + filled).")

if __name__ == "__main__":
    main()
