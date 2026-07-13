#!/usr/bin/env python3
"""Create a new Unit in Atlas and fill its 4 free-text fields, all in the persistent
watchable Chrome (:9222).

Reads the unit name from the data-model file's H1 (`# Rubicon Atlas — Unit NN: Title`)
and the field content via fill_unit's parser. Leaves dates at the placeholder default
(2026-27 week dates aren't exposed until after Aug 1, 2026) and Draft unchecked, matching
unit 01. Prints the new unit_id parsed from the resulting /unit-planner/<id> URL.

The new unit is created in the course of whatever page exposes "Add New Unit":
  --course <id>  → open that course's unit calendar (/develop/course-map/<id>/unit-calendar/year)
                   and add there. Use for the FIRST unit of a course that has none yet
                   (e.g. apologetics = 190).
  --anchor <id>  → open an existing unit's planner and add from there (default: Foundations
                   unit 2224). Works once the course already has at least one unit.

Usage:
    create_unit.py <unit_md_path> [--course <course_id> | --anchor <unit_id>] [--no-fill] [--dry-run]
"""
import re, sys, pathlib
from playwright.sync_api import sync_playwright
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from session import attach
from fill_unit import FIELDS, section_text, parse_blocks, fill_field

ANCHOR_UNIT = "2224"  # default anchor (Foundations); any existing unit exposes "Add New Unit"
BASE = "https://watersprings.rubiconatlas.org"


def opt_value(argv, name):
    """Return the value following `--name`, or None."""
    if name in argv:
        i = argv.index(name)
        if i + 1 < len(argv):
            return argv[i + 1]
        raise SystemExit(f"{name} requires a value")
    return None

def unit_name(md: str) -> str:
    m = re.search(r"^#\s+Rubicon Atlas — Unit\s+(.+?)\s*$", md, re.M)
    if not m:
        raise SystemExit("Could not parse unit name from H1")
    return m.group(1).strip()

def main():
    if len(sys.argv) < 2:
        print("Usage: create_unit.py <unit_md_path> [--course <course_id> | --anchor <unit_id>] [--no-fill] [--dry-run]"); sys.exit(1)
    md_path = pathlib.Path(sys.argv[1])
    no_fill = "--no-fill" in sys.argv
    dry = "--dry-run" in sys.argv
    course_id = opt_value(sys.argv, "--course")
    anchor = opt_value(sys.argv, "--anchor") or ANCHOR_UNIT
    if course_id:
        # The course-map "Add New Unit" is a link to this route, which renders the unit
        # form directly (#unit-form-input-name). Navigate straight to it — no button click.
        add_from = f"{BASE}/develop/course-map/{course_id}/add-new-unit"
        where = f"course {course_id} (add-new-unit route)"
        click_add = False
    else:
        add_from = f"{BASE}/develop/unit-planner/{anchor}"
        where = f"anchor unit {anchor}"
        click_add = True
    md = md_path.read_text()
    name = unit_name(md)
    plan = {label: parse_blocks(section_text(md, n)) for label, n in FIELDS.items()}
    print(f"Unit name: {name!r}")
    print(f"Adding via: {where}")
    for label, blocks in plan.items():
        print(f"  {label}: {len(blocks)} block(s)")
    if dry:
        print("[dry-run] not creating."); return

    with sync_playwright() as p:
        b, ctx, pg = attach(p)
        pg.bring_to_front()
        pg.goto(add_from, wait_until="networkidle")
        pg.wait_for_timeout(1500)
        if click_add:
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
        pg.wait_for_timeout(4000)
        # Anchor flow lands on the new unit's planner; the course-map flow lands back on the
        # unit calendar. Capture the id from either.
        uid = None
        m = re.search(r"/unit-planner/(\d+)", pg.url)
        if m:
            uid = m.group(1)
        else:
            try:
                href = pg.locator(f'a:has-text("{name}")').first.get_attribute("href") or ""
                mm = re.search(r"/unit(?:-planner)?/(\d+)", href)
                uid = mm.group(1) if mm else None
            except Exception:
                uid = None
        print(f"CREATED {name!r} -> unit_id={uid or '?'}  ({pg.url})")

        if not no_fill and uid:
            pg.goto(f"{BASE}/develop/unit-planner/{uid}", wait_until="networkidle")
            pg.wait_for_timeout(2500)
            for label, blocks in plan.items():
                if blocks: fill_field(pg, label, blocks)
        b.close()
    print("Done." if no_fill else "Done (created + filled).")

if __name__ == "__main__":
    main()
