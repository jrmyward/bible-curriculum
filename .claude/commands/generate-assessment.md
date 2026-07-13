---
name: generate-assessment
description: Generate assessment rubrics, capstone projects, and exam materials
args: "<assessment-type> --class [class-name] [options]"
---

# Generate Assessment

Create assessment materials including capstone rubrics, unit test study guides, and final exam prompts.

## Usage

```bash
/generate-assessment <assessment-type> --class <class-name> [options]
```

**Examples:**

```bash
/generate-assessment capstone --class foundations --number 1
/generate-assessment unit-test --class foundations --unit 2 --chapters 3-4
/generate-assessment final-reflection --class foundations
/generate-assessment capstone --class worldview --number 2 --type debate
```

## Prerequisites

Before running this command, ensure:

- **Teaching map exists**: `classes/<class-name>/teaching-maps/teaching-map-<year>.md`
- **Lesson plans directory exists**: `classes/<class-name>/lesson-plans-<year>/`
- **Assessment stubs exist**: `lesson-plans-<year>/assessments/` (created by `/scaffold-lesson-structure`)

If missing:

- Teaching map → Run `/generate-map <class-name>`
- Lesson plans directory → Run `/scaffold-lesson-structure <class-name>`

## Assessment Types

### 1. **capstone**

Major project assessment given at trimester ends.

**Required args:** `--class`, `--number` (1, 2, 3, or final)
**Optional args:** `--type` (essay / debate / presentation / portfolio), `--chapters` (chapters covered)

**Process:**
1. Read the teaching map to find this capstone's placement, chapters covered, and context
2. Read any existing lesson plans for the relevant weeks to understand what students learned
3. Read `_shared/cohort-tools.md` for proper capstone structure
4. Determine capstone type based on teaching map notes or `--type` flag:
   - **Essay**: Extended written argument (2-3 pages)
   - **Debate**: Formal in-class debate with rubric
   - **Presentation**: Individual or group presentation
   - **Portfolio**: Collection of revised work from the trimester
5. Generate the rubric with clear criteria, point values, and descriptions for each level
6. Include student-facing instructions, format requirements, and due dates
7. Write to `lesson-plans-<year>/assessments/capstone-XX-rubric.md`

**Rubric structure:**
```markdown
# Capstone #X: [Title]

**Class:** [Class name]
**Due:** [Date from teaching map]
**Chapters Covered:** [Chapters]
**Type:** [Essay / Debate / Presentation / Portfolio]
**Weight:** [Percentage of trimester grade]

---

## Assignment

[2-3 paragraph description of what students must do]

## Requirements

- [Requirement 1]
- [Requirement 2]
- [Requirement 3]

## Rubric

| Criterion | Excellent (5) | Proficient (4) | Developing (3) | Beginning (1-2) |
|-----------|---------------|-----------------|-----------------|------------------|
| [Criterion 1] | [Description] | [Description] | [Description] | [Description] |
| [Criterion 2] | [Description] | [Description] | [Description] | [Description] |
| [Criterion 3] | [Description] | [Description] | [Description] | [Description] |
| [Criterion 4] | [Description] | [Description] | [Description] | [Description] |

**Total: _____ / XX points**

## Format

- [Format requirements]

## Timeline

| Milestone | Date | What's Due |
|-----------|------|------------|
| [Milestone 1] | [Date] | [Deliverable] |
| [Milestone 2] | [Date] | [Deliverable] |
| Final submission | [Date] | [Everything] |
```

---

### 2. **unit-test**

Study guide and test outline for a unit assessment.

**Required args:** `--class`, `--unit` (unit number), `--chapters` (chapter range)
**Optional args:** `--format` (multiple-choice / short-answer / essay / mixed)

**Process:**
1. Read teaching map for unit boundaries and key concepts
2. Read lesson plans for the relevant weeks (if they exist) to identify what was taught
3. Generate a study guide with key terms, concepts, Scripture references, and review questions
4. Generate a test outline (not the full test — teacher fills in specific questions)
5. Write study guide to `lesson-plans-<year>/assessments/unit-XX-study-guide.md`
6. Write test outline to `lesson-plans-<year>/assessments/unit-XX-test-outline.md`

**Study guide structure:**
```markdown
# Unit X Study Guide: [Unit Title]

**Chapters:** [Chapters]
**Test Date:** [Date from teaching map]

---

## Key Terms

| Term | Definition |
|------|-----------|
| [Term 1] | [Definition] |
| [Term 2] | [Definition] |

## Key Concepts

1. [Concept with brief explanation]
2. [Concept with brief explanation]

## Scripture References

- [Verse]: [Why it matters for this unit]

## Review Questions

1. [Question — recall level]
2. [Question — analysis level]
3. [Question — application level]
4. [Question — synthesis level]
```

---

### 3. **final-reflection**

End-of-course reflection essay prompt and rubric.

**Required args:** `--class`
**Optional args:** `--prompts` (custom reflection prompts)

**Process:**
1. Read teaching map for full course arc and major themes
2. Generate 3-5 reflection prompts that span the entire course
3. Include rubric focused on depth of reflection, not content recall
4. Write to `lesson-plans-<year>/assessments/final-reflection-essay.md`

---

## General Principles

- **Align to what was taught**: Only assess content students actually encountered
- **Use the grading guide**: Reference `_shared/grading-guide.md` for grade-level expectations
- **Rubrics are student-facing**: Write in clear language students understand
- **Include multiple levels**: Every rubric criterion should have at least 3 performance levels
- **Balance cognitive levels**: Mix recall, analysis, application, and synthesis
- **Reference cohort tools**: Capstones should build on skills practiced through Discussion Briefs, Pair & Defend, and Case Studies

## Output

All assessment files are written to `lesson-plans-<year>/assessments/`.

After generating, report:

```
Assessment generated for [class-name]:
- [filename] (assessment type, X points total)

Next steps:
- Review rubric criteria and point values
- Adjust dates if schedule has changed
- Print student copies before the due date
```

## Notes

- Assessment stubs are created by `/scaffold-lesson-structure` — this command fills them in
- If a stub already exists with content, ask before overwriting
- Capstone rubrics should feel achievable, not intimidating — tone matters
- The teacher may want to customize point values after generation
