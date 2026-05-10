---
name: build-blended-lecture-notes
description: Build per-worldview lecture notes (Teacher + Student versions) blending publisher Ch X content with Ch 8-17 worldview slices, for the unit's lecture-bearing days
args: "<unit-number>"
---

# Build Blended Lecture Notes

Build the per-unit lecture notes that the teacher delivers from on the unit's lecture days. Each unit has lecture content on Day 1 (Framing), Days 2–3 (Deep Dive Pts 1 + 2 — five lenses each), and a brief Day 7 lecture frame (Four-Test + vs. Christianity). The skill produces two parallel versions following the publisher's Teacher/Student split:

- **Teacher version** — full notes with answers, board prompts, time markers, anticipated questions, transitions
- **Student version** — same structure as Teacher version with key terms blanked out as fill-in-the-blank, so students follow along during the lecture and walk away with a complete study reference

"Blended" means the same source pattern as the blended test and the reading packet: each lens pulls from BOTH the publisher's worldview chapter (Ch X) AND the publisher's discipline-comparative chapter (Ch 8–17 worldview slice). The vocabulary students fill in during the lecture is the vocabulary they'll be tested on.

## Usage

```
/build-blended-lecture-notes 1     # Christianity (13-day unit; extra Day 4 + Day 8)
/build-blended-lecture-notes 2     # Judaism (standard 9-day; supplemental — no publisher Ch X)
/build-blended-lecture-notes 3     # Islam (standard 9-day)
/build-blended-lecture-notes 4     # Mormonism (standard 9-day; supplemental)
/build-blended-lecture-notes 5     # Hinduism (standard 9-day; partial publisher coverage via Ch 6)
/build-blended-lecture-notes 6     # Buddhism (standard 9-day; partial publisher coverage via Ch 6)
/build-blended-lecture-notes 7     # New Spirituality (5-day compressed)
/build-blended-lecture-notes 8     # Secularism (standard 9-day)
/build-blended-lecture-notes 9     # Revolutionary Lineage (13-day; three movements — Marxism, Progressivism, Postmodernism)
```

This skill targets Units 1–9 (the worldview units). For Unit 0 (Foundations) and Unit 10 (Capstone), build lecture notes manually — those units have different shapes (framework intro and capstone facilitation respectively).

## Process

### 1. Read context

1. `classes/worldview/teaching-map.md` — locate the Unit `<N>` section; read purpose, key anchors, day-by-day schedule, Gospel-conversation focus
2. `classes/worldview/handouts/unit-<NN>-<slug>-reading-packet.md` if it exists — for narrative consistency with what students have read
3. `classes/worldview/worldview-grid.md` — find this unit's column; lecture builds toward students filling it in
4. **Publisher worldview chapter** (the textbook):
   - Unit 0 → Ch 1; Unit 1 → Ch 2; Unit 3 → Ch 3; Unit 5/6/7 → Ch 6; Unit 8 → Ch 4; Unit 9 → Ch 5 + Ch 7
   - Path: `classes/worldview/_source-text/textbook/ch<NN>.md`
   - For Units 2, 4 (Judaism, Mormonism — no publisher coverage): use the unit's reading packet and primary sources as the source-of-truth instead
5. **Publisher teacher's manual chapter** (matching above):
   - Path: `classes/worldview/_source-text/teaching-manual/ch<NN>.md`
   - The teacher's manual is the single most valuable source for this skill — it's literally written to teach from. Mine it for discussion questions, activity prompts, anticipated student responses, pedagogical guidance.
6. **Worldview slices of Ch 8–17 (textbook):**
   - For Day 2 lenses (Theology, Philosophy, Ethics, Biology, Psychology): pull this worldview's slice from `classes/worldview/_source-text/textbook/ch08.md` through `ch12.md`
   - For Day 3 lenses (Sociology, Law, Politics, Economics, History): pull from `ch13.md` through `ch17.md`
   - Find each chapter's section labeled with this worldview (e.g., `2. SECULARISM`, `7. CHRISTIANITY`)
