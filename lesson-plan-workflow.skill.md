---
name: lesson-plan-workflow
description: Interactive workflow guide for building out lesson plans for a class
args: "[class-name] [--year YYYY-YY]"
---

# Lesson Plan Workflow

Interactive guide to build out a complete set of lesson plans for a class, from scaffolding to final week.

## Usage

```
/lesson-plan-workflow [class-name] [--year YYYY-YY]
```

**Examples:**
```
/lesson-plan-workflow understanding-the-faith
/lesson-plan-workflow understanding-the-faith --year 2026-27
/lesson-plan-workflow worldview --year 2027-28
```

## What This Skill Does

This is a **guided workflow** that walks you through:
1. Setting up the lesson plan directory structure
2. Generating week-by-week lesson plans in order
3. Tracking progress
4. Identifying what's complete and what's still needed

Think of it as a project manager for lesson planning.

---

## Process

### 1. **Validate Class and Year**

- If `[class-name]` not provided, detect from current directory or ask user
- Verify `classes/<class-name>/` exists
- If `--year` not provided, detect from existing directories or default to current school year
- Check for teaching map: `classes/<class-name>/teaching-maps/teaching-map-<year>.md`
  - Fall back to `classes/<class-name>/teaching-map.md` if teaching-maps doesn't exist
  - If missing: "No teaching map found for <year>. Generate one first with `/generate-map [class-name]`" → Exit

### 2. **Check Current Status**

Scan the `classes/<class-name>/lesson-plans-<year>/` directory:

**If directory doesn't exist:**
```
📋 Lesson Plan Status: Not Started

No lesson-plans directory found. 

Next step: Scaffold the directory structure with `/scaffold-lesson-structure [class-name]`

Would you like me to run that now? (yes/no)
```

**If directory exists but mostly empty:**
```
📋 Lesson Plan Status: Scaffolded

Structure exists, but no lesson plans generated yet.

Weeks completed: 0 / XX
Handouts created: 0
Substitute plans: 0 / X

Next step: Generate lesson plans week-by-week, starting with Week 1.

Would you like to start with Week 1? (yes/no)
```

**If directory has some lesson plans:**
```
📋 Lesson Plan Status: In Progress

Weeks completed: X / XX
├─ Week 1: ✅ Complete
├─ Week 2: ✅ Complete
├─ Week 3: ⚠️  Stub only (not generated)
├─ Week 4: ⚠️  Stub only
[...]

Handouts created: XX files
Substitute plans: X / X complete

Next incomplete week: Week 3

Would you like to generate Week 3 now? (yes/no/choose different week)
```

**If all lesson plans complete:**
```
📋 Lesson Plan Status: Complete ✅

All XX weeks have lesson plans.
All X substitute plans generated.
Total handouts: XXX files

Would you like to:
1. Review a specific week
2. Regenerate a week with updates
3. Generate assessment rubrics
4. Exit workflow
```

### 3. **Interactive Week-by-Week Generation**

If user chooses to generate a week:

```
Generating lesson plans for Week X...

According to the teaching map:
- Dates: [dates]
- Chapter(s): [chapter]
- Topic: [topic]
- Activities: [list from teaching map]
- Substitute day: [yes/no]

Do you have textbook chapter images ready? (yes/no/skip)
```

**If yes:**
- "Great! Upload images for [Chapter X] now."
- Wait for user to upload images
- Run `/generate-lesson-plans X` with images

**If no:**
- "No problem. I can wait while you take photos, or generate from teaching map only (less detail). Wait or skip?"
  - **Wait**: "Let me know when you're ready with the images."
  - **Skip**: Run `/generate-lesson-plans X` without images

**If skip:**
- Run `/generate-lesson-plans X` without images (teaching-map-only mode)

After generating:
```
✅ Week X complete!

Created:
- lesson-plans-<year>/week-XX-lesson-plans.md
- X handouts
- [Substitute plan if applicable]

Progress: X / XX weeks complete

Next week: Week [X+1] — [Chapter] — [Topic]

Continue to Week [X+1]? (yes/no/pause)
```

**If yes**: Loop back to Step 3 for next week  
**If no**: Go to Step 4 (Summary & Next Steps)  
**If pause**: Go to Step 4 (Summary & Next Steps)

### 4. **Summary & Next Steps**

When user pauses or completes the workflow:

```
📊 Lesson Plan Progress Summary

Class: [class-name]
Total weeks: XX

✅ Completed: X weeks
⚠️  Not generated: X weeks
📄 Handouts created: XXX files
📝 Substitute plans: X / X

Weeks still needed:
- Week X: [Chapter] — [Topic]
- Week X: [Chapter] — [Topic]
[...]

Assessments still needed:
- Capstone #1 Rubric (Ch 3-4)
- Capstone #2 Rubric (Ch 7-8)
[...]

---

Next time you run `/lesson-plan-workflow [class-name]`, I'll pick up where you left off.

You can also generate specific weeks manually with:
  `/generate-lesson-plans <week-number>`

Or generate specific handouts with:
  `/generate-handout <type> --week <number>`
```

---

## Advanced Options

### **Batch Mode**

If user wants to generate multiple weeks at once:

```
/lesson-plan-workflow understanding-the-faith --batch 5-10
```

This generates Weeks 5–10 in sequence, pausing between each to allow textbook image uploads.

### **Regenerate Mode**

If user wants to update existing lesson plans:

```
/lesson-plan-workflow understanding-the-faith --regenerate 7
```

This backs up Week 7, then regenerates it (useful if teaching approach changes mid-year).

### **Assessment Mode**

If user wants to focus on generating assessment rubrics:

```
/lesson-plan-workflow understanding-the-faith --assessments
```

This skips weekly lesson plans and generates:
- All Capstone rubrics
- Final reflection essay prompts
- Any other major assessments from teaching map

---

## Progress Tracking

This skill maintains a hidden progress file: `lesson-plans-<year>/.progress.json`

**Structure:**
```json
{
  "class": "understanding-the-faith",
  "total_weeks": 39,
  "completed_weeks": [1, 2, 5, 6],
  "substitute_plans_complete": ["week-01-friday", "week-02-thursday"],
  "assessments_complete": ["capstone-01-rubric"],
  "last_updated": "2026-04-22",
  "next_suggested_week": 3
}
```

**Why track progress?**
- Resume workflow exactly where you left off
- Avoid accidentally regenerating completed weeks
- Show visual progress (motivating!)
- Suggest next logical step

**Update triggers:**
- After each week is generated
- After each substitute plan is created
- After each assessment rubric is created

---

## Smart Suggestions

Based on progress and teaching map context, suggest logical next steps:

**Example 1: Week 1 complete, but Week 2 is a short week**
```
💡 Suggestion: Week 2 is a 3-day week (Sep 3 is a sub day). 
This is a good week to generate next since it's lighter.
```

**Example 2: Week 6 complete, Week 7 is Capstone prep**
```
💡 Suggestion: Week 7 includes Capstone #1 prep. 
You may want to generate the Capstone #1 rubric first so students know expectations.

Generate Capstone #1 rubric now? (yes/no)
```

**Example 3: Approaching a trimester end**
```
💡 Suggestion: You're approaching the end of Trimester 1 (Week 12). 
Consider generating Weeks 10-12 as a batch so you can see the full T1 arc.
```

**Example 4: Multiple weeks share the same chapter**
```
💡 Suggestion: Weeks 2-3 both cover Chapter 2. 
Generate Week 2 first, then use the same chapter images for Week 3 (I'll remember them).
```

---

## Example Workflow Session

```
User: /lesson-plan-workflow understanding-the-faith