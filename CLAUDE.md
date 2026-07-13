# Bible Curriculum — Agentic Context

## Project Overview

This is a personal curriculum repository for a high school Bible teacher at Watersprings School. It contains 4–6 courses built on the *Understanding the Times* series. Courses use a cohort-style, discussion-first teaching model where students engage with ideas through structured dialogue, case studies, and peer defense before lecture.

## Repo Conventions

- All content is Markdown.
- `_skill/` contains the reusable teaching map generator skill.
- `_shared/` contains content reused across classes (calendar, tools, resources).
- Each class lives in `classes/<class-name>/` with subfolders: `lesson-plans/`, `assessments/`, `handouts/`.
- File naming: lowercase, hyphenated, prefixed with chapter number — e.g. `ch01-lesson.md`, `ch01-test.md`, `ch03-case-study.md`.

## Automation & integrations (`_scripts/`)

- `_scripts/atlas/` — pushes the Rubicon Atlas curriculum map (unit fields + daily lessons) from
  the repo data model. Runbook: [`_scripts/atlas/README.md`](_scripts/atlas/README.md).
- `_scripts/classroom/` — publishes the **Google Classroom** class and mirrors it in **Google
  Drive** (topics = units, materials/assignments as drafts, handouts as editable Google Docs filed
  into per-unit Drive folders), via the official Google APIs on `jward@waterspringsschool.net`.
  Runbook: [`_scripts/classroom/README.md`](_scripts/classroom/README.md). Secrets
  (`credentials.json`, `token.json`) are gitignored.

## How to Set Up / Build Out a Class

A complete class spans **three pillars**: repo content · **Rubicon Atlas** (Playwright) · **Google**
(Classroom/Forms/Slides). The slash-command pipeline (in `.claude/commands/`) covers all three;
**`/setup-class <class>`** orchestrates it end to end. Per chapter: `/build-chapter` (week-style daily
plans) → `/build-atlas` (unit fields + daily lessons) → `/push-atlas` → `/publish-chapter`. The
lesson-plan template + the two models (`publisher` default / `cohort` for worldviews/apologetics) are
defined in [`_shared/lesson-plan-standards.md`](_shared/lesson-plan-standards.md). Runbooks:
[`_scripts/atlas/README.md`](_scripts/atlas/README.md), [`_scripts/classroom/README.md`](_scripts/classroom/README.md).
**Foundations Ch 1–2 is the worked exemplar for all three pillars.**

## How to Generate a New Teaching Map

1. Read `_skill/SKILL_cohort_teaching_map.md` for the full process.
2. Read `_shared/school-calendar-2026-27.md` for no-school dates.
3. Ask the teacher for the syllabus/chapter list if not already provided.
4. Generate the teaching map and write it to `classes/<class-name>/teaching-map.md`.

## Tone & Style

- All teacher-facing docs: professional but warm.
- All student-facing handouts: clear, direct, age-appropriate for 11th–12th grade.
- Avoid edu-jargon. Write like a thoughtful teacher, not a textbook.

## Current Classes

The school updated the curriculum for 2026–27. Four new classes replace the prior
lineup; the old classes are retained for reference during the transition.

**New curriculum (2026–27):**

| Class | Grade | Status |
| --- | --- | --- |
| `to-the-ends-of-the-earth` | 8 | Not started. |
| `foundations` | 9 | Being built. Source text transcription in progress (18 chapters). |
| `apologetics` | 10–11 | Being built. Stage 0 done (18 ch, UtT Book II; publisher model + surgical debate days). **Ch 1 complete across all three pillars** (repo plans · Atlas unit 2242 + 8 lessons · Classroom drafts: materials, Form quiz, 8 Slides). Atlas/Classroom tooling now multi-course. Ch 2–18 pending. |
| `worldviews` | 12 | Not started. |

**Deprecated (retained for reference):**

| Class | Grade | Status |
| --- | --- | --- |
| `understanding-the-faith` | 11–12 | Deprecated. Teaching map + lesson plans complete. |
| `worldview` | 11–12 | Deprecated. Superseded by 12th-grade `worldviews`. |
