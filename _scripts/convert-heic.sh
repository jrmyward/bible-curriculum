#!/bin/bash

# HEIC to JPG Converter
# Usage: ./convert-heic.sh [directory]
# If no directory provided, uses current directory

set -e

# Default to current directory if no arg provided
DIR="${1:-.}"

# Check if sips is available (macOS only)
if ! command -v sips &> /dev/null; then
    echo "Error: 'sips' command not found. This script requires macOS."
    exit 1
fi

# Find all HEIC files (case insensitive)
shopt -s nocaseglob
HEIC_FILES=("$DIR"/*.heic)
shopt -u nocaseglob

# Check if any HEIC files exist
if [ ! -e "${HEIC_FILES[0]}" ]; then
    echo "No HEIC files found in $DIR"
    exit 0
fi

echo "Converting HEIC files to JPG in: $DIR"
echo "---"

count=0
for file in "${HEIC_FILES[@]}"; do
    if [ -f "$file" ]; then
        # Get base filename without extension
        base="${file%.*}"
        output="${base}.jpg"

        echo "Converting: $(basename "$file") → $(basename "$output")"
        sips -s format jpeg "$file" --out "$output" > /dev/null 2>&1

        # Optional: delete original HEIC after successful conversion
        # Uncomment the next line if you want to auto-delete HEICs
        # rm "$file"

        ((count++))
    fi
done

echo "---"
echo "Converted $count file(s)"
echo ""
echo "To delete original HEIC files, run:"
echo "  rm $DIR/*.heic"
