# Apologetics

**Grade Level:** 10–11
**School:** Watersprings School
**School Year:** 2026–2027
**Source Text:** Summit's _Understanding the Times_ series, **Book II — Apologetics** (Student Textbook + Teacher Manual; 18 chapters, 10 subsections each)
**Delivery Model:** **Publisher** — with a few _signature debate days_ layered in where the content genuinely warrants it (see below)
**Instructor:** Jeremy Ward

---

## Status

**Being built — Stage 0.** Part of the 2026–27 curriculum refresh. Class shell + portal
scaffold are in place; all 18 chapters of the textbook + teacher manual are transcribing
(OCR pipeline). Model decided; syllabus, teaching map, and lesson scaffold are next.

### Decisions locked in

- **Delivery model: `publisher`** (same as Foundations). Decided at the post-OCR model
  checkpoint after reading the source together. The publisher's scope & sequence is
  genuinely strong and already builds in discussion questions, activities, group work, and
  case-study dialogues, so a diffuse "light cohort layer" would mostly relabel what's
  already there.
- **Signature debate days — surgical, not systematic.** The one thing cohort adds that the
  publisher doesn't is _defense-first sequencing_ (students commit to / defend a position
  **before** the answer is taught). That's worth doing **only** on the back-half
  objection-and-response chapters where it transforms the lesson — e.g. **Ch 9.9 "A Dialogue
  with a Muslim," Ch 11 arguments for God / the resurrection, Ch 13 the problem of evil,
  Ch 14 hell, Ch 8 truth & tolerance.** Run these as a real Pair & Defend / Case Study
  (see [`_shared/cohort-tools.md`](../../_shared/cohort-tools.md)) _if/when_ it makes sense
  for the class — not as a standing requirement. The front third (Bible, metanarrative,
  Logic & Love skills) stays publisher content-first.
- **18 chapters, 8 class lessons/chapter** (per the publisher scope & sequence; Ch 18
  Conclusion is a shorter 5-subsection review). Compressed pacing is set at the map stage.

## Current Focus (Stage 0)

- [x] **Upload source images** — all 18 chapters (textbook + teacher manual) + portal assets staged.
- [x] **Transcribe source text** — OCR pipeline (`convert-heic` → `ocr.swift` → `clean-ocr`) → `_source-text/**/chNN.md`.
- [x] **Model checkpoint** — decided: **`publisher`** + surgical signature debate days (recorded above).
- [x] **Official syllabus** — [syllabus/syllabus.md](syllabus/syllabus.md) (from the born-digital portal scope & sequence + course overview).
- [x] **Teaching map** — [teaching-map.md](teaching-map.md); 6/6/6 trimester split, 5 signature debate days, calendar-exact for 2026–27. **Teacher-approved.**
- [x] **Lesson-plan scaffold** — [lesson-plans-2026-27/](lesson-plans-2026-27/) (publisher model; week folders built per chapter by `/build-chapter`).

**Stage 0 complete.** Next: **Stage 1** per chapter — `/build-chapter` → `/build-atlas` →
`/push-atlas` → `/publish-chapter`, starting at Ch 1. Also pending: create the 18 Atlas unit
shells + 18 Google Classroom topics (structural, from the approved map).

Then per chapter: `/build-chapter` → `/build-atlas` → `/push-atlas` → `/publish-chapter`.
The orchestrator **`/setup-class apologetics`** sequences all of this and is resumable —
re-run it and it reports what's done vs. pending.

## Repository Structure

- `teaching-map.md` — calendar-exact pacing for all chapters, 2026–27 _(created by `/generate-map`)_
- [syllabus/](syllabus/) — syllabus images in, deduced scope & sequence out
- [_source-text/](_source-text/) — OCR transcripts of the textbook and teacher manual (the
  source of truth all skills read from); see [_source-text/README.md](_source-text/README.md)
- [rubicon-atlas/](rubicon-atlas/) — UbD unit fields + Madeline Hunter daily lessons (Atlas pillar)
- `handouts/` — application handouts generated during lesson planning

`lesson-plans-2026-27/` is added by `/scaffold-lesson-structure` once the model is decided.

## The three pillars

A complete class spans **repo content** · **Rubicon Atlas** · **Google** (Classroom/Forms/Slides).
See the root [CLAUDE.md](../../CLAUDE.md) and [`_shared/lesson-plan-standards.md`](../../_shared/lesson-plan-standards.md).
**Foundations Ch 1–2 is the worked exemplar for all three.**
