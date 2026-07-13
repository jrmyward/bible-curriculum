---
name: build-reading-packet
description: Build a per-worldview reading packet for the Worldview class
args: "<unit-number>"
---

# Build Reading Packet

Build one stapled reading packet (~10–20 markdown pages) for a Worldview unit. Replaces cross-chapter textbook navigation: students read the packet, not the textbook, during the unit. Build packets in teaching order so each can reference forward to earlier ones.

## Usage

```
/build-reading-packet 1     # Christianity (baseline)
/build-reading-packet 3     # Islam
/build-reading-packet 5     # Hinduism
/build-reading-packet 9     # Revolutionary Lineage
```

Unit numbers map to: 1 Christianity · 2 Judaism · 3 Islam · 4 Mormonism · 5 Hinduism · 6 Buddhism · 7 New Spirituality · 8 Secularism · 9 Revolutionary Lineage.

## Process

### 1. Read context

Read in this order:
1. `classes/understanding-the-times/teaching-map.md` — locate the Unit `<N>` section; read purpose, key anchors, day-by-day schedule, Gospel-conversation focus
2. `classes/understanding-the-times/teaching-methodology.md` — section "The Capital Investment That Makes This Work" defines packet anatomy
3. `classes/understanding-the-times/worldview-grid.md` — find this unit's column; you'll embed a blank slice
4. `classes/understanding-the-times/syllabus/syllabus.md` — note the publisher's prescribed supplemental reading for the matching Myers/Noebel chapter
5. **The publisher's matching chapter test** at `classes/understanding-the-times/_source-text/_cd/UTT Unit <NN> Files/<NN> Test Questions/UTT Chapter <NN> Test-Teacher.pdf` — this is the dual-credit alignment standard for the unit. Read every fill-in-the-blank, multiple-choice, and short-answer question; extract every defined term and Scripture reference. The packet's Publisher Vocabulary section (see structure below) must include all of these.
6. **The worldview's slices of Ch 8–17 publisher tests.** The Day-9 blended test combines the publisher Ch X test (above) with each worldview's relevant questions from Ch 8 (Theology) through Ch 17 (History). The reading packet must prepare students for both halves of that blended test, so the Publisher Vocabulary section must also include defined terms from each Ch 8–17 test that pertain to this worldview. Look up `_source-text/_cd/UTT Unit 08 Files/`, `09`, `10`, ..., `17` and extract worldview-relevant vocabulary.
7. **The publisher's Doug Letter** at `classes/understanding-the-times/_source-text/_cd/UTT Unit <NN> Files/<NN> Writing Assignment/UTT Chapter <NN> Assignment-Teacher.pdf` — read the four embedded questions and the model answers. The packet's Doug Letter Preview (see structure below) introduces students to the format before they write their own response.

### 2. Map sources

**Textbook OCR:** `classes/understanding-the-times/_source-text/textbook/ch<NN>.md`
**Teacher's manual:** `classes/understanding-the-times/_source-text/teaching-manual/ch<NN>.md`

**Per-unit Myers/Noebel mapping:**

| Unit | Worldview | Worldview chapter | Discipline slices (Ch 8–17) |
|------|---|---|---|
| 1 | Christianity | Ch 2 | Christianity (in all of Ch 8–17) |
| 2 | Judaism | NONE | NONE — build from primary sources |
| 3 | Islam | Ch 3 | Islam (in all of Ch 8–17) |
| 4 | Mormonism | NONE | NONE — build from primary sources |
| 5 | Hinduism | Ch 6 (partial) | NONE distinct — see asymmetric note |
| 6 | Buddhism | Ch 6 (partial) | NONE distinct — see asymmetric note |
| 7 | New Spirituality | Ch 6 (proper) | "New Spirituality" (in all of Ch 8–17) |
| 8 | Secularism | Ch 4 | Secularism (in all of Ch 8–17) |
| 9 | Revolutionary Lineage | Ch 5 + Ch 7 | Marxism + Postmodernism (in all of Ch 8–17) + supplemental Progressivism |

**Asymmetric note.** Ch 8–17 only treat 6 worldviews (Christianity, Islam, Secularism, Marxism, Postmodernism, New Spirituality). Judaism, Mormonism, Hinduism-distinct, and Buddhism-distinct have NO textbook slices — build per-discipline content from primary sources and the worldview's own chapter.

In Ch 8–17 the worldview sections are clearly labeled (e.g., `2. SECULARISM`, `3. MARXISM`). Extract the relevant section verbatim or paraphrased with attribution.

**Publisher-prescribed supplemental sources** (dual-credit alignment, non-negotiable for matching units):

