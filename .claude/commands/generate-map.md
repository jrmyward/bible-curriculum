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
   - Present available teaching map styles:
     1. **Cohort Teaching Model** - Discussion-first, debate-heavy (default)
     2. **Lecture-Seminar Model** - Teacher-led content + discussion days
     3. **Inductive Bible Study (IBS)** - Observation → Interpretation → Application
     4. **Chronological Narrative** - Bible as one unified story
   - If the teacher doesn't specify, recommend based on course type:
     - Apologetics/Worldview → Cohort
     - Survey courses → Lecture-Seminar or Chronological Narrative
     - Book studies → Inductive Bible Study
     - Theology courses → Cohort or Lecture-Seminar

4. **Determine the school year**
   - Auto-detect from current date (Aug-May = current school year)
   - Or ask teacher: "Which school year is this map for? (e.g., 2026-27)"
   - This determines which school calendar to use

5. **Read required files**
   - `_shared/teaching-map-styles/<style>-teaching-map.md` — teaching map generation process for chosen style
   - `_shared/school-calendar-<year>.md` — school calendar and no-school dates (use year from step 4)
   - Style-specific tool files (e.g., `_shared/cohort-tools.md` for cohort style)
   - `_shared/supplemental-content.md` — guide for integrating supplemental units (if needed)

6. **Determine which syllabus to use**
   - Check for syllabi in this order:
     1. `classes/<class-name>/syllabus/custom-syllabus.md` (if exists, ask whether to use custom or official)
     2. `classes/<class-name>/syllabus/syllabus.md` (official extracted syllabus)
     3. If neither exists, ask teacher for chapter list/content outline
   - If custom syllabus is selected:
     - Read `_shared/supplemental-content.md` for integration guidance
     - Follow the structure defined in the custom syllabus (condensed core + supplemental, extended course, etc.)
     - Mark supplemental units clearly in the teaching map

7. **Generate the teaching map**
   - Follow the process in the selected teaching style's internal command file
   - Incorporate school calendar, no-school dates, and trimester ends
   - Integrate style-specific tools (e.g., cohort tools: Discussion Brief, Pair & Defend, Case Study, Capstone)
   - Build realistic pacing for high school instruction
   - Account for all breaks, half-days, and assessment checkpoints

8. **Write the map**
   - Save to `classes/<class-name>/teaching-maps/teaching-map-<year>.md` (e.g., `teaching-map-2026-27.md`)
   - If this is the first/only teaching map, also create a symlink: `classes/<class-name>/teaching-map.md` → `teaching-maps/teaching-map-<year>.md`
   - Follow the format specified in the teaching style definition
   - If using custom syllabus, add note at top referencing supplemental content

9. **Remind the teacher**
   - After generating, remind them to review for school events, field trips, or special schedules that may need adjustment

## Notes

- The teaching map aligns chapter content with the actual school calendar
- Cohort tools follow a rhythm: Reading → Discussion Brief → Pair & Defend → Case Study → (occasional) Capstone
- Major capstones are placed at trimester ends for summative assessment
- Flex days are built in for catch-up and review
