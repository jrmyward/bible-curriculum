---
name: generate-handout
description: Generate a specific handout for a lesson
args: "[handout-type] --week [week-number] [additional-args]"
---

# Generate Handout

Create a specific handout for a lesson using templates or custom generation.

## Usage

```bash
/generate-handout <handout-type> --week <week-number> [options]
```

**Examples:**

```bash
/generate-handout core-reading-guide --week 5 --chapter 3
/generate-handout note-catcher --week 5 --chapter 3
/generate-handout discussion-brief --week 5 --number 3 --prompt "What is the strongest objection to biblical reliability?"
/generate-handout case-study --week 7 --topic "Historical parallel: how early Christians defended Scripture to Romans"
/generate-handout pair-and-defend --week 3 --prompt "Is objective truth possible in a pluralistic society?"
/generate-handout video-note-catcher --week 5 --video "The Case for Reliability of the Gospels"
/generate-handout reflection --week 1 --title "Week 1 Reflection"
```

## Prerequisites

Before running this command, ensure:

- ✅ **Teaching map exists**: For context about the week's content
- ✅ **Week directory exists**: `lesson-plans-<year>/week-XX-<date>/handouts/`

If the week directory doesn't exist, run `/scaffold-lesson-structure` first.

**Note:** Handouts are written to `lesson-plans-<year>/week-XX-<date>/handouts/` directory.

## Handout Types

### 1. **core-reading-guide**
Strategic reading guide that identifies core sections to read and sections to skip.

**Required args:** `--week`, `--chapter`  
**Optional args:** `--total-pages`

**Process:**
1. Read the teaching map to understand the week's context and goals
2. Ask user to provide images of the textbook chapter (or confirm chapter structure)
3. Analyze chapter structure: sections, headings, page count
4. Identify core sections (essential concepts, arguments, Scripture references)
5. Identify skippable sections (examples, statistics, administrative content, tangents)
6. Generate a table format:
   ```markdown
   | Section | Pages | Why Read This | What to Skip |
   ```
7. Aim for ~40-50% of total pages as "core reading"
8. Write to `lesson-plans-<year>/week-XX-<date>/handouts/core-reading-guide-chXX.md`

**Template structure:**
```markdown
# Core Reading Guide — Chapter X: "[Chapter Title]"

**READ THESE SECTIONS ONLY (≈X-X pages):**

| Section | Pages | Why Read This | What to Skip |
|---------|-------|---------------|--------------|
| 1. [Title] | X-X | [Reason] | [What to skip] |
[...]

**SKIP ENTIRELY:**
- Section X: [Title] ([reason])
[...]

**Reading Strategy:**
- Focus on definitions, key arguments, and Scripture references
- Skim examples unless they're unfamiliar to you
- Use the Note-Catcher to stay focused on big ideas

**Estimated Reading Time:** XX minutes
```

---

### 2. **note-catcher**
Guided note-taking worksheet that focuses on key concepts from the reading.

**Required args:** `--week`, `--chapter`  
**Optional args:** `--sections` (specific sections to focus on)

**Process:**
1. Read the teaching map to understand learning objectives
2. Read the core-reading-guide for this chapter (if it exists) or ask for chapter structure
3. Create 5-7 prompts that capture the essential concepts
4. Use varied question types:
   - Fill-in tables (e.g., "The Five Questions")
   - Definition prompts (e.g., "Hard vs. Soft Authority")
   - Short answer (e.g., "What's the main point of the cat/dog dialogue?")
   - Comparison (e.g., "How did Jesus respond to Thomas vs. John the Baptist?")
5. Include a final open-ended question: "One question I still have:"
6. Write to `lesson-plans-<year>/week-XX-<date>/handouts/note-catcher-chXX.md`

**Template structure:**
```markdown
# Chapter X Note-Catcher: "[Chapter Title]"

**Name:** ______________________  
**Date:** ______________________

---

**1. [SECTION NAME] (Sections X & X)**

[Prompt with table/fill-in/short answer]

---

**2. [SECTION NAME] (Section X)**

[Prompt]

---

[... 5-7 total sections]

---

**X. ONE QUESTION I STILL HAVE:**

---
```

