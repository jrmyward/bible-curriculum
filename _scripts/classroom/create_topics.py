#!/usr/bin/env python3
"""Create the 18 unit Topics in the Bible 9 Foundations Classroom class (path A,
browser automation, :9222). Topic names come from the Atlas unit files' H1s so they
match the units exactly. Idempotent: skips any topic that already exists.

Creates in reverse (18 -> 01): Classroom adds new topics at the TOP of Classwork, so
building 18 first and 01 last leaves the display reading 01 ... 18 top-to-bottom.

Usage: create_topics.py [--limit N] [--dry-run]
"""
import sys, re, glob, pathlib
from playwright.sync_api import sync_playwright

CDP = "http://localhost:9222"
COURSE = "ODU1NTEwMzM0MDA3"
UNIT_GLOB = "classes/foundations/rubicon-atlas/unit-*.md"
OUT = pathlib.Path(__file__).parent / "probe-output"

def unit_names():
    names = []
    for f in sorted(glob.glob(UNIT_GLOB)):
        m = re.search(r"^#\s+Rubicon Atlas — Unit\s+(.+?)\s*$", pathlib.Path(f).read_text(), re.M)
        if m: names.append(m.group(1).strip())
    return names  # ascending 01..18

def main():
    dry = "--dry-run" in sys.argv
    limit = int(sys.argv[sys.argv.index("--limit") + 1]) if "--limit" in sys.argv else None
    order = list(reversed(unit_names()))          # 18..01
    if limit: order = order[:limit]
    print(f"Creating {len(order)} topic(s) in reverse order (18->01).")
    if dry:
        for n in order: print("  would create:", n)
        return
    OUT.mkdir(exist_ok=True)
    with sync_playwright() as p:
        b = p.chromium.connect_over_cdp(CDP)
        ctx = b.contexts[0]
        pg = ctx.pages[0] if ctx.pages else ctx.new_page()
        pg.bring_to_front()
        pg.goto(f"https://classroom.google.com/w/{COURSE}/t/all", wait_until="domcontentloaded")
        pg.wait_for_timeout(4000)
        if "classroom.google.com" not in pg.url or "accounts.google.com" in pg.url:
            print("! Not on the class Classwork page:", pg.url); b.close(); sys.exit(2)
        created = 0
        for name in order:
            if pg.evaluate("(n) => document.body.innerText.includes(n)", name):
                print(f"  skip (exists): {name}"); continue
            pg.get_by_role("button", name=re.compile(r"^\s*Create\s*$", re.I)).first.click()
            pg.wait_for_timeout(700)
            pg.get_by_role("menuitem", name=re.compile(r"^\s*Topic\s*$", re.I)).first.click()
            pg.wait_for_timeout(900)
            dlg = pg.get_by_role("dialog")
            dlg.wait_for(timeout=8000)
            dlg.get_by_role("textbox").first.fill(name)
            pg.wait_for_timeout(300)
            dlg.get_by_role("button", name=re.compile(r"Add topic", re.I)).first.click()
            pg.wait_for_timeout(2000)
            created += 1
            print(f"  created: {name}")
        pg.screenshot(path=str(OUT / "topics.png"), full_page=True)
        print(f"Done. Created {created} this run.")
        b.close()

if __name__ == "__main__":
    main()
