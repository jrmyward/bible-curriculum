---
name: new-class
description: Create a new class in this Bible curriculum repository
args: "[class-name]"
---

# Create New Class

Create a new class directory with all necessary structure for lesson planning.

## Usage

```bash
/new-class [class-name]
```

**Examples:**

```bash
/new-class apologetics
/new-class old-testament-survey
/new-class biblical-ethics
```

## Process

### 1. Gather class information

Ask the teacher for:

- Class name (will be used as the folder name, lowercased and hyphenated)
- Grade level (e.g. 11–12)
- Textbook or series used
- Number of chapters or units

### 2. Create the class directory structure

Create `classes/<class-name>/` with this structure (matches the Foundations exemplar):

```text
classes/<class-name>/
├── README.md
├── teaching-map.md                    (created later by /generate-map)
├── syllabus/
│   └── .gitkeep
├── handouts/
│   └── .gitkeep
├── _source-text/
│   ├── textbook/         .gitkeep     (chNN.md transcriptions / chapter images)
│   ├── teaching-manual/  .gitkeep     (chNN.md — discussion Qs + model answers)
│   └── portal/           .gitkeep     (chNN/ — publisher tests, keys, study guides)
├── rubicon-atlas/
│   ├── .gitkeep                       (unit-NN-*.md UbD fields — Atlas pillar)
│   └── lessons/  .gitkeep             (chNN-lessons.md Madeline Hunter dailies)
└── lesson-plans-YYYY-YY/              (created later by /scaffold-lesson-structure)
```

**Note:** Add `.gitkeep` files to empty directories so Git tracks them. Ask which **model** the class
uses — `publisher` (Summit default) or `cohort` (worldviews/apologetics) — and note it in the README.

### 3. Generate the class README

Create `classes/<class-name>/README.md` with:

- Class title (properly capitalized)
- Grade level
- Textbook/series
- Number of chapters
- Brief course description (ask teacher or draft for review)
- Explanation of subfolder structure
- Link to next steps

### 4. Update project index

Add new class to the "Current Classes" table in `/CLAUDE.md`

### 5. Next steps reminder

After creating the class, remind the teacher. For a full build across all three pillars (content,
Atlas, Google), the orchestrator **`/setup-class`** sequences everything; the manual path is:

```text
✅ Class created: <class-name>

Next steps:
1. Upload syllabus images to classes/<class-name>/syllabus/
2. /generate-official-syllabus <class-name>   — extract chapter structure
3. /generate-map <class-name>                  — create the teaching map
4. /scaffold-lesson-structure <class-name>     — week folders + stubs
5. Per chapter: /build-chapter → /build-atlas → /push-atlas → /publish-chapter

Or just run /setup-class <class-name> and it walks the whole thing.
```
