"""Shared: attach to the persistent Chrome launched by launch-browser.sh (CDP :9222).

Scripts import `page()` to get a live page in the watchable browser without opening
or closing anything — the window stays open for the user to watch.
"""
from playwright.sync_api import sync_playwright

CDP_URL = "http://localhost:9222"

def attach(p):
    """Return (browser, context, page) attached to the running Chrome."""
    browser = p.chromium.connect_over_cdp(CDP_URL)
    ctx = browser.contexts[0]
    pg = ctx.pages[0] if ctx.pages else ctx.new_page()
    return browser, ctx, pg
