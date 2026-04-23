---
name: generate-lesson-plans
description: Generate comprehensive day-by-day lesson plans for a week from textbook chapter images
args: "<week-number> [--class class-name] [--year YYYY-YY]"
---

# Generate Lesson Plans

Generate comprehensive, day-by-day lesson plans for a specific week based on textbook chapter images and the teaching map.

## Usage

```bash
/generate-lesson-plans <week-number> [--class class-name] [--year YYYY-YY]
```

**Examples:**

```bash
/generate-lesson-plans 5
/generate-lesson-plans 12 --class understanding-the-faith
/generate-lesson-plans 23 --year 2026-27
```

## Prerequisites

Before running this command, ensure:

- ✅ **Teaching map exists**: `classes/<class-name>/teaching-maps/teaching-map-<year>.md`
- ✅ **School calendar exists**: `_shared/school-calendar-<year>.md`
- ✅ **Class directory exists**: `classes/<class-name>/`

If missing:

- Teaching map → Run `/generate-map <class-name>`
- School calendar → Create manually in `_shared/`
- Class directory → Run `/new-class <class-name>`

**Note:** The lesson structure will be scaffolded automatically if it doesn't exist.

## Process

### 1. **Validate Inputs**

- If `--class` not provided, detect from current directory or ask user
- Verify the class exists in `classes/<class-name>/`
- If `--year` not provided, detect from directory structure or default to current school year
- Verify week number is valid (check teaching map for total weeks)
- Determine week directory name from teaching map (e.g., `week-05-sep-21`)
- Check if `lesson-plans-<year>/week-XX-<date>/lesson-plans.md` already exists
  - If exists: "Week X lesson plan already exists. Regenerate? (yes/no)"
  - If regenerating: back up existing file to `lesson-plans.backup.md` in the same directory

### 2. **Read Teaching Map Context**

From `classes/<class-name>/teaching-maps/teaching-map-<year>.md` (or fall back to `teaching-map.md`), extract for this week:

