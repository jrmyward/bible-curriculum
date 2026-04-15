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
   - `_skill/SKILL_supplemental_content.md` — guide for integrating supplemental units

5. **Determine which syllabus to use**
   - Check for syllabi in this order:
     1. `classes/<class-name>/syllabus/custom-syllabus.md` (if exists, ask whether to use custom or official)
     2. `classes/<class-name>/syllabus/syllabus.md` (official extracted syllabus)
     3. If neither exists, ask teacher for chapter list/content outline
   - If custom syllabus is selected:
     - Read `_skill/SKILL_supplemental_content.md` for integration guidance
     - Follow the structure defined in the custom syllabus (condensed core + supplemental, extended course, etc.)
     - Mark supplemental units clearly in the teaching map

6. **Generate the teaching map**
   - Follow the process in `_skill/SKILL_cohort_teaching_map.md`
   - Incorporate school calendar, no-school dates, and trimester ends
   - Integrate cohort tools (Discussion Brief, Pair & Defend, Case Study, Capstone)
   - Build realistic pacing for high school discussion-heavy instruction
   - Account for all breaks, half-days, and assessment checkpoints

7. **Write the map**
   - Save to `classes/<class-name>/teaching-map.md`
   - Follow the format specified in the skill definition
   - If using custom syllabus, add note at top referencing supplemental content

8. **Remind the teacher**
   - After generating, remind them to review for school events, field trips, or special schedules that may need adjustment

## Notes

- The teaching map aligns chapter content with the actual school calendar
- Cohort tools follow a rhythm: Reading → Discussion Brief → Pair & Defend → Case Study → (occasional) Capstone
- Major capstones are placed at trimester ends for summative assessment
- Flex days are built in for catch-up and review
