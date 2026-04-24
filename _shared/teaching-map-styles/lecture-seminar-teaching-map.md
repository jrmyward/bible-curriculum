# Skill: Lecture-Seminar Teaching Map Generator

## Purpose

Generate a lecture-seminar style teaching map for a high school Bible class. This style balances teacher-led content delivery with designated discussion days, allowing for faster content coverage while maintaining depth on key topics.

## Best For

- Survey courses (Old Testament Survey, New Testament Survey)
- Theology courses with high information content
- Church history
- Courses where foundational knowledge is needed before deep discussion

## Inputs Required

1. **School calendar** — Read from `_shared/school-calendar-2026-27.md`
2. **Chapter list or syllabus** — From teacher or `classes/<class-name>/syllabus/syllabus.md`
3. **Class metadata** — Class name, grade level, textbook/series

## Weekly Rhythm

A typical 5-day week follows this pattern:

| Day | Activity | Description |
|-----|----------|-------------|
| Mon | Lecture | Introduce new chapter/topic with guided notes |
| Tue | Lecture | Continue content delivery, Q&A |
| Wed | Lecture + Application | Complete content delivery, begin connecting to life |
| Thu | Seminar Discussion | Student-led discussion on week's material |
| Fri | Review/Assessment | Quiz, review game, or application activity |

**For 4-day weeks** (due to holidays): Compress to Lecture (Mon-Tue), Seminar (Wed), Review (Thu)

## Process

### Step 1: Map Available Instructional Days

The school calendar (`_shared/school-calendar-<year>.md`) contains **TWO separate tables** that must be handled differently:

- **No-School Dates** — actual school closures (holidays, breaks, teacher work days). Skip these entirely; they are NOT instructional days.
- **Teacher Absences (J. Ward)** — days the teacher is out but **school is in session**. These ARE instructional days that need a substitute. Count them toward your total.

Then:

- Start with first day of school, end with last day
- Remove all **no-school dates** from calendar
- Count total available instructional days (this count **includes** teacher-absence/sub days)
- Divide into trimesters using trimester end dates
- Assume 5 days per week unless specified otherwise

When building the daily schedule, **mark teacher-absence days with `**SUB:**`** at the start of that day's plan. On a sub day, replace the lecture/seminar with a self-contained, non-lecture activity a substitute can run (film + worksheet, in-class essay, individual study guide work, etc.). The `/generate-substitute-plan` skill produces the detailed plan; the teaching map only needs the `**SUB:**` marker.

**Never label a teacher-absence day as "NO SCHOOL" — that is a correctness bug that makes the day disappear from instruction.**

### Step 2: Chunk Content into Weekly Units

- Each week covers 1-2 chapters (depending on chapter length)
- Faster pacing than cohort model — aim to cover full syllabus
- Group related chapters for thematic coherence
- Leave 1-2 buffer weeks before each trimester end for exam review

### Step 3: Plan Lecture Content

For each chapter/topic:
- Identify 3-5 key learning objectives
- Outline main points for lecture days (Mon-Wed)
- Create guided notes outline (students fill in as you lecture)
- Prepare visual aids (maps, timelines, slides, etc.)

### Step 4: Design Seminar Discussions

For each Thursday seminar:
- Write 5-7 discussion questions tied to the week's content
- Include mix of comprehension, interpretation, and application questions
- Identify 1-2 "essential questions" that frame the whole discussion
- Plan seminar format: full class, small groups, or fishbowl

### Step 5: Plan Assessments

- **Weekly quizzes** (Fridays): 5-10 questions on the week's content
- **Unit exams** (every 3-4 weeks): Cumulative on major sections
- **Trimester exams**: Cover all content from the trimester
- **Essays or research papers**: 1-2 per trimester on major themes

### Step 6: Build the Week-by-Week Map

For each week, specify:
- Week number and date range
- Chapter(s) covered
- Lecture topics for Mon-Wed
- Seminar essential question for Thu
- Assessment for Fri (quiz, review, or activity)
- Notes (no-school days, half-days, exam weeks, etc.)

## Output Format

Write the completed map to `classes/<class-name>/teaching-map.md` using this structure:

```markdown
# <Class Name> — Teaching Map

**School Year:** 2026–2027  
**Grade Level:** <grade>  
**Textbook:** <textbook/series>  
**Teaching Style:** Lecture-Seminar  
**Total Instructional Days:** <count>

## Course Overview

<Brief description of the course and learning goals>

## Weekly Rhythm

| Day | Activity | Description |
|-----|----------|-------------|
| Mon | Lecture | Introduce new chapter/topic |
| Tue | Lecture | Continue content delivery |
| Wed | Lecture + Application | Complete content, connect to life |
| Thu | Seminar | Student-led discussion |
| Fri | Quiz/Review | Assessment or review activity |

## Content Outline

| Week | Chapters | Topics | Assessment |
|------|----------|--------|------------|
| 1 | Ch 1-2 | <topics> | Quiz #1 |
| ... | ... | ... | ... |

## Week-by-Week Schedule

### Week 1 — Aug 17–21, 2026
**Chapters:** Ch 1–2  
**Topics:** <main topics for the week>

**Lecture Content (Mon-Wed):**
- Mon: <lecture outline>
- Tue: <lecture outline>
- Wed: <lecture outline + application>

**Seminar Discussion (Thu):**
- Essential Question: <question>
- Discussion Questions:
  1. <question>
  2. <question>
  3. <question>

**Assessment (Fri):** Quiz #1 (Ch 1-2)

**Notes:** <any special notes for this week>

---

(Repeat for each week)

## Assessment Schedule

| Date | Assessment | Chapters | Weight |
|------|------------|----------|--------|
| ... | ... | ... | ... |
```

## Guidelines

- **Pace for coverage**: Lecture-seminar allows you to cover more ground than discussion-heavy models. Plan to complete the full syllabus.
- **Use guided notes**: Students fill in key points during lecture. This keeps them engaged and provides a study tool.
- **Seminar prep is key**: Thursday discussions only work if students actually did the reading. Consider brief reading quizzes (5 questions) at start of seminar to incentivize preparation.
- **Vary Friday activities**: Not every Friday needs a quiz. Mix in review games, application scenarios, debates, or guest speakers.
- **Leave buffer time**: 1-2 weeks before each trimester end should be exam review, not new content.
- **Account for shortened weeks**: When holidays disrupt the Mon-Wed lecture rhythm, adjust by condensing content or moving seminar to Wed.

## Assessment Best Practices

### Weekly Quizzes
- 5-10 questions (mix of multiple choice, short answer, quote identification)
- Cover the week's reading and lecture content
- Graded quickly (ideally returned by Monday)
- Focus on key facts, concepts, and vocabulary

### Unit Exams
- 25-40 questions covering 3-4 weeks of material
- Mix of formats: multiple choice, true/false, short answer, essay
- Include at least one essay question requiring synthesis
- Schedule 1-2 days before the exam for in-class review

### Trimester Exams
- Cumulative, covering all content from the trimester
- 50-75 questions (or shorter with longer essays)
- Weight these more heavily than weekly quizzes
- Provide study guide 1-2 weeks in advance

### Research Papers/Essays
- 1-2 per trimester (don't overload with writing if you have weekly quizzes)
- Tie to major themes, not just chapter summaries
- Provide rubric and examples of strong work
- Consider building in drafts + revisions for at least one paper per semester