| Ch | Reading | Use for unit |
|---|---|---|
| 2 | "The Gospel of Mark" 1–3, 11–16 | Unit 1 (Christianity) |
| 3 | "Sura 3–4" (Quran) | Unit 3 (Islam) |
| 4 | "Humanist Manifesto" | Unit 8 (Secularism) |
| 5 | "The Communist Manifesto" | Unit 9 (Revolutionary Lineage) |
| 6 | "Bhagavad Gita" Ch. 6–9 | Unit 5 (Hinduism) |
| 7 | "The Parable of the Mad Man" | Unit 9 (Revolutionary Lineage) |

For non-matching units, pull primary sources from teaching-map.md's "Contemporary Resources" or "Key Anchors" section.

### 3. Write the packet

Write to: `classes/understanding-the-times/handouts/unit-<NN>-<worldview-slug>-reading-packet.md`

Use the prefix-zero pattern (`unit-01-...`, `unit-03-...`).

**Structure (in order):**

```
# Unit <N> — <Worldview> Reading Packet

[Cover block: framing question, dates, 8-cell student checklist for the unit]

## Part 1 — The Worldview on Its Own Terms (Framing)
2–3 pages of charitable representation. Steel-man only. Critique belongs in
Day 7 of the unit, not in the packet.

## Part 2 — The 10 Lenses
Ten subsections, fixed order: Theology, Philosophy, Ethics, Biology,
Psychology, Sociology, Law, Politics, Economics, History.

Each ½–1 page:
- Lead with this worldview's answer to the discipline's core question
- Pull from the matching slice of Myers Ch 8–17 where available (verbatim
  or paraphrased with attribution)
- For worldviews without textbook slices: build from primary sources and
  the worldview's own chapter; cite carefully
- End with one sentence flagging where this worldview most diverges from
  the Christian baseline (a teaser for Day 7's Four-Test exercise — do
  NOT pre-empt it)

## Part 3 — Primary Sources
1–3 excerpts:
- Always include the publisher-prescribed supplemental if one matches
  this unit (see table above)
- Add 1–2 from teaching-map.md
- Each excerpt: 1–3 pages, full citation, brief contextual intro, 2–3
  reading questions

## Part 4 — Worldview Grid Slice (Blank)
Pull this unit's column from worldview-grid.md. Render as a blank fill-in
table (discipline | blank cell). On the back: one row of the grid filled
in for an adjacent worldview, so students see what a complete cell looks
like.

## Part 5 — Publisher Vocabulary (for the blended Day-9 test)
Every defined term and Scripture reference students will see on the Day-9
blended chapter test, in flashcard format (term | definition).
Compiled from:
- The publisher's matching Ch X test (fill-in-the-blank section)
- The worldview's relevant questions extracted from each Ch 8–17 test

For Hindu / Buddhist / New Spirituality units: include a clear note that
the publisher tests Hindu/Buddhist content under "New Spirituality"
labels, with mapping ("When the publisher's test says 'New Spirituality
holds X,' our Hinduism/Buddhism unit teaches that X derives from...").

## Sources to Acquire (if any)
List anything the packet needs that wasn't in the repo. Do NOT fabricate
content for missing sources — flag and move on.
```

### 4. Rules

1. **Charitable representation first.** Part 1 must be a steel-man. Critique belongs in Day 7 of the unit, not in the packet.
2. **Never fabricate.** If a primary source isn't available in the repo, list it under "Sources to Acquire" rather than inventing content. Same for textbook slices that don't exist.
3. **Cite everything.** Every claim from the textbook gets a `(Myers Ch X, §Y)` attribution. Every primary source gets a full citation.
4. **Don't pre-empt the teaching.** The packet is reading material, not lecture notes. The teacher delivers the synthesis, comparison, and Gospel conversation in class.
5. **Length budget: 10–20 pages.** If you exceed 20, trim Part 2 first (each lens to ½ page); never trim Part 1 (charitable framing) or Part 3 (primary sources). Rough rule: 600–1200 words per printed page.
6. **Write for 11th–12th graders.** Clear, direct, age-appropriate. Whole sentences; the textbook's tone is a reasonable target. No edu-jargon.
7. **Match project conventions.** No emojis. Markdown only. Compact-style tables (consistent with teaching-map.md). Lowercase-hyphenated filename.

### 5. Report

After writing, report:

```
✅ Built Unit <N> — <Worldview> reading packet
   Output: classes/understanding-the-times/handouts/unit-<NN>-<slug>-reading-packet.md
   Estimated pages: <count>
   Primary sources included: <list>
   Sources to acquire: <list, or "none">
   Pedagogical notes for teacher: <anything worth flagging before printing>
```
