# Lesson Planning Skills — Quick Reference

This document explains how to use the lesson planning skills to build comprehensive, week-by-week lesson plans for your Bible curriculum courses.

---

## Overview

You have **5 skills** for lesson planning:

| Skill | Purpose | When to Use |
|-------|---------|-------------|
| **`/lesson-plan-workflow`** | Interactive project manager | Starting lesson planning for a class; resume in-progress work |
| **`/scaffold-lesson-structure`** | Set up directory structure | First step for any new class |
| **`/generate-lesson-plans`** | Create week-by-week plans | Generate detailed plans for a specific week |
| **`/generate-handout`** | Create specific handouts | Make individual handouts (reading guides, case studies, etc.) |
| **`/generate-substitute-plan`** | Create sub teacher plans | Generate detailed plans for teacher absence days |

---

## Recommended Workflow

### **Starting from Scratch**

If you're building lesson plans for a class that has a teaching map but no lesson plans yet:

1. **Run the workflow skill:**
   ```
   /lesson-plan-workflow understanding-the-faith
   ```
   
   This will:
   - Check if the directory structure exists (if not, offer to scaffold it)
   - Show you progress (how many weeks are complete)
   - Guide you week-by-week through lesson plan generation
   - Track progress so you can pause and resume

2. **Follow the prompts:**
   - Upload textbook chapter images when requested
   - Choose whether to continue to the next week or pause
   - Review generated lesson plans and handouts

3. **Repeat until all weeks are complete**

That's it! The workflow skill orchestrates everything.

---

### **Generating a Specific Week**

If you want to generate (or regenerate) a specific week's lesson plans:

```
/generate-lesson-plans 5
```

This will:
- Read the teaching map for Week 5 context
- Ask you to upload textbook chapter images
- Generate day-by-day lesson plans
- Generate all necessary handouts (reading guides, note-catchers, discussion briefs, etc.)
- Generate substitute plan if the week has a sub day

**Options:**
```
/generate-lesson-plans 5 --class understanding-the-faith
```

---

### **Creating Individual Handouts**

If you need to create (or recreate) a specific handout:

```
/generate-handout core-reading-guide --week 5 --chapter 3
/generate-handout case-study --week 7 --topic "Historical parallel: early church defending Scripture"
/generate-handout pair-and-defend --week 3 --prompt "Is objective truth possible?"
```

**Available handout types:**
- `core-reading-guide` — Strategic reading guide (skip/read sections)
- `note-catcher` — Guided note-taking worksheet
- `discussion-brief` — Discussion Brief template with prompt and rubric
- `case-study` — Case Study scenario with group work instructions
- `pair-and-defend` — Pair & Defend debate prep sheet
- `video-note-catcher` — Guided notes for a video
- `reflection` — Reflection writing prompts

---

### **Creating Substitute Plans**

If you need to create a substitute teacher plan for a specific day:

```
/generate-substitute-plan 1 friday
/generate-substitute-plan 33 monday
```

This will:
- Read the teaching map for that day's context
- Generate a detailed, minute-by-minute plan for the substitute
- Use non-cohort activities (video, reflection, individual work)
- Create a prep checklist for you (what to print, what to queue up)
- Write both a standalone version (for the sub) and embed it in the weekly lesson plan

---

## Directory Structure

After scaffolding, your `lesson-plans/` directory will look like this:

```
classes/understanding-the-faith/lesson-plans/
├── week-01-lesson-plans.md
├── week-02-lesson-plans.md
├── [...through week-39]
│
├── handouts/
│   ├── week-01/
│   │   ├── core-reading-guide-ch01.md
│   │   ├── note-catcher-ch01.md
│   │   ├── discussion-brief-01-template.md
│   │   ├── rhetoric-101.md
│   │   ├── video-note-catcher.md
│   │   └── week-01-reflection.md
│   ├── week-02/
│   │   └── [...]
│   └── [...through week-39]
│
├── substitute-plans/
│   ├── week-01-friday-sub.md
│   ├── week-01-friday-checklist.md
│   ├── week-02-thursday-sub.md
│   └── [...]
│
└── assessments/
    ├── capstone-01-rubric.md
    ├── capstone-02-rubric.md
    ├── capstone-03-rubric.md
    ├── capstone-final-rubric.md
    └── final-reflection-essay.md
```

