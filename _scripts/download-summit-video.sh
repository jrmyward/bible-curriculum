#!/bin/bash
# Download a Summit portal (Vimeo) lesson video for local classroom playback.
#
# Summit's videos are private/whitelisted Vimeo embeds locked to summitportal.org.
# yt-dlp with a matching referer fetches a fresh signed config each run, so this
# works without hand-copying expiring stream URLs.
#
# Usage:
#   ./_scripts/download-summit-video.sh <vimeo_id> <unlisted_hash> <output.mp4>
#
# Find the id + hash in the portal page source — each video is an iframe:
#   https://player.vimeo.com/video/<VIMEO_ID>?h=<HASH>
#
# Example:
#   ./_scripts/download-summit-video.sh 492199971 84a005ac05 \
#     classes/foundations/_source-text/portal/ch01/videos/01-what-is-a-worldview-myers.mp4
#
# Downloads best quality <=1080p (plenty for a projector) and merges A/V to mp4.
set -euo pipefail

if [ "$#" -lt 3 ]; then
  echo "Usage: $0 <vimeo_id> <unlisted_hash> <output.mp4>" >&2
  exit 1
fi
ID="$1"; HASH="$2"; OUT="$3"
mkdir -p "$(dirname "$OUT")"

if ! command -v yt-dlp >/dev/null 2>&1; then echo "Error: yt-dlp not installed (brew install yt-dlp)"; exit 1; fi
if ! command -v ffmpeg >/dev/null 2>&1; then echo "Error: ffmpeg not installed (brew install ffmpeg)"; exit 1; fi

echo "Downloading Vimeo $ID -> $OUT"
yt-dlp \
  --referer "https://summitportal.org/" \
  -S "res:1080" \
  --merge-output-format mp4 \
  --no-warnings --no-progress \
  -o "$OUT" \
  "https://player.vimeo.com/video/${ID}?h=${HASH}"
echo "Done: $OUT"
