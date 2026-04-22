Generate a cohort teaching map for a class in this Bible curriculum repository.

Follow these steps:

1. Read `.claude/commands/cohort-teaching-map.md` for the full teaching map generation process and format.

2. Read `_shared/school-calendar-2026-27.md` for the school calendar, trimester dates, and all no-school dates.

3. Ask the teacher: which class is this teaching map for? List the available classes from `classes/`.

4. Check if `classes/<class-name>/teaching-map.md` already exists.
   - If it exists, ask whether to regenerate or update it.
   - If it doesn't exist, check for `classes/<class-name>/syllabus/syllabus.md` to use as the source.
   - If no syllabus exists, ask the teacher to paste or describe the chapter list, syllabus, or unit breakdown.

5. Generate the full cohort teaching map following the skill definition, incorporating:
   - The school calendar and no-school dates
   - The cohort tools from `_shared/cohort-tools.md`
   - The chapter/unit list from the syllabus or provided by the teacher
   - Realistic pacing for a high school Bible class (discussion-heavy, not lecture-heavy)

6. Write the completed map to `classes/<class-name>/teaching-map.md`.

7. After generating, remind the teacher to review the map and flag any weeks that need adjustment for school events, field trips, or special schedules.
