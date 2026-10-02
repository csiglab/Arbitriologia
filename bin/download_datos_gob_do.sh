#!/usr/bin/env bash
# Download dataset metadata from the datos.gob.do API into data/raw/.
#
# Moved from scripts/download.bash. Differences from the original:
# - Proper .sh extension; `set -euo pipefail`; --help; configurable
#   START/LIMIT/TOTAL/INTERVAL/OUT_DIR via flags (no hardcoded resume
#   offset, no output to CWD).
# - No hardcoded session cookies: the original embedded an expired
#   Cloudflare cf_clearance/_ga Cookie header. If the API needs
#   Cloudflare clearance, export CF_COOKIE and it is sent; otherwise a
#   plain request with a normal User-Agent is used.
# - curl uses --fail --retry so HTTP errors stop the run instead of
#   writing error pages to disk.
# - Detects Cloudflare challenge pages ("Just a moment...") and aborts
#   with a hint instead of silently continuing.
#
# Usage:
#   bash bin/download_datos_gob_do.sh [--start N] [--limit N] [--total N]
#       [--interval SEC] [--out-dir data/raw] [--dry-run]
set -euo pipefail

BASE_URL="https://datos.gob.do/api/datasets"
START=0
LIMIT=8
TOTAL=959
INTERVAL=2
OUT_DIR="data/raw"
DRY_RUN=0

usage() {
  sed -n '2,/^set /p' "$0" | sed 's/^# \{0,1\}//'
  echo "Flags: --start N --limit N --total N --interval SEC --out-dir DIR --dry-run --help"
}

while [ $# -gt 0 ]; do
  case "$1" in
    --start) START="$2"; shift 2 ;;
    --limit) LIMIT="$2"; shift 2 ;;
    --total) TOTAL="$2"; shift 2 ;;
    --interval) INTERVAL="$2"; shift 2 ;;
    --out-dir) OUT_DIR="$2"; shift 2 ;;
    --dry-run) DRY_RUN=1; shift ;;
    --help|-h) usage; exit 0 ;;
    *) echo "Unknown flag: $1 (see --help)" >&2; exit 2 ;;
  esac
done

mkdir -p "$OUT_DIR"

echo "[download] base=$BASE_URL start=$START limit=$LIMIT total=$TOTAL out=$OUT_DIR"

start="$START"
while [ "$start" -lt "$TOTAL" ]; do
  url="${BASE_URL}?skip=${start}&limit=${LIMIT}"
  filename="${OUT_DIR}/data_${start}.json"

  echo "Downloading data from URL: $url"
  echo "Saving to file: $filename"

  if [ "$DRY_RUN" -eq 1 ]; then
    start=$((start + LIMIT))
    continue
  fi

  if [ -n "${CF_COOKIE:-}" ]; then
    curl -fsSL --retry 3 --compressed \
      -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:129.0) Gecko/20100101 Firefox/129.0' \
      -H "Cookie: $CF_COOKIE" \
      "$url" -o "$filename"
  else
    curl -fsSL --retry 3 --compressed \
      -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:129.0) Gecko/20100101 Firefox/129.0' \
      "$url" -o "$filename"
  fi

  if grep -qi "Just a moment" "$filename"; then
    echo "[download] ERROR: Cloudflare challenge page saved to $filename." >&2
    echo "[download] Set CF_COOKIE with a fresh clearance cookie and retry." >&2
    exit 1
  fi

  start=$((start + LIMIT))

  echo "Waiting for $INTERVAL seconds before the next download..."
  sleep "$INTERVAL"
done

echo "Download process completed."
