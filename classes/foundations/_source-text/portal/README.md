# Foundations — Publisher Portal Resources

Downloaded teaching materials from the Summit portal (summitportal.org) for the
*Foundations* course: chapter tests, answer keys, quizzes, student Study Guides,
slides, and any course-wide documents.

These are **reused as-is** under the course's "lean layer" approach — the class does not
regenerate what the publisher already provides (see [../../teaching-map.md](../../teaching-map.md)).

## Layout

```text
portal/
├── _course/          ← course-wide: official syllabus, scope & sequence, rubrics, master slides
└── chNN/             ← per chapter (01–18)
    ├── test.pdf              (publisher TR NN.10A chapter test)
    ├── test-answer-key.pdf
    ├── quiz.pdf              (if any)
    ├── study-guide.pdf       (student-manual study guide)
    ├── slides.pdf            (or .pptx)
    └── test.md / study-guide.md   ← markdown transcription (skills read these)
```

## Conventions

- **Preferred format: PDF.** Export each Google Doc to PDF (print-ready, faithful to the
  publisher layout). Export to `.docx` instead only for docs you intend to edit (e.g., a
  test you'll trim for the compressed pacing).
- **PDFs are committed** (a backup of the teaching materials). The usual `_source-text`
  image-ignore rules are negated under `portal/` — see the repo `.gitignore` — so charts
  exported as images are committed too. **Exception: slide decks are kept local, not
  committed** (they're large presentation files); anything named `*slides*.pdf`, `*.pptx`,
  or `*.key` under `portal/` is gitignored.
- **Naming:** lowercase, hyphenated, descriptive (`test.pdf`, `test-answer-key.pdf`,
  `study-guide.pdf`, `quiz.pdf`, `slides.pdf`). Keep the chapter number in the folder, not
  every filename.
- **Markdown transcriptions:** because these are born-digital (selectable text), the
  assessable docs (tests, quizzes, study guides) can be converted to markdown with no OCR
  loss. Skills read the `.md` to align each chapter's review day to what the test asks.
  The PDF stays as the print-ready artifact.

## Getting resources in

1. Log in to summitportal.org and export each chapter's Google Docs to PDF.
2. Drop them into the matching `chNN/` folder using the names above.
3. Ask Claude to transcribe the assessable docs to markdown and commit.
