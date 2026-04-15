# Skill: Generate Official Syllabus

**Purpose**: Convert syllabus images from a textbook into a structured markdown file that can be consumed by the teaching map generator.

---

## Process

### 1. Locate Syllabus Images
- Check `classes/<class-name>/syllabus/` for image files (`.jpg`, `.png`, `.heic`, etc.)
- If no images found, ask the user to add them first

### 2. Read Images
- Use the Read tool to view each syllabus image
- Extract:
  - Chapter numbers and titles
  - Lesson/section breakdown within each chapter
  - Any suggested pacing (days per chapter, weeks per unit, etc.)
  - Key themes, learning objectives, or essential questions if listed

### 3. Structure the Markdown Syllabus
Create `classes/<class-name>/syllabus/syllabus.md` with this format:

```markdown
# [Course Name] — Official Syllabus

*Extracted from [Book Title] on [Date]*

---

## Course Overview
[If the syllabus includes an overview, summary, or course description, include it here]

---

## Chapter Breakdown

### Chapter 1: [Title]
**Suggested Duration**: [X days/weeks, if provided]

**Lessons/Sections**:
1. [Lesson/section name]
2. [Lesson/section name]
3. ...

**Key Themes**: [if provided]

**Learning Objectives**: [if provided]

---

### Chapter 2: [Title]
...

---

## Pacing Notes
[If the syllabus includes overall pacing guidance — e.g., "complete in one semester", "2 weeks per chapter" — note it here]

---

## Additional Resources
[If the syllabus lists supplementary materials, videos, case studies, etc., include them here]
```

### 4. Validate & Save
- Ensure chapter numbering is sequential
- Check that all visible content from images is captured
- Write the file to `classes/<class-name>/syllabus/syllabus.md`
- Confirm completion with the user

---

## Output
- **File**: `classes/<class-name>/syllabus/syllabus.md`
- **Format**: Structured markdown with chapters, lessons, pacing, and themes
- **Usage**: Consumed by `/generate-map` to align teaching map with official syllabus

---

## Notes
- If the syllabus spans multiple images, read all before generating the markdown
- Preserve the textbook's structure/order exactly — don't reorganize or editorialize
- If any content is unclear from the image, flag it in the markdown with `[UNCLEAR: ...]`
