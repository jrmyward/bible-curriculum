#!/usr/bin/env python3
"""Create + fill daily lessons for a Foundations chapter in Rubicon Atlas.

Reads classes/foundations/rubicon-atlas/lessons/chNN-lessons.md (one '## Day N - Title'
section per day, with '**Row Label:** content' lines mapping to the daily Madeline Hunter
template). For each day: create the lesson if it doesn't exist, insert the default (daily)
template if the Details table is missing, then fill the template cells.

Attaches to the watchable Chrome (launch-browser.sh, CDP :9222).

Usage:
    _scripts/atlas/.venv/bin/python _scripts/atlas/lesson_fill.py <chNN-lessons.md> <unit_id> [--only N] [--dry-run]
"""
import re, sys, pathlib
from playwright.sync_api import sync_playwright
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from session import attach

BASE = "https://watersprings.rubiconatlas.org"
ROWS = ["Anticipatory Set","Objective and Purpose","Input","Modeling",
        "Check for Understanding","Guided Practice","Independent Practice","Closure"]

def parse(md_path):
    md = pathlib.Path(md_path).read_text()
    days = []
    for m in re.finditer(r"^## (Day \d+[^\n]*)\n(.*?)(?=^## |\Z)", md, re.S | re.M):
        title, body = m.group(1).strip(), m.group(2)
        rows = {}
        for rm in re.finditer(r"\*\*([^:]+):\*\*\s*(.+)", body):
            label = rm.group(1).strip()
            if label in ROWS:
                rows[label] = rm.group(2).strip()
        days.append((title, rows))
    return days

def existing_lessons(pg, unit_id):
    pg.goto(f"{BASE}/develop/unit/{unit_id}/lessons?backLinkId=unitCalendarYear", wait_until="networkidle")
    pg.wait_for_timeout(2500)
    return {l["title"]: l["id"] for l in pg.evaluate("""()=>{
        const out=[]; document.querySelectorAll("a[href*='/develop/lesson/']").forEach(a=>{
            const m=a.getAttribute('href').match(/lesson\\/(\\d+)/); const t=(a.innerText||'').trim();
            if(m&&t) out.push({id:m[1], title:t}); }); return out; }""")}

def create_lesson(pg, unit_id, title):
    pg.goto(f"{BASE}/develop/unit/{unit_id}/lessons/add-new-lesson?backLinkId=unitCalendarYear", wait_until="networkidle")
    pg.wait_for_timeout(2000)
    pg.fill("#lesson-editor-form-title", title)
    pg.wait_for_timeout(400)
    pg.click("#lesson-editor-save-button")
    pg.wait_for_timeout(5000)
    m = re.search(r"/lesson/(\d+)", pg.url)
    return m.group(1) if m else None

def ensure_template(pg):
    ed = pg.query_selector(".fr-element")
    if ed and ed.query_selector("table tr"):
        return True   # template already present
    btn = pg.query_selector("button:has-text('Insert Default Template')")
    if not btn:
        print("    ! no Insert Default Template button"); return False
    btn.click()
    pg.wait_for_timeout(2500)
    return bool(pg.query_selector(".fr-element table tr"))

def fill_details(pg, rows):
    filled = pg.evaluate("""(cells)=>{
        const ed=document.querySelector('.fr-element'); if(!ed) return [];
        ed.focus(); const done=[];
        for(const tr of ed.querySelectorAll('table tr')){
            const tds=tr.querySelectorAll('td,th'); if(tds.length<2) continue;
            const l=tds[0].innerText.trim();
            for(const k of Object.keys(cells)){ if(l.startsWith(k)){ tds[1].textContent=cells[k]; done.push(k); } }
        }
        ed.dispatchEvent(new InputEvent('input',{bubbles:true})); return done;
    }""", rows)
    pg.wait_for_timeout(500)
    pg.evaluate("()=>{const e=document.querySelector('.fr-element'); if(e) e.blur();}")
    pg.wait_for_timeout(3000)
    return filled

def main():
    args = sys.argv[1:]
    if len(args) < 2:
        print("Usage: lesson_fill.py <chNN-lessons.md> <unit_id> [--only N] [--dry-run]"); sys.exit(1)
    md_path, unit_id = args[0], args[1]
    only = None
    if "--only" in args: only = int(args[args.index("--only")+1])
    dry = "--dry-run" in args
    days = parse(md_path)
    print(f"Parsed {len(days)} day(s) from {pathlib.Path(md_path).name}")
    for i,(t,r) in enumerate(days,1):
        print(f"  Day {i}: '{t}' -> rows: {list(r)}")
    if dry: return
    with sync_playwright() as p:
        b, ctx, pg = attach(p); pg.bring_to_front()
        exist = existing_lessons(pg, unit_id)
        print(f"existing lessons: {len(exist)}")
        for i,(title, rows) in enumerate(days,1):
            if only and i != only: continue
            if title in exist:
                lid = exist[title]; print(f"Day {i}: exists (id {lid}) -> fill")
                pg.goto(f"{BASE}/develop/lesson/{lid}/view", wait_until="networkidle"); pg.wait_for_timeout(3000)
            else:
                lid = create_lesson(pg, unit_id, title)
                print(f"Day {i}: created (id {lid})")
            if not lid: print(f"  ! Day {i}: no lesson id, skip"); continue
            if not ensure_template(pg): print(f"  ! Day {i}: no template, skip fill"); continue
            done = fill_details(pg, rows)
            print(f"  ✓ Day {i}: filled {len(done)} row(s)")
        b.close()

if __name__ == "__main__":
    main()
