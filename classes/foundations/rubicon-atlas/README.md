# Foundations — Rubicon Atlas Content (data model)

The source-of-truth content for the school's **Rubicon Atlas** curriculum map
(`watersprings.rubiconatlas.org`), course **Bible 9 Foundations**. Rubicon uses the
Understanding-by-Design framework, with one **Unit per textbook chapter** (18 total) and daily
**Lessons** inside each unit.

These files are the reviewable data model. A Playwright tool pushes them into Atlas — see the
**runbook: [_scripts/atlas/README.md](../../../_scripts/atlas/README.md)**. Review the content
here before running the fill scripts; the scripts never invent content.

## Unit fields — `unit-NN-*.md`

Five fields per unit:

1. **Unit Overview** — a paragraph
2. **Essential Questions** — open-ended UbD questions
3. **Objectives** — SWBAT learning objectives
4. **Faith Learning Integration** — how the Christian faith shapes the approach (prose reference
   only — in Atlas this is a "Choose Standards" picker, not free text, so it isn't auto-filled)
5. **Biblical Integration** — specific Scripture and biblical truths

`fill_unit.py` fills fields 1, 2, 3, and 5 (the free-text ones).

## Daily lessons — `lessons/chNN-lessons.md`

One Atlas lesson per instructional day. Each `## Day N - Title` section has `**Row Label:**
content` lines mapping to the daily **Madeline Hunter** template rows (Anticipatory Set ·
Objective and Purpose · Input · Modeling · Check for Understanding · Guided Practice ·
Independent Practice · Closure). Concise per row — the full timed plan lives in
[../lesson-plans-2026-27/chNN-lesson-plan.md](../lesson-plans-2026-27/). Only rows that apply to
a day are filled; Modeling/Guided Practice get real detail on days that have them.
`lesson_fill.py` creates + fills these.

## Files & status

- `unit-01-introduction.md` — Ch 1 unit fields (the template). **Done in Atlas** (4/5 fields).
- `lessons/ch01-lessons.md` — Ch 1's 8 daily lessons (the template). **Done in Atlas** (all 8).
- `unit-NN-*.md`, `lessons/chNN-lessons.md` — Ch 2–18, added as each chapter is built.

Each file is grounded in that chapter's transcribed source (`../_source-text/`), the
[syllabus](../syllabus/syllabus.md), and the [teaching map](../teaching-map.md). Prose is
humanized (no AI-slop tells) and cites specific manual/ST/SM page numbers.

## Academic year

The teaching map is **2026–27** and is correct. Atlas exposes 2026-27 week dates only after
**Aug 1, 2026**, so units/lessons created now carry placeholder 2025 dates; date-setting is
deferred until then (targets are in `_scripts/atlas/config.yaml`).
