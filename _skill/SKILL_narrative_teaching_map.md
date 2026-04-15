# Skill: Chronological Narrative Teaching Map Generator

## Purpose

Generate a chronological narrative teaching map for a high school Bible class. This style walks through Scripture in story order, emphasizing the Bible as one unified story pointing to Christ. Ideal for survey courses.

## Best For

- Old Testament Survey
- New Testament Survey
- Biblical Theology (tracing themes through redemptive history)
- Courses where students need to see the "big picture" of Scripture

## Inputs Required

1. **School calendar** — Read from `_shared/school-calendar-2026-27.md`
2. **Books/passages to cover** — Typically all 39 OT books or all 27 NT books (for survey courses)
3. **Class metadata** — Class name, grade level, Bible translation being used

## The Narrative Approach

The Bible is taught as **one story in four movements**:

1. **Creation** — God creates a good world and places humans in it (Gen 1-2)
2. **Fall** — Humans rebel, sin enters, the world breaks (Gen 3-11)
3. **Redemption** — God pursues His people through covenant and promise (Gen 12 - Revelation 20)
4. **Restoration** — God will make all things new (Revelation 21-22)

Every passage is taught with two questions:
- **Where are we in the story?** (timeline, characters, plot)
- **How does this point to Christ?** (typology, prophecy, fulfillment)

## Process

### Step 1: Map Available Instructional Days

- Start with first day of school, end with last day
- Remove all no-school dates from calendar
- Count total available instructional days
- Divide into trimesters using trimester end dates

### Step 2: Organize Content Chronologically

**For Old Testament Survey**, follow this order:
- **Creation to Patriarchs**: Genesis
- **Exodus and Wandering**: Exodus, Leviticus, Numbers, Deuteronomy
- **Conquest and Judges**: Joshua, Judges, Ruth
- **United Kingdom**: 1-2 Samuel, 1 Kings 1-11, Psalms (selections)
- **Divided Kingdom and Prophets**: 1 Kings 12 - 2 Kings, Isaiah, Jeremiah, minor prophets (selections)
- **Exile and Return**: Daniel, Ezekiel, Ezra, Nehemiah, Esther
- **Wisdom Literature**: Job, Proverbs, Ecclesiastes, Song of Solomon (interspersed throughout)

**For New Testament Survey**, follow this order:
- **Gospels** (chronological life of Christ): Matthew, Mark, Luke, John (harmonized)
- **Early Church**: Acts 1-12
- **Paul's Journeys and Letters**: Acts 13-28 with epistles inserted chronologically
- **General Epistles**: Hebrews, James, 1-2 Peter, 1-3 John, Jude
- **Revelation**: The culmination of the story

### Step 3: Chunk into Narrative Arcs

Group books/passages into logical narrative units (not just by book divisions):

**Example for OT Survey**:
- Unit 1: Creation and Fall (Gen 1-11) — 2 weeks
- Unit 2: Patriarchs (Gen 12-50) — 3 weeks
- Unit 3: Exodus and Law (Exod, Lev, Num, Deut) — 4 weeks
- Unit 4: Conquest and Judges (Josh, Judg, Ruth) — 3 weeks
- Unit 5: Kingdom Rising (1-2 Sam, 1 Kings 1-11) — 4 weeks
- Unit 6: Kingdom Divided (1 Kings 12 - 2 Kings, prophets) — 6 weeks
- Unit 7: Exile and Return (Dan, Ezra, Neh, Esth) — 3 weeks
- Unit 8: Wisdom and Worship (Psalms, Proverbs, Job, Eccl, SoS) — 3 weeks

### Step 4: Plan the Weekly Rhythm

Typical week:

| Day | Activity | Description |
|-----|----------|-------------|
| Mon | Story Introduction | Context, characters, timeline placement |
| Tue | Read and Discuss | What happens in the text? Key events and themes |
| Wed | Read and Discuss | Continue the narrative, identify turning points |
| Thu | Connect to the Whole | How does this fit the larger story? Where's Christ? |
| Fri | Creative Response | Timeline work, journaling, art, discussion, or quiz |

