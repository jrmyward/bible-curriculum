# Bible Curriculum Skills — Complete Overview

This repository includes a comprehensive set of skills for building Bible curriculum teaching maps and lesson plans.

---

## Skill Categories

### **📅 Teaching Map Generation** (1 skill)

| Skill | Purpose | Example |
|-------|---------|---------|
| `/generate-map` | Create teaching map for a class | `/generate-map understanding-the-faith` |

**What it does:**
- Reads syllabus and school calendar
- Generates week-by-week schedule aligned to actual school dates
- Integrates cohort teaching tools (Discussion Briefs, Pair & Defend, Case Studies, Capstones)
- Accounts for no-school days, teacher absences, trimester ends
- Produces a comprehensive `teaching-map.md` file

**When to use:**
- Starting a new class
- Updating a class for a new school year
- Revising pacing or assessment schedule

---

### **📚 Lesson Planning** (5 skills)

| Skill | Purpose | Example |
|-------|---------|---------|
| `/lesson-plan-workflow` | Interactive project manager for lesson planning | `/lesson-plan-workflow understanding-the-faith` |
| `/scaffold-lesson-structure` | Set up directory structure | `/scaffold-lesson-structure understanding-the-faith` |
| `/generate-lesson-plans` | Generate week-by-week lesson plans | `/generate-lesson-plans 5` |
| `/generate-handout` | Create specific handouts | `/generate-handout case-study --week 7 --topic "Early church apologetics"` |
| `/generate-substitute-plan` | Create detailed sub teacher plans | `/generate-substitute-plan 1 friday` |

**What they do:**

**`/lesson-plan-workflow`**
- Checks current progress (which weeks are complete)
- Guides you week-by-week through lesson plan generation
- Tracks progress and resumes where you left off
- Suggests next logical steps based on teaching map context

**`/scaffold-lesson-structure`**
- Creates full directory structure (week folders, handout folders, substitute plans, assessments)
- Generates README files explaining the structure
- Creates stub files for all weeks (filled in later by `/generate-lesson-plans`)
- Parses teaching map to create weeks overview table

**`/generate-lesson-plans`**
- Reads teaching map context for a specific week
- Analyzes textbook chapter images (if provided)
- Generates detailed day-by-day lesson plans (45-min periods, minute-by-minute timing)
- Creates all necessary handouts (reading guides, note-catchers, discussion briefs, etc.)
- Generates substitute plan if the week includes a sub day
- Follows Week 1 as the exemplar for tone and structure

**`/generate-handout`**
- Creates individual handouts using templates
- Types: core-reading-guide, note-catcher, discussion-brief, case-study, pair-and-defend, video-note-catcher, reflection
- Each handout is self-contained (includes instructions, rubrics, prompts)
- Written to `handouts/week-XX/` with consistent naming

**`/generate-substitute-plan`**
- Reads teaching map context for a specific day
- Designs non-cohort activities (video, reflection, individual work)
- Creates detailed minute-by-minute plan for the substitute
- Includes exact scripts for sub to read, materials checklist, behavior guidance
- Writes both standalone version (for sub) and embedded version (in weekly lesson plan)
- Generates prep checklist for teacher (what to print, what to queue up)

**When to use:**
- **Workflow**: Starting lesson planning or resuming in-progress work
- **Scaffold**: First step before generating any lesson plans
- **Lesson Plans**: After scaffold, generate week-by-week (or regenerate specific weeks)
- **Handouts**: Create/recreate individual handouts as needed
- **Substitute Plans**: Generate detailed plans for teacher absence days

---

## Recommended Usage Flow

### **Starting a New Class**

```
1. /generate-map understanding-the-faith
   → Creates teaching-map.md

2. /lesson-plan-workflow understanding-the-faith
   → Scaffolds structure (if needed)
   → Guides you week-by-week through lesson plan generation
   → Tracks progress and resumes where you left off
```

That's it! The workflow skill orchestrates everything else.

---

### **Manual Control (Advanced)**

If you prefer step-by-step control instead of the workflow:

```
1. /scaffold-lesson-structure understanding-the-faith
   → Sets up directory structure

2. /generate-lesson-plans 1
   → Upload textbook Chapter 1 images
   → Generates Week 1 plans + handouts

3. /generate-lesson-plans 2
   → Upload textbook Chapter 2 images
   → Generates Week 2 plans + handouts

[Repeat for all weeks]

4. /generate-substitute-plan 1 friday
   → Creates detailed sub plan for Week 1 Friday

5. /generate-handout case-study --week 7 --topic "Historical parallel"
   → Creates a custom handout
```

