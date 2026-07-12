---
name: setup-class
description: End-to-end setup for a new class — content, Rubicon Atlas, and Google
args: "<class-name> [--model publisher|cohort] [--year YYYY-YY]"
---

# Set Up a Class from Scratch

The front-to-back orchestrator. Stands up a brand-new class across all **three pillars**, then drives
it chapter by chapter. It doesn't reimplement the stages — it sequences the focused commands and
tracks where you are, pausing for the human-in-the-loop steps (image uploads, reviews, live browsers).

**The three pillars of a complete class:**

1. **Repo content** — syllabus, teaching map, week-style daily lesson plans.
2. **Rubicon Atlas** — unit UbD fields + Madeline Hunter daily lessons (Playwright push).
3. **Google** — Classroom coursework, the test as a Form quiz, and daily Slides decks.

## Usage

```bash
/setup-class apologetics
/setup-class worldviews --model cohort
```

## Stage 0 — Class shell + source text (once)

1. `/new-class <class>` — create `classes/<class>/` (README, `syllabus/`, `handouts/`,
   `_source-text/{textbook,teaching-manual,portal}/`, `rubicon-atlas/lessons/`) and add it to the
   CLAUDE.md Current Classes table. **Model = TBD** (decided at the checkpoint below, not now).
2. Determine the chapter count; scaffold `_source-text/chNN/` as needed. Upload the textbook +
   teacher-manual images (**HEIC ok — convert to JPEG first**) and the `portal/` assets.
3. `/transcribe-source-text <class>` — OCR/transcribe the images to `_source-text/**/chNN.md`.
4. **⛑ Model checkpoint (after OCR, before building) — a genuine stop-and-talk point; don't
   auto-pick.** Read the OCR'd source text *together* and decide the model. The publisher's own
   material often builds in discussion/activity structure, so this can't be decided blind up front.
   Discuss: `publisher` (default), `cohort` (`--model cohort`), or a **blend** (publisher structure +
   cohort discussion moves — see the blending note in the standards doc). Record the decision in the
   class README.
5. `/generate-official-syllabus <class>` (from `syllabus/` images) and `/generate-map <class>` — the
   teaching map (pacing, units, sub days). Confirm `_shared/school-calendar-<year>.md` covers the year.
6. `/scaffold-lesson-structure <class>` — week folders, READMEs, `.generation-log.md` (now that the
   model is known, so cohort rubric stubs are created only if chosen).

Also confirm the class's **Google** container (Classroom course + topics) and **Atlas** units exist
or need creating (see the per-chapter Google/Atlas steps).

## Stage 1 — Per chapter (loop)

For each chapter N, in order:

1. **Content** — `/build-chapter <class> N [--model …]` → week-style daily plans (+ sub plans,
   no-school markers, week READMEs). Needs the chapter's `_source-text` / portal test staged.
2. **Atlas data** — `/build-atlas <class> N` → `rubicon-atlas/unit-NN-*.md` + `lessons/chNN-lessons.md`.
   **Review with the teacher.**
3. **Atlas push** — `/push-atlas <class> N` → fills the unit + daily lessons in Rubicon Atlas
   (persistent Chrome; watchable).
4. **Google** — `/publish-chapter <class> N` → Classroom materials + video worksheet + Form-quiz test
   + daily Slides decks (all drafts).

Track progress in `.generation-log.md`. Do a few chapters, review, continue — this is designed to be
resumable across sessions (re-run `/setup-class <class>` and it reports what's done vs. pending).

## Human-in-the-loop checkpoints (don't skip)

- **Uploads:** syllabus images (Stage 0); per-chapter textbook/manual images + the publisher test PDF.
- **Reviews:** the teaching map, and each chapter's Atlas data models, before pushing.
- **Live browsers / auth:** Atlas push needs the CDP Chrome up (`/push-atlas` setup); Google needs the
  APIs enabled + `auth_api.py` consented once.
- **Drafts:** Classroom items publish as drafts — nothing reaches students until the teacher posts.

## What "done" looks like for a class

- All chapters have week-style daily plans + Slides decks.
- Every unit's fields + daily lessons are in Rubicon Atlas.
- Every chapter's Classroom coursework (materials, worksheet, Form-quiz test) exists as drafts.
- Sub days have substitute plans; no-school days are marked; the status table is current.

## Reference

- Lesson-plan template + models: [`_shared/lesson-plan-standards.md`](../../_shared/lesson-plan-standards.md)
- Atlas runbook: [`_scripts/atlas/README.md`](../../_scripts/atlas/README.md)
- Google runbook: [`_scripts/classroom/README.md`](../../_scripts/classroom/README.md)
- Exemplar (all pillars done): **Foundations** Ch 1–2.
