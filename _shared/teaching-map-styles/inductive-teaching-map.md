# Skill: Inductive Bible Study Teaching Map Generator

## Purpose

Generate an Inductive Bible Study (IBS) teaching map for a high school Bible class. This style trains students to discover truth directly from the biblical text using the Observation → Interpretation → Application method. Minimal lecture; maximum text engagement.

## Best For

- Scripture-focused courses (book studies, biblical theology)
- Gospel studies (John, Mark, Luke, Matthew)
- Epistle studies (Romans, Ephesians, Galatians)
- Courses where the goal is Bible study skills, not just knowledge

## Inputs Required

1. **School calendar** — Read from `_shared/school-calendar-2026-27.md`
2. **Scripture passage list** — Which book(s) of the Bible will be studied
3. **Class metadata** — Class name, grade level, biblical text being studied

## The Inductive Method

Every lesson follows this three-step process:

### 1. Observation (What does the text say?)
- Read the passage multiple times (aloud, silently, in different translations)
- Mark up the text: circle key words, underline themes, note repeated phrases
- List observable facts: who, what, when, where
- Identify literary structure: narrative, poetry, epistle, etc.

**Tools**: Observation worksheets, text marking guides, "5 W's" charts

### 2. Interpretation (What does the text mean?)
- Study context: What comes before and after? Who wrote it and why?
- Cross-reference: What do other passages say about this theme?
- Word studies: What do key words mean in the original language? (simplified for high school)
- Identify the main idea: What is the author's purpose in this passage?

**Tools**: Context charts, cross-reference guides, word study sheets, commentaries (used sparingly)

### 3. Application (How does this apply to life?)
- Personal response: How does this passage challenge, comfort, or correct me?
- Action steps: What specific obedience does this require?
- Prayer: How does this shape how I pray?
- Memorization: Which verse(s) should I internalize?

**Tools**: Application journals, Scripture memory cards, accountability questions

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

When building the daily schedule, **mark teacher-absence days with `**SUB:**`** at the start of that day's plan. On a sub day, swap the planned IBS phase for a self-contained activity a substitute can facilitate (annotated reading + observation worksheet, application journal, scripture memory work, etc.). The `/generate-substitute-plan` skill produces the detailed plan; the teaching map only needs the `**SUB:**` marker.

**Never label a teacher-absence day as "NO SCHOOL" — that is a correctness bug that makes the day disappear from instruction.**

### Step 2: Select and Chunk Passages

- **For a single book study**: Divide the book into manageable passages (5-15 verses each for narrative, 3-8 verses for dense epistles)
- **For a thematic study**: Select key passages across multiple books
- Plan to spend 3-5 days per passage (full inductive cycle)
- Slower pacing = deeper mastery

Example pacing for Gospel of John (21 chapters):
- 36 weeks of instruction
- 30-35 passages (not every verse, but key sections)
- 3-5 days per passage
- Leaves buffer for review and exams

### Step 3: Plan the Weekly Rhythm

Typical week for a single passage:

| Day | Phase | Activity |
|-----|-------|----------|
| Mon | Observation | Read passage, mark up text, list facts |
| Tue | Observation | Continue marking, complete observation worksheet |
| Wed | Interpretation | Context and cross-references |
| Thu | Interpretation | Word studies and main idea |
| Fri | Application | Journaling, memory, and wrap-up |

For longer passages, extend observation and interpretation to 2 days each.

### Step 4: Create IBS Worksheets

For each passage, prepare:
- **Observation Sheet**: 5 W's (who, what, when, where, why), key words to mark, structure notes
- **Context Chart**: Author, audience, occasion, purpose (AAOP)
- **Cross-Reference Guide**: 3-5 related passages to compare
- **Word Study**: 1-2 key words to explore (Greek/Hebrew simplified)
- **Application Journal Prompt**: Specific question tied to the passage

### Step 5: Plan Assessments

- **Annotated Bible Passages**: Students submit their marked-up text (graded on thoroughness)
- **Interpretation Worksheets**: Context charts and word studies (graded on accuracy)
- **Application Journals**: Weekly reflections (graded on thoughtfulness, not "correctness")
- **Scripture Memory**: Recitation of key verses (weekly or bi-weekly)
- **Unit Exams**: Covering multiple passages (focus on interpretation and synthesis, not just recall)

### Step 6: Build the Week-by-Week Map

