---
name: build-doug-letter
description: Build a Doug Letter writing assignment for a supplemental Worldview unit (Judaism, Mormonism, distinct Hinduism, distinct Buddhism)
args: "<unit-number>"
---

# Build Doug Letter

Build a per-unit "Doug Letter" writing assignment in the publisher's exact format, for a Worldview unit the publisher does not cover. Doug is a fictional college freshman whose worldview is being challenged by his secular professor and roommates; each chapter, Doug writes home asking for help thinking through the worldview the unit is teaching. Students respond with a 1–2 page letter answering the four embedded questions.

This skill is for the 4 units the publisher's CD does NOT cover with its own Doug Letter:

- Unit 2 — Judaism
- Unit 4 — Mormonism
- Unit 5 — Hinduism (distinct treatment beyond what publisher Ch 6 supplies)
- Unit 6 — Buddhism (distinct treatment beyond what publisher Ch 6 supplies)

For all other units (0, 1, 3, 7, 8, 9), use the publisher's existing Doug Letter directly from `_source-text/_cd/UTT Unit <NN> Files/<NN> Writing Assignment/`.

## Usage

```
/build-doug-letter 2     # Judaism
/build-doug-letter 4     # Mormonism
/build-doug-letter 5     # Hinduism
/build-doug-letter 6     # Buddhism
```

## Process

### 1. Read context

1. `classes/worldview/teaching-map.md` — locate the Unit `<N>` section; read purpose, key anchors, Gospel-conversation focus
2. `classes/worldview/handouts/unit-<NN>-<slug>-reading-packet.md` if it exists — for content alignment
3. **Read 2–3 publisher Doug Letters** as format models — recommend Ch 02 (Christianity), Ch 03 (Islam), Ch 06 (New Spirituality):
   - `classes/worldview/_source-text/_cd/UTT Unit 02 Files/02 Writing Assignment/UTT Chapter 02 Assignment-Teacher.pdf`
   - `classes/worldview/_source-text/_cd/UTT Unit 03 Files/03 Writing Assignment/UTT Chapter 03 Assignment-Teacher.pdf`
   - `classes/worldview/_source-text/_cd/UTT Unit 06 Files/06 Writing Assignment/UTT Chapter 06 Assignment-Teacher.pdf` (if it exists)

### 2. Match the publisher's voice and format

Each Doug Letter has the same shape:

- **Salutation** ("Hello!" or similar — Doug's casual voice)
- **Setup paragraph(s)** — Doug describes the encounter (a conversation with his professor, his roommate Nathan, a friend, a class). The encounter raises the unit's worldview as a real question Doug needs help with.
- **Four embedded questions in bold** — these are the writing prompts students answer. The questions are usually:
  1. A definitional question ("What is ___?")
  2. A "why" question ("Why does it matter / why should we engage with this?")
  3. A "what does the Christian view say" question
  4. A personal application question
- **Sign-off** ("–Doug")
- **Teacher version (page 2)** — sample answers to each of the four questions, with curriculum reference codes like `[2.5]`

The voice is breezy and specific (Doug's roommate's name is Nathan; Doug is taking specific classes; specific things happened). Avoid generic. Avoid adult voice — Doug sounds like a college freshman.

### 3. Compose the letter

For the assigned unit:

- **Setup:** Find a plausible college-freshman scenario where Doug encounters this worldview (a Jewish friend invites him to Shabbat dinner; an LDS friend's family hosts him; a Hindu philosophy professor; a Buddhist meditation app his roommate is into)
- **Four questions** that map to the unit's pedagogical anchors:
  1. Definitional ("What is ___ on its own terms?")
  2. Why-engage ("Why should I take this seriously?")
  3. Christian-comparison ("What does the Christian view say differently?")
  4. Gospel-conversation ("How would I actually talk about Jesus with my friend?")
- **Sample answers** that draw from the unit's Key Anchors, the worldview's primary sources, and the unit's Gospel-conversation focus
- Reference codes that point to sections of the unit's reading packet (e.g., `[U2.3a]` for Unit 2 packet section 3a)

### 4. Write to

`classes/worldview/assessments/unit-<NN>-<slug>-doug-letter.md`

Use the prefix-zero pattern:
- `unit-02-judaism-doug-letter.md`
- `unit-04-mormonism-doug-letter.md`
- `unit-05-hinduism-doug-letter.md`
- `unit-06-buddhism-doug-letter.md`

### 5. Output structure

Match the publisher's two-page layout:

```
# Unit <N> — Doug Letter (Locally-Built)

*This Doug Letter follows the publisher's format for use in Unit <N>
(<Worldview>), which Myers/Noebel does not cover. Use as the per-unit
writing assignment on Day 9, replacing the Worldview Brief.*

---

## Page 1 — Letter to Students

[Salutation]

[Setup paragraphs: Doug encounters the worldview. ~2–4 paragraphs of
narrative. Specific details. Doug's voice.]

[Four embedded questions in bold, naturally folded into the narrative.]

[Sign-off]

–Doug

---

## Page 2 — Teacher Version (Sample Answers)

Doug brought up four different questions; below is a rough outline of
possible responses:

1. **[Question 1 verbatim]**
   [Sample answer drawing on unit's Key Anchors. Reference code in brackets.]

2. **[Question 2 verbatim]**
   [Sample answer.]

3. **[Question 3 verbatim]**
   [Sample answer with explicit Christian-comparison content.]

4. **[Question 4 verbatim]**
   [Sample Gospel-conversation sketch. Note if "Answers will vary."]
```

### 6. Rules

1. **Match the publisher's Doug voice.** Casual, specific, unguarded. He's a college freshman, not a theologian.
2. **The four questions must be answerable in 1–2 pages combined.** Don't write a 10-question essay.
3. **Sample answers must come from the unit's reading packet content.** No content the student couldn't have learned in the unit.
4. **For supplemental-only worldviews**, sample answers should also reference the relevant primary sources used in the unit (e.g., Yoma 39b for Judaism; D&C for Mormonism; Bhagavad Gita for Hinduism; Dhammapada for Buddhism).
5. **Charitable representation is preserved.** Doug does not encounter caricatures of the worldview. His friends are real people; the worldview is on its own terms.
6. **Match project conventions.** No emojis. Markdown only. Lowercase-hyphenated filename.

### 7. Report

```
✅ Built Unit <N> — <Worldview> Doug Letter
   Output: classes/worldview/assessments/unit-<NN>-<slug>-doug-letter.md
   Estimated student reading time: ~5 min
   Estimated student writing time: ~30–45 min
   Format reference used: Ch 02 / Ch 03 / Ch 06 publisher Doug Letters
   Pedagogical notes for teacher: <anything worth flagging before printing>
```
