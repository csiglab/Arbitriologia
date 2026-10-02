#!/bin/sh
set -eu

IMAGE="ghcr.io/csiglab/arbitriologia:latest"
CONTAINER="arbitriologia"

cd "$(dirname "$0")"

# Local defaults from .env (e.g. ARBITRIOLOGIA_PORT); real env vars still win.
# NOTE: this must run BEFORE deriving PORT below, otherwise .env is ignored.
if [ -f .env ]; then
  while IFS='=' read -r key value || [ -n "$key" ]; do
    case $key in
      ''|\#*) continue ;;
    esac
    if [ -z "$(eval "printf '%s' \"\${$key:-}\"")" ]; then
      eval "$key=\$value"
    fi
  done < .env
fi

PORT="${ARBITRIOLOGIA_PORT:-8080}"

docker pull "$IMAGE"
docker rm -f "$CONTAINER" 2>/dev/null || true
exec docker run -d --name "$CONTAINER" --restart unless-stopped \
  -p "$PORT:80" \
  "$IMAGE"
