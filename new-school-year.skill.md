---
name: new-school-year
description: Copy lesson plans forward to a new school year with updated dates
args: "<class-name> --from YYYY-YY --to YYYY-YY"
---

# New School Year

Copy lesson plans from a previous school year to a new school year, updating dates and flagging schedule changes.

## Usage

```
/new-school-year <class-name> --from <previous-year> --to <new-year>
```

**Examples:**
```
/new-school-year understanding-the-faith --from 2026-27 --to 2027-28
/new-school-year worldview --from 2027-28 --to 2028-29
```

## Process

### 1. **Validate Inputs**

- Check that `classes/<class-name>/` exists
- Verify `--from` year has lesson plans: `lesson-plans-<from-year>/` exists
- Verify `--to` year doesn't already have lesson plans (or ask to overwrite)
- Check that both teaching maps exist:
  - `teaching-maps/teaching-map-<from-year>.md`
  - `teaching-maps/teaching-map-<to-year>.md` (if not, offer to generate it first)

### 2. **Generate New Teaching Map** (if needed)

If teaching map for new year doesn't exist:

```
Teaching map for <to-year> not found.

Would you like me to generate it now using /generate-map? (yes/no)
```

If yes, run `/generate-map <class-name>` and ensure it uses the new year's school calendar.

### 3. **Compare Teaching Maps**

Read both teaching maps and compare week-by-week:

- Week count (same or different?)
- Week dates (how much do dates shift?)
- Schedule changes (5-day week → 4-day week, new no-school days, etc.)
- Assessment placement (do Capstones fall on the same weeks?)

Create a diff report:

```markdown
## Teaching Map Comparison: 2026-27 vs. 2027-28

| Week | 2026-27 Dates | 2027-28 Dates | Days | Schedule Changes |
|------|---------------|---------------|------|------------------|
| 1 | Aug 24–28 | Aug 23–27 | 5 → 5 | None |
| 2 | Aug 31–Sep 2 | Aug 30–Sep 3 | 3 → 4 | ⚠️ Fri added (was Teacher Work Day) |
| 5 | Sep 21–25 | Sep 20–24 | 5 → 5 | None |
| [...]
```

Identify weeks needing regeneration:
- ⚠️ **Schedule change**: Number of days changed
- ⚠️ **Content shift**: Different chapter assigned to this week
- ⚠️ **Assessment moved**: Capstone/major assessment shifted to different week

### 4. **Create New Directory Structure**

Create `lesson-plans-<to-year>/` with subdirectories for all weeks:

```
lesson-plans-2027-28/
├── .generation-log.md (new, empty)
├── README.md (copied and updated)
├── week-01-aug-23/ (new dates)
│   ├── README.md (stub)
│   └── handouts/ (empty)
├── week-02-aug-30/
└── [...]
```

### 5. **Copy Lesson Plans Week-by-Week**

For each week:

**If no schedule changes detected:**

1. Copy entire week directory:
   ```
   lesson-plans-2026-27/week-01-aug-24/
     ↓
   lesson-plans-2027-28/week-01-aug-23/
   ```

2. Update dates in copied files:
   - `README.md`: Update week dates (Aug 24–28, 2026 → Aug 23–27, 2027)
   - `lesson-plans.md`: Update day-of-week dates (Monday, Aug 24 → Monday, Aug 23)
   - All handouts: Update any date references

3. Mark in generation log:
   ```markdown
   | 1 | Aug 23–27 | 📋 Copied from 2026-27 (Aug 24 → Aug 23) | 2027-05-15 | No changes |
   ```

**If schedule changes detected:**

