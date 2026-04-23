---
name: scaffold-lesson-structure
description: Set up the complete lesson plan directory structure for a class
args: "[class-name] [--year YYYY-YY]"
---

# Scaffold Lesson Structure

Create the complete directory structure for lesson plans, handouts, substitute plans, and assessments for a class.

## Usage

```bash
/scaffold-lesson-structure <class-name> [--year YYYY-YY]
```

**Example:**

```bash
/scaffold-lesson-structure understanding-the-faith
/scaffold-lesson-structure understanding-the-faith --year 2026-27
/scaffold-lesson-structure worldview --year 2027-28
```

## Prerequisites

Before running this command, ensure:

- ✅ **Teaching map exists**: `classes/<class-name>/teaching-maps/teaching-map-<year>.md`
- ✅ **Class directory exists**: `classes/<class-name>/`

If missing:

- Teaching map → Run `/generate-map <class-name>`
- Class directory → Run `/new-class <class-name>`

## Process

1. **Validate class name and year**
   - Check that `classes/<class-name>/` exists
   - If not, list available classes and exit
   - If `--year` not provided, detect from teaching map or default to current school year
   - Year format: `YYYY-YY` (e.g., `2026-27`)

2. **Read the teaching map**
   - Try `classes/<class-name>/teaching-maps/teaching-map-<year>.md` first
   - Fall back to `classes/<class-name>/teaching-map.md` if teaching-maps doesn't exist
   - Extract:
     - Total number of weeks (e.g., 39 weeks)
     - Week dates (for directory naming: `week-01-aug-24`, `week-02-aug-31`, etc.)
     - Which weeks have substitute days (marked with **SUB:** in the teaching map)
     - Which weeks have capstones or major assessments

