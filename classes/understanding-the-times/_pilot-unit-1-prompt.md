# Pilot Prompt: End-to-End Unit 1 (Christianity) Production

> **⚠ Superseded — historical record only. Do not copy-paste as-is for other units.**
>
> This prompt was executed for Unit 1 in commits `b946f09` → `7280864` → `d4157d2`. The final commit pivoted the unit's artifact architecture: the two `lecture-notes-*.md` files that this prompt's Step 2 produced were **deleted** and replaced by `learning-outline.md` + `learning-outline-student.md` (in `handouts/`, organized by lens rather than by lecture day). See the pivot commit message for the design rationale.
>
> **Consequence:** re-running this prompt for any other unit will reintroduce the deleted lecture-notes architecture, because `/build-blended-lecture-notes` (Step 2) has not been updated to match the post-pivot model. Before scaling to Units 2–9, decide one of:
>
> 1. **Update the skill spec** (`.claude/commands/build-blended-lecture-notes.md`) to output the learning-outline pair instead of the lecture-notes pair. Then a revised version of this prompt becomes safe to reuse.
> 2. **Replace it** with a new `/build-learning-outline` skill modeled on the Unit 1 outline structure.
> 3. **Hand-build** subsequent units' outlines following the Unit 1 pattern without a skill.
>
> Two questions the pivot commit explicitly deferred and that should be settled before a second-unit pilot:
>
> - Whether the learning outline should follow the reading packet's flow (the packet has Christian Story narrative + primary sources the outline currently doesn't cover).
> - What a "lecture companion" artifact should look like — i.e., the teacher-only depth-and-character layer described in the lecture-philosophy memory but not currently committed as a file. Until this is settled the per-unit architecture remains five files (reading packet + learning outline ×2 + test ×2), not six.
>
> The original prompt text follows below for the historical record.

---

## The Prompt

