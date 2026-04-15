---
name: generate-map
description: Generate a cohort teaching map for a Bible curriculum class
args: "[class-name]"
---

# Generate Teaching Map

Generate a cohort-style teaching map for a class in this Bible curriculum repository.

## Usage

```
/generate-map <class-name>
```

**Example:**
```
/generate-map understanding-the-faith
/generate-map worldview
/generate-map old-testament-survey
```

## Process

1. **Validate class name**
   - Check that `classes/<class-name>/` exists
   - If not, list available classes and exit

2. **Check for existing teaching map**
   - If `classes/<class-name>/teaching-map.md` exists, ask whether to regenerate or update
   - If it doesn't exist, proceed to generation

3. **Ask which teaching style to use**
   - Present options from `_shared/teaching-styles.md`:
     1. Cohort Teaching Model
     2. Lecture-Seminar Model
     3. Inductive Bible Study (IBS)
     4. Flipped Classroom
     5. Project-Based Learning (PBL)
     6. Chronological Narrative
     7. Catechetical (Q&A)
   - If the teacher doesn't specify, recommend based on course type:
     - Apologetics/Worldview → Cohort
     - Survey courses → Lecture-Seminar or Chronological Narrative
     - Book studies → Inductive Bible Study
     - Application-heavy → Project-Based Learning

4. **Read required files**
   - `_skill/SKILL_<style>_teaching_map.md` — teaching map generation process for chosen style
   - `_shared/school-calendar-2026-27.md` — school calendar and no-school dates
   - `_shared/teaching-styles.md` — teaching style reference
   - Style-specific tool files (e.g., `_shared/cohort-tools.md` for cohort style)
   - `classes/<class-name>/syllabus/syllabus.md` — official syllabus (if it exists)

4. **Gather chapter/syllabus data**
   - If official syllabus exists in `classes/<class-name>/syllabus/syllabus.md`, use it
   - Otherwise, ask the teacher to provide chapter list, syllabus, or unit breakdown

5. **Generate the teaching map**
   - Follow the process in `_skill/SKILL_cohort_teaching_map.md`
   - Incorporate school calendar, no-school dates, and trimester ends
   - Integrate cohort tools (Discussion Brief, Pair & Defend, Case Study, Capstone)
   - Build realistic pacing for high school discussion-heavy instruction
   - Account for all breaks, half-days, and assessment checkpoints

6. **Write the map**
   - Save to `classes/<class-name>/teaching-map.md`
   - Follow the format specified in the skill definition

7. **Remind the teacher**
   - After generating, remind them to review for school events, field trips, or special schedules that may need adjustment

## Notes

- The teaching map aligns chapter content with the actual school calendar
- Cohort tools follow a rhythm: Reading → Discussion Brief → Pair & Defend → Case Study → (occasional) Capstone
- Major capstones are placed at trimester ends for summative assessment
- Flex days are built in for catch-up and review
