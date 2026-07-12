---
name: publish-chapter
description: Publish a chapter to Google — Classroom coursework, Form quiz test, and daily Slides
args: "<class-name> <chapter-number>"
---

# Publish Chapter to Google

Roll a chapter out to Google for the class's Classroom course: reference **Docs**, a per-student
**video worksheet**, the chapter **test as a Google Form quiz**, and one **Slides deck per day** —
all as **drafts** (hidden from students until posted). Wraps the tools in `_scripts/classroom/`.

## Usage

```bash
/publish-chapter foundations 3
```

## Prerequisites

- ✅ Daily plans exist (`/build-chapter`) — the Slides decks are generated from them.
- ✅ Publisher test PDF at `classes/<class>/_source-text/portal/chNN/` (editable + answer key).
- ✅ Classroom integration authorized (token + APIs). One-time: enable the **Classroom, Drive, Forms,
  and Slides** APIs and run `_scripts/classroom/auth_api.py` to consent. See
  [`_scripts/classroom/README.md`](../../_scripts/classroom/README.md).
- ⚠️ **Scoped to the existing course.** `_scripts/classroom` targets `COURSE_NAME = "Bible 9
  Foundations"` and its 18 topics. Publishing a *different* class first requires generalizing the
  integration (create the Classroom class + topics + per-course config) — flag this and stop if the
  class isn't wired up yet.

## Process

Run each with the venv: `_scripts/classroom/.venv/bin/python _scripts/classroom/<script>.py`.

### 1. Test → source of truth
- Transcribe `portal/chNN/` (test + answer key PDFs) → `classes/<class>/_source-text/portal/chNN/test.md`
  (human-readable) and author `_scripts/classroom/content/unitNN/chapter-N-test.form.json`
  (machine build spec: type, points, correct answers per question). **Compute the real total** and
  set `totalPoints`; the builder asserts the sum matches.
- Objective items (matching→dropdown, multi-answer MC→checkbox, T/F→radio, fill-in→short-text) are
  auto-keyed; short-answer + essay are paragraph items (points only, hand-graded). Multi-answer MC is
  all-or-nothing in Forms — the teacher bumps partial credit in the grading view.

### 2. Content files + handouts
- `_scripts/classroom/content/unitNN/`: `start-here.txt`, `readings.txt` (aligned to the day
  schedule), `video-questions.txt` (worksheet assignment description), `chapter-test.txt` (Form
  assignment description).
- Handouts (become Google Docs): `classes/<class>/handouts/chNN-study-guide.md`,
  `chNN-<reference>.md` (a per-chapter reference — the "Six Acts"/"Key Concepts" analog), and
  `chNN-video-questions.md` (the per-student worksheet: the videos' questions).

### 3. Build in Classroom (all drafts)
```bash
build_unitNN.py                     # Start Here + Readings materials (copy build_unit02.py; set TOPIC)
create_doc_material.py --md <study-guide.md> --topic "NN: <Topic>" --title "Unit N · Study Guide" --desc "…"
create_doc_material.py --md <reference.md>   --topic "NN: <Topic>" --title "Unit N · <Reference>"   --desc "…"
build_doc_assignment.py --md <video-questions.md> --topic "NN: <Topic>" --title "Video Questions — Chapter N" --points 20 --desc content/unitNN/video-questions.txt
build_form.py --spec content/unitNN/chapter-N-test.form.json --desc content/unitNN/chapter-test.txt
```

### 4. Slides — one deck per day
```bash
build_slides.py classes/<class>/lesson-plans-<year>/week-*/<the chapter's day files>.md
```
Decks auto-file into `<NN: Topic>/Slides/` (the chapter number is read from each file's
`**Chapter:** Ch N` line).

### 5. Verify
- Read the Form back (quiz mode on, question count, total points, auto-keyed count).
- List the unit's Classroom items + the `Slides/` folder to confirm counts.
- **First run:** eyeball the Form + a deck in the UI, and confirm the test assignment shows
  "Import grades."

## Reference

[`_scripts/classroom/README.md`](../../_scripts/classroom/README.md) documents every script, the
scopes, and the recipes. Foundations Ch 1–2 (`content/foundations/unit01/`, `unit02/`) are the
exemplars. All scripts take `--course <class-key>` (from `courses.json`); provision a new class's
course + topics with `create_class_api.py` + `create_topics_api.py` first.
