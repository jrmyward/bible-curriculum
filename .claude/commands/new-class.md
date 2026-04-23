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

Create `classes/<class-name>/` with this structure:

```text
classes/<class-name>/
├── README.md
├── teaching-maps/         (will hold year-specific maps)
├── syllabus/              (for syllabus images and extracted content)
└── lesson-plans-YYYY-YY/  (created later by /scaffold-lesson-structure)
```

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

After creating the class, remind the teacher:

```text
✅ Class created: <class-name>

Next steps:
1. Upload syllabus images to classes/<class-name>/syllabus/
2. Run /generate-official-syllabus to extract chapter structure
3. Run /generate-map <class-name> to create teaching map
4. Run /lesson-plan-workflow <class-name> to build lesson plans
```
