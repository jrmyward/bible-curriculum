#!/usr/bin/env python3
"""Read-only: check whether the persistent Chrome (:9222) is signed into a Google
account with access to Google Classroom, and report which account. Screenshots the
Classroom home so we can see the login/account state. Creates nothing.
"""
import pathlib
from playwright.sync_api import sync_playwright

CDP = "http://localhost:9222"
OUT = pathlib.Path(__file__).parent / "probe-output"

def main():
    OUT.mkdir(exist_ok=True)
    with sync_playwright() as p:
        b = p.chromium.connect_over_cdp(CDP)
        ctx = b.contexts[0]
        pg = ctx.pages[0] if ctx.pages else ctx.new_page()
        pg.bring_to_front()
        pg.goto("https://classroom.google.com/", wait_until="domcontentloaded")
        pg.wait_for_timeout(4000)
        print("URL:", pg.url)
        print("TITLE:", (pg.title() or "")[:100])
        # Try to read the signed-in account from the Google account button aria-label.
        acct = pg.evaluate("""() => {
            const el = document.querySelector("a[aria-label*='Google Account'], a[href*='SignOutOptions'], [aria-label*='@']");
            return el ? (el.getAttribute('aria-label')||el.textContent||'').trim().slice(0,160) : null;
        }""")
        print("ACCOUNT HINT:", acct)
        signed_in = "classroom.google.com" in pg.url and "accounts.google.com" not in pg.url
        print("SIGNED IN TO CLASSROOM:", signed_in)
        pg.screenshot(path=str(OUT / "classroom-login.png"), full_page=False)
        print("screenshot:", OUT / "classroom-login.png")
        b.close()  # detach only

if __name__ == "__main__":
    main()