7. **Worldview slices of Ch 8–17 (teacher's manual):** same as above but `_source-text/teaching-manual/`. Often contains discussion-launcher questions for the discipline-comparative work.
8. **The publisher's matching chapter test** (`_source-text/_cd/UTT Unit <NN> Files/<NN> Test Questions/UTT Chapter <NN> Test-Teacher.pdf`) — the lecture must teach every defined term that appears as a fill-in-the-blank on the test, in the publisher's exact vocabulary.

### 2. Compose the lecture notes

Structure the notes by lecture day. For a standard 9-day unit, this means four sections (Days 1, 2, 3, 7). For Unit 1 (Christianity, 13d), add Day 4 (extra Deep Dive) and Day 8 (intra-Christian survey). For Unit 7 (New Spirituality, 5d), combine Days 2–3 into one. For Unit 9 (Revolutionary Lineage, 13d), produce three Framing+Deep-Dive sets (one per movement: Marxism, Progressivism, Postmodernism).

### Day 1 — Framing (Teacher version layout)

```
## Day 1 — Framing the <Worldview> [target: 45 min]

### Opening hook [5 min]
[A specific story, statistic, or scenario that grounds the worldview in a
real person or moment. Pull from the textbook's chapter opener if strong;
adapt if not.]

### What this worldview actually is [15 min]
**WRITE ON BOARD:** <Worldview's central claim, one sentence>

[2–3 paragraphs of teacher-spoken narrative: who holds this worldview,
why, in its strongest form. Charitable representation. No strawmen.]

KEY VOCAB (blank in student version):
- **<Term>** — definition (publisher Ch X, §Y)
- **<Term>** — definition (publisher Ch X, §Y)

### The framing question [10 min]
**WRITE ON BOARD:** <Unit's framing question from teaching-map.md>

[How this worldview answers it differently from Christianity, in 1–2
sentences. Don't pre-empt Day 7 critique — just frame the contrast.]

### Anticipated student questions [10 min response window]
- "Why are we even studying this?" → [Pre-prepared response]
- "[Likely worldview-specific objection]" → [Pre-prepared response]

### Transition to Day 2 [5 min]
[Set up the 10-lens deep dive. Reading assignment confirmation.]
```

### Day 2 — Deep Dive Pt 1 (5 lenses)

```
## Day 2 — Deep Dive Pt 1: Theology, Philosophy, Ethics, Biology, Psychology [target: 50 min]

### Opening review [5 min]
[Quick recap of Day 1 framing. One question to surface anything still unclear.]

### Lens 1: Theology [8 min]
**WRITE ON BOARD:** <Worldview>'s answer to "Who is God?": <one-line answer>

**From the worldview's own chapter (Ch X):**
[Key claim from publisher Ch X, with citation]

**From Ch 8 (Theology), <Worldview> slice:**
[Key claim from Ch 8 §<section>, with citation]

KEY VOCAB:
- **<Term>** — definition (Ch 8, §<sec>)
- **<Term>** — definition (Ch 8, §<sec>)

**STUDENTS FILL IN GRID:** <Worldview> column, Theology row.

[Repeat the above structure for Lenses 2–5.]

### Synthesis check [3 min]
[Quick verbal check: "What's the through-line across these five lenses?"]

### Bridge to Day 3 [2 min]
```

### Day 3 — Deep Dive Pt 2 (5 lenses)
Same structure as Day 2 but covering Sociology, Law, Politics, Economics, History.

### Day 7 — Four-Test + vs. Christianity (brief lecture frame)

```
## Day 7 — Four-Test + vs. Christianity [lecture frame: 10 min, then small-group: 35 min]

### Lecture frame [10 min]
**WRITE ON BOARD:** The four tests
1. Reason — Is the worldview internally coherent?
2. Outer World — Does it match what we observe?
3. Inner World — Does it match our deepest moral intuitions?
4. Real-World Consequences — When lived at scale, what fruit does it bear?

[Brief teacher-spoken framing of how these four tests apply specifically
to <this worldview>. 2–3 highest-value tension points to surface for the
small groups.]

### Hand off to small groups [35 min]
[Small-group worksheet structure. Groups of 3–4. Each group takes one
test and applies it to <this worldview>, then reports back.]

### Whole-class synthesis [last 5 min]
[Capture the strongest cracks each group surfaced. Reinforce the publisher's
expected vocabulary for the test.]
```

### Special cases

**Unit 1 (Christianity, 13d):** Add Day 4 (extra Deep Dive — drill Theology and Philosophy more deeply since this is the baseline) and Day 8 (intra-Christian survey: Catholic / Protestant / Orthodox).

**Unit 7 (New Spirituality, 5d):** Combine the Day 2 + Day 3 Deep Dives into one combined day (all 10 lenses, accelerated). Skip Day 7 brief — fold the Four-Test into the combined Deep Dive day.

**Unit 9 (Revolutionary Lineage, 13d):** Produce three sets of Framing+Deep-Dive notes (one per movement: Marxism, American Progressivism, Postmodernism). The Movement 2 (Progressivism) notes are entirely locally-built since the publisher doesn't cover it; use [unit-09-revolutionary-lineage-outline.md](../classes/worldview/unit-09-revolutionary-lineage-outline.md) as the source.

**Units 2, 4 (Judaism, Mormonism):** No publisher Ch X to mine. Build entirely from primary sources, the unit's reading packet, and the Key Anchors in teaching-map.md. The skill should still produce Teacher + Student versions in the same shape.

### 3. Two output files

**Teacher version:**
`classes/worldview/lectures/unit-<NN>-<slug>-lecture-notes-teacher.md`

**Student version (guided fill-in-blank handout):**
`classes/worldview/lectures/unit-<NN>-<slug>-lecture-notes-student.md`

The Student version is the Teacher version with key vocabulary terms replaced by blanks (`__________`) and answer keys stripped. Board prompts, time markers, and discussion-launchers stay (so students know when to listen vs. write). Keep the section structure identical so teacher and students are literally on the same page.

### 4. Rules

1. **Teach the publisher's vocabulary, in the publisher's words.** When the publisher says "Trinitarian monotheism," the lecture notes say "Trinitarian monotheism" — not "the doctrine of three-in-one God." Vocabulary fidelity is the bridge to the test.
2. **Time markers are non-negotiable.** Every section has a time budget. The teacher will be glancing at these while standing at the front of the room.
3. **WRITE ON BOARD prompts are explicit.** Use the literal phrase `**WRITE ON BOARD:**` so the teacher's eye catches it during delivery. Match these prompts exactly between Teacher and Student versions so students know to copy the board content.
4. **Charitable representation comes first.** Day 1 Framing is steel-man. Critique belongs in Day 7. Don't editorialize in Day 2/3 Deep Dives — present each worldview's claim on its own terms.
5. **Anticipate student questions explicitly.** Each Day 1 includes 2–3 likely student questions with pre-prepared responses. This is the single highest-value section for a teacher under pressure.
6. **Don't write the lecture verbatim.** These are notes, not a script. Bullet points, key sentences, board prompts — not paragraphs of teacher monologue.
7. **Length budget.** Teacher version: ~12–15 pages per standard 9-day unit (3 pages Day 1, 5 pages Day 2, 5 pages Day 3, 1 page Day 7). Student version: ~8–10 pages (same shape, less density).
8. **Match project conventions.** No emojis. Markdown only. Lowercase-hyphenated filenames.

### 5. Report

```
✅ Built Unit <N> — <Worldview> Blended Lecture Notes
   Outputs:
     classes/worldview/lectures/unit-<NN>-<slug>-lecture-notes-teacher.md
     classes/worldview/lectures/unit-<NN>-<slug>-lecture-notes-student.md
   Lecture days covered: Day 1, Day 2, Day 3, Day 7 [+ extras for Unit 1, 7, 9]
   Estimated teacher version length: ~<count> pages
   Estimated student version length: ~<count> pages
   Source breakdown:
     Publisher textbook Ch <X>: <pages mined>
     Publisher teacher's manual Ch <X>: <pages mined>
     Publisher Ch 8–17 worldview slices: <chapters mined>
     Publisher chapter test vocabulary: <terms incorporated>
   Sources to acquire: <list, or "none">
   Pedagogical notes for teacher: <anything worth flagging before delivery>
```
