#!/usr/bin/env python3
"""Navigate the persistent Chrome (:9222) to Google sign-in so the user can log in
to their teacher account in that watchable window. Signs in nothing itself."""
import sys
from playwright.sync_api import sync_playwright

CDP = "http://localhost:9222"
CONT = "https://classroom.google.com/"
hint = sys.argv[1] if len(sys.argv) > 1 else ""

def main():
    url = "https://accounts.google.com/AccountChooser?continue=" + CONT
    if hint:
        url = f"https://accounts.google.com/signin/v2/identifier?continue={CONT}&Email={hint}"
    with sync_playwright() as p:
        b = p.chromium.connect_over_cdp(CDP)
        ctx = b.contexts[0]
        pg = ctx.pages[0] if ctx.pages else ctx.new_page()
        pg.bring_to_front()
        pg.goto(url, wait_until="domcontentloaded")
        print("Opened sign-in in the watchable Chrome:", pg.url)
        b.close()  # detach; window stays open for the user to sign in

if __name__ == "__main__":
    main()