```
You're piloting the per-unit production pipeline for the Worldview class
(Understanding the Times by Myers & Noebel, grades 11-12, Watersprings
School, school year 2026-27). The pipeline consists of four slash
commands that together produce a complete unit's teaching artifacts
from a shared blended-source pattern (publisher Ch X chapter + the
worldview's slices of Ch 8-17 + publisher teacher's manual + the unit's
reading packet + teaching-map.md).

For Unit 1 (Christianity), the publisher already provides the Doug
Letter (Ch 02 Writing Assignment), so /build-doug-letter is not needed
here. You'll produce three artifacts:

  1. Regenerate the Christianity reading packet (the existing one was a
     calibration draft built before the skill was updated; the updated
     skill now pulls vocabulary from Ch 8-17 worldview slices too)
  2. Build the Christianity lecture notes (Teacher + Student versions)
  3. Build the Christianity blended chapter test (Teacher + Student)

This is a calibration pilot. Before scaling to Units 2-9, the four
skills need at least one full pass to surface format, length, and
content issues.

────────────────────────────────────────────────────────────────────
ORIENTATION (read first, in order)
────────────────────────────────────────────────────────────────────

Read these documents to understand the full context. Don't skip — the
artifacts must reflect the design decisions in these documents:

  1. classes/worldview/README.md
  2. classes/worldview/teaching-map.md (especially Unit 1 section)
  3. classes/worldview/teaching-methodology.md
  4. classes/worldview/worldview-grid.md (Christianity column)
  5. classes/worldview/handouts/unit-01-christianity-reading-packet.md
     (the existing calibration draft you'll regenerate)

Then skim these to understand the source material landscape:

  6. classes/worldview/_source-text/textbook/ch02.md (publisher
     Christianity chapter)
  7. classes/worldview/_source-text/teaching-manual/ch02.md
     (publisher's teaching guide for Ch 2)
  8. classes/worldview/_source-text/_cd/UTT Unit 02 Files/ — directory
     listing only; the publisher's CD assets for Ch 02 (test, writing
     assignment, supplemental quizzes)

Skill specs (read each before invoking):

  9. .claude/commands/build-reading-packet.md
 10. .claude/commands/build-blended-lecture-notes.md
 11. .claude/commands/build-blended-chapter-test.md

────────────────────────────────────────────────────────────────────
EXECUTION ORDER
────────────────────────────────────────────────────────────────────

Run the three skills in this order, with a calibration pause after
each one. Use the Skill tool to invoke each.

STEP 1 — Regenerate the reading packet
  /build-reading-packet 1

  After this completes, read the produced packet end-to-end. Confirm:
  - Publisher Vocabulary section now includes terms from each of
    Ch 8 through Ch 17 (the prior calibration draft only had Ch 2 +
    partial Ch 8)
  - The Doug Letter Preview section references the publisher's Ch 02
    Doug Letter (not a generic preview)
  - Length budget is 10-20 printed pages
  - All claims are cited
  - "Where this view will be tested" sentences at end of each lens
    correctly preview later worldviews

  If anything is off, note it but proceed. Surface skill-spec issues
  in the final report.

STEP 2 — Build the lecture notes
  /build-blended-lecture-notes 1

  This produces TWO files: a Teacher version and a Student version.
  After this completes, read both. Confirm:
  - Teacher version has time markers, "WRITE ON BOARD" prompts, and
    anticipated student questions
  - Student version is the same shape with key vocabulary blanked
    out as fill-in (__________)
  - Coverage spans Days 1, 2, 3, AND extra days for Unit 1 (Day 4
    extra Deep Dive + Day 8 intra-Christian survey are Unit 1
    specials per the skill spec)
  - Day 7 has the brief Four-Test lecture frame
  - Vocabulary used in lectures matches what's in the reading packet
    AND what will be on the test
  - Teacher version length: ~12-15 pages; Student version: ~8-10 pages

STEP 3 — Build the blended chapter test
  /build-blended-chapter-test 1

  This produces TWO files: Teacher (with answers) and Student
  (questions only). After this completes, read both. Confirm:
  - Total questions land between 45-60
  - Question types match publisher format: Matching, MC, T/F (with
    correction for false), Fill-in-Blank, Short Answer, Essay
  - Reference codes are preserved from publisher items (e.g., [2.5],
    [8.6]) and locally-built items use [U1.<section>] format
  - Christianity-relevant questions extracted from each of Ch 8-17
    are present
  - Cross-comparative items have been adapted to per-worldview format
    where they don't fit the per-unit scope ("Does Christianity deny
    X?" instead of "Which worldviews deny X?")
  - Single class period administration time (~50 min)

────────────────────────────────────────────────────────────────────
CROSS-ARTIFACT COHERENCE CHECK
────────────────────────────────────────────────────────────────────

After all three artifacts exist, do a coherence pass across them.
Verify:

  - The same publisher vocabulary appears in all three artifacts
    (reading packet's Publisher Vocabulary section, lecture notes'
    fill-in terms, test's fill-in-the-blank items)
  - The unit's Key Theological Anchors from teaching-map.md
    (Trinitarian Monotheism, Imago Dei, Special Creation, Natural
    Law, Redemptive Narrative, Sphere Sovereignty, Agape Love,
    Biblical Stewardship) appear in all three
  - Day 7's Four-Test exercise in the lecture notes prepares
    students for the test's analytical questions
  - The Doug Letter (publisher's Ch 02) is referenced in the reading
    packet and the lecture notes' Day 9 wrap

Flag any divergences. The whole point of "blended" is that all
four artifacts share one source-of-truth.

────────────────────────────────────────────────────────────────────
COMMIT
────────────────────────────────────────────────────────────────────

After all three artifacts are produced and coherence-checked, commit
in one logical commit:

  git add classes/worldview/handouts/unit-01-christianity-reading-packet.md \
          classes/worldview/lectures/unit-01-christianity-lecture-notes-teacher.md \
          classes/worldview/lectures/unit-01-christianity-lecture-notes-student.md \
          classes/worldview/assessments/unit-01-christianity-test-teacher.md \
          classes/worldview/assessments/unit-01-christianity-test-student.md

Use a Conventional Commits message in the project's style:

  feat(worldview): produce Unit 1 (Christianity) full artifact set

  Pilots the four-skill production pipeline end-to-end. Regenerates
  the reading packet with full Ch 8-17 vocabulary, builds Teacher +
  Student lecture notes for Days 1-4 + 7-8, and builds the Day-9
  blended chapter test (Teacher + Student) combining publisher Ch 02
  with extracted Christianity questions from Ch 8-17.

  Calibration pass before scaling to Units 2-9. [Note any
  skill-spec issues surfaced — the prompt has a section on this.]

Do NOT stage:
  - .claude/commands/transcribe-source-text.md (untracked, unrelated)
  - .claude/settings.local.json (settings)
  - classes/worldview/_source-text/_cd/ (publisher CD content;
    keep as local-only working copy unless the user has decided
    otherwise)

────────────────────────────────────────────────────────────────────
FINAL REPORT
────────────────────────────────────────────────────────────────────

Report back with:

  - Confirmation of each artifact's location and approximate length
  - Cross-artifact coherence: did vocabulary/anchors line up across
    all three?
  - SKILL-SPEC ISSUES surfaced (this is the most valuable output of
    the pilot — what needs to change in the skill specs before
    scaling to Units 2-9?)
  - Pedagogical issues for the teacher (anything that would surprise
    or trouble them when they actually use these artifacts in class)
  - Recommended next unit to pilot (probably Unit 3 Islam — full
    publisher coverage; or Unit 2 Judaism — fully local build to
    stress-test the supplemental-unit path)

Keep the final report under ~600 words. The full content of the
artifacts is in the files; the report is for triage decisions.

────────────────────────────────────────────────────────────────────
GROUND RULES
────────────────────────────────────────────────────────────────────

  - Use the Skill tool for the three slash commands; don't manually
    build artifacts
  - Do NOT modify the skill specs themselves during this run; surface
    needed changes in the final report so the user can review before
    you (or the next session) make them
  - Do NOT modify teaching-map.md, pacing-priority-guide.md, or other
    design documents during this run; they are the source of truth
    the artifacts must reflect
  - Use TodoWrite to track the three steps + commit
  - The Christianity reading packet currently exists at
    classes/worldview/handouts/unit-01-christianity-reading-packet.md
    as a calibration draft (~5,100 words). The /build-reading-packet
    skill will overwrite it. That's intentional.
  - Match project conventions per CLAUDE.md: no emojis in artifacts;
    professional but warm tone; lowercase-hyphenated filenames;
    compact-style markdown tables
  - When the publisher's CD assets need to be read, the chapter test
    PDFs and Doug Letter PDFs are readable by the Read tool
    directly. The xlsx Syllabi files cannot be read without
    conversion — don't try.
```

---

## Notes for the user (you)

- Save this file (already done at `classes/worldview/_pilot-unit-1-prompt.md`); you can re-paste from here for any future pilot.
- The same shape works for Units 2–9 with the unit number swapped — but Units 2 and 4 (Judaism, Mormonism) need `/build-doug-letter` added as a fourth skill, since the publisher doesn't provide one.
- Expect the new session to use a lot of tokens reading the source material (especially the textbook and teacher's manual chapters). That's the cost of producing high-quality artifacts; the alternative — fragmented context — produces lower-quality output.
- The "SKILL-SPEC ISSUES" section of the report is the most valuable feedback from this pilot. Before scaling to Units 2–9, expect to make 1–3 small adjustments to one or more of the skill specs based on what the pilot surfaces.
