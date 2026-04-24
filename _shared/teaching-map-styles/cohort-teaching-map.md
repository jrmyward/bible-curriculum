# Skill: Cohort Teaching Map Generator

## Purpose

Generate a complete semester-long teaching map for a high school Bible class. The map aligns chapter content with the school calendar, integrates cohort teaching tools, and produces a week-by-week schedule the teacher can follow and adjust.

## Inputs Required

1. **School calendar** — Read from `_shared/school-calendar-2026-27.md`. Contains first/last day, trimester end dates, and all no-school dates.
2. **Chapter list** — Provided by the teacher. Should include chapter numbers, titles, and approximate page counts or scope.
3. **Cohort tools** — Read from `_shared/cohort-tools.md`. The four tools (Discussion Brief, Pair & Defend, Case Study, Capstone) that structure each unit.
4. **Class metadata** — Class name, grade level, textbook/series.

## Process

### Step 1: Map Available Instructional Days

The school calendar (`_shared/school-calendar-<year>.md`) contains **TWO separate tables** that must be handled differently:

- **No-School Dates** — actual school closures (holidays, breaks, teacher work days). Skip these entirely; they are NOT instructional days.
- **Teacher Absences (J. Ward)** — days the teacher is out but **school is in session**. These ARE instructional days that need a substitute. Count them toward your total.

Then:

- Start with the first day of school and end with the last day.
- Remove all **no-school dates** from the calendar.
- Count the total available instructional days (this count **includes** teacher-absence/sub days).
- Divide into trimesters using the trimester end dates.
- Assume the class meets 5 days per week (Monday–Friday) unless the teacher specifies otherwise.

When building the daily schedule (Step 4), **mark teacher-absence days with `**SUB:**`** at the start of that day's plan. Examples:

> - **Fri (Aug 28):** **SUB:** Substitute-friendly activity (film + reflection, individual reading + worksheet, in-class writing assignment, etc.)
> - **Mon (Apr 5):** **SUB:** Independent worldview chart work + journal entry

Sub-day activities should be self-contained, **non-cohort** activities a substitute can facilitate without deep content knowledge. The `/generate-substitute-plan` skill produces the detailed sub plan; the teaching map only needs the `**SUB:**` marker so downstream skills know to generate one.

**Never label a teacher-absence day as "NO SCHOOL" — that is a correctness bug that makes the day disappear from instruction.**

### Step 2: Chunk Chapters into Units

- Group chapters into logical units (typically 2–4 chapters per unit, depending on length and thematic coherence).
- Each unit should span roughly 2–4 weeks of instruction.
- Leave buffer days before trimester ends for review and assessment.

### Step 3: Assign Cohort Tools to Each Unit

Each unit follows this rhythm:

| Phase | Tool | Duration | Description |
|---|---|---|---|
| 1. Introduce | Reading + Discussion Brief | 1–2 days | Students read the chapter(s) and submit a discussion brief |
| 2. Engage | Pair & Defend | 1 day | Structured debate on the unit's core question |
| 3. Apply | Case Study | 1 day | Small group work on a real-world scenario |
| 4. Synthesize | Capstone (end of major unit) | 1–2 days | Presentation, Q&A, and final brief |

Not every unit needs a full capstone — reserve capstones for the end of each major section (roughly once per trimester or every 2–3 units).

### Step 4: Build the Week-by-Week Map

For each week, specify:

- **Week number and date range**
- **Chapter(s) covered**
- **Key topic or question for the week**
- **Cohort tool(s) used**
- **Assignments due**
- **Notes** (no-school days, half-days, trimester deadlines, etc.)

### Step 5: Add Assessment Checkpoints

- **Trimester 1 end (November 12):** Major assessment or capstone due
- **Trimester 2 end (February 25):** Major assessment or capstone due
- **Trimester 3 end (May 21):** Final capstone or cumulative assessment

Include smaller checkpoints (quizzes, brief collections, participation grades) at the end of each unit.

## Output Format

Write the completed map to `classes/<class-name>/teaching-map.md` using this structure:

```markdown
# <Class Name> — Teaching Map

**School Year:** 2026–2027
**Grade Level:** <grade>
**Series:** <textbook/series>
**Total Instructional Days:** <count>

## Unit Overview

| Unit | Chapters | Weeks | Key Question |
|---|---|---|---|
| 1 | Ch 1–3 | Weeks 1–3 | <question> |
| ... | ... | ... | ... |

## Week-by-Week Schedule

### Week 1 — Aug 17–21, 2026
**Chapter:** Ch 1 — <Title>
**Topic:** <key topic>
**Activities:**
- Mon: Introduce chapter, assign reading
- Tue–Wed: Discussion briefs due; class discussion
- Thu: Pair & Defend
- Fri: Debrief and preview next chapter

**Due:** Discussion Brief #1
**Notes:** First week of school

---

### Week 2 — ...
(continue for each week)

## Assessment Schedule

| Assessment | Type | Due Date | Weight |
|---|---|---|---|
| ... | ... | ... | ... |
```

## Guidelines

- Pace for depth over coverage. It's better to discuss 3 chapters well than rush through 5.
- Build in at least 2 flex days per trimester for catching up or going deeper.
- Front-load reading-heavy chapters earlier in the trimester when energy is higher.
- Place capstones at least one week before trimester end dates so grades can be finalized.
- Note half-days and shortened schedules — don't plan heavy activities on those days.
- If a no-school day falls mid-unit, adjust the week's plan so continuity isn't broken.
