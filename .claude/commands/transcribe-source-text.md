---
name: transcribe-source-text
description: Transcribe source text images for a chapter into markdown files
args: "<chapter> [textbook|student-manual|both]"
---

# Transcribe Source Text

Transcribe all images for a chapter into clean markdown files, one per source type.

## Usage

```
/transcribe-source-text ch01
/transcribe-source-text ch03 textbook
/transcribe-source-text ch07 student-manual
```

If source type is omitted, transcribe both.

## Process

### 1. Resolve paths

- Chapter images live at `classes/understanding-the-faith/_source-text/<chapter>/`
- Textbook images: `textbook/`
- Student manual images: `student-manual/`
- Output files: `textbook.md` and `student-manual.md` in the same chapter folder

If the target folder has no images, report it and stop.

### 2. List and sort images

List all `.jpg` / `.jpeg` / `.png` files in the folder. Sort by filename (the IMG_ numbers are sequential and correspond to page order).

### 3. Transcribe in small batches

**Critical: process images in batches of 2 to avoid timeouts.** Do not try to hold the entire chapter in memory at once.

For each batch:

1. Read 2 images using the Read tool.
2. Transcribe them following the formatting rules below.
3. **Immediately append** the transcription to a working file at `classes/understanding-the-faith/_source-text/<chapter>/<source-type>.wip.md` using the Bash tool (`cat >>` or similar). Do not wait until all images are read.
4. Move to the next batch.

#### Formatting rules

For each page, extract all visible text and render it as clean markdown:

- **Headings**: Use `#`, `##`, `###` to match visual hierarchy
- **Body text**: Plain paragraphs
- **Numbered lists**: `1.`, `2.`, etc.
- **Bullet lists**: `-`
- **Bold/italic**: Preserve where visually prominent
- **Fill-in-the-blank blanks** (student manual): Render as `___`
- **Scripture references**: Preserve exactly as printed
- **Tables**: Render as markdown tables where readable; otherwise prose
- **Sidebars / callout boxes**: Wrap in a blockquote `>`
- **Page numbers**: Omit
- **Headers/footers** (book title, chapter title repeating): Omit after first occurrence
- **Section labels** like `[1.6]`: Preserve — they're used as cross-references

Do not summarize, paraphrase, or editorialize. Transcribe the actual text. Separate pages with a blank line — do not insert `---` page break markers.

### 4. Finalize output

After all batches are written, rename the working file to the final output path:
- `classes/understanding-the-faith/_source-text/<chapter>/textbook.md`
- `classes/understanding-the-faith/_source-text/<chapter>/student-manual.md`

If the final output file already exists, ask before overwriting.

### 6. Report

```
✅ Transcribed <chapter> <source-type>
   Images processed: N
   Output: _source-text/<chapter>/<source-type>.md
```
