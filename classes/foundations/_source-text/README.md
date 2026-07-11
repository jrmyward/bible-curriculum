# Foundations — Source Material

All publisher-provided source material for the 9th-grade Foundations course, in one place:
the transcribed textbook + teacher manual, and the downloaded portal resources.
Skills read from the cleaned markdown under `textbook/`, `teaching-manual/`, and `portal/`.

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
└── portal/              ← publisher portal downloads (tests, quizzes, study guides, slides)
    ├── _course/         ← course-wide docs
    └── chNN/            ← per-chapter resources; see portal/README.md
```

All 18 chapters are transcribed. During transcription, page photos live in transient
per-chapter staging folders (`chNN/textbook/`, `chNN/teaching-manual/`) that are gitignored
and **deleted after cleaning** — the committed `.raw-ocr/chNN.txt` dumps are the re-OCR
insurance. To transcribe a re-shot chapter, recreate its staging folder (below) and run the
workflow; delete it again when done.

Image extensions (`*.jpg`, `*.jpeg`, `*.png`, `*.heic`) under `_source-text/` are gitignored
so raw scans never get committed — **except** under `portal/`, where downloaded resources
(including image-format slides) ARE committed. See the repo `.gitignore`.

## Per-chapter workflow

Replace `01` with the chapter number you're processing.

```bash
# 1. Drop photos into the staging folders for the chapter
classes/foundations/_source-text/ch01/textbook/IMG_*.HEIC
classes/foundations/_source-text/ch01/teaching-manual/IMG_*.HEIC

# 2. Convert HEIC → JPG (Apple Vision OCR doesn't handle HEIC directly)
./_scripts/convert-heic.sh classes/foundations/_source-text/ch01/textbook
./_scripts/convert-heic.sh classes/foundations/_source-text/ch01/teaching-manual
rm classes/foundations/_source-text/ch01/{textbook,teaching-manual}/*.HEIC

# 3. OCR → raw text (per source)
swift _scripts/ocr.swift classes/foundations/_source-text/ch01/textbook/*.jpg \
  > classes/foundations/_source-text/textbook/.raw-ocr/ch01.txt
swift _scripts/ocr.swift classes/foundations/_source-text/ch01/teaching-manual/*.jpg \
  > classes/foundations/_source-text/teaching-manual/.raw-ocr/ch01.txt

# 4. Clean → final markdown
python3 _scripts/clean-ocr.py classes/foundations/_source-text/textbook 1
python3 _scripts/clean-ocr.py classes/foundations/_source-text/teaching-manual 1

# 5. Verify the markdown reads well, then delete the staging folder
rm -rf classes/foundations/_source-text/ch01/

# 6. Commit
git add classes/foundations/_source-text/
git commit -m "chore(foundations): transcribe ch01 source text"
```

## Adding a new chapter

```bash
mkdir -p classes/foundations/_source-text/chNN/{textbook,teaching-manual}
```

Then run the per-chapter workflow above with `NN` substituted.

## Re-OCR insurance

The raw OCR text dumps (`.raw-ocr/chNN.txt`) are committed. If a markdown error is later
spotted that traces back to OCR (rather than cleaning), diff against the raw text. If the
raw OCR itself was wrong, re-shoot the affected pages, drop them in the staging folder,
and re-run from step 2.
