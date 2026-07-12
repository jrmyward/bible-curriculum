---
name: build-atlas
description: Author the Rubicon Atlas data models for a chapter (unit fields + daily lessons)
args: "<class-name> <chapter-number>"
---

# Build Atlas Data Models

Author the two human-reviewable repo files that drive the **Rubicon Atlas** push for a chapter. This
is authoring only — the Playwright push is `/push-atlas`. The data models are the source of truth and
are reviewed *before* anything touches Atlas; never invent content at push time.

## Usage

```bash
/build-atlas foundations 3
```

## What it produces

Under `classes/<class>/rubicon-atlas/`:

1. **`unit-NN-<slug>.md`** — the unit's UbD fields (humanized prose):
   - **Unit Overview**
   - **Essential Questions**
   - **Objectives**
   - **Biblical Integration** *(kept as prose reference; Atlas's Faith Learning Integration is a
     Standards picker, not free text — see gotchas in the atlas runbook)*
2. **`lessons/chNN-lessons.md`** — one `## Day N - Title` section per instructional day, with
   `**Row Label:** content` lines mapping to the **Madeline Hunter** lesson template rows (Objective,
   Anticipatory Set, Input/Modeling, Guided Practice, Independent Practice, Closure, etc.). Concise;
   include Modeling / Guided Practice detail on days that have them.

## Process

1. **Read the sources of truth:**
   - The chapter's daily lesson plans (`classes/<class>/lesson-plans-<year>/week-*/`) — build these
     first with `/build-chapter` if they don't exist.
   - The teaching map (unit topic, EQs, objectives, dates).
   - An existing `unit-NN-*.md` (e.g. Foundations Ch 1) as the **format exemplar**.
2. **Author `unit-NN-<slug>.md`** — fill the four free-text fields from the teaching map + daily
   plans. Humanize. **Plain text only** — Atlas strips markdown; use `**` solely as the parser's
   label syntax, avoid em-dashes, use en-dashes only for Scripture ranges (`Genesis 1–2`).
3. **Author `lessons/chNN-lessons.md`** — one Madeline Hunter section per instructional day, derived
   from that day's lesson plan. Keep it tight; Atlas cells are plain text.
4. **Review with the teacher** before pushing — these files are meant to be read and corrected first.

## Reference

Full field list, the Madeline Hunter row mapping, and the hard-won formatting rules are in the
**atlas runbook**: [`_scripts/atlas/README.md`](../../_scripts/atlas/README.md). Read it before
authoring so the models push cleanly (markdown-stripping, en-dash rule, plain-text cells).

## Next step

`/push-atlas <class> <N>` — push the unit fields + daily lessons to Rubicon Atlas via Playwright.
