# Restructure Summary — Understanding the Faith

**Date:** April 22, 2026  
**Purpose:** Transition to year-stamped lesson plan directories for better archival and year-over-year workflow

---

## What Changed

### **Before (Flat Structure)**

```
classes/understanding-the-faith/
├── teaching-map.md
└── lesson-plans/
    ├── week-01-lesson-plans.md
    ├── week-02-lesson-plans.md
    ├── handouts/
    │   ├── week-01/
    │   └── week-02/
    ├── substitute-plans/
    └── assessments/
```

### **After (Year-Stamped, Nested by Week)**

```
classes/understanding-the-faith/
├── teaching-maps/
│   └── teaching-map-2026-27.md
├── teaching-map.md (symlink → teaching-maps/teaching-map-2026-27.md)
└── lesson-plans-2026-27/
    ├── .generation-log.md
    ├── README.md
    ├── week-01-aug-24/
    │   ├── README.md
    │   ├── lesson-plans.md
    │   ├── handouts/
    │   │   ├── core-reading-guide-ch01.md
    │   │   ├── note-catcher-ch01.md
    │   │   └── [...]
    │   └── substitute-plan-friday.md (if applicable)
    ├── week-02-aug-31/
    ├── [... through week-39-may-17]
    └── assessments/
        ├── capstone-01-rubric.md
        └── [...]
```

---

## Key Changes

### 1. **Year-Stamped Directories**

- **Teaching maps:** Now in `teaching-maps/teaching-map-YYYY-YY.md`
- **Lesson plans:** Now in `lesson-plans-YYYY-YY/`
- **Symlink:** `teaching-map.md` points to current year for backwards compatibility

### 2. **Week-Based Organization**

- Each week gets its own directory: `week-XX-mon-day/` (e.g., `week-01-aug-24/`)
- Week directory names include the Monday date for easy reference
- Everything for the week lives in one place:
  - `lesson-plans.md` — All 5 days in one file
  - `handouts/` — All handouts for the week
  - `substitute-plan-<day>.md` — Sub plan if applicable
  - `README.md` — Week overview and post-teaching notes

### 3. **Generation Tracking**

- `.generation-log.md` tracks how each week was created (generated, copied, regenerated, edited)
- Each week's README has a "Post-Week Notes" section for reflection after teaching

### 4. **Assessments**

- Moved to `lesson-plans-YYYY-YY/assessments/`
- Still separate from weeks (since they span multiple weeks)

---

## Files Migrated

### **Week 1 (Aug 24–28, 2026)**

✅ **Migrated successfully**

- `week-01-lesson-plans.md` → `week-01-aug-24/lesson-plans.md`
- All handouts from `lesson-plans/chapter-1/` → `week-01-aug-24/handouts/`
- Created `week-01-aug-24/README.md` with week overview

---

## Skills Updated

All 6 lesson-planning skills have been updated to use the new structure:

1. **`/scaffold-lesson-structure`** — Creates year-stamped directories
2. **`/generate-lesson-plans`** — Writes to `week-XX-<date>/` directories
3. **`/generate-handout`** — Writes to `week-XX-<date>/handouts/`
4. **`/generate-substitute-plan`** — Writes to `week-XX-<date>/substitute-plan-<day>.md`
5. **`/lesson-plan-workflow`** — Works with year-stamped structure
6. **`/new-school-year`** (NEW) — Copies lesson plans forward year-over-year

---

## Benefits of New Structure

### **For This Year (2026-27)**

1. **Localization**: Everything for Week 5 is in `week-05-sep-21/`
   - No jumping between folders to prep for a week
   - Print all handouts from one directory

2. **Week context**: Week README shows goals, assessments, notes at a glance

3. **Post-teaching reflection**: Document what worked/didn't work for next year

### **For Next Year (2027-28)**

1. **Copy forward**: Use `/new-school-year` to copy 2026-27 → 2027-28
   - Dates auto-update
   - Schedule changes flagged for regeneration
   - No starting from scratch

2. **Year-over-year comparison**: Compare Week 5 2026-27 vs. 2027-28 side-by-side

3. **Archival**: Entire 2026-27 directory can be archived after school year ends

---

## Next Steps

### **For Current Work (2026-27)**

1. Continue generating weeks using `/generate-lesson-plans <week-number>`
   - Files will be written to `lesson-plans-2026-27/week-XX-<date>/`

2. OR use the guided workflow: `/lesson-plan-workflow understanding-the-faith`
   - Automatically picks up where you left off (Week 1 is complete, start Week 2)

### **For Next Year (2027-28)**

1. Generate new teaching map: `/generate-map understanding-the-faith --year 2027-28`

2. Copy lessons forward: `/new-school-year understanding-the-faith --from 2026-27 --to 2027-28`
   - Copies all weeks, updates dates
   - Flags weeks where schedule changed
   - Offers to regenerate flagged weeks

3. Start teaching in August 2027 with minimal prep work

---

## Backwards Compatibility

- **Symlink maintained**: `teaching-map.md` → `teaching-maps/teaching-map-2026-27.md`
- Old file references in documentation still work (symlink redirects)
- Skills check for both old and new structure (auto-detect)

---

## Questions?

See the updated documentation:

- **Quick reference:** `/README-LESSON-PLANNING.md` (repo root)
- **Skills overview:** `/SKILLS-OVERVIEW.md` (repo root)
- **Individual skill docs:** Each `.skill.md` file has full documentation

---

**Restructure completed:** April 22, 2026  
**Ready for:** Week 2+ lesson plan generation
