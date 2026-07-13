# Command Quick Reference

Quick guide to all available curriculum generation commands.

---

## Class setup pipeline (current)

A complete class has **three pillars**: repo content · **Rubicon Atlas** · **Google**
(Classroom/Forms/Slides). The orchestrator **`/setup-class <class>`** walks all of it; the stages it
sequences:

**Once per class:** `/new-class` → upload syllabus → `/generate-official-syllabus` → `/generate-map`
→ `/scaffold-lesson-structure`.

**Per chapter:** `/build-chapter` (week-style daily plans) → `/build-atlas` (unit fields + Madeline
Hunter dailies) → `/push-atlas` (Playwright) → `/publish-chapter` (Classroom + Form-quiz test +
Slides).

| Command | Pillar | Purpose |
|---------|--------|---------|
| `/setup-class` | all | Front-to-back orchestrator; resumable |
| `/build-chapter` | content | One chapter's daily plans (`--model publisher`/`cohort`) |
| `/build-atlas` | Atlas | Author `rubicon-atlas/` unit fields + daily lessons |
| `/push-atlas` | Atlas | Push to Rubicon Atlas via Playwright (live Chrome) |
| `/publish-chapter` | Google | Classroom materials + video worksheet + Form quiz + Slides decks |

**Model:** `publisher` (Summit default — Start Slide template, publisher activities, Form-quiz tests)
or `cohort` (worldviews/apologetics — Discussion Briefs / Pair & Defend). See
[`lesson-plan-standards.md`](lesson-plan-standards.md). Runbooks: [`_scripts/atlas/README.md`](../_scripts/atlas/README.md),
[`_scripts/classroom/README.md`](../_scripts/classroom/README.md). Exemplar: **Foundations Ch 1–2**.

> The sections below predate this pipeline (they describe the older cohort-only, one-`lesson-plans.md`
> -per-week flow). Kept for reference; prefer the pipeline above.

---

## Getting Started (New Class)

**Step 1:** Create the class structure

```bash
/new-class <class-name>
```

**Step 2:** Upload syllabus images to `classes/<class-name>/syllabus/`, then extract:

```bash
/generate-official-syllabus <class-name>
```

**Step 3:** Generate teaching map

```bash
/generate-map <class-name>
```

**Step 4:** Build lesson plans (recommended - orchestrated workflow)

```bash
/lesson-plan-workflow <class-name>
```

---

## Primary Commands (User-Facing)

| Command | Purpose | When to Use |
|---------|---------|-------------|
| `/new-class` | Create new class | First time setup for a course |
| `/generate-map` | Create teaching map | After syllabus is ready; start of planning |
| `/lesson-plan-workflow` | **Start here for lesson planning** | Interactive, week-by-week generation |
| `/generate-lesson-plans <week>` | Generate specific week | Manual control; regenerate single week |
| `/generate-handout <type>` | Generate single handout | Create/recreate individual handouts |
| `/generate-substitute-plan <week> <day>` | Sub teacher plan | Teacher absence days |
| `/scaffold-lesson-structure` | Set up directories only | Before generating any lesson content |
| `/new-school-year` | Copy forward to new year | End of year; prep for next school year |
| `/generate-official-syllabus` | Extract syllabus from images | After uploading textbook syllabus images |
| `/supplemental-content` | Guide for custom content | Adding non-textbook content to curriculum |

---

## Workflow Comparison

### Recommended: Orchestrated Workflow

```bash
/lesson-plan-workflow foundations
```

**What it does:**

- Checks prerequisites (teaching map exists, etc.)
- Scaffolds structure if needed
- Guides you week-by-week
- Tracks progress
- Resumes where you left off

**Best for:** Most users; hands-off approach

---

### Advanced: Manual Control

```bash
1. /scaffold-lesson-structure foundations
2. /generate-lesson-plans 1
3. /generate-lesson-plans 2
... (repeat for each week)
```

**What it does:**

- Full control over each step
- Generate weeks in any order
- Regenerate specific weeks as needed

**Best for:** Users who want granular control or need to jump around

---

## Teaching Map Styles

When running `/generate-map`, you'll choose a teaching style:

| Style | Best For | Characteristics |
|-------|----------|-----------------|
| **Cohort** | Apologetics, Worldview | Discussion-first, debate-heavy, student-led |
| **Lecture-Seminar** | Survey courses, Theology | Teacher-led content + discussion days |
| **Inductive Bible Study** | Book studies, Scripture-focus | Observation → Interpretation → Application |
| **Chronological Narrative** | OT/NT Survey | Bible as one unified story, timeline-focused |

Teaching map style files are in `_shared/teaching-map-styles/`

---

## File Structure After Full Generation

```text
classes/foundations/
├── README.md
├── teaching-maps/
│   └── teaching-map-2026-27.md
├── syllabus/
│   ├── syllabus.md (extracted)
│   └── [syllabus images]
└── lesson-plans-2026-27/
    ├── README.md
    ├── .generation-log.md
    ├── week-01-aug-24/
    │   ├── README.md
    │   ├── lesson-plans.md
    │   ├── handouts/
    │   │   ├── core-reading-guide-ch01.md
    │   │   ├── note-catcher-ch01.md
    │   │   ├── discussion-brief-01-template.md
    │   │   └── [...]
    │   └── substitute-plan-friday.md (if applicable)
    ├── week-02-aug-31/
    │   └── [...]
    └── assessments/
        ├── capstone-01-rubric.md
        ├── capstone-02-rubric.md
        └── [...]
```

---

## Common Patterns

### Pattern 1: Start from scratch

```bash
/new-class apologetics
# [Upload syllabus images]
/generate-official-syllabus apologetics
/generate-map apologetics
/lesson-plan-workflow apologetics
```

### Pattern 2: Regenerate one week

```bash
/generate-lesson-plans 5 --class foundations --year 2026-27
```

### Pattern 3: Create custom handout

```bash
/generate-handout case-study --week 7 --topic "Problem of evil in pastoral context"
```

### Pattern 4: Copy to new year

```bash
/new-school-year foundations --from 2026-27 --to 2027-28
```

---

## Prerequisites

**Before running `/generate-map`:**

- ✅ Class directory exists (`/new-class`)
- ✅ Syllabus extracted or chapter list ready
- ✅ School calendar exists in `_shared/school-calendar-<year>.md`

**Before running `/lesson-plan-workflow`:**

- ✅ Teaching map exists (`/generate-map`)
- ✅ School calendar exists

**Before running `/generate-lesson-plans <week>`:**

- ✅ Teaching map exists
- ✅ Lesson structure scaffolded (or workflow will scaffold it)

---

## Tips

- **Use the workflow**: `/lesson-plan-workflow` handles most complexity for you
- **Upload textbook images**: Richer lesson plans when you provide chapter images
- **Review generated content**: All commands create drafts; customize as needed
- **Year-stamp everything**: All directories use `YYYY-YY` format (e.g., `2026-27`)
- **Preserve post-week notes**: After teaching, add notes to `week-XX/README.md` for next year

---

## Support

- **Detailed docs**: See `SKILLS-OVERVIEW.md` for comprehensive guide
- **Command definitions**: Each command file in `.claude/commands/` has full documentation
- **Example output**: See `classes/foundations/lesson-plans-2026-27/week-01-aug-24/` for reference

---

**Last Updated:** 2026-04-22
