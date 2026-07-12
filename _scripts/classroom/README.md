# Google Classroom + Google Drive integration

Tooling that publishes the **Bible 9 Foundations** course into Google Classroom and mirrors it in
Google Drive, driven from this repo. Owner account: **jward@waterspringsschool.net**.

Everything runs through the **official Google APIs** (Classroom + Drive) via a single OAuth token.
An earlier browser-automation approach was used once to create the class and the 18 topics; those
scripts are kept as reference (see [Legacy](#legacy-browser-automation)) but coursework, handouts,
and Drive organization all go through the API now — it is deterministic and idempotent.

## Architecture

```
this repo (source of truth)                Google (via API, as jward@waterspringsschool.net)
──────────────────────────                 ─────────────────────────────────────────────────
classes/foundations/
  lesson-plans-2026-27/   ─┐
  rubicon-atlas/unit-*.md  ├─ (authored) ─▶ Classroom  Bible 9 Foundations
  handouts/*.md            ─┘                 ├─ 18 Topics  (= units, "01: Introduction" …)
_scripts/classroom/                           └─ per topic: Materials + Assignments (drafts)
  content/<unit>/*.txt  (item copy)
  cl.py + build/create scripts ───────────▶ Drive  Classroom/Bible 9 Foundations/
                                              └─ one subfolder per unit  ← handout Google Docs
```

**Mapping.** 1 Classroom class = the course · 1 Topic = 1 unit (chapter) · Materials/Assignments =
the unit's coursework · Drive mirrors it (a folder per unit holding that unit's Docs).

**Source-of-truth model.** The repo markdown is what we *generate from*. Handouts become **Google
Docs** in Drive (editable by the teacher, and what students download). Small edits happen in the
Doc; substantive/bulk changes happen in the repo markdown and are re-generated.

## Current state

- **Course:** Bible 9 Foundations · Section Grade 9 · course id `855510334007` ·
  class code `kegl4xsb` · <https://classroom.google.com/c/ODU1NTEwMzM0MDA3>
- **Topics:** 18, named exactly like the Atlas units (`01: Introduction` … `18: Conclusion`).
- **Units 01–02 built** (all **drafts**, hidden from students until posted). Each has: Start Here +
  Readings materials, editable Doc references (Study Guide + a per-chapter reference — *Six Acts* for
  Ch 1, *Key Concepts* for Ch 2), a **per-student video worksheet** assignment, and the **chapter
  test as a Google Form quiz** (Ch 1: 87 pts / 54 auto; Ch 2: 84 pts / 65 auto). Each day also has a
  **Google Slides deck** in the unit's `Slides/` folder (built by `build_slides.py`).
- **Drive:** `Classroom/Bible 9 Foundations/` (Google-created course folder) holds an
  `01: Introduction/` … `18: Conclusion/` subfolder each; handout Docs auto-file into their unit
  folder, and daily decks into `<unit>/Slides/`.
- **Dates:** deferred — Classroom exposes 2026-27 week dates only after Aug 1, 2026.

## Setup (one-time, already done)

Google Cloud project **Watersprings Teaching** (`watersprings-teaching`, in the
`waterspringsschool.net` org):

1. Enabled APIs: **Google Classroom API**, **Google Drive API**.
2. OAuth consent screen: **Internal** (Workspace org → no Google verification needed).
3. Credential: **OAuth client ID → Desktop app**, downloaded to `credentials.json` (gitignored).
4. Python env + authorization:

   ```bash
   python3 -m venv _scripts/classroom/.venv
   _scripts/classroom/.venv/bin/pip install -r _scripts/classroom/requirements.txt
   _scripts/classroom/.venv/bin/python _scripts/classroom/auth_api.py   # browser consent → token.json
   ```

Re-run `auth_api.py` whenever the scope list changes (it re-consents and overwrites `token.json`).

### Scopes (`auth_api.py`)
- `classroom.courses` — the class
- `classroom.topics` — unit topics
- `classroom.courseworkmaterials` — materials (Start Here, Readings, Study Guide)
- `classroom.coursework.students` — assignments (reflection, test)
- `drive` (full) — organize Drive into the Classroom-created course folder (the folder was made by
  Classroom, not this app, so `drive.file` can't reach it — full `drive` is required to add the
  unit subfolders and move Docs in)
- `forms.body` — create/edit the Google Form chapter-test quizzes (`build_form.py`). **Added after
  the initial setup** — enable the **Google Forms API** in the Cloud project, then re-run
  `auth_api.py` to re-consent.

## Scripts

Run everything with the venv: `_scripts/classroom/.venv/bin/python _scripts/classroom/<script>.py`

| Script | Purpose |
| --- | --- |
| `auth_api.py` | One-time OAuth consent (`credentials.json` → `token.json`). |
| `cl.py` | Shared helpers: `service()` / `drive_service()`, `course_id()`, `topics()`, `existing_titles()`, `teacher_folder()`, `ensure_folder()`, `move_file()`. |
| `create_class_api.py` | Create (or find) the course. Idempotent by name. |
| `build_unit01.py` | Create Unit 01's text materials + the Video Reflection assignment as drafts under `01: Introduction`. Idempotent (skips existing titles). (The test is built by `build_form.py`, not here.) |
| `build_form.py` | `--spec <form.json> [--desc <txt>] [--force]`. Builds a chapter test as a **Google Form quiz** (point values + correct answers), files it in the unit's Drive folder, and attaches it to the matching Classroom assignment as a link (Classroom then offers grade import). Needs the `forms.body` scope. |
| `create_doc_material.py` | `--md <file> --topic "<unit>" --title "<name>" [--desc …] [--post]`. Renders markdown → a **Google Doc** in the unit's Drive folder → attaches it to the topic as a material (draft by default). Reusable for any handout. |
| `build_doc_assignment.py` | `--md <file> --topic "<unit>" --title "<name>" --points N [--desc …] [--replace "<old title>"] [--force]`. Renders markdown → a **Google Doc** worksheet → attaches it to a new **assignment** as a **per-student copy** (`STUDENT_COPY`). Used for written worksheets students fill in and submit (e.g. the video questions). |
| `build_slides.py` | `<day.md> [<day.md> …]`. Generates a **Google Slides** deck per day: slide 1 is a styled Start Slide (Do Now / Objective / Agenda / Reminders + "today is …" header) mimicking the classroom template; the rest are one slide per item in that day's *Slide-Deck Outline*. The day `.md` is the source of truth. Files decks into `<unit>/Slides/` in Drive. Needs the `presentations` scope. Teacher decks — not attached to Classroom. |
| `organize_drive.py` | Create the per-unit Drive subfolders inside the course folder and move listed Docs into their unit folder. Idempotent. |

### Recipes

Add a handout (e.g. a study guide) — author `classes/foundations/handouts/<name>.md`, then:

```bash
_scripts/classroom/.venv/bin/python _scripts/classroom/create_doc_material.py \
  --md classes/foundations/handouts/ch01-study-guide.md \
  --topic "01: Introduction" --title "Unit 1 · Study Guide" \
  --desc "Downloadable study guide for the Chapter 1 Test."
```

Add the Six Acts reference (a Doc material):

```bash
_scripts/classroom/.venv/bin/python _scripts/classroom/create_doc_material.py \
  --md classes/foundations/handouts/ch01-six-acts.md \
  --topic "01: Introduction" --title "Unit 1 · Six Acts of the Bible" \
  --desc "The spine of the whole course — learn the six acts in order."
```

Build a unit's coursework — copy `build_unit01.py`, edit the `ITEMS` list + `content/<unit>/`
copy, run it. (Generalizing this into one `build_unit.py` that reads a per-unit manifest is the
next step for the 02–18 rollout.)

## Chapter tests → Google Form quizzes (`build_form.py`)

A chapter test is authored once as a JSON **build spec** and turned into a Google Form quiz.
Source of truth: the human-readable transcription lives at `classes/foundations/_source-text/
portal/chNN/test.md`; the machine spec lives at `content/unitNN/chapter-N-test.form.json`. Keep
the two in sync.

The spec marks each question's type, points, and correct answer(s). Auto-graded types: matching
(dropdowns), multiple choice (checkboxes), true/false (radio), fill-in-the-blank (short text).
Hand-graded: short answer + essay (paragraphs — point value only, graded in the Form).

**Multi-answer MC is all-or-nothing** in Forms (full points only for an exact match). The publisher
awards 1 pt per correct answer, so for partial-credit cases the teacher bumps the score in the
Forms grading view. (See the `simplify`/decision note in the repo history.)

### One-time enablement (interactive — cannot be done headless)

1. In the Cloud project **Watersprings Teaching**, enable the **Google Forms API**.
2. Re-consent to the new scope (opens a browser):

   ```bash
   _scripts/classroom/.venv/bin/python _scripts/classroom/auth_api.py
   ```

### Build the Chapter 1 test

```bash
_scripts/classroom/.venv/bin/python _scripts/classroom/build_form.py \
  --spec _scripts/classroom/content/unit01/chapter-1-test.form.json \
  --desc _scripts/classroom/content/unit01/chapter-test.txt
```

This creates the Form, files it in `01: Introduction/` in Drive, and (re)creates the *Chapter 1
Test* assignment (draft, /87) with the Form attached. **Verify in the UI on first run:** open the
Form (question rendering, points, correct answers) and the Classroom assignment (that "Import
grades" appears). Re-run with `--force` to rebuild.

## Daily slide decks (`build_slides.py`)

One Google Slides deck per teaching day, generated from the day's lesson-plan `.md` (the source of
truth). Slide 1 is a styled **Start Slide** (Do Now / Objective / Agenda / Reminders + a "today is
…" header) that mimics the classroom start-slide template; the rest are one slide per item in that
day's *Slide-Deck Outline*. The chapter number + unit are read from each file's `**Chapter:** Ch N`
line, so decks auto-file into the right `<unit>/Slides/` folder — teacher decks, not Classroom
materials. Layout + accent colors approximate the template, not its hand-lettered fonts.

One-time: enable the **Google Slides API** in the Cloud project and re-run `auth_api.py` (adds the
`presentations` scope). Then, for Chapter 1's eight days:

```bash
_scripts/classroom/.venv/bin/python _scripts/classroom/build_slides.py \
  classes/foundations/lesson-plans-2026-27/week-01-aug-24/{1-monday,2-tuesday,3-wednesday,4-thursday,5-friday}.md \
  classes/foundations/lesson-plans-2026-27/week-02-aug-31/{1-monday,2-tuesday,3-wednesday}.md
```

Re-running creates fresh decks (it does not update in place) — trash the old ones if you rebuild.

## Legacy (browser automation)

Used once, over a persistent authenticated Chrome on CDP `:9222`, to create the class and the 18
topics before the API path existed. Kept for reference; not needed for ongoing work.

- `open_signin.py` — point the watchable Chrome at Google sign-in.
- `check_login.py` — report the signed-in account / Classroom state (read-only).
- `create_class.py` — create the class via the "Create class" UI.
- `create_topics.py` — create the 18 topics (reads names from the Atlas `unit-*.md` files).

These use the Atlas venv's Playwright: `_scripts/atlas/.venv/bin/python …`.

## Security

`credentials.json`, `token.json`, `.venv/`, and `probe-output/` (screenshots can show the account)
are gitignored — never commit them. The token grants access to the teacher's Google account; treat
it like a password.
