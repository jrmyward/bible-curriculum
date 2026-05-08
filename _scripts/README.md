# Utility Scripts

Helper scripts for managing the Bible curriculum repository.

## convert-heic.sh

Converts HEIC images to JPG format (macOS only, uses built-in `sips` command).

```bash
./_scripts/convert-heic.sh                                                # current directory
./_scripts/convert-heic.sh classes/understanding-the-faith/syllabus       # specific directory
```

What it does:

- Finds all `.heic` files (case-insensitive)
- Converts each to `.jpg` in the same directory
- Keeps originals (delete manually with `rm path/*.heic`)
- Silent mode — only shows progress

## ocr.swift

Apple Vision OCR (the engine behind Live Text and Preview). Reads images, returns clean text on stdout. Auto-detects orientation.

```bash
swift _scripts/ocr.swift path/to/IMG_0001.jpg path/to/IMG_0002.jpg
swift _scripts/ocr.swift classes/understanding-the-faith/syllabus/*.jpg > all-pages.txt
```

Each image's text is preceded by `===== <filename> =====`. The script tries all four 90° orientations and picks the one with the most recognized characters, so rotated phone photos work without manual rotation.

Requirements: macOS with Xcode (`xcrun --find swift`).

## clean-ocr.py

Cleans raw OCR text dumps into structured markdown. Pairs with `ocr.swift` for the chapter-by-chapter source-text pipeline.

```bash
python3 _scripts/clean-ocr.py <target-dir> <chapter-number|all>
```

Examples:

```bash
python3 _scripts/clean-ocr.py classes/understanding-the-faith/_source-text/teaching-manual all
python3 _scripts/clean-ocr.py classes/understanding-the-faith/_source-text/textbook 5
```

Reads from `<target-dir>/.raw-ocr/chNN.txt` and writes to `<target-dir>/chNN.md`. Idempotent — safe to re-run after editing the raw text.

What it cleans:

- Strips repeating headers/footers
- Drops standalone page-number lines
- Replaces `=== IMG_NNNN.jpg ===` markers with `<!-- page-N -->` comments
- Stitches numbered list items where the number is on its own line
- Fixes common OCR errors in `[N.M]` section labels (`(3.4)`, `[3.4)`, etc.)
- Collapses runs of 3+ blank lines

## Source-text OCR pipeline

The full re-OCR workflow for a chapter:

```bash
# 1. OCR the chapter images into a raw text dump
swift _scripts/ocr.swift classes/<class>/_source-text/<ch>/textbook/*.jpg \
  > classes/<class>/_source-text/textbook/.raw-ocr/<ch>.txt

# 2. Clean the raw text into markdown
python3 _scripts/clean-ocr.py classes/<class>/_source-text/textbook <ch>
```

Same pattern works for `teaching-manual` (substitute the path).