---

### 3. **discussion-brief**
Template for Discussion Brief assignments with prompt and rubric.

**Required args:** `--week`, `--number`, `--prompt`  
**Optional args:** `--thinking-points` (bullet points to consider)

**Process:**
1. Read the teaching map to understand the Discussion Brief context
2. Generate the template with the provided prompt
3. Include 2-4 "Think about:" prompts to guide student thinking
4. Include the standard rubric from `lesson-plans-<year>/assessments/discussion-brief-rubric.md`
5. Write to `lesson-plans-<year>/week-XX-<date>/handouts/discussion-brief-XX.md`

**Template structure:**
```markdown
# Discussion Brief #X: "[Prompt]"

**Name:** ______________________  
**Date:** ______________________  
**Due:** [Day, Month Date from teaching map]

---

## Instructions

Write a 1-page, double-spaced response to the prompt above. Your brief should include:

1. **A clear thesis** — Answer the question directly in 1–2 sentences
2. **Reasoning** — Explain *why* you hold this position (2–3 reasons)
3. **Evidence** — Support your reasoning with Scripture, textbook references, or examples
4. **Conclusion** — Restate your thesis and offer one implication or application

## Think About

[2-4 bullet points to guide thinking, derived from chapter content]

## Format

- 12-point font, Times New Roman or Arial
- Double-spaced
- 1-inch margins
- No heading beyond your name at the top

## Rubric

[Include rubric from `../../assessments/discussion-brief-rubric.md`]

**Total: _____ / 20 points**
```

---

### 4. **case-study**
Case Study scenario with group work instructions.

**Required args:** `--week`, `--topic`  
**Optional args:** `--type` (ethical-dilemma / cultural-encounter / historical-parallel)

**Process:**
1. Read the teaching map to understand which chapters/concepts this applies
2. Generate a realistic scenario based on the topic and type
3. Include discussion questions (3-5)
4. Include group roles (Facilitator, Scribe, Presenter, Researcher)
5. Reference the shared rubric from `lesson-plans-<year>/assessments/case-study-rubric.md` (pass/fail, participation-based)
6. Write to `lesson-plans-<year>/week-XX-<date>/handouts/case-study-[topic-slug].md`

**Template structure:**
```markdown
# Case Study: [Topic]

**Type:** [Ethical Dilemma / Cultural Encounter / Historical Parallel]  
**Chapters:** [Relevant chapters]  
**Time:** 20-30 minutes (group work) + 10 minutes (presentations)

---

## Scenario

[2-3 paragraph realistic scenario that requires students to apply course concepts]

---

## Your Task

Working in groups of 3-4, discuss the scenario and answer the following questions:

1. [Question 1]
2. [Question 2]
3. [Question 3]
4. [Question 4]
5. [Question 5]

---

## Group Roles

- **Facilitator:** Keeps discussion on track, ensures everyone speaks
- **Scribe:** Takes notes, prepares write-up
- **Presenter:** Shares group's answers with class
- **Researcher:** References textbook/Scripture to support arguments

(For groups of 3, combine Scribe + Presenter)

---

## Group Deliverables

Your group must produce all three:

1. **Summary of the dilemma** — What's the situation? What makes it hard?
2. **Recommended response** — What should the person/group do, and why?
3. **Strongest counterargument** — What's the best objection to your own recommendation?

---

## Grading

Case Studies are graded on **participation** (pass/fail). See `../../assessments/case-study-rubric.md` for full details.

| Score | Criteria |
|-------|----------|
| **100%** | Participated in group work. Group produced all 3 deliverables. Contributed to presentation. |
| **50%** | Participated but group deliverables were incomplete or rushed. |
| **0%** | Absent, refused to participate, or clearly did not contribute. |
```

---

### 5. **pair-and-defend**
Pair & Defend debate prep sheet with pro/con arguments.

**Required args:** `--week`, `--prompt`  
**Optional args:** `--chapters` (relevant chapters for research)

**Process:**
1. Read the teaching map to understand the debate context
2. Generate the prompt and structure
3. Provide a "How to Prepare" section with tips for both sides
4. Include a prep worksheet with argument scaffolding
5. Write to `lesson-plans-<year>/week-XX-<date>/handouts/pair-and-defend-prep.md`