- **Week dates** (e.g., "Sep 21–25, 2026")
- **Chapter(s)** being covered (e.g., "Ch 3 — Is the Bible Reliable?")
- **Topic** (e.g., "Manuscript evidence, textual criticism, historical reliability")
- **Activities planned** (from the teaching map's week-by-week schedule)
- **Assessments due** (Discussion Briefs, Case Studies, Capstones)
- **Teacher absence days** (marked with **SUB:** in teaching map)
- **No-school days** (marked with **NO SCHOOL**)
- **Notes** (any special context from teaching map)
- **Trimester** (T1, T2, or T3)
- **Unit** (which unit this week belongs to)

### 3. **Request Textbook Chapter Images**

Prompt the user:

```
To generate lesson plans for Week X ([Chapter]), I need images of the textbook chapter.

Please provide:
- Chapter X from "[Textbook name]"
- All pages (title page through end-of-chapter review)
- Images can be photos, scans, or screenshots

Upload images now, or type 'skip' to generate plans from teaching map only (less detailed).
```

If user uploads images:
- Acknowledge: "Received X images for Chapter X. Analyzing chapter structure..."

If user types 'skip':
- Acknowledge: "Generating plans from teaching map context only. You can regenerate later with chapter images for more detail."

### 4. **Analyze Chapter Structure** (if images provided)

From the textbook chapter images, identify:

- **Total page count**
- **Section titles** and page numbers (Section 1: "Introduction" pp. 1-2, etc.)
- **Core vs. Supplemental content**:
  - Core: Definitions, main arguments, Scripture references, key examples
  - Supplemental: Statistics, extended examples, tangents, administrative content
- **Key concepts** (terms, ideas, questions)
- **Scripture references** mentioned
- **Discussion questions** or reflection prompts in the chapter
- **Charts, diagrams, tables** (note what they illustrate)
- **Pedagogical features** (sidebars, case studies, review questions)

Create a mental chapter outline:
```
Chapter X: [Title] (XX pages)

Core Sections (~40-50% of total):
- Section 1: [Title] (pp. X-X) — [what it covers]
- Section 4: [Title] (pp. X-X) — [what it covers]
- Section 9: [Title] (pp. X-X) — [what it covers]
[...]

Supplemental Sections (can skim/skip):
- Section 5: [Title] (pp. X-X) — [why skippable]
- Section 6: [Title] (pp. X-X) — [why skippable]
[...]

Key Concepts:
- [Concept 1]
- [Concept 2]
[...]

Scripture References:
- [Verse 1]
- [Verse 2]
[...]
```

### 5. **Design the Week's Lesson Arc**

Based on teaching map activities and chapter content, design a 5-day (or 3-4 day for short weeks) arc:

**Typical Cohort Rhythm:**
- **Day 1**: Introduce chapter, assign reading (use Core Reading Guide), preview Discussion Brief
- **Day 2**: Guided reading in class OR reading discussion
- **Day 3**: Discussion Brief due; class discussion based on briefs
- **Day 4**: Pair & Defend OR Case Study
- **Day 5**: Debrief activity; preview next week

**Adjustments:**
- **Substitute days**: Non-cohort activities (video, reflection, individual work)
- **Short weeks**: Compress rhythm; move Discussion Brief earlier
- **Capstone weeks**: More work days, presentations, less new content
- **Assessment-heavy weeks**: Build in review and synthesis time

**Teaching Map Activities Override Default Rhythm**: Always use the specific activities listed in the teaching map for this week. The above rhythm is a fallback if teaching map doesn't specify.

### 6. **Generate Day-by-Day Lesson Plans**

For each instructional day, create a detailed lesson plan following this structure:

```markdown
## **[DAY], [MONTH DATE] — [Lesson Focus]**

### **Objectives:**
- [Objective 1: content goal]
- [Objective 2: skill goal]
- [Objective 3: assessment or application goal]

### **Materials:**
- [Material 1]
- [Material 2]
- [Handout name] (file: `handouts/week-XX/[filename].md` — one per student)

### **Lesson Flow:**

#### **[0–X min] [Activity Name]**

**[Teacher instruction or student activity description]**

**Say:** [Optional: exact script for teacher to say to class]

> "[Blockquote format for teacher scripts]"

**[Additional context, questions to ask, or facilitation notes]**

**Ask:** "[Question for class]"

**Clarify if needed:** "[Key point to emphasize]"

**Teacher role:** [What teacher does during this segment]

---

#### **[X–X min] [Next Activity Name]**

[Repeat structure]

---

[Continue for all activities until end of period]

---

**Due:** [What's due this day]  
**Notes:** [Any important reminders or context]

---
```

**Each lesson should:**
- Be **45 minutes** total (standard class period)
- Include **exact timing** for each activity segment
- Provide **teacher scripts** for key moments (introductions, transitions, prompts)
- Anticipate **student questions** and provide suggested responses
- Include **"Ask:" prompts** for class discussion
- Specify **"Say:" scripts** for direct instruction moments
- Note **what to write on the board** (prompts, agendas, key terms)
- Include **exit tickets** or closing activities
- Reference **handouts** with file paths
- Specify **homework** or prep for next day

**Tone:**
- Professional but warm
- Assumes teacher is competent but appreciates scaffolding
- Not condescending or overly prescriptive
- Balances structure with flexibility

### 7. **Generate Required Handouts**

Based on the lesson plans, generate all handouts referenced:

**Standard weekly handouts:**
1. **Core Reading Guide** (if chapter reading assigned)
   - Use `/generate-handout core-reading-guide --week X --chapter X`
   - Base on chapter structure analysis from Step 4

2. **Note-Catcher** (if guided reading in class)
   - Use `/generate-handout note-catcher --week X --chapter X`
   - Base on key concepts from chapter analysis

3. **Discussion Brief Template** (if Discussion Brief assigned)
   - Use `/generate-handout discussion-brief --week X --number X --prompt "[prompt]"`
   - Prompt comes from teaching map or is inferred from chapter content

4. **Case Study** (if Case Study activity scheduled)
   - Use `/generate-handout case-study --week X --topic "[topic from teaching map]"`

5. **Pair & Defend Prep** (if Pair & Defend scheduled)
   - Use `/generate-handout pair-and-defend --week X --prompt "[prompt from teaching map]"`

6. **Video Note-Catcher** (if video shown in class)
   - Use `/generate-handout video-note-catcher --week X --video "[video title]"`

7. **Reflection** (if reflection writing assigned)
   - Use `/generate-handout reflection --week X --title "[title]"`

**Substitute day handouts:**
- If the week includes a substitute day, generate appropriate handouts for that day's activities

### 8. **Generate Substitute Plan** (if applicable)

If the teaching map marks any day this week as **SUB:**:
- Use `/generate-substitute-plan <week-number> <day>`
- Write to `lesson-plans-<year>/week-XX-<date>/substitute-plan-<day>.md`

### 9. **Write Files to Week Directory**

Write all files to `lesson-plans-<year>/week-XX-<date>/`:

**Main lesson plan file:** `lesson-plans.md`

```markdown
# Week X Lesson Plans — [Class Name]

**Week:** [Dates]  
**Chapter:** [Chapter]  
**Topic:** [Topic]  
**Class Period:** 45 minutes  
**Teacher Absence:** [None / Day if substitute]

---

## **[DAY 1], [MONTH DATE] — [Lesson Focus]**

[Full lesson plan as generated in Step 6]

---

## **[DAY 2], [MONTH DATE] — [Lesson Focus]**

[Full lesson plan]

---

[Continue for all 5 days, or 3-4 for short weeks]

---

**End of Week X Lesson Plans**
```

**Handouts:** All handouts written to `handouts/` subdirectory
- `handouts/core-reading-guide-chXX.md`
- `handouts/note-catcher-chXX.md`
- `handouts/discussion-brief-XX-template.md`
- etc.

**Substitute plan** (if applicable): `substitute-plan-<day>.md`

**Week README**: Update `README.md` to mark as generated:
```markdown
## Files in This Directory

- **`lesson-plans.md`** — Complete day-by-day lesson plans (5 days) ✅ Generated
- **`handouts/`** — All handouts for this week (6 files)
- **`substitute-plan-friday.md`** — Detailed substitute plan ✅ Generated
```

### 10. **Cross-Reference with Teaching Map**

Verify that the generated lesson plans:
- ✅ Cover all activities listed in the teaching map for this week
- ✅ Include all assessments due (Discussion Briefs, Case Studies)
- ✅ Account for all no-school days
- ✅ Match the pacing and rhythm from teaching map
- ✅ Use the correct chapter(s)
- ✅ Hit the learning objectives implied by the teaching map's "Key Question" for this unit

If discrepancies, note them and ask user:
```
⚠️ Teaching map shows [X], but I generated [Y]. 
This is because [reason]. 
Proceed with this approach? (yes/no/adjust)
```

### 11. **Update Generation Log**

Update `.generation-log.md` with this week's entry:

```markdown
| 5 | Sep 21–25 | 🆕 Generated | 2026-04-22 | Generated from Chapter 3 textbook images |
```

### 12. **Report Completion**

Display summary:

```
✅ Week X lesson plans generated for [class-name] (<year>)

Created in lesson-plans-<year>/week-XX-<date>/:
- lesson-plans.md (X days, XX pages)
- handouts/ (X files):
  - core-reading-guide-chXX.md
  - note-catcher-chXX.md
  - discussion-brief-XX-template.md
  - [... list all handouts]
- substitute-plan-<day>.md [if applicable]
- README.md (updated)

Updated:
- .generation-log.md

Total: X files created

Next steps:
- Review the lesson plans for accuracy and pacing
- Upload or queue any videos referenced
- Print handouts before the week starts (all in week-XX-<date>/handouts/)
- [If sub day] Prepare substitute folder packet
```

---

## Lesson Plan Quality Standards

Generated lesson plans must meet all standards defined in `_shared/lesson-plan-standards.md`. Read that file before generating any lesson plans.

---

## Example Week Arc

**Week 5: Chapter 3 — Is the Bible Reliable?**

**Monday:**
- Return Discussion Brief #3 with feedback
- Class discussion on strongest objections to biblical reliability
- Introduce manuscript evidence (mini-lecture with slides)
- Assign video for Tuesday: "The Case for Reliability of the Gospels"

**Tuesday:**
- Watch video (15 min) + Video Note-Catcher
- Debrief video: What's the strongest evidence mentioned?
- Introduce textual criticism concept (brief direct instruction)
- Preview Chapter 4 reading for next week

**Wednesday:**
- **Pair & Defend**: "The Gospels are historically reliable vs. The Gospels are faith documents, not history"
- Students prep using Pair & Defend Prep handout (15 min)
- Debates (20 min)
- Debrief (10 min)

**Thursday:**
- Debrief Pair & Defend from Wednesday
- **Case Study**: "Historical parallel — how early church fathers defended Scripture to Roman critics"
- Group work (20 min)
- Group presentations (15 min)

**Friday:**
- Case Study write-ups due; collect and give feedback
- Unit 2 review: Connect Ch 3-4 themes (reliability + authority)
- Preview next week: Chapter 5 (Who is God?)
- Exit ticket: "What's one thing you learned this week that surprised you?"

---

## Notes

- **Textbook chapter images are optional but highly recommended** — they enable much richer, more detailed lesson plans
- **Without chapter images**, lesson plans will be based on teaching map activities only (less detailed, more generic)
- **Cohort tools** (Discussion Brief, Pair & Defend, Case Study, Capstone) are defined in `_shared/cohort-tools.md` — reference this for proper implementation
- **Student age**: Assume 11th–12th grade (ages 16-18); adjust language and expectations accordingly
- **Class period**: Default is 45 minutes; adjust if user specifies different period length
- **Teaching map is the source of truth**: Always defer to teaching map for activities, pacing, and assessment schedule
- **Iterate as needed**: If user provides feedback ("Too much direct instruction" or "Need more discussion time"), regenerate with adjustments
