# Worldview — Source Text

Source-of-truth chapter content for *Understanding the Times* (Myers & Noebel). Skills (`/generate-lesson-plans`, `/generate-handout`, etc.) read from the markdown under `textbook/` and `teaching-manual/`.

## Layout

```
_source-text/
├── textbook/
│   ├── .raw-ocr/        ← raw OCR text per chapter (committed)
│   │   └── chNN.txt
│   └── chNN.md          ← cleaned markdown (committed, source of truth)
├── teaching-manual/
│   ├── .raw-ocr/
│   │   └── chNN.txt
│   └── chNN.md
└── chNN/                ← per-chapter image staging (transient)
    ├── textbook/        ← drop textbook page photos here
    └── teaching-manual/ ← drop teacher's manual page photos here
```

Image extensions (`*.jpg`, `*.jpeg`, `*.png`, `*.heic`) under `_source-text/` are gitignored. Only the cleaned markdown and raw OCR text dumps are committed.

## Per-chapter workflow

Replace `01` with the chapter number you're processing.

```bash
# 1. Drop photos into the staging folders for the chapter
classes/worldview/_source-text/ch01/textbook/IMG_*.HEIC
classes/worldview/_source-text/ch01/teaching-manual/IMG_*.HEIC

# 2. Convert HEIC → JPG (Apple Vision OCR doesn't handle HEIC directly)
./_scripts/convert-heic.sh classes/worldview/_source-text/ch01/textbook
./_scripts/convert-heic.sh classes/worldview/_source-text/ch01/teaching-manual
rm classes/worldview/_source-text/ch01/{textbook,teaching-manual}/*.HEIC

# 3. OCR → raw text (per source)
mkdir -p classes/worldview/_source-text/{textbook,teaching-manual}/.raw-ocr
swift _scripts/ocr.swift classes/worldview/_source-text/ch01/textbook/*.jpg \
  > classes/worldview/_source-text/textbook/.raw-ocr/ch01.txt
swift _scripts/ocr.swift classes/worldview/_source-text/ch01/teaching-manual/*.jpg \
  > classes/worldview/_source-text/teaching-manual/.raw-ocr/ch01.txt

# 4. Clean → final markdown
python3 _scripts/clean-ocr.py classes/worldview/_source-text/textbook 1
python3 _scripts/clean-ocr.py classes/worldview/_source-text/teaching-manual 1

# 5. Verify the markdown reads well, then delete the staging folder
rm -rf classes/worldview/_source-text/ch01/

# 6. Commit
git add classes/worldview/_source-text/
git commit -m "chore(worldview): transcribe ch01 source text"
```

## Adding a new chapter

```bash
mkdir -p classes/worldview/_source-text/chNN/{textbook,teaching-manual}
```

Then run the per-chapter workflow above with `NN` substituted.

## Re-OCR insurance

The raw OCR text dumps (`.raw-ocr/chNN.txt`) are committed. If a markdown error is later spotted that traces back to OCR (rather than cleaning), diff against the raw text. If the raw OCR itself was wrong, re-shoot the affected pages, drop them in the staging folder, and re-run from step 2.