**Template structure:**
```markdown
# Pair & Defend Prep: "[Prompt]"

**Date:** [Date from teaching map]  
**Chapters:** [Relevant chapters]

---

## The Debate

You will be paired with a partner and assigned a position (pro or con). Your job is to make the **strongest possible argument** for your assigned side, even if you don't personally agree with it.

**Prompt:** [Prompt with "vs." structure]

---

## Format

1. **Opening statement** (3 minutes each): Present your position
2. **Rebuttal** (2 minutes each): Respond to your partner's argument
3. **Class Q&A** (3 minutes): Answer questions from classmates

---

## How to Prepare

### If you're arguing PRO:
[3-4 bullet points suggesting angles, Scripture, or textbook sections to use]

### If you're arguing CON:
[3-4 bullet points suggesting angles, Scripture, or textbook sections to use]

---

## Prep Worksheet

**Your Position:** [ ] Pro  [ ] Con

**Main Argument (1-2 sentences):**

---

**Supporting Reason #1:**

**Evidence (Scripture/textbook/example):**

---

**Supporting Reason #2:**

**Evidence (Scripture/textbook/example):**

---

**Supporting Reason #3:**

**Evidence (Scripture/textbook/example):**

---

**Anticipated Objection:**

**Your Response:**

---

## Grading

Pair & Defend is graded on **participation** (pass/fail). See `../../assessments/pair-and-defend-rubric.md` for full details.

| Score | Criteria |
|-------|----------|
| **100%** | Participated fully. Defended assigned position for 3 min. Asked/answered follow-up questions. |
| **50%** | Participated but unprepared. Didn't use full time or struggled to articulate position. |
| **0%** | Absent or refused to participate. |
```

---

### 6. **video-note-catcher**
Guided notes for a video shown in class.

**Required args:** `--week`, `--video` (video title)  
**Optional args:** `--length` (video length in minutes)

**Process:**
1. Generate 5-7 questions that students answer while watching
2. Mix question types: factual, analytical, application
3. Include a reflection prompt at the end
4. Write to `lesson-plans-<year>/week-XX-<date>/handouts/video-note-catcher-[slug].md`

**Template structure:**
```markdown
# Video Note-Catcher: "[Video Title]"

**Date:** ______________________  
**Video Length:** ~XX minutes

---

## Instructions

Watch the video and answer the questions below. You don't need complete sentences — bullet points are fine.

---

**1. [Question about background/context]**

---

**2. [Question about main argument]**

---

**3. [Question about evidence mentioned]**

---

**4. [Question about objections addressed]**

---

**5. [Analytical question]**

---

**6. [Application question]**

---

## Reflection

What's the most convincing point made in this video? Why?

---
```

---

### 7. **reflection**
Open-ended reflection prompt for synthesis or end-of-week processing.

**Required args:** `--week`, `--title`  
**Optional args:** `--prompts` (custom prompts)

**Process:**
1. Generate 3-5 reflection prompts based on the week's content
2. Mix cognitive levels: recall, analysis, application, synthesis
3. Include length/format guidelines
4. Write to `lesson-plans-<year>/week-XX-<date>/handouts/[slug]-reflection.md`

**Template structure:**
```markdown
# [Title]

**Name:** ______________________  
**Date:** ______________________  
**Due:** [Date]

---

## Instructions

Write 1-2 pages reflecting on this week's learning. Answer all prompts below.

---

**1. [Prompt 1 — recall or summary]**

---

**2. [Prompt 2 — analysis or interpretation]**

---

**3. [Prompt 3 — application or personal connection]**

---

**4. [Prompt 4 — synthesis or open question]**

---

## Format

- Typed, double-spaced
- 12-point font
- 1-2 pages total
- This is formative (feedback only, not graded)
```

---

## Notes

- All handouts follow the same naming convention: lowercase, hyphenated
- Handouts are self-contained (include all instructions, rubrics, prompts)
- Handouts reference the teaching map for due dates and context
- Generated handouts are written to `lesson-plans-<year>/week-XX-<date>/handouts/`
- If a handout already exists, ask before overwriting
