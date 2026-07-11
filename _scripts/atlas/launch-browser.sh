#!/bin/bash
# Launch a persistent, watchable Chrome for Atlas automation.
#
# This window STAYS OPEN. Log into Atlas once here; the profile under
# .auth/chrome-profile persists, so you won't need to log in again. Claude's
# scripts attach to this browser over the debug port (9222) and leave it open —
# you watch every action happen live.
#
# Run it (leave it running):
#   _scripts/atlas/launch-browser.sh
set -e
HERE="$(cd "$(dirname "$0")" && pwd)"
CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
PROFILE="$HERE/.auth/chrome-profile"
URL="https://watersprings.rubiconatlas.org/develop/unit-planner/2224?backLinkId=unitCalendarYear"

exec "$CHROME" \
  --remote-debugging-port=9222 \
  --user-data-dir="$PROFILE" \
  --no-first-run \
  --no-default-browser-check \
  "$URL"