---

## Typical Week-by-Week Generation Process

Here's what happens when you generate a week's lesson plans:

### **Step 1: You run the command**
```
/generate-lesson-plans 5
```

### **Step 2: Skill reads teaching map**
```
Week 5 (Sep 21–25, 2026)
Chapter: Ch 3 — Is the Bible Reliable?
Topic: Manuscript evidence, textual criticism, historical reliability
Activities:
- Mon: Discussion Brief #3 due
- Tue: Video — "The Case for Reliability of the Gospels"
- Wed: Debrief video; introduce skeptical objections
- Thu: Continue discussion; preview Ch 4
- Fri: Ch 4 reading
```

### **Step 3: Skill asks for chapter images**
```
To generate detailed lesson plans, please upload images of Chapter 3.
(Or type 'skip' to generate from teaching map only)
```

### **Step 4: You upload images**
You take photos of the textbook chapter and upload them.

### **Step 5: Skill analyzes chapter**
```
Chapter 3: "Is the Bible Reliable?" (24 pages)

Core sections identified:
- Section 1: Introduction (pp. 1-2)
- Section 2: Manuscript Evidence (pp. 3-7)
- Section 4: Textual Criticism (pp. 10-12)
[...]

Key concepts: manuscript count, reliability vs. inerrancy, textual variants

Scripture references: 2 Timothy 3:16, 2 Peter 1:21
```

### **Step 6: Skill designs the week arc**
```
Week 5 Arc:
- Mon: Discussion Brief #3 due; discuss objections to biblical reliability
- Tue: Watch video + Video Note-Catcher; debrief
- Wed: Introduce textual criticism; prep for Pair & Defend
- Thu: Pair & Defend — "Gospels are historical vs. faith documents"
- Fri: Ch 4 reading introduced; Unit 2 review
```

### **Step 7: Skill generates detailed lesson plans**
Creates a comprehensive markdown file with:
- 5 days of minute-by-minute lesson plans
- Teacher scripts, discussion prompts, activity instructions
- Timing for each segment (e.g., "[0-5 min] Opening", "[5-15 min] Activity 1")
- References to all handouts needed

### **Step 8: Skill generates handouts**
Creates all handouts referenced in the lesson plans:
- `core-reading-guide-ch03.md` (which sections to read/skip)
- `note-catcher-ch03.md` (guided notes for the reading)
- `discussion-brief-03-template.md` (prompt: "What's the strongest objection to biblical reliability?")
- `video-note-catcher-gospels.md` (guided notes for the video)
- `pair-and-defend-prep.md` (debate prep sheet)

### **Step 9: Skill writes files**
```
✅ Week 5 lesson plans generated

Created:
- lesson-plans/week-05-lesson-plans.md (5 days, 18 pages)

Handouts:
- handouts/week-05/core-reading-guide-ch03.md
- handouts/week-05/note-catcher-ch03.md
- handouts/week-05/discussion-brief-03-template.md
- handouts/week-05/video-note-catcher-gospels.md
- handouts/week-05/pair-and-defend-prep.md

Next steps:
- Review lesson plans for accuracy
- Queue up video: "The Case for Reliability of the Gospels"
- Print handouts before Monday
```

---

## Tips for Efficient Lesson Planning

### **1. Generate in Batches**

If multiple weeks cover the same chapter, generate them together:
- Weeks 2-3 both cover Ch 2 → Upload chapter images once, generate both weeks

### **2. Use the Workflow Skill**

Don't manually track progress — let `/lesson-plan-workflow` do it:
- It remembers what's complete
- It suggests the next logical week
- It picks up where you left off

