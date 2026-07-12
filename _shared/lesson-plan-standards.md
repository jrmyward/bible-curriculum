# Lesson Plan Quality Standards

Generated lesson plans must meet these standards. There are **two lesson-plan models** — pick per
class:

- **Publisher model (default)** — for the Summit *Understanding the Times* classes (To the Ends of
  the Earth · Foundations · Apologetics · Worldviews). Publisher-activity–driven, ~60 min (Wed ~45).
  This is the format built for **Foundations Ch 1–2** and the default for new classes.
- **Cohort model (`--model cohort`)** — discussion-first, 45 min, Discussion Briefs / Pair & Defend /
  Case Studies. The deprecated *worldview* class used this. Choose it for **worldviews** (and possibly
  **apologetics**) when you want the debate-heavy rhythm.

Both models share the week-directory convention and the quality bar further down.

---

## Directory & file conventions (both models)

```
classes/<class>/lesson-plans-<year>/
  README.md                     ← format status + chapter→week map
  week-NN-<mon-dd>/             ← one folder per CALENDAR week (Mon start date)
    README.md                   ← week overview + post-week notes
    1-monday.md … 5-friday.md   ← one file per weekday (number prefix keeps order)
    substitute-plan-<day>.md    ← teacher-absence days
    handouts/                   ← week-specific handouts
```

- **Chapters cross week boundaries.** An 8-day chapter spans ~2 calendar-week folders. Put each day
  in the folder for its real calendar week; a chapter can start mid-week (e.g. Foundations Ch 2 Day 1
  is a Thursday). The week folder — not the chapter — owns the five weekday files.
- **No-school days get a marker file**, not a lesson. A `1-monday.md` that lands on Labor Day is a
  short file: `# Mon Sep 7, 2026 · **NO SCHOOL**` + reason + pointer to the next instructional day.
  The [school calendar](school-calendar-2026-27.md) is the source of truth for these.
- **Chapter boundaries that fall inside a week** leave the rest of the week as **stubs** for the next
  chapter (a placeholder day file that says which chapter/day it will hold).
- **Period length:** publisher model ~60 min most days, **~45 on Wednesdays** (short day — label the
  header `· *short day*` and put tests/review/single-activity days there). Cohort model = 45 min.

---

## Publisher day-file template (the default — exact structure)

Every instructional day is one file with **these sections, in this order**. The
[`/build-slides`](../_scripts/classroom/build_slides.py) generator parses the marked-★ sections, so
their formatting must match exactly.

```markdown
# Day N — <Weekday Mon DD, YYYY>            (append " · *short day*" / " · **TEST**" as needed)

**Chapter:** Ch N — *Chapter Title* (Day N of M)        ★ (chapter number is read from here)
**Publisher lesson:** Lesson X (§§N.a–N.b) · **Reading:** ST pp–pp
**Period:** ~60 min                                       (or "~45 min (Wednesday short day)")
**Prep flag:** ⚠️ <what to print/queue beforehand>

---

## 🟦 Start Slide — *project as students enter* · **Today is <Weekday> · <Month DD>**   ★

**Do Now** — <bell-ringer prompt>                         ★
**Objective** — I can <student-friendly "I can…">          ★
**Agenda**                                                ★
1. <step>
2. <step>
**Reminders** — Due today: … · Homework: … · <announcements>   ★  (carries Due Today + Assignment)

---

## Supplies & Prep
## Learning Objectives          (teacher; tie each to publisher §§, e.g. `[1.2]`)
## Teaching Outline (~NN min)   (### time-cued segments: `### 0:00–0:06 · <segment>`)
## Slide-Deck Outline — *paste into Google Slides*    ★
1. **Start Slide** — Do Now · Objective · Agenda · Reminders
2. **<Slide title>** — bullet · bullet · bullet         ★ (title in **bold**, bullets after "—", split on " · ")
…
## Board Plan · Key Terms & Verses
## Announcements & Assignments   (Homework · Due next · Collected today)
## Exit Ticket
## Teacher Notes & Flex
## Links                         (source text, teacher manual pages, study guide, teaching map)
```

**Rules for the ★ sections** (so slides + downstream tooling parse cleanly):

- Start Slide header must contain `**Today is <Weekday> · <Month DD>**`.
- `**Do Now**`, `**Objective**`, `**Reminders**` are each one line beginning with `**Label** —`.
- `**Agenda**` is followed by a numbered list.
- Slide-Deck Outline items are `N. **Title** — bullet · bullet` (bullets separated by ` · `). The
  first item is always the Start Slide and is skipped by the generator (it renders the styled one).
- A minimal day (test day, sub day) may have a short Slide-Deck Outline or none — that's fine.

Always **cite specific page numbers** (ST / SM / teacher-manual p.) when referencing source material,
per the source-of-truth model: the plan *sequences and times* the publisher's own activities and
discussion questions rather than reproducing them.

---

## Cohort day-file template (`--model cohort`)

Same file/naming conventions, but the body follows the discussion-first rhythm. Keep the Start Slide
(Do Now · Objective · Agenda · Reminders) for classroom consistency, then:

- **Objectives** (content + skill + application) · **Materials**
- **Lesson Flow** — time-cued segments with **Say:** / **Ask:** teacher scripts
- Cohort tools used correctly and in rhythm: **Reading → Discussion Brief → Discussion → Pair &
  Defend → Case Study → Application.** Tools are defined in [cohort-tools.md](cohort-tools.md).
- Rubrics live in `assessments/` and are referenced, not inlined.
- Students are scaffolded into tools (Week 1 teaches *how* to write a brief; later weeks assume it).
- Student agency grows over the year (teacher-led → student-led); build in reflection/metacognition.

---

## Quality bar (both models)

**Depth & detail** — each day fully fleshed out; specific timing (not "10–15 min"); teacher moves and
transitions explicit.

**Pedagogical soundness** — clear arc (hook → instruction → practice → synthesis); activities match
objectives; appropriate cognitive load; assessment aligns with what was taught.

**Substitute-friendly** — sub days use self-contained activities; sub instructions assume zero content
knowledge; students can work independently. Every sub day has a `substitute-plan-<day>.md`.

**Contextual awareness** — short weeks are lighter; the week before Christmas break and the last week
of school stay light/instruction-free; pre-break weeks aren't assessment-heavy; post-break weeks
reconnect (review/synthesis).

**Consistency** — match the tone, structure, and detail of the Foundations Ch 1 exemplar
(`classes/foundations/lesson-plans-2026-27/week-01-aug-24/`). Warm, clear, not condescending.
Handouts are standalone files in the week's `handouts/`; the teaching map is the source of truth for
activities, pacing, and the assessment schedule.