### Step 5: Create Narrative Tools

For each unit, prepare:
- **Timeline**: Visual representation of when events happen (post in classroom, update weekly)
- **Map**: Where events take place (geography matters for understanding)
- **Character List**: Who are the key people? What's their role in the story?
- **Theme Tracker**: How do key themes (covenant, temple, sacrifice, kingship) develop?
- **Christological Connections**: How does this passage point to Jesus? (typology, prophecy, fulfillment)

### Step 6: Plan Assessments

- **Timeline Projects**: Students create visual timelines (can be ongoing, added to each week)
- **Story Retellings**: Oral or written summaries of major narrative arcs
- **Thematic Essays**: Trace a theme (e.g., "covenant") from Genesis to Revelation
- **Map Quizzes**: Identify key locations and movements of God's people
- **Character Studies**: Deep dive on major figures (Abraham, Moses, David, Paul, etc.)
- **Unit Exams**: Covering major narrative arcs (not just factual recall, but story comprehension)

### Step 7: Build the Week-by-Week Map

For each week, specify:
- Week number and date range
- Books/passages covered
- Narrative arc (what's happening in the story?)
- Timeline placement (where are we in redemptive history?)
- Christological connection (how does this point to Jesus?)
- Creative response or assessment

## Output Format

Write the completed map to `classes/<class-name>/teaching-map.md`:

```markdown
# <Class Name> — Teaching Map

**School Year:** 2026–2027  
**Grade Level:** <grade>  
**Biblical Text:** <Old Testament / New Testament / Full Bible>  
**Teaching Style:** Chronological Narrative  
**Total Instructional Days:** <count>

## Course Overview

<Brief description: teaching the Bible as one story, creation to new creation, with Christ at the center>

## The Story in Four Acts

1. **Creation** — God makes a good world (Gen 1-2)
2. **Fall** — Humans rebel, the world breaks (Gen 3-11)
3. **Redemption** — God pursues His people through covenant (Gen 12 - Rev 20)
4. **Restoration** — God makes all things new (Rev 21-22)

## Narrative Arc Overview

| Unit | Weeks | Books/Passages | Key Events | Timeline |
|------|-------|----------------|------------|----------|
| 1: Creation & Fall | 1-2 | Genesis 1-11 | Creation, Fall, Flood, Babel | ~4000-2000 BC |
| 2: Patriarchs | 3-5 | Genesis 12-50 | Abraham, Isaac, Jacob, Joseph | 2000-1800 BC |
| ... | ... | ... | ... | ... |

## Week-by-Week Schedule

### Week 1 — Aug 17–21, 2026
**Unit 1: Creation and Fall**  
**Passage:** Genesis 1-2  
**Narrative:** In the beginning, God creates a good world and places humans in it to rule and serve.

**Mon: Story Introduction**
- Set the stage: Why does the Bible start here? What does it tell us about God, humanity, and the world?
- Introduce the creation account (Gen 1-2)
- Post "Creation" on the class timeline

**Tue-Wed: Read and Discuss**
- Tue: Read Gen 1. What does the structure of the 7 days reveal about God? What is humanity's role?
- Wed: Read Gen 2. How does this complement Gen 1? What's the relationship between God, Adam, Eve, and creation?
- Key themes: order, goodness, image of God, Sabbath, stewardship

**Thu: Connect to the Whole**
- How does this opening chapter set up the entire story of the Bible?
- Christological connection: Jesus is the "image of the invisible God" (Col 1:15), the true human who fulfills Adam's calling

**Fri: Creative Response**
- Add Creation to the class timeline (draw or post visual)
- Journal: "What does it mean that you are made in God's image? How does that shape how you see yourself and others?"

**Due:** Timeline entry (drawn or written)

**Notes:** First week of school — focus on setting the stage for the whole story

---

### Week 2 — Aug 24-28, 2026
**Unit 1: Creation and Fall**  
**Passage:** Genesis 3-11  
**Narrative:** Humans rebel against God. Sin enters the world, and everything breaks. But God promises redemption.

**Mon: Story Introduction**
- What happens when humans reject God's design? Genesis 3-11 shows the cascading consequences of the Fall.
- Timeline: Move from Creation to Fall

**Tue-Wed: Read and Discuss**
- Tue: Read Gen 3. The Fall and its consequences. What is lost? What does God promise (Gen 3:15)?
- Wed: Read Gen 4-11. Sin spreads: Cain and Abel, the Flood, the Tower of Babel. How does each story show the effects of sin?

**Thu: Connect to the Whole**
- The "proto-evangelium" (Gen 3:15): the first promise of a Redeemer who will crush the serpent
- Christological connection: Jesus is the "seed of the woman" who defeats Satan (Rom 16:20, Rev 12:9)

**Fri: Assessment**
- Quiz #1: Creation and Fall (Gen 1-11)
- Preview next week: God chooses Abraham and makes a covenant

**Due:** Quiz #1

---

(Continue for each week, walking chronologically through Scripture)

## Assessment Schedule

| Date | Assessment | Content | Type |
|------|------------|---------|------|
| Week 2 | Quiz #1 | Genesis 1-11 | Written quiz |
| Week 6 | Timeline Project #1 | Creation to Exodus | Visual timeline |
| Week 12 | Unit Exam #1 | Genesis - Ruth | Written exam |
| ... | ... | ... | ... |
```

## Guidelines

- **Emphasize the arc, not just the facts**: Students should see how each book fits into the larger story.
- **Use visuals constantly**: Timelines and maps are essential. Post a large timeline in the classroom and add to it each week.
- **Make Christological connections explicit**: Don't assume students will see how OT points to Jesus. Teach typology (Adam/Christ, Passover/Cross, Temple/Jesus, etc.).
- **Don't skip the "boring" parts**: Leviticus, genealogies, and minor prophets have a place in the story. Explain why they matter.
- **Tell the story, then analyze it**: First let students hear the narrative, then discuss themes, theology, and application.
- **Pace for comprehension, not just coverage**: It's better to cover 75% of the OT well than rush through 100% superficially.
- **Connect to students' lives**: Every week, ask "How does this part of God's story intersect with your story?"

## Narrative Tools

### Timeline
- Large visual timeline posted in classroom (can be butcher paper, poster board, or digital display)
- Mark major events, characters, and books as you progress
- Color-code by era (Patriarchs, Exodus, Kingdom, Exile, etc.)
- Include dates (even if approximate) to give historical context

### Maps
- Ancient Near East (for OT survey)
- Israel and surrounding nations (for Kingdom period)
- Roman Empire (for NT survey)
- Paul's missionary journeys (for Acts and Epistles)
- Use physical maps or digital tools (BibleProject, Visual Unit, etc.)

### Character Tracker
- Create a running list of major characters and their role in the story
- Update weekly as new characters are introduced
- Include: Name, Time Period, Role in God's Plan, Christological Connection

### Theme Tracker
- Track how major themes develop across Scripture:
  - **Covenant**: God's promises to His people (Abrahamic, Mosaic, Davidic, New)
  - **Temple**: God's dwelling with His people (Tabernacle, Temple, Jesus, Church, New Jerusalem)
  - **Sacrifice**: Atonement for sin (Levitical system, Jesus' death)
  - **Kingship**: God's rule through human representatives (Judges, Kings, Jesus)
  - **Exile and Return**: God's people scattered and regathered (Babylon, Diaspora, Final Return)

### Christological Connections Chart
- For each major OT passage, identify how it points to Christ:
  - **Typology**: OT persons, events, or institutions that prefigure Christ (Adam, Passover, Temple, David)
  - **Prophecy**: Direct predictions of the Messiah (Isa 53, Mic 5:2, etc.)
  - **Fulfillment**: How NT shows Jesus fulfilling OT patterns (Matt constantly cites "to fulfill what was spoken")