### **3. Start with Week 1**

Week 1 is already complete and serves as the **exemplar** for all other weeks. The skills use it as a template for tone, structure, and level of detail.

### **4. Regenerate as Needed**

If you change your teaching approach mid-year, regenerate weeks:
```
/generate-lesson-plans 12  # Backs up existing, generates new version
```

### **5. Customize After Generation**

Generated lesson plans are comprehensive but not prescriptive. Feel free to:
- Adjust timing based on your class's pace
- Swap activities if something isn't working
- Add your own examples or stories
- Modify scripts to match your voice

---

## What Gets Generated

### **Lesson Plans Include:**
- ✅ Day-by-day breakdown (Monday–Friday, or shorter for 3-4 day weeks)
- ✅ Minute-by-minute timing for each activity
- ✅ Teacher scripts for key moments ("Say:", "Ask:")
- ✅ Discussion prompts and anticipated student responses
- ✅ Transition instructions between activities
- ✅ Exit tickets and homework assignments
- ✅ References to all handouts (with file paths)
- ✅ Notes about pacing, context, and special considerations

### **Handouts Include:**
- ✅ Core Reading Guides (strategic reading — skip/read sections)
- ✅ Note-Catchers (guided note-taking worksheets)
- ✅ Discussion Brief Templates (prompts + rubrics)
- ✅ Case Study Scenarios (realistic situations + discussion questions)
- ✅ Pair & Defend Prep Sheets (debate scaffolding for both sides)
- ✅ Video Note-Catchers (guided notes for videos)
- ✅ Reflection Prompts (synthesis writing)

### **Substitute Plans Include:**
- ✅ Detailed minute-by-minute instructions for the sub
- ✅ Exact scripts for the sub to read to the class
- ✅ Materials checklist (what to print, what to queue up)
- ✅ Student activity handouts (video note-catchers, reflection prompts, etc.)
- ✅ Behavior guidance ("If students ask X, say Y")
- ✅ Collection instructions (what to collect, where to leave it)
- ✅ Prep checklist for you (night-before setup)

---

## FAQ

### **Q: Do I need textbook chapter images?**
A: No, but **highly recommended**. With images, lesson plans are detailed and tailored to the actual chapter content. Without images, plans are based on the teaching map only (less detailed, more generic).

### **Q: Can I regenerate a week if I don't like the result?**
A: Yes! Just run `/generate-lesson-plans <week>` again. The skill will back up the existing file and create a new version.

### **Q: What if the teaching map changes?**
A: Regenerate the teaching map first with `/generate-map`, then regenerate affected weeks with `/generate-lesson-plans`.

### **Q: Can I generate handouts separately?**
A: Yes! Use `/generate-handout <type> --week <number>` to create or recreate any handout.

### **Q: How do I track progress across multiple work sessions?**
A: Use `/lesson-plan-workflow` — it tracks progress automatically and picks up where you left off.

### **Q: Can I use these skills for other classes?**
A: Yes! The skills work for any class in the `classes/` directory. Just specify `--class <class-name>` or run the skill from that class's directory.

### **Q: What if I want to customize the lesson format?**
A: The skills use Week 1 as the exemplar. If you update Week 1's format, regenerate other weeks and they'll follow the new pattern.

### **Q: How do substitute plans work?**
A: Substitute plans are generated automatically when you create a week that has a sub day (marked **SUB:** in the teaching map). They're written as both:
1. Standalone files in `substitute-plans/` (for printing and leaving for the sub)
2. Embedded in the weekly lesson plan file (for your reference)

---

## Next Steps

Ready to start? Run:

```
/lesson-plan-workflow understanding-the-faith
```

This will guide you through the entire process, from scaffolding to final week.

Or, if you prefer manual control, start with:

```
/scaffold-lesson-structure understanding-the-faith
/generate-lesson-plans 1
```

Happy planning! 📚
