# Bible Curriculum

High school Bible curriculum for Watersprings School, built around Summit Ministries' *Understanding
the Times* series. Content is authored as Markdown in this repo (the source of truth), then pushed to
the school's two systems: **Rubicon Atlas** (the curriculum map) and **Google Classroom** (coursework,
tests, and slides).

## Repository structure

```
bible-curriculum/
├── CLAUDE.md              # Agentic context + how to build out a class
├── .claude/commands/      # Slash-command skills (the class-setup pipeline)
├── _shared/               # Calendar, lesson-plan standards, teaching styles, grading guides
├── _scripts/
│   ├── atlas/             # Push units + daily lessons to Rubicon Atlas (Playwright)
│   └── classroom/         # Publish to Google Classroom + Forms + Slides (Google APIs)
└── classes/               # One folder per course
    └── <class>/
        ├── teaching-map.md
        ├── syllabus/  handouts/  rubicon-atlas/
        ├── _source-text/{textbook,teaching-manual,portal}/
        └── lesson-plans-<year>/week-NN-<mon-dd>/…
```

## The three pillars of a class

1. **Repo content** — teaching map, syllabus, and week-style day-by-day lesson plans.
2. **Rubicon Atlas** — per-unit UbD fields + Madeline Hunter daily lessons (`_scripts/atlas/`).
3. **Google** — Classroom materials, a per-student worksheet, the chapter test as a **Form quiz**,
   and one **Slides deck per day** (`_scripts/classroom/`).

## Quick start (Claude Code)

The setup pipeline lives in `.claude/commands/`. **`/setup-class <class>`** runs it end to end:

```
Once per class:  /new-class → (upload syllabus) → /generate-official-syllabus → /generate-map → /scaffold-lesson-structure
Per chapter:     /build-chapter → /build-atlas → /push-atlas → /publish-chapter
```

Two lesson-plan **models**: `publisher` (default — Start-Slide template, publisher activities,
Form-quiz tests) and `cohort` (`--model cohort` — Discussion Briefs / Pair & Defend, for worldviews
and possibly apologetics). See [`_shared/lesson-plan-standards.md`](_shared/lesson-plan-standards.md).
Runbooks: [`_scripts/atlas/README.md`](_scripts/atlas/README.md) ·
[`_scripts/classroom/README.md`](_scripts/classroom/README.md). **Foundations Ch 1–2 is the worked
exemplar for all three pillars.**

## Classes (2026–27)

| Class | Grade | Status |
| --- | --- | --- |
| `to-the-ends-of-the-earth` | 8 | Not started |
| `foundations` | 9 | In progress — Ch 1–2 complete across all three pillars |
| `apologetics` | 10–11 | Not started |
| `worldviews` | 12 | Not started |

Deprecated (retained for reference): `understanding-the-times`.

## Teaching models

- **Publisher (default)** — mirrors the Summit chapter: a projectable **Start Slide**
  (Do Now · Objective · Agenda · Reminders), publisher activities, and the chapter test as a Google
  Form quiz. ~60 min (Wed ~45).
- **Cohort** — discussion-first: Discussion Brief → Pair & Defend → Case Study → Capstone. 45 min.
  See [`_shared/cohort-tools.md`](_shared/cohort-tools.md).