---

## Skill Dependencies

```
generate-map (standalone — no dependencies)
    ↓
lesson-plan-workflow (orchestrates all below)
    ↓
    ├─ scaffold-lesson-structure (sets up directories)
    ├─ generate-lesson-plans (creates week plans)
    │       ↓
    │       ├─ generate-handout (creates handouts)
    │       └─ generate-substitute-plan (if sub day in the week)
    │
    └─ generate-handout (can be used standalone)
```

**Key points:**
- `generate-map` is run first (creates teaching map)
- `lesson-plan-workflow` orchestrates the lesson planning process
- `scaffold-lesson-structure` is run once per class (sets up folders)
- `generate-lesson-plans` can call `generate-handout` and `generate-substitute-plan` automatically
- All skills can be run standalone for manual control

---

## File Outputs

### **After `/generate-map`:**
```
classes/understanding-the-faith/
└── teaching-map.md
```

### **After `/scaffold-lesson-structure`:**
```
classes/understanding-the-faith/
├── teaching-map.md
└── lesson-plans/
    ├── README.md
    ├── week-01-lesson-plans.md (stub)
    ├── week-02-lesson-plans.md (stub)
    ├── [...through week-39]
    ├── handouts/
    │   ├── README.md
    │   ├── week-01/ (empty)
    │   ├── week-02/ (empty)
    │   └── [...]
    ├── substitute-plans/
    │   └── README.md
    └── assessments/
        ├── README.md
        ├── capstone-01-rubric.md (stub)
        ├── capstone-02-rubric.md (stub)
        ├── capstone-03-rubric.md (stub)
        └── capstone-final-rubric.md (stub)
```

### **After `/generate-lesson-plans 1`:**
```
classes/understanding-the-faith/lesson-plans/
├── week-01-lesson-plans.md (fully generated, 20+ pages)
├── handouts/
│   └── week-01/
│       ├── core-reading-guide-ch01.md
│       ├── note-catcher-ch01.md
│       ├── discussion-brief-01-template.md
│       ├── rhetoric-101.md
│       ├── video-note-catcher.md
│       └── week-01-reflection.md
└── substitute-plans/
    ├── week-01-friday-sub.md
    └── week-01-friday-checklist.md
```

---

## What's Generated vs. What You Provide

| You Provide | Skills Generate |
|-------------|-----------------|
| Syllabus (chapter list, learning objectives) | Teaching map (week-by-week schedule) |
| School calendar (no-school days, breaks) | Lesson plans (day-by-day, minute-by-minute) |
| Textbook chapter images (photos/scans) | Handouts (reading guides, worksheets, case studies) |
| Teaching style preference (cohort, IBS, etc.) | Substitute plans (detailed instructions for subs) |
| Assessment weights (from syllabus) | Assessment rubrics (criteria, point values) |

**In other words:**
- You provide the **raw inputs** (syllabus, calendar, textbook)
- Skills generate the **teaching materials** (maps, plans, handouts)

---

## Skill Quality Standards

All generated content follows these standards:

### **Teaching Maps**
- ✅ Aligned to actual school calendar (no-school days, breaks, trimester ends)
- ✅ Realistic pacing for high school discussion-heavy instruction
- ✅ Cohort tool rhythm (Reading → Brief → Debate → Case Study → Capstone)
- ✅ Buffer and flex time built in
- ✅ Capstones placed at natural stopping points (trimester ends, before breaks)

### **Lesson Plans**
- ✅ Detailed day-by-day breakdown (Monday–Friday or shorter for short weeks)
- ✅ Minute-by-minute timing (e.g., "[0-5 min] Opening")
- ✅ Teacher scripts for key moments ("Say:", "Ask:")
- ✅ Discussion prompts with anticipated responses
- ✅ Transitions between activities
- ✅ Exit tickets and homework
- ✅ Follows Week 1 exemplar for tone and structure

### **Handouts**
- ✅ Self-contained (includes all instructions, rubrics, prompts)
- ✅ Age-appropriate for 11th–12th grade
- ✅ Clear formatting (tables, bullet points, fill-in sections)
- ✅ Consistent naming convention (lowercase, hyphenated)
- ✅ Referenced from lesson plans with file paths

