#!/bin/bash

# sudo apt install imagemagick

# Check if an argument was provided
if [[ -z "$1" ]]; then
  echo "Error: No file path provided." >&2
  echo "Usage: $0 <file_path>" >&2
  exit 1
fi

INPUT="$1"

# Check if the file exists
if [[ ! -f "$INPUT" ]]; then
  echo "Error: File '$INPUT' does not exist." >&2
  exit 1
fi

# Original image
NAME=$(basename "$INPUT" | cut -f 1 -d '.')

echo $NAME

# List of sizes (WIDTHxHEIGHT)
SIZES=("64x64" "128x128" "256x256" "512x512" "1024x1024")

# Output directory
OUTDIR="resized"
mkdir -p "$OUTDIR"

# Loop through sizes and generate images
for SIZE in "${SIZES[@]}"; do
    echo "$OUTDIR/${NAME}_${SIZE}.png"
    convert "$INPUT" -resize "$SIZE" "$OUTDIR/${NAME}_${SIZE}.png"
done
