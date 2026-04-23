---
name: generate-substitute-plan
description: Generate a detailed substitute teacher plan for a specific day
args: "<week-number> <day>"
---

# Generate Substitute Plan

Create a detailed, self-contained substitute teacher plan for a teacher absence day.

## Usage

```
/generate-substitute-plan <week-number> <day>
```

**Examples:**
```
/generate-substitute-plan 1 friday
/generate-substitute-plan 2 thursday
/generate-substitute-plan 33 monday
```

## Process

1. **Validate inputs**
   - Check that week number is valid (1–39 for most courses)
   - Check that day is valid (monday, tuesday, wednesday, thursday, friday)
   - Read the teaching map to confirm this day is marked as **SUB:**
   - If not marked as SUB, ask: "This day isn't marked as a substitute day in the teaching map. Generate anyway? (yes/no)"

2. **Read context from teaching map**
   
   Extract for this specific day:
   - Week dates
   - Chapter being studied
   - Topic
   - What came before (previous day's activity)
   - What comes after (next day's activity)
   - Any notes about pacing or context

3. **Determine appropriate substitute activities**

   Substitute plans should use **non-cohort activities** that a substitute can facilitate without deep content knowledge:
   
   ✅ **Good substitute activities:**
   - Video with guided notes (video-note-catcher)
   - Individual reading with comprehension questions
   - Reflection writing (structured prompts)
   - Review worksheets
   - Chapter preview reading
   - Silent work on Discussion Brief drafts
   - Case Study write-up work (individual, not group facilitation)
   
   ❌ **Avoid for substitute days:**
   - Class discussion (requires teacher facilitation)
   - Pair & Defend debates (requires teacher moderation)
   - Case Study presentations (teacher needs to debrief)
   - Capstone presentations (teacher grading)
   - New concept introduction (needs expert instruction)

4. **Generate the substitute plan**

   Create a detailed, minute-by-minute plan using this structure:

   ```markdown
   # Substitute Plan — [Day, Month Date, Year]
   
   **Class:** [Class Name] ([Grade Level])  
   **Week:** Week X — [Chapter]  
   **Topic:** [Topic from teaching map]  
   **Period:** 45 minutes  
   **Teacher:** Mr. Ward
   
   ---
   
   ## Overview for Substitute
   
   Thank you for covering this class! This is a high school [course type] course. Students have been learning about [context from teaching map]. Today is a [video/reading/reflection/review] day. The lesson is fully structured — students should be working the entire period.
   
   **What you need to know:**
   - [1-2 sentences about where students are in the unit]
   - [1 sentence about what they did yesterday]
   - [1 sentence about what they'll do tomorrow when Mr. Ward returns]
   
   ---
   
   ## Materials Provided
   
   **On the teacher's desk:**
   - [ ] Attendance roster
   - [ ] [Handout name] (XX copies — one per student)
   - [ ] [Additional handout] (XX copies)
   - [ ] [Answer key / rubric] (for your reference only)
   - [ ] Collection folder (labeled "[Week X — Day]")
   
   **Technology:**
   - [ ] Video queued up on classroom computer: "[Video title]"
   - [ ] OR: Video link written on board (in case tech fails)
   
   ---
   
   ## Lesson Flow
   
   ### [0–5 min] Attendance & Introduction
   
   **Take attendance** (roster provided)
   
   **Introduce yourself briefly**, then say:
   
   > "[Mr. Ward's script for sub to read aloud]"
   
   ---
   
   ### [5–X min] [Activity 1 Name]
   
   **Instructions for sub:**
   [Detailed step-by-step for what the sub should do]
   
   **If students ask [common question]:**
   [Suggested response]
   
   **What students are doing:**
   [What students should be working on]
   
   ---
   
   ### [X–X min] [Activity 2 Name]
   
   [Repeat structure]
   
   ---
   
   ### [X–45 min] Wrap-Up & Collection
   
   **5 minutes before the bell:**
   
   Say:
   > "[Closing script]"
   
   **Collect:**
   - [ ] [Handout/worksheet name] — place in collection folder
   - [ ] [Other materials]
   
   **Leave on the desk:**
   - [ ] Attendance roster (with any notes about behavior or issues)
   - [ ] Collection folder
   
   ---
   
   ## If You Finish Early
   
   If students complete the work before the period ends:
   
   - Option 1: [Preview reading / silent reading]
   - Option 2: [Review previous chapter notes]
   - No free time / phone time — keep students working
   
   ---
   
   ## Behavior Notes
   
   - This is a discussion-heavy class, but today should be individual work (silent or quiet)
   - If students claim "Mr. Ward lets us work in groups" — today is individual work only
   - If a student finishes early and asks to leave: no early dismissal; use "If You Finish Early" options
   
   **If there are issues:**
   Please note on the attendance roster:
   - Student name
   - What happened
   - How you responded
   
   Mr. Ward will follow up when he returns.
   
   ---
   
   ## Contact Information
   
   **If you need help during class:**
   - Front office: [extension]
   - Department chair: [name, room number]
   
   **For Mr. Ward (non-urgent):**
   - Email: jeremy@workhorsesolutions.llc
   
   ---
   
   **Thank you for covering today!**
   ```

5. **Generate necessary handouts**

   If the substitute plan references handouts that don't exist yet, generate them:
   
   - Video note-catchers: Use `/generate-handout video-note-catcher`
   - Comprehension questions: Create based on chapter reading
   - Reflection prompts: Use `/generate-handout reflection`
   - Review worksheets: Create based on recent chapters

6. **Write files**

   Write substitute plan to week directory:
   
   **Main substitute plan** → `lesson-plans-<year>/week-XX-<date>/substitute-plan-<day>.md`
   - Full self-contained plan
   - Includes all materials references
   - Formatted for printing and leaving for the sub

7. **Create a substitute folder packet checklist**

   Generate a checklist file in the same directory: `lesson-plans-<year>/week-XX-<date>/substitute-checklist-<day>.md`
   
   ```markdown
   # Substitute Packet Checklist — Week X, [Day]
   
   **Date:** [Date]  
   **Class:** [Class name]
   
   ## What to Print
   
   - [ ] Substitute plan (this packet) — 1 copy
   - [ ] [Handout name] — XX copies (one per student)
   - [ ] [Handout name] — XX copies
   - [ ] Answer key / rubric — 1 copy (for sub reference)
   
   ## What to Queue Up
   
   - [ ] Video: "[Video title]" — link: [URL]
   - [ ] OR: Video file saved to Desktop: [filename]
   
   ## What to Leave on Desk
   
   - [ ] Attendance roster
   - [ ] All printed materials above
   - [ ] Collection folder labeled "Week X — [Day]"
   - [ ] Whiteboard markers (in case sub needs to write)
   
   ## Night Before
   
   - [ ] Email sub plan to front office
   - [ ] Leave printed packet on desk
   - [ ] Set up video on classroom computer
   - [ ] Write today's agenda on board (or leave note for sub to copy from plan)
   
   ---
   
   **Generated:** [Date]
   ```

8. **Report completion**

   Display summary:
   
   ```
   ✅ Substitute plan generated for Week X, [Day]
   
   Created in lesson-plans-<year>/week-XX-<date>/:
   - substitute-plan-<day>.md (full plan)
   - substitute-checklist-<day>.md (prep checklist)
   - handouts/ (if new handouts generated)
   
   Updated:
   - README.md (marked substitute plan as generated)
   
   Next steps:
   - Review the plan for accuracy
   - Queue up the video (if applicable)
   - Print materials the night before (use checklist)
   ```

## Substitute Plan Principles

Follow these principles when generating substitute plans:

1. **Assume zero content knowledge**: The sub doesn't know apologetics, theology, or the course structure
2. **Minimize decisions**: Don't ask the sub to make judgment calls — script everything
3. **Anticipate questions**: Include "If students ask X, say Y" sections
4. **Keep students working**: No downtime, no early dismissal, no "free time"
5. **Use proven activities**: Video + guided notes is gold; open discussion is risky
6. **Provide scripts**: Give the sub exact words to say to the class
7. **Make collection simple**: "Put everything in the folder" — don't ask sub to grade or evaluate
8. **Include behavior guidance**: Students will test a sub; give clear boundaries

## Context Awareness

When generating substitute plans, consider:

- **Timing in the unit**: Is this the first day of a new chapter (preview reading) or mid-chapter (review/synthesis)?
- **What came before**: If yesterday was heavy discussion, today can be lighter (video/reflection)
- **What comes after**: If tomorrow is a major assessment, today should be review or prep
- **Short weeks**: If it's a 3-day week, don't overload the sub day
- **Proximity to breaks**: Right before Thanksgiving/Christmas? Keep it simple and engaging.

## Notes

- All substitute plans are **non-cohort activities** (no Pair & Defend, no Case Study facilitation)
- Every sub plan includes a **collection folder** for student work
- Video is the most reliable sub activity (low-prep, keeps students engaged, requires no content expertise)
- Reflection writing is second-best (structured prompts, individual work, easy to collect)
- Reading comprehension questions work well but can feel tedious — mix with video or reflection
- **Never leave a sub plan that says "facilitate class discussion"** — that's asking for chaos