### **Substitute Plans**
- ✅ Assumes sub has zero content knowledge
- ✅ Minute-by-minute instructions
- ✅ Exact scripts for sub to read aloud
- ✅ Non-cohort activities (video, reflection, individual work — no facilitated discussion)
- ✅ Materials checklist, behavior guidance, collection instructions
- ✅ Prep checklist for teacher (night-before setup)

---

## Customization & Iteration

All skills support iteration and customization:

- **Regenerate weeks**: Run `/generate-lesson-plans <week>` again to regenerate with new approach
- **Customize after generation**: Edit generated files to match your teaching style
- **Update teaching map**: Regenerate with `/generate-map` if schedule changes
- **Reuse across years**: Same skills work for 2026-27, 2027-28, etc. (just update calendar)

**Key principle**: Skills generate **high-quality first drafts**, not rigid prescriptions. You're the teacher — customize as needed.

---

## Examples

### **Example 1: Start Understanding the Faith lesson plans**

```
/lesson-plan-workflow understanding-the-faith
```

**Output:**
```
📋 Lesson Plan Status: Not Started

No lesson-plans directory found.

Next step: Scaffold the directory structure.

Would you like me to run `/scaffold-lesson-structure` now? (yes)

[Scaffolds structure]

✅ Structure scaffolded. 39 week folders created.

Next: Generate Week 1 lesson plans.

Do you have textbook Chapter 1 images ready? (yes)

[Upload images]

Generating Week 1 lesson plans...

✅ Week 1 complete! (5 days, 6 handouts, 1 sub plan)

Progress: 1 / 39 weeks

Continue to Week 2? (yes)
```

---

### **Example 2: Generate a specific week**

```
/generate-lesson-plans 12
```

**Output:**
```
Generating lesson plans for Week 12...

Week 12 (Nov 9-10, 2026)
Chapter: Ch 7-8 Synthesis (Capstone #2 Prep)
Topic: Trimester 1 wrap-up
Activities:
- Mon: Ch 8 reading (resurrection evidence)
- Tue: Discussion Brief #8 due; peer feedback on discussion habits

Do you have textbook Chapter 8 images? (yes)

[Upload images]

Analyzing Chapter 8 structure...

✅ Week 12 complete!

Created:
- lesson-plans/week-12-lesson-plans.md
- handouts/week-12/core-reading-guide-ch08.md
- handouts/week-12/note-catcher-ch08.md
- handouts/week-12/discussion-brief-08-template.md
- handouts/week-12/peer-feedback-form.md

No substitute plan needed (no sub days this week).
```

---

### **Example 3: Generate a custom handout**

```
/generate-handout case-study --week 14 --topic "Ethical dilemma: responding to the problem of evil in pastoral context"
```

**Output:**
```
Generating Case Study for Week 14...

Topic: Ethical dilemma — problem of evil in pastoral setting
Chapters: Ch 9 (Good and Evil)

✅ Case Study created!

File: handouts/week-14/case-study-problem-of-evil-pastoral.md

Scenario: A high school student asks for counsel after a family tragedy...

Includes:
- Realistic scenario (3 paragraphs)
- 5 discussion questions
- Group roles (Facilitator, Scribe, Presenter, Researcher)
- Write-up instructions
- Rubric (20 points)
```

---

## Next Steps

Ready to start? Choose your path:

### **Path 1: Guided (Recommended)**
```
/lesson-plan-workflow understanding-the-faith
```
Let the workflow guide you step-by-step.

### **Path 2: Manual Control**
```
1. /scaffold-lesson-structure understanding-the-faith
2. /generate-lesson-plans 1
3. /generate-lesson-plans 2
[...repeat for all weeks]
```
Generate each component manually.

### **Path 3: Just the Teaching Map**
```
/generate-map understanding-the-faith
```
Generate only the teaching map (no lesson plans yet).

---

## Support

- **Quick Reference**: See `README-LESSON-PLANNING.md` for detailed usage guide
- **Skill Definitions**: Each `.skill.md` file has full documentation
- **Example Output**: Week 1 lesson plans are already complete — see `classes/understanding-the-faith/lesson-plans/week-01-lesson-plans.md`

Happy teaching! 📚
