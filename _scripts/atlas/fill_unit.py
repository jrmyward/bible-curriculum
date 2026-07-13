#!/usr/bin/env python3
"""Fill a Bible 9 Foundations unit's free-text fields in Rubicon Atlas.

Reads the unit's data-model markdown (classes/foundations/rubicon-atlas/unit-NN-*.md),
attaches to the watchable Chrome (launch-browser.sh, CDP :9222), and fills the four
free-text Froala fields. (Faith Learning Integration is a Standards picker — handled
separately, not here.)

Usage:
    _scripts/atlas/.venv/bin/python _scripts/atlas/fill_unit.py <unit_md_path> [--dry-run]

Flow per field: click the field -> wait for Froala to init -> clear -> insert text
blocks (paragraphs / list items separated by Enter) -> blur so Atlas autosaves.
"""
import re, sys, pathlib
from playwright.sync_api import sync_playwright
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from session import attach

BASE = "https://watersprings.rubiconatlas.org"

# md field section number -> Atlas field label (the free-text ones only)
FIELDS = {
    "Unit Overview": 1,
    "Essential Questions": 2,
    "Objectives": 3,
    "Biblical Integration": 5,
}

def clean(s: str) -> str:
    s = re.sub(r"\*\*(.+?)\*\*", r"\1", s)      # bold
    s = re.sub(r"\*(.+?)\*", r"\1", s)          # italic
    s = re.sub(r"`(.+?)`", r"\1", s)            # code
    s = re.sub(r"\[(.+?)\]\((.+?)\)", r"\1", s) # links -> text
    return s.strip()

def section_text(md: str, n: int) -> str:
    m = re.search(rf"## {n} · [^\n]+\n(.*?)(?:\n---|\Z)", md, re.S)
    return m.group(1).strip() if m else ""

def parse_blocks(section: str):
    """Group wrapped prose into paragraphs and each '- ' bullet into its own block."""
    blocks, cur = [], None
    for line in section.splitlines():
        st = line.strip()
        if not st:
            if cur is not None: blocks.append(cur); cur = None
            continue
        if st.startswith("- "):
            if cur is not None: blocks.append(cur)
            cur = st[2:].strip()
        else:
            cur = f"{cur} {st}" if cur else st
    if cur is not None: blocks.append(cur)
    return [clean(b) for b in blocks if clean(b)]

ACTIVE = ".fr-element[contenteditable='true']"

def fill_field(pg, label, blocks):
    # Scope everything to THIS field's category so an editor open elsewhere can't
    # steal our input (that bug doubled Unit Overview and left others empty).
    cat = pg.evaluate_handle(
        """(label) => {
            for (const c of document.querySelectorAll('.template-renderer-category'))
                if (c.textContent.trim().startsWith(label)) return c;
            return null; }""", label).as_element()
    if not cat:
        print(f"  ! '{label}': field not found"); return False
    view = cat.query_selector(".unit-text-content")
    view.scroll_into_view_if_needed()
    view.click()
    # wait for THIS category's editor to init
    pg.wait_for_function(f"(c) => !!c.querySelector(\"{ACTIVE}\")", arg=cat, timeout=12000)
    ed = cat.query_selector(ACTIVE)
    ed.click()
    # clear (macOS: select-all is Meta+A, not Control+A), then verify empty
    pg.keyboard.press("Meta+a"); pg.keyboard.press("Delete")
    if (ed.inner_text() or "").strip():
        ed.evaluate("e => { e.innerHTML=''; }")   # fallback: empty the editor directly
        ed.click()
    for i, blk in enumerate(blocks):
        if i: pg.keyboard.press("Enter")
        pg.keyboard.insert_text(blk)
    pg.wait_for_timeout(500)
    ed.evaluate("e => e.blur()")           # blur commits the autosave
    pg.wait_for_timeout(2500)
    saved = len((cat.query_selector(".unit-text-content, .fr-view").inner_text() or "").strip())
    print(f"  {'✓' if saved else '✗'} '{label}': {len(blocks)} block(s), {saved} chars in field")
    return saved > 0

def main():
    if len(sys.argv) < 2:
        print("Usage: fill_unit.py <unit_md_path> [--unit <unit_id>] [--dry-run]"); sys.exit(1)
    md_path = pathlib.Path(sys.argv[1])
    dry = "--dry-run" in sys.argv
    unit_id = None
    if "--unit" in sys.argv:
        i = sys.argv.index("--unit")
        if i + 1 >= len(sys.argv):
            print("--unit requires a value"); sys.exit(1)
        unit_id = sys.argv[i + 1]
    md = md_path.read_text()
    plan = {label: parse_blocks(section_text(md, n)) for label, n in FIELDS.items()}
    print(f"Unit: {md_path.name}" + (f" -> unit_id {unit_id}" if unit_id else " (current page)"))
    for label, blocks in plan.items():
        print(f"  {label}: {len(blocks)} block(s) — e.g. {blocks[0][:60] if blocks else '(empty)'}...")
    if dry:
        print("\n[dry-run] nothing written."); return
    with sync_playwright() as p:
        b, ctx, pg = attach(p)
        pg.bring_to_front()
        if unit_id:  # navigate to the unit planner first; otherwise fill the current page
            pg.goto(f"{BASE}/develop/unit-planner/{unit_id}", wait_until="networkidle")
            pg.wait_for_timeout(2500)
        for label, blocks in plan.items():
            if blocks: fill_field(pg, label, blocks)
        b.close()  # detach only; window stays open
    print("Done. Faith Learning Integration (Standards picker) still to do manually/separately.")

if __name__ == "__main__":
    main()