1. Create stub README only (don't copy lesson plans)
2. Mark in generation log:
   ```markdown
   | 2 | Aug 30–Sep 3 | ⚠️ NEEDS REGENERATION | 2027-05-15 | Schedule changed: 3 days → 4 days |
   ```

3. Add to "Needs Regeneration" list

### 6. **Update Date References**

For all copied files, use regex/find-replace to update:

- **Year references**: `2026` → `2027`, `2026-27` → `2027-28`
- **Day-of-week + date**: `Monday, Aug 24` → `Monday, Aug 23` (based on teaching map)
- **Due dates**: `Due Tuesday, Sep 1` → `Due Tuesday, Aug 31` (verify day-of-week matches)
- **Month/day only**: `Aug 24–28` → `Aug 23–27`

**Special cases to watch:**

- Dates in markdown tables
- Dates in handout headers
- Due dates in assignment prompts
- Holiday references ("Before Thanksgiving") — verify these are still accurate

### 7. **Validate Date Updates**

For a sample of copied weeks (e.g., Weeks 1, 10, 20, 30), verify:

- Monday's date in lesson plan matches teaching map
- Friday's date matches teaching map
- Day-of-week is correct (Monday Aug 24, 2026 was actually a Sunday — teaching maps should be correct, but verify)

Spot-check method: Pick 3-5 dates and verify with a calendar API or manually.

### 8. **Generate Summary Report**

Create `lesson-plans-<to-year>/.copy-forward-report.md`:

```markdown
# Copy Forward Report: <from-year> → <to-year>

**Generated:** [Date]  
**Class:** [Class name]

---

## Summary

- **Total weeks:** XX
- **Weeks copied:** XX
- **Weeks needing regeneration:** X

---

## Weeks Copied Successfully

| Week | From | To | Notes |
|------|------|----|-------|
| 1 | Aug 24–28 | Aug 23–27 | Dates updated, no schedule changes |
| 3 | Sep 8–11 | Sep 7–10 | Dates updated, no schedule changes |
[...]

---

## Weeks Needing Regeneration

| Week | Reason | Recommendation |
|------|--------|----------------|
| 2 | Schedule changed: 3 days → 4 days | Use `/generate-lesson-plans 2` to rebuild |
| 12 | Capstone moved from Week 12 to Week 13 | Review pacing, regenerate if needed |
[...]

---

## Next Steps

1. **Review flagged weeks** and decide whether to regenerate or manually adjust
2. **Regenerate flagged weeks** using `/generate-lesson-plans <week-number>`
3. **Spot-check dates** in copied weeks (especially around holidays)
4. **Update assessments** if Capstone timing changed
5. **Review Week 1** to ensure course intro is still accurate

Use `/lesson-plan-workflow <class-name> --year <to-year>` to regenerate weeks interactively.
```

### 9. **Update Generation Log**

Fill in `.generation-log.md` for the new year:

```markdown
# Generation Log — 2027-28 Lesson Plans

This file tracks how each week's lesson plans were created.

**Legend:**
- 🆕 Generated from scratch
- 📋 Copied from previous year
- 🔄 Regenerated (after initial generation)
- ✏️ Manually edited

---

## Week-by-Week Log

| Week | Dates | Method | Date Generated | Notes |
|------|-------|--------|----------------|-------|
| 1 | Aug 23–27 | 📋 Copied from 2026-27 | 2027-05-15 | Dates updated automatically |
| 2 | Aug 30–Sep 3 | ⚠️ NEEDS REGENERATION | | Schedule changed: 3 → 4 days |
[...]
```

### 10. **Prompt for Next Steps**

Display summary and ask what to do with flagged weeks:

```
✅ Lesson plans copied from 2026-27 to 2027-28

Summary:
- XX weeks copied successfully
- X weeks flagged for regeneration

Weeks needing regeneration:
  Week 2: Schedule changed (3 → 4 days)
  Week 12: Capstone timing shifted
  [...]

Would you like to:
1. Regenerate flagged weeks now (interactive)
2. Skip regeneration (I'll do it manually later)
3. Review the copy-forward report first

Choice: [1/2/3]
```

**If choice 1 (Regenerate now):**

Run `/lesson-plan-workflow <class-name> --year <to-year> --only-flagged` to regenerate only the weeks marked as needing regeneration.

**If choice 2 (Skip):**

```
✅ Copy forward complete. 

Review the copy-forward report:
  lesson-plans-2027-28/.copy-forward-report.md

Regenerate weeks manually with:
  /generate-lesson-plans <week-number> --year 2027-28

Or use the workflow:
  /lesson-plan-workflow <class-name> --year 2027-28
```

**If choice 3 (Review first):**

Display the copy-forward report, then re-prompt with choices 1 and 2.

---

## Smart Date Updating Algorithm

### Challenge: Day-of-Week Changes

When copying forward, dates shift but day-of-week may change:

- 2026: Aug 24 is a Sunday
- 2027: Aug 24 is a Monday

But school weeks start on Monday, so:

- 2026 Week 1: Aug 24 (Mon)
- 2027 Week 1: Aug 23 (Mon)

**Solution:** Always reference the teaching map for the new year, which has already calculated correct week start/end dates.

### Find-Replace Strategy

1. **Parse teaching map for date mappings:**
   ```
   Week 1: 2026-27 (Aug 24–28) → 2027-28 (Aug 23–27)
   Week 2: 2026-27 (Aug 31–Sep 2) → 2027-28 (Aug 30–Sep 3)
   [...]
   ```

2. **Build replacement table:**
   ```
   "Aug 24–28, 2026" → "Aug 23–27, 2027"
   "Monday, Aug 24" → "Monday, Aug 23"
   "Tuesday, Aug 25" → "Tuesday, Aug 24"
   [...]
   ```

3. **Apply replacements** to all copied markdown files

4. **Verify with regex:** Find any remaining old year references:
   ```regex
   \b2026\b
   ```

   If found, review manually (may be intentional, e.g., "In 2026, we changed the approach...")

---

## Edge Cases

### 1. **Week count changes**

If 2026-27 had 39 weeks but 2027-28 has 40 weeks:

- Copy first 39 weeks
- Mark Week 40 as "New week — needs generation from scratch"

### 2. **Major curriculum changes**

If the teaching map shows a different chapter sequence (e.g., Ch 5-6 swapped with Ch 7-8):

- Flag all affected weeks for regeneration
- Note in copy-forward report: "Curriculum sequence changed — review Weeks 10-15"

### 3. **Handout references across weeks**

If Week 5 says "Review the handout from Week 3":

- This reference is still valid (Week 3 exists in new year)
- No update needed

If Week 5 says "Review the handout from Week 3 (Sep 14)":

- Update the date reference: "(Sep 14, 2026)" → "(Sep 13, 2027)"

### 4. **Post-week notes**

If Week 5 README has post-teaching notes from 2026-27:

- Preserve these notes in a section: `## Notes from 2026-27`
- Keep `## Post-Week Notes` section empty for new year

---

## Notes

- This skill assumes the new teaching map has already been generated with correct dates
- Copied lesson plans are backups, not originals — original 2026-27 files remain untouched
- If you want to update the new year mid-year (e.g., regenerate Week 5 in November), just run `/generate-lesson-plans 5 --year 2027-28`
- The copy-forward report is a reference document — it's not updated after initial copy (use `.generation-log.md` for ongoing tracking)
