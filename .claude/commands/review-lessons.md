---
name: review-lessons
description: Audit lesson plans for completeness, alignment, and consistency
args: "[class-name] [--week week-number] [--year YYYY-YY]"
---

# Review Lessons

Audit existing lesson plans for completeness, teaching map alignment, and consistency issues.

## Usage

```bash
/review-lessons <class-name> [--week <week-number>] [--year YYYY-YY]
```

**Examples:**

```bash
/review-lessons understanding-the-faith
/review-lessons understanding-the-faith --week 5
/review-lessons understanding-the-faith --year 2026-27
```

## Modes

### Full Course Audit (no `--week` flag)

Reviews all generated lesson plans for a class and produces a summary report.

### Single Week Review (with `--week` flag)

Deep review of one week's lesson plans with specific feedback.

---

## Process

### 1. Validate Inputs

- Verify `classes/<class-name>/` exists
- Determine year from `--year` flag, directory structure, or current school year
- Read teaching map: `classes/<class-name>/teaching-maps/teaching-map-<year>.md`
- Scan `lesson-plans-<year>/` for generated weeks

### 2. Completeness Check

For each generated week (or the specified week), verify:

- [ ] `lesson-plans.md` exists and has content (not just a stub)
- [ ] All days in the week have lesson plans (account for no-school days)
- [ ] Each lesson has objectives, materials, and lesson flow sections
- [ ] Timing segments cover the full 45-minute period
- [ ] All referenced handouts exist in `handouts/`
- [ ] Substitute plan exists for days marked **SUB:** in teaching map
- [ ] `.generation-log.md` entry exists for this week

**Report format:**
```
Week X: [status]
  lesson-plans.md: [exists/missing/stub]
  Days covered: X/X
  Handouts: X referenced, X exist, X missing
  Sub plan: [exists/missing/not-needed]
  Generation log: [logged/not-logged]
```

### 3. Teaching Map Alignment

Compare each week's lesson plans against the teaching map:

- [ ] **Chapter match**: Lesson plans cover the chapter listed in the teaching map
- [ ] **Activities match**: All activities from teaching map appear in lesson plans
- [ ] **Assessments match**: Due dates and assessment types match teaching map
- [ ] **No-school days respected**: No lessons planned on days marked **NO SCHOOL**
- [ ] **Sub days respected**: Sub days use non-cohort activities

**Flag mismatches:**
```
⚠️ Week 5: Teaching map lists "Pair & Defend" but lesson plans have "Case Study" on Thursday
⚠️ Week 8: Discussion Brief #4 due Wednesday in teaching map, but Thursday in lesson plans
```

### 4. Timing Audit

For each lesson plan day:

- Parse timing segments (e.g., `[0-5 min]`, `[5-20 min]`)
- Verify segments are contiguous (no gaps)
- Verify total equals 45 minutes (or the configured period length)
- Flag over/under:

```
⚠️ Week 3, Monday: Timing adds to 40 min (5 min gap)
⚠️ Week 7, Thursday: Timing adds to 50 min (5 min over)
```

### 5. Handout Cross-Reference

For each week:

- Scan `lesson-plans.md` for handout file references (paths in backticks or `file:` annotations)
- Check that each referenced file exists in `handouts/`
- Check for orphaned handouts (files in `handouts/` not referenced by any lesson plan)

```
Week 5 handout audit:
  Referenced: 4 files
  ✅ core-reading-guide-ch03.md
  ✅ note-catcher-ch03.md
  ✅ discussion-brief-03-template.md
  ❌ video-note-catcher-reliability.md (MISSING)
  
  Orphaned: 1 file
  ⚠️ pair-and-defend-prep.md (not referenced in lesson plans)
```

### 6. Quality Spot-Check (single week only)

When reviewing a single week (`--week` flag), also check against `_shared/lesson-plan-standards.md`:

- Does each day follow the arc: hook → instruction → practice → synthesis?
- Are teacher scripts provided for key moments?
- Do activities match the stated objectives?
- Is cognitive load appropriate (not too many new concepts per day)?
- Are transitions between activities explicit?

### 7. Generate Report

**Full course audit** → write to `lesson-plans-<year>/.audit-report.md`:

```markdown
# Lesson Plan Audit — [Class Name] ([Year])

**Generated:** [Date]
**Weeks audited:** X of Y generated

---

## Summary

| Metric | Status |
|--------|--------|
| Weeks with lesson plans | X / Y |
| Weeks fully complete | X |
| Missing handouts | X |
| Timing issues | X |
| Teaching map mismatches | X |
| Sub plans complete | X / X needed |

---

## Issues by Priority

### Must Fix
- [Critical issues: missing files, wrong chapters, broken references]

### Should Fix
- [Timing gaps, missing handouts, alignment issues]

### Nice to Fix
- [Orphaned files, minor inconsistencies]

---

## Week-by-Week Status

| Week | Dates | Status | Issues |
|------|-------|--------|--------|
| 1 | Aug 24-28 | ✅ Complete | None |
| 2 | Aug 31-Sep 2 | ⚠️ Issues | Missing sub plan |
| 3 | Sep 8-11 | ❌ Not generated | — |
[...]
```

**Single week review** → display inline (don't write a file):

```
Review: Week 5 — Chapter 3 (Sep 21-25)

✅ Completeness: All 5 days covered, all handouts present
✅ Alignment: Matches teaching map activities and assessments
⚠️ Timing: Wednesday adds to 50 min (trim Pair & Defend debrief by 5 min)
✅ Handouts: 4/4 referenced files exist
✅ Sub plan: Not needed this week

Quality notes:
- Monday's hook is strong (opens with a provocative question)
- Thursday's Case Study could use a clearer transition from group work to presentations
- Friday exit ticket is good but consider adding a preview of next week's topic

Overall: Good to teach as-is. One timing fix recommended.
```

---

## Notes

- This command is read-only — it reports issues but does not fix them
- To fix issues, use `/generate-lesson-plans` (regenerate week) or edit manually
- The audit report is a snapshot — re-run after making changes to verify fixes
- Full course audits can take a moment for classes with many generated weeks
