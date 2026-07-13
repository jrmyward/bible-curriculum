---
name: generate-student-syllabus
description: Generate a printable student-facing syllabus for Day 1 of a class
args: "[class-name] [--year YYYY-YY]"
---

# Generate Student Syllabus

Generate a polished, printable student-facing syllabus for a class — the kind you hand out on Day 1 and reference all year. This is NOT the textbook syllabus (see `/generate-official-syllabus`); this is the teacher's course syllabus for students.

## Usage

```bash
/generate-student-syllabus <class-name>
/generate-student-syllabus foundations --year 2026-27
```

## Prerequisites

Before running this command, ensure:

- ✅ **Teaching map exists**: `classes/<class-name>/teaching-maps/teaching-map-<year>.md`
- ✅ **Cohort tools defined**: `_shared/cohort-tools.md`
- ✅ **School calendar exists**: `_shared/school-calendar-<year>.md`

If missing:

- Teaching map → Run `/generate-map <class-name>`
- School calendar → Create manually in `_shared/`

## Process

### 1. Validate Inputs

- If `--class` not provided, detect from current directory or ask user
- Verify the class exists in `classes/<class-name>/`
- If `--year` not provided, detect from directory structure or default to current school year
- Check if `classes/<class-name>/lesson-plans-<year>/student-syllabus.md` already exists
  - If exists: "Student syllabus already exists. Regenerate? (yes/no)"
  - If regenerating: back up existing file to `student-syllabus.backup.md` in the same directory

### 2. Read Source Files

Read the following to extract syllabus content:

1. **Teaching map**: `classes/<class-name>/teaching-maps/teaching-map-<year>.md`
   - Extract: course description, unit overview table, assessment schedule (weights), cohort tool rhythm, trimester dates, total instructional days
2. **Cohort tools**: `_shared/cohort-tools.md`
   - Extract: brief description of each tool (Discussion Brief, Pair & Defend, Case Study, Capstone) — student-friendly summaries, not teacher implementation details
3. **School calendar**: `_shared/school-calendar-<year>.md`
   - Extract: trimester start/end dates, major breaks, exam periods
4. **Class README** (if exists): `classes/<class-name>/README.md`
   - Extract: grade level, textbook title, any course description

### 3. Ask Teacher for Missing Info

If any of the following aren't derivable from existing files, ask:

- **Teacher name** (for the header)
- **Contact info** (email, office hours, preferred contact method)
- **Late work policy** (deductions, grace period, etc.)
- **Academic integrity policy** (or reference to school handbook)
- **Technology policy** (phones, laptops, etc.)
- **Accommodations statement** (or reference to school policy)
- **Any class-specific policies** the teacher wants included

If the teacher says "use defaults" or "skip" for any of these, omit that section rather than inventing a policy.

### 4. Generate the Student Syllabus

Write the syllabus to `classes/<class-name>/lesson-plans-<year>/student-syllabus.md` using this structure:

```markdown
# [Course Title] — Student Syllabus

**School Year:** [Year]
**Teacher:** [Name]
**Contact:** [Email / preferred method]
**Grade Level:** [Grade]
**Textbook:** [Title by Author (Publisher)]

---

## Course Description

[2–3 sentences from the teaching map's course context. Written for students — what they'll learn and why it matters. No edu-jargon.]

---

## What You'll Study

[Unit overview table from the teaching map, simplified for students. Show unit number, topic/key question, and approximate weeks — NOT chapter numbers or assessment details.]

| Unit | Topic | Weeks |
|------|-------|-------|
| 1 | [Key question from teaching map] | Weeks 1–3 |
| 2 | ... | ... |
| ... | ... | ... |

---

## How This Class Works

This is a **discussion-first** class. You won't sit through lectures. Instead, you'll read, write, debate, and defend ideas — often positions you don't personally hold. Here's what that looks like:

### Discussion Briefs
[1–2 sentence student-friendly description. What it is, when it's due, what's expected.]

### Pair & Defend
[1–2 sentence student-friendly description.]

### Case Studies
[1–2 sentence student-friendly description.]

### Capstone Projects
[1–2 sentence student-friendly description.]

---

## Grading

| Category | Weight |
|----------|--------|
| [From teaching map assessment schedule — group ongoing items together] | XX% |
| ... | ... |
| **Total** | **100%** |

[If the teaching map breaks capstones into individual weights, group them as "Capstone Projects (4 total)" with the combined weight, then note individual weights in a parenthetical or sub-list.]

---

## Expectations

1. **Come prepared.** Complete all reading before class. You can't discuss what you haven't read.
2. **Engage respectfully.** Disagree without being disagreeable. Attack ideas, not people.
3. **Take intellectual risks.** It's okay to be wrong. It's not okay to be silent.

[Add any class-specific expectations from the teaching map or teacher input.]

---

## Important Dates

[Key dates only — trimester ends, capstone presentation windows, final project. NOT every Discussion Brief due date.]

| Date | Event |
|------|-------|
| [Date] | [Event] |
| ... | ... |

---

## Policies

[Only include sections the teacher provided info for. Omit any the teacher skipped.]

### Late Work
[Teacher's policy]

### Academic Integrity
[Teacher's policy or school handbook reference]

### Technology
[Teacher's policy]

### Accommodations
[Statement or school policy reference]

---

*[Course Title] — [School Year]*
```

### 5. Tone & Style Guidelines

- **Audience:** 11th–12th grade students reading this on Day 1
- **Tone:** Direct, warm, confident. Not corporate, not cutesy.
- **Length:** Aim for 2 pages when printed (single-spaced). Students won't read a 5-page syllabus.
- **Formatting:** Clean headers, tables, short paragraphs. Easy to scan.
- Write like a teacher talking to students, not an administrator writing a compliance document.
- Use "you" and "your" — address students directly.
- Avoid: "learner," "stakeholder," "demonstrate mastery," "learning outcomes," "rubric alignment"
- Prefer: "you'll learn," "here's what I expect," "this is how it works"

### 6. Report Completion

Display summary:

```
✅ Student syllabus generated for [class-name] ([year])

Created: classes/<class-name>/lesson-plans-<year>/student-syllabus.md

Sources used:
- Teaching map: teaching-maps/teaching-map-<year>.md
- Cohort tools: _shared/cohort-tools.md
- School calendar: _shared/school-calendar-<year>.md

Next steps:
- Review the syllabus and adjust policies/wording to your preference
- Print copies for Day 1 (one per student)
- Update Week 1 lesson plan to reference this file during syllabus walkthrough
```

---

## Notes

- This generates a **student-facing** document. It should not include teacher notes, implementation details, or internal planning info.
- The syllabus should be **self-contained** — a student (or parent) should be able to understand the course from this document alone.
- If the teaching map's assessment schedule uses detailed breakdowns (individual capstone weights, etc.), simplify for the student syllabus. Students need to know the categories and weights, not the internal accounting.
- The generated syllabus pairs with the Week 1 lesson plan, which typically includes a "Syllabus Walkthrough" activity. After generating, the teacher may want to update that lesson plan to reference specific sections.
- Do NOT invent policies (late work, integrity, etc.) that the teacher didn't provide. Better to omit a section than to guess wrong.
