#!/usr/bin/env python3
"""Capture the Atlas unit-editor DOM so selectors can be written.

Uses the saved session from auth.py. Give it the URL of the page you want captured
(e.g. the "Add New Unit" form, or a unit's edit view). It saves the full rendered
HTML and a full-page screenshot to probe-output/ for inspection.

Usage:
    _scripts/atlas/.venv/bin/python _scripts/atlas/probe.py "<atlas-url>" [name]

Example:
    ... probe.py "https://rubiconatlas.org/.../add-new-unit" add-unit-form
"""
import sys
import pathlib
from playwright.sync_api import sync_playwright

HERE = pathlib.Path(__file__).parent
STATE = HERE / ".auth" / "state.json"
OUT = HERE / "probe-output"

def main():
    if len(sys.argv) < 2:
        print("Usage: probe.py <url> [name]"); sys.exit(1)
    url = sys.argv[1]
    name = sys.argv[2] if len(sys.argv) > 2 else "probe"
    if not STATE.exists():
        print(f"No saved session at {STATE}. Run auth.py first."); sys.exit(1)
    OUT.mkdir(exist_ok=True)
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, channel="chrome")
        ctx = browser.new_context(storage_state=str(STATE))
        page = ctx.new_page()
        page.goto(url, wait_until="networkidle")
        page.wait_for_timeout(2500)  # let the SPA settle
        html_path = OUT / f"{name}.html"
        png_path = OUT / f"{name}.png"
        html_path.write_text(page.content(), encoding="utf-8")
        page.screenshot(path=str(png_path), full_page=True)
        # Dump form controls (labels, inputs, selects) as a quick selector cheat-sheet.
        controls = page.eval_on_selector_all(
            "input, textarea, select, [contenteditable='true'], button",
            """els => els.map(e => ({
                tag: e.tagName.toLowerCase(),
                type: e.getAttribute('type'),
                name: e.getAttribute('name'),
                id: e.id || null,
                placeholder: e.getAttribute('placeholder'),
                aria: e.getAttribute('aria-label'),
                text: (e.innerText||'').trim().slice(0,40)
            }))""",
        )
        (OUT / f"{name}-controls.txt").write_text(
            "\n".join(str(c) for c in controls), encoding="utf-8")
        print(f"✅ saved:\n  {html_path}\n  {png_path}\n  {OUT/f'{name}-controls.txt'}")
        print("Leave the browser open or close it — capture is done.")
        browser.close()

if __name__ == "__main__":
    main()
