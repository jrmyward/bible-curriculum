---
name: build-chapter
description: Build one chapter's week-style daily lesson plans (rich Start-Slide template)
args: "<class-name> <chapter-number> [--model publisher|cohort] [--year YYYY-YY]"
---

# Build Chapter — daily lesson plans

Generate a chapter's day-by-day lesson plans in the **week-directory** structure, one file per
weekday, using the canonical template. This is the content-authoring step; the Atlas and Google
pushes are separate (`/build-atlas` + `/push-atlas`, `/publish-chapter`).

## Usage

```bash
/build-chapter foundations 3
/build-chapter worldviews 1 --model cohort
/build-chapter apologetics 2 --year 2026-27
```

## The one reference to read first

**Read [`_shared/lesson-plan-standards.md`](../../_shared/lesson-plan-standards.md) before writing
anything.** It defines both models, the exact day-file template (the ★ sections the `/build-slides`
parser depends on), the no-school marker convention, and the chapter-crosses-week rule. Match the
[Foundations Ch 1 exemplar](../../classes/foundations/lesson-plans-2026-27/week-01-aug-24/) for tone
and depth.

## Model

- **`--model publisher` (default)** — Summit publisher-activity template (Start Slide · Supplies ·
  Teaching Outline · Slide-Deck Outline · Board Plan · Exit Ticket · Links; ~60 min, Wed ~45).
- **`--model cohort`** — discussion-first template (Discussion Briefs / Pair & Defend / Case Studies;
  45 min). Use for worldviews (and optionally apologetics). Cohort tools: `_shared/cohort-tools.md`.

If `--model` is omitted, use the model **recorded in the class README** at the post-OCR checkpoint
(`/setup-class` Stage 0); fall back to `publisher`. A **blend** is valid — publisher structure with
cohort discussion moves layered in where the source text invites it (see the blending note in the
standards doc). If the README still says model = TBD, stop and hold the model checkpoint first.

## Process

### 1. Resolve inputs & dates
- Class dir `classes/<class>/`; year from `--year` or the existing `lesson-plans-<year>/`.
- Read the teaching map (`classes/<class>/teaching-map.md`) for this chapter's dates, day count,
  topic, activities, and test date.
- Read [`_shared/school-calendar-<year>.md`](../../_shared/school-calendar-2026-27.md) — the **source
  of truth** for no-school days and teacher-absence (sub) days.

### 2. Map the chapter onto calendar weeks
- An ~8-day chapter spans ~2 `week-NN-<mon-dd>/` folders and may start mid-week. Lay every
  instructional day into the folder for its real calendar week.
- Mark no-school days as **marker files** (not lessons). Leftover weekdays past the chapter boundary
  become **stubs** for the next chapter.
- Put the test and any single-activity/review days on Wednesdays (short days) where the map allows.

### 3. Gather source content
- Prefer an existing chapter-file draft (`classes/<class>/lesson-plans-<year>/chNN-lesson-plan.md`) —
  convert it into the per-day template, then **delete the chapter-file** and update the folder README
  status table (as done for Foundations Ch 1–2).
- Otherwise read `classes/<class>/_source-text/{textbook,teaching-manual}/chNN.md` (or images) and the
  publisher test at `_source-text/portal/chNN/` to aim the review at what the test asks.
- **Always cite specific page numbers** (ST / SM / manual p.).

### 4. Write the files
For each instructional day, write `<n>-<weekday>.md` per the template in the standards doc — including
a projectable **🟦 Start Slide** (Do Now · Objective · Agenda · Reminders) and a **Slide-Deck Outline**
(so `/build-slides` can generate the deck). Also write/refresh:
- the week `README.md`(s) (overview, prep, post-week notes),
- `substitute-plan-<day>.md` for each teacher-absence day (self-contained; see `/generate-substitute-plan`),
- no-school marker files and next-chapter stubs.

### 5. Verify
- Confirm the ★ sections parse: run the slides parser offline —
  `_scripts/classroom/.venv/bin/python -c "import sys;sys.path.insert(0,'_scripts/classroom');import build_slides as b,pathlib;print(b.parse_day(pathlib.Path('<file>').read_text()))"`
  and check `weekday/date/do_now/objective/agenda/reminders` are all populated.
- Cross-check against the teaching map: every activity covered, assessments placed, no-school days
  accounted for, correct chapter/sections.

### 6. Report
List files created, the chapter→week mapping, and the next steps:
`/build-atlas <class> <N>` (Atlas data models) → `/push-atlas` and `/publish-chapter <class> <N>`.

## Notes
- Humanize the prose before finishing (run the `humanizer` skill) — strip AI-slop tells.
- Keep the week before Christmas break and the last week of school light/instruction-free.
- This skill writes repo files only; it never touches Atlas or Google.