3. **Check for existing structure**
   - If `classes/<class-name>/lesson-plans-<year>/` already exists, ask:
     - "This class already has lesson plans for <year>. Recreate structure? (yes/no)"
   - If yes, proceed (won't delete existing files, just ensure structure is complete)
   - If no, exit

4. **Create directory structure**

   Create the following directories:
   
   ```
   classes/<class-name>/lesson-plans-<year>/
   classes/<class-name>/lesson-plans-<year>/assessments/
   classes/<class-name>/lesson-plans-<year>/handouts/
   classes/<class-name>/lesson-plans-<year>/week-01-<mon-day>/
   classes/<class-name>/lesson-plans-<year>/week-01-<mon-day>/handouts/
   classes/<class-name>/lesson-plans-<year>/week-02-<mon-day>/
   classes/<class-name>/lesson-plans-<year>/week-02-<mon-day>/handouts/
   [...through week-XX based on teaching map]
   ```

   **Directory purpose:**
   - `assessments/` — Shared rubrics and assessment materials used across all weeks
   - `handouts/` — Shared handouts used across multiple weeks (top-level)
   - `week-XX/handouts/` — Week-specific handouts (reading guides, note-catchers, etc.)

   Note: Week directory names include the date (e.g., `week-01-aug-24`) parsed from teaching map.

   **Important:** Add `.gitkeep` files to all empty directories so Git tracks them.

5. **Create main README file**

   **`lesson-plans-<year>/README.md`:**
   ```markdown
   # Lesson Plans — [Class Name] (School Year <year>)
   
   This directory contains comprehensive, day-by-day lesson plans for the <year> school year.
   
   ## Structure
   
   Each week has its own directory with all materials:
   
   - **`assessments/`**: Shared rubrics for all grading categories
   - **`handouts/`**: Shared handouts used across multiple weeks
   - **`week-XX-<mon-day>/`**: Week directory (named with start date)
     - **`README.md`**: Week overview and post-teaching notes
     - **`1-monday.md`** through **`5-friday.md`**: Daily lesson plans (number prefix keeps them ordered)
     - **`handouts/`**: Week-specific handouts
   - **`.generation-log.md`**: Tracks how each week was created
   
   ## Generating Lesson Plans
   
   Use `/generate-lesson-plans <week-number>` to create comprehensive plans from textbook chapters.
   
   ## Weeks Overview
   
   [Auto-generated table from teaching map showing week number, dates, chapter, and key activities]
   ```

6. **Create generation log**

   **`.generation-log.md`:**
   ```markdown
   # Generation Log — <year> Lesson Plans
   
   This file tracks how each week's lesson plans were created.
   
   **Legend:**
   - 🆕 Generated from scratch
   - 📋 Copied from previous year
   - 🔄 Regenerated (after initial generation)
   - ✏️  Manually edited
   
   ---
   
   ## Week-by-Week Log
   
   | Week | Dates | Method | Date Generated | Notes |
   |------|-------|--------|----------------|-------|
   [Auto-generated rows for all weeks]
   ```

7. **Create week-by-week directories with README stubs**

   For each week in the teaching map, create:
   
   **Directory:** `week-XX-<mon-day>/` (e.g., `week-01-aug-24/`, `week-05-sep-21/`)
   
   **File:** `week-XX-<mon-day>/README.md`
   ```markdown
   # Week XX — [Dates]
   
   **Chapter:** [Chapter from teaching map]  
   **Topic:** [Topic from teaching map]  
   **Class Period:** 45 minutes
   
   ---
   
   ## Week Overview
   
   ### Activities
   [Copy activities from teaching map for this week]
   
   ### Assessments Due
   [List assessments due this week]
   
   ### Notes
   [Any notes from teaching map]
   
   ---
   
   ## Files in This Directory
   
   ### Lesson Plans
   - `1-monday.md` through `5-friday.md` — Daily lesson plans (not yet generated)
   
   ### Handouts (`handouts/`)
   - Week-specific handouts (empty until generated)
   
   ---
   
   ## Post-Week Notes
   
   _Add notes here after teaching this week to inform next year's planning._
   
   **What worked:**
   - 
   
   **What needs adjustment:**
   - 
   
   **Timing notes:**
   - 
   
   **Student feedback:**
   - 
   ```
   
   **Also create:** Empty `handouts/` subdirectory for each week

8. **Create assessments directory with README**

   **`assessments/README.md`:**
   ```markdown
   # Assessments — [Class Name] (<year>)
   
   Major course assessments and rubrics.
   
   [Auto-generated list of capstones and final assessments from teaching map]
   ```

9. **Create assessment stub files**

   Create shared rubric files for all grading categories:

   **Shared rubrics (always created):**

   - `assessments/discussion-brief-rubric.md` — 20-point rubric (thesis, reasoning, evidence, clarity, mechanics)
   - `assessments/case-study-rubric.md` — Pass/fail participation rubric (100/50/0)
   - `assessments/pair-and-defend-rubric.md` — Pass/fail participation rubric (100/50/0)
   - `assessments/capstone-rubric.md` — 100-point rubric (thesis, evidence, counterargument, presentation, final brief)

   **Assessment-specific stubs (from teaching map):**

   - `assessments/capstone-01-rubric.md` — Capstone #1 prompt and timeline
   - `assessments/capstone-02-rubric.md` — Capstone #2 prompt and timeline
   - `assessments/capstone-03-rubric.md` — Capstone #3 prompt and timeline
   - `assessments/capstone-final-rubric.md` — Final Capstone prompt and timeline
   - `assessments/final-reflection-essay.md` — End-of-course reflection

   Each capstone stub includes the shared rubric structure plus capstone-specific details (prompt, chapters, due dates) from the teaching map.

10. **Generate weeks overview table**

    Parse the teaching map to create a table for the lesson-plans README:
    
    ```markdown
    | Week | Dates | Chapter(s) | Key Activities | Sub Day |
    |------|-------|------------|----------------|---------|
    | 1 | Aug 24–28 | Ch 1 | Intro, Discussion Brief #1 | Fri |
    | 2 | Aug 31–Sep 2 | Ch 2 | Truth & relativism | Thu |
    [...]
    ```

11. **Report completion**

    Display a summary:
    
    ```
    ✅ Lesson structure scaffolded for [class-name] (<year>)
    
    Created:
    - lesson-plans-<year>/ directory
    - XX week directories (week-01-<date> through week-XX-<date>)
    - XX README stubs (one per week)
    - XX handout subdirectories (empty, one per week)
    - assessments/ directory with X stub files
    - .generation-log.md
    - Main README.md
    
    Next steps:
    - Use `/generate-lesson-plans <week-number>` to create detailed plans
    - Use `/lesson-plan-workflow [class-name]` for guided week-by-week generation
    ```

## Notes

- This skill only creates the *structure* — it doesn't generate actual lesson content
- Existing files are never overwritten
- Stub files contain context from the teaching map to guide future generation
- The structure is based on the teaching map, so run `/generate-map` first if needed