For each week, specify:
- Week number and date range
- Passage being studied (book, chapter, verses)
- Main idea or theme of the passage
- Observation focus (what to mark, what to notice)
- Interpretation questions (context, cross-references, word studies)
- Application prompt (journal question, action step)
- Scripture memory verse(s)

## Output Format

Write the completed map to `classes/<class-name>/teaching-map.md`:

```markdown
# <Class Name> — Teaching Map

**School Year:** 2026–2027  
**Grade Level:** <grade>  
**Biblical Text:** <book(s) being studied>  
**Teaching Style:** Inductive Bible Study  
**Total Instructional Days:** <count>

## Course Overview

<Brief description: which book(s), why this text matters, what skills students will develop>

## Inductive Method Overview

Every passage follows this rhythm:
1. **Observation** (1-2 days): What does the text say?
2. **Interpretation** (1-2 days): What does the text mean?
3. **Application** (1 day): How does this apply to life?

## Passage List

| Week | Passage | Main Idea | Memory Verse |
|------|---------|-----------|--------------|
| 1 | John 1:1-18 | The Word became flesh | John 1:14 |
| ... | ... | ... | ... |

## Week-by-Week Schedule

### Week 1 — Aug 17–21, 2026
**Passage:** John 1:1-18 (The Prologue)  
**Main Idea:** Jesus is the eternal Word who became flesh to reveal God and bring salvation.

**Observation (Mon-Tue):**
- Read the passage 3 times (aloud, silently, in NIV and ESV)
- Mark up the text:
  - Circle: "Word," "light," "life," "darkness"
  - Underline: statements about who Jesus is
  - Note repeated phrases: "was," "came," "received"
- Complete Observation Worksheet: Who is being described? What attributes are given?

**Interpretation (Wed-Thu):**
- Wed: Context — How does this prologue set up the whole Gospel? What OT echoes do you hear (Gen 1, creation language)?
- Thu: Word study — What does "Logos" (Word) mean? Why this term? Cross-reference: Psalm 33:6, Proverbs 8:22-31
- Identify the main idea: What is John saying about Jesus in these opening verses?

**Application (Fri):**
- Journal prompt: *"John 1:14 says the Word became flesh and dwelt among us. How does the incarnation (God becoming human) change the way you relate to God?"*
- Scripture memory: John 1:14
- Preview next week: John 1:19-34 (John the Baptist's testimony)

**Due:** Observation Worksheet (Tue), Context Chart (Wed), Application Journal (Fri)

---

(Repeat for each week)

## Assessment Schedule

| Date | Assessment | Passage(s) | Type |
|------|------------|------------|------|
| Week 2 | Scripture Memory Check | John 1:14 | Recitation |
| Week 6 | Unit Exam #1 | John 1-3 | Written exam |
| ... | ... | ... | ... |
```

## Guidelines

- **Pace for mastery, not coverage**: IBS is slow by design. It's better to deeply understand 10 passages than skim 30.
- **Model the method first**: Week 1 should be heavily guided. By Week 10, students should be able to do observation on their own.
- **Use multiple translations**: Have students compare NIV, ESV, NASB to see nuances.
- **Limit commentary use**: Students should wrestle with the text first. Commentaries come later to confirm or challenge their interpretation.
- **Emphasize reproducibility**: The goal is that students can use this method on any passage for the rest of their lives.
- **Connect passages**: As you progress, help students see how passages connect (themes, prophecy fulfillment, theological threads).
- **Celebrate discoveries**: When a student notices something insightful, affirm it publicly. IBS thrives on student ownership.

## IBS Tools and Resources

### Observation Worksheets
- 5 W's Chart (Who, What, When, Where, Why)
- Key Words to Mark (provided by teacher for each passage)
- Structure Notes (identify narrative arc, argument flow, etc.)

### Interpretation Tools
- Context Chart (Author, Audience, Occasion, Purpose)
- Cross-Reference Guide (3-5 related passages)
- Word Study Template (simplified Greek/Hebrew with concordance)
- Main Idea Statement (one-sentence summary of the passage)

### Application Tools
- Journal Prompts (specific to each passage)
- Accountability Questions (How will you obey this? Who will you tell?)
- Scripture Memory Cards (verse on front, reflection on back)

### Assessment Rubrics
- Annotated Bible grading (thoroughness, accuracy, insight)
- Interpretation worksheet grading (context understanding, cross-reference connections)
- Journal grading (honesty, depth, application specificity)
- Memory grading (accuracy, expression, meditation)
