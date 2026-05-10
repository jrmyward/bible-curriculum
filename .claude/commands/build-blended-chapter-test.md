---
name: build-blended-chapter-test
description: Build a blended Day-9 chapter test for a Worldview unit (publisher Ch X test + worldview-specific questions extracted from Ch 8-17)
args: "<unit-number>"
---

# Build Blended Chapter Test

Build the per-unit Day-9 blended chapter test. Each test combines:

- The publisher's matching Ch X chapter test (worldview-comprehensive — tests how this worldview answers each of 10 disciplines holistically), AND
- The worldview's relevant questions extracted from each Ch 8–17 publisher chapter test (discipline-comparative — questions about this specific worldview's view of theology, philosophy, ethics, biology, psychology, sociology, law, politics, economics, history)

This means each per-unit assessment covers both worldview-holistic mastery (the publisher's Ch X) AND that worldview's discipline-by-discipline mastery (slices of Ch 8–17). The Ch 8–17 publisher tests in T3 finals can then serve their actual purpose: cross-comparative practice for the Ch 18 dual-credit final.

## Usage

```
/build-blended-chapter-test 1     # Christianity (uses publisher Ch 02 + Christianity slices of Ch 8-17)
/build-blended-chapter-test 2     # Judaism (locally-built Ch X equivalent + nothing from Ch 8-17, since publisher doesn't cover Judaism)
/build-blended-chapter-test 3     # Islam (publisher Ch 03 + Islam slices of Ch 8-17)
/build-blended-chapter-test 4     # Mormonism (locally-built; publisher silent)
/build-blended-chapter-test 5     # Hinduism (locally-built Ch X + Hindu-relevant questions from Ch 8-17 New Spirituality slices)
/build-blended-chapter-test 6     # Buddhism (locally-built Ch X + Buddhist-relevant questions from Ch 8-17 New Spirituality slices)
/build-blended-chapter-test 7     # New Spirituality (publisher Ch 06 + New Spirituality slices of Ch 8-17)
/build-blended-chapter-test 8     # Secularism (publisher Ch 04 + Secularism slices of Ch 8-17)
/build-blended-chapter-test 9     # Revolutionary Lineage (publisher Ch 05 + Ch 07 + Marxism + Postmodernism slices of Ch 8-17)
```

## Process

### 1. Read context

1. `classes/worldview/teaching-map.md` — locate the Unit `<N>` section; understand what content was taught
2. `classes/worldview/handouts/unit-<NN>-<slug>-reading-packet.md` if it exists — for terminology alignment
3. **The publisher's matching Ch X test:** `classes/worldview/_source-text/_cd/UTT Unit <NN> Files/<NN> Test Questions/UTT Chapter <NN> Test-Teacher.pdf`
   - For Unit 0 → Ch 01; Unit 1 → Ch 02; Unit 3 → Ch 03; Unit 7 → Ch 06; Unit 8 → Ch 04; Unit 9 → Ch 05 + Ch 07
   - For Units 2, 4 (no publisher coverage): no Ch X test — use Ch 02 (Christianity) as a format template
   - For Units 5, 6 (Hindu/Buddhist split from Ch 06): use Ch 06 as the partial source, supplement with locally-built questions on the distinct content
4. **All 10 discipline-comparative tests** (`UTT Unit 08 Files/` through `UTT Unit 17 Files/`):
   - Read each one
   - Find every question that tests THIS worldview specifically (e.g., for Unit 1 Christianity: every "According to Christianity..." or "The Christian view of..." question)
   - Note the publisher's reference codes (e.g., `[8.9c]` is Ch 8 Section 9c)

### 2. Compose the blended test

Structure the test in the publisher's exact format:

- **Header:** Total points / 100 (or scaled), Name field
- **MATCHING** (if applicable — 1 point each)
- **MULTIPLE CHOICE** (1 point each)
- **TRUE OR FALSE** (1 point each — false items require correction)
- **FILL-IN-THE-BLANK** (2 points each)
- **SHORT ANSWER** (3 points each — at least one sentence)
- **ESSAY** (4 points each — at least one paragraph)

For each section, sequence questions by:

1. Publisher Ch X questions verbatim (with original reference codes preserved)
2. Worldview-relevant questions extracted from Ch 8–17 (with original reference codes preserved, e.g., `[8.9c]` for Ch 8 Section 9c)
3. Where a Ch 8–17 question is cross-comparative ("Which of the following worldviews deny X?"), adapt to per-worldview format: "Does <this worldview> deny X? Why or why not?" — preserve the spirit, change the angle.

Aim for **45–60 total questions** (single class period, ~50 minutes). Don't bloat.

### 3. Two output files (Student + Teacher versions)

**Teacher version** (with answers + reference codes):
`classes/worldview/assessments/unit-<NN>-<slug>-test-teacher.md`

**Student version** (questions only, no answers):
`classes/worldview/assessments/unit-<NN>-<slug>-test-student.md`

Match publisher conventions:

- Highlight correct MC answers (Teacher version) with `**` or background
- Show False corrections in Teacher version: `False: <correction>`
- Reference codes in brackets after each answer

### 4. Special cases

**Units 2, 4 (Judaism, Mormonism — publisher silent):**
The blended test is entirely locally-built. Use Ch 02 (Christianity) test as a format template — same six question types, same proportions, same point values, same style of wording. Reference codes use `[U<N>.<section>]` format pointing to the unit's reading packet (e.g., `[U2.3a]`).

**Units 5, 6 (Hinduism, Buddhism — publisher rolls them into "New Spirituality"):**
Pull the Ch 06 (New Spirituality) test items where they pertain to Hindu or Buddhist content. Add a brief note: "The publisher's Ch 06 test refers to these as 'New Spirituality' — our distinct treatment of Hinduism/Buddhism teaches them as separate traditions; the publisher's terminology is correct for the test." Then add locally-built questions for the distinct content (Brahman/Atman/karma for Hinduism; Four Noble Truths/anatta/dependent origination for Buddhism).

**For Hinduism + Buddhism + New Spirituality units:** the same Ch 06 test items may appear in multiple units' blended tests (each time framed for that unit's specific worldview). This is intentional — students see the same publisher items three times across the year, each time from a different angle.

### 5. Rules

1. **Preserve publisher reference codes.** When pulling a question from Ch 8 Test Q22, mark it `[8.22 → blended]` so the teacher can trace back.
2. **Preserve publisher voice for publisher items.** Don't rewrite for "charity." The publisher's tone is the test standard.
3. **Locally-built items match publisher voice.** Same six question types, same point structures, same wording style.
4. **Don't double-test.** If the publisher's Ch X test asks "Define theology" and the Ch 8 Christianity slice also asks "Define theology," include it once.
5. **Single class period.** 45–60 questions. If you exceed 60, cut publisher items most redundant with the Ch X test.
6. **Match project conventions.** No emojis. Markdown only. Compact tables. Lowercase-hyphenated filenames.

### 6. Report

```
✅ Built Unit <N> — <Worldview> Blended Chapter Test
   Outputs:
     classes/worldview/assessments/unit-<NN>-<slug>-test-teacher.md
     classes/worldview/assessments/unit-<NN>-<slug>-test-student.md
   Total questions: <count>
   Total points: <count>
   Estimated administration time: ~<min> min
   Source breakdown:
     Publisher Ch <X> Test items: <count>
     Ch 08 (Theology) slice items: <count>
     Ch 09 (Philosophy) slice items: <count>
     ... [and so on for Ch 10-17]
     Locally-built items: <count>
   Pedagogical notes for teacher: <anything worth flagging before printing>
```
