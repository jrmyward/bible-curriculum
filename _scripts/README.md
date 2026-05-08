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
swift _scripts/ocr.swift --min-confidence 0.5 classes/<class>/_source-text/ch01/textbook/*.jpg > ch01.txt
```

Each image's text is preceded by `=== <filename> ===`. The script tries all four 90° orientations and picks the one with the most recognized characters, so rotated phone photos work without manual rotation.

**`--min-confidence VALUE`** (default 0.0): drop text observations below this confidence floor. Useful for skipping handwriting and other low-confidence content. Empirical guidance:

- `0.5` filters most clear handwriting; risk of dropping smudgy printed text
- `0.4` more lenient; keeps marginal printed content
- `0.0` (default) keeps everything Vision recognized

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
- Drops standalone page-number lines from body content
- Replaces `=== IMG_NNNN.jpg ===` markers with `<!-- page-N (book p.X) -->` comments. The book page number is detected from the first/last 3 non-empty lines of each block (where headers/footers live); falls back to `<!-- page-N -->` if no plausible page number is found
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
