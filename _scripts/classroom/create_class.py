#!/usr/bin/env python3
"""Create the Google Classroom class via browser automation in the persistent
watchable Chrome (:9222). Requires the teacher to be signed in already
(open_signin.py + sign in; verify with check_login.py).

Usage:
    create_class.py [--name "Bible 9 Foundations"] [--section "Grade 9"] [--dry-run]
"""
import sys, re, pathlib
from playwright.sync_api import sync_playwright

CDP = "http://localhost:9222"
OUT = pathlib.Path(__file__).parent / "probe-output"

def arg(flag, default):
    return sys.argv[sys.argv.index(flag) + 1] if flag in sys.argv else default

def main():
    name = arg("--name", "Bible 9 Foundations")
    section = arg("--section", "Grade 9")
    dry = "--dry-run" in sys.argv
    print(f"Class name: {name!r} | Section: {section!r}" + (" [dry-run]" if dry else ""))
    OUT.mkdir(exist_ok=True)
    with sync_playwright() as p:
        b = p.chromium.connect_over_cdp(CDP)
        ctx = b.contexts[0]
        pg = ctx.pages[0] if ctx.pages else ctx.new_page()
        pg.bring_to_front()
        pg.goto("https://classroom.google.com/", wait_until="domcontentloaded")
        pg.wait_for_timeout(3500)
        if "accounts.google.com" in pg.url or "classroom.google.com" not in pg.url:
            print("! Not signed in to Classroom. Run open_signin.py and sign in first."); b.close(); sys.exit(2)

        # guard: bail if a class with this name already exists (avoid duplicates)
        existing = pg.evaluate("(n) => document.body.innerText.includes(n)", name)
        if existing:
            print(f"! A class named {name!r} may already exist on this page — aborting to avoid a duplicate.")
            pg.screenshot(path=str(OUT / "create-class-abort.png")); b.close(); sys.exit(3)

        if dry:
            print("[dry-run] not creating."); b.close(); return

        # open the Create class flow (empty-state button, or the top-right "+")
        try:
            pg.get_by_role("button", name=re.compile("Create class", re.I)).first.click(timeout=6000)
        except Exception:
            pg.get_by_role("button", name=re.compile("Add class|Create or join", re.I)).first.click()
            pg.wait_for_timeout(800)
            pg.get_by_role("menuitem", name=re.compile("Create class", re.I)).first.click()
        pg.wait_for_timeout(1500)

        # first-run acknowledgment dialog (personal-account warning) — check box + Continue if present
        try:
            cb = pg.get_by_role("checkbox").first
            if cb.is_visible():
                cb.check()
                pg.get_by_role("button", name=re.compile("Continue", re.I)).first.click()
                pg.wait_for_timeout(1200)
        except Exception:
            pass

        # the Create class dialog: fill Class name (required) + Section
        dlg = pg.get_by_role("dialog")
        dlg.wait_for(timeout=10000)
        filled = False
        for lbl in ("Class name (required)", "Class name"):
            try:
                dlg.get_by_label(lbl).fill(name); filled = True; break
            except Exception:
                continue
        if not filled:  # fallback: first textbox in dialog
            dlg.get_by_role("textbox").first.fill(name)
        try:
            dlg.get_by_label("Section").fill(section)
        except Exception:
            print("  (Section field not filled — optional)")
        pg.wait_for_timeout(500)
        pg.screenshot(path=str(OUT / "create-class-dialog.png"))

        dlg.get_by_role("button", name=re.compile(r"^\s*Create\s*$", re.I)).first.click()
        # wait for the class to open (/c/<id>) or a class tile to appear
        try:
            pg.wait_for_url(re.compile(r"classroom\.google\.com/(c|u/\d+/c)/"), timeout=20000)
        except Exception:
            pg.wait_for_timeout(6000)
        pg.wait_for_timeout(3000)
        m = re.search(r"/c/([\w-]+)", pg.url)
        print(f"CREATED class {name!r} -> {pg.url}" + (f"  course_id={m.group(1)}" if m else ""))
        pg.screenshot(path=str(OUT / "create-class-done.png"), full_page=True)
        b.close()
    print("Done.")

if __name__ == "__main__":
    main()
