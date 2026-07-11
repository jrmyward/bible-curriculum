#!/usr/bin/env python3
"""One-time interactive login to Rubicon Atlas.

Launches a real browser window. YOU log in (Google / Clever / Office SSO — whatever
your school uses). The script then saves the authenticated session to .auth/state.json
so every later script reuses it — no credentials ever touch this code.

Run it yourself (it's interactive). Optionally pass your Atlas URL; otherwise just
navigate to it in the browser window that opens:
    _scripts/atlas/.venv/bin/python _scripts/atlas/auth.py
    _scripts/atlas/.venv/bin/python _scripts/atlas/auth.py "https://<your-school>.rubiconatlas.org/"

Re-run any time the saved session expires.
"""
import sys
import pathlib
from playwright.sync_api import sync_playwright

HERE = pathlib.Path(__file__).parent
STATE = HERE / ".auth" / "state.json"

def main():
    start_url = sys.argv[1] if len(sys.argv) > 1 else None
    STATE.parent.mkdir(exist_ok=True)
    with sync_playwright() as p:
        # channel="chrome" uses your installed Google Chrome — best SSO compatibility.
        browser = p.chromium.launch(headless=False, channel="chrome")
        ctx = browser.new_context()
        page = ctx.new_page()
        if start_url:
            try:
                page.goto(start_url)
            except Exception as e:
                print(f"(Couldn't open {start_url}: {e}\n Just type your Atlas URL into the browser.)")
        print("\n" + "=" * 64)
        print("A browser window opened. Go to your school's Rubicon Atlas URL")
        print("(the one in your address bar right now) and log in.")
        print("Navigate until you can SEE your course dashboard (fully logged in).")
        print("Then return HERE and press Enter to save the session.")
        print("=" * 64)
        input("\nPress Enter once you are logged in and on your dashboard... ")
        ctx.storage_state(path=str(STATE))
        print(f"\n✅ Session saved to {STATE.relative_to(HERE.parent.parent)}")
        print("   You can close the browser window. You won't need to log in again")
        print("   until this session expires.")
        browser.close()

if __name__ == "__main__":
    main()
