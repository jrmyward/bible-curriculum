# Atlas Automation — Runbook

Fill Rubicon Atlas (course **Bible 9 Foundations**, `watersprings.rubiconatlas.org`) from
repo data models, so Claude does the form entry instead of hand-typing 18 units and ~145
daily lessons.

Two things get pushed per chapter:

1. the **Unit's fields** (Unit Overview, Essential Questions, Objectives, Biblical Integration)
2. the **Unit's daily Lessons** (one Atlas lesson per instructional day, Madeline Hunter template)

The data models are the source of truth and are human-reviewable *before* anything touches
Atlas — Claude never invents content at fill time.

---

## Architecture

```text
Repo data models (authored + reviewed)                Atlas (via Playwright)
──────────────────────────────────────                ──────────────────────
classes/foundations/rubicon-atlas/
  unit-NN-*.md            ── fill_unit.py   ─────────▶ Unit fields
  lessons/chNN-lessons.md ── lesson_fill.py ─────────▶ Unit → daily Lessons
```

- **Persistent watchable Chrome** on CDP port 9222 (`launch-browser.sh`). It stays open the
  whole session; scripts attach over CDP (`session.py`), act, and detach — the window never
  closes between runs, so you watch every action.
- Auth: a one-time login is saved to `.auth/state.json` (gitignored). Cookies are injected into
  the CDP Chrome, so no re-login (5 of 13 cookies are enough to authenticate).
- venv + Playwright + Chromium are installed under `.venv/` (see `requirements.txt`).

## One-time setup

```bash
PY=_scripts/atlas/.venv/bin/python

# 1. Log in once (interactive) — saves the session:
$PY _scripts/atlas/auth.py "https://watersprings.rubiconatlas.org/"

# 2. Start the persistent Chrome (leave it running; log in if prompted):
_scripts/atlas/launch-browser.sh &
```

To re-auth an expired session, re-run `auth.py`. To inject the saved cookies into a running
CDP Chrome (skips re-login), see the snippet in git history / the `session.attach` pattern.

## Per-chapter workflow (what a fanout session does)

For each chapter NN:

1. **Repo lesson plan** — build `classes/foundations/lesson-plans-2026-27/chNN-lesson-plan.md`
   following the [ch01 exemplar](../../classes/foundations/lesson-plans-2026-27/ch01-lesson-plan.md):
   compress the publisher's 10 lessons into the ~8-day block, keep the activity rhythm, cite
   specific manual/ST/SM page numbers, humanize the prose.
2. **Author the two Atlas data files:**
   - `classes/foundations/rubicon-atlas/unit-NN-*.md` — the 5 fields (humanized). Faith Learning
     Integration stays as prose reference only (see gotchas).
   - `classes/foundations/rubicon-atlas/lessons/chNN-lessons.md` — one `## Day N - Title` section
     per day, `**Row Label:** content` lines mapping to the Madeline Hunter rows. Concise, with
     Modeling/Guided Practice detail on days that have them.
3. **Ensure the Unit exists in Atlas** and grab its unit id from the URL
   (`/develop/unit-planner/<unit_id>`). Ch 1 = `2224`. New units can be created via the
   "Add New Unit" form (not yet scripted).
4. **Push:**

   ```bash
   # unit fields — NOTE: browser must already be on the unit's planner page (see TODO)
   $PY _scripts/atlas/fill_unit.py classes/foundations/rubicon-atlas/unit-NN-*.md

   # daily lessons — creates missing lessons, inserts the template, fills cells
   $PY _scripts/atlas/lesson_fill.py classes/foundations/rubicon-atlas/lessons/chNN-lessons.md <unit_id>
   ```

   Both are idempotent-ish: `lesson_fill.py` skips lessons that already exist (matched by title)
   and re-fills them; re-running overwrites cells with the same content.

## Scripts

| Script | Purpose |
| --- | --- |
| `auth.py` | One-time interactive login → `.auth/state.json` |
| `launch-browser.sh` | Persistent watchable Chrome on CDP :9222 |
| `session.py` | `attach(p)` → (browser, context, page) over CDP |
| `probe.py` | Dump a page's DOM + screenshot + control cheat-sheet (for new selectors) |
| `create_unit.py` | Create a new Unit (Add New Unit form) + fill its 4 free-text fields from `unit-NN-*.md`; prints the new unit_id |
| `fill_unit.py` | Fill a unit's 4 free-text Froala fields from `unit-NN-*.md` (browser must be on the unit planner) |
| `lesson_fill.py` | Create + fill a chapter's daily lessons from `chNN-lessons.md` |

`create_unit.py` clicks "Add New Unit" from an anchor unit's planner, fills `#unit-form-input-name`
with the file's `Unit NN: Title`, leaves dates at the placeholder default and Draft unchecked
(matching Ch 1), saves, reads the new `/unit-planner/<id>` URL, then fills the 4 fields on that
page. Run it once per `unit-NN-*.md`.

## Gotchas (learned the hard way)

- **macOS clear = `Meta+A`, not `Control+A`.** Ctrl+A moves the cursor to line-start on Mac, so
  content accumulates instead of clearing (this doubled Unit Overview before the fix).
- **Free-text Froala fields:** click the field's `.unit-text-content` → wait for
  `.fr-element[contenteditable='true']` *scoped to that field's `.template-renderer-category`* →
  `Meta+A`, Delete → `keyboard.insert_text` → blur to autosave. Category-scope the selector so a
  still-open editor elsewhere can't steal the input.
- **Froala TABLE cells (lesson Details): do NOT click cells** — Froala's table popup toolbar
  overlays and blocks the next click. Instead set each row's 2nd-cell `textContent` via JS,
  dispatch an `input` event on `.fr-element`, then blur. This persists.
- **New lessons need the template inserted:** after creating a lesson, click
  **"Insert Default Template"** to get the daily Madeline Hunter table (it's the account default).
- **Markdown is stripped** — Atlas fields are plain text. Don't rely on `**bold**`/`*italic*`;
  the data models use `**` only as parser syntax. Avoid em-dashes; use en-dashes only for
  Scripture ranges (`Genesis 1–2`).
- **Faith Learning Integration and Standards are "Choose Standards" pickers, not text** —
  `fill_unit.py` skips Faith Learning Integration. Populating it means selecting from the school's
  standards set (unsolved; probe the standards modal or set manually).
- **Dates are parked until after Aug 1, 2026** — Atlas exposes 2026-27 week dates only then.
  `config.yaml` holds the target dates from the teaching map; re-run date-setting after Aug 1.

## Atlas map (URLs & selectors)

- Base: `https://watersprings.rubiconatlas.org`
- Unit planner (fields): `/develop/unit-planner/<unit_id>` — Ch 1 = `2224`
- Unit lessons list: `/develop/unit/<unit_id>/lessons`
- Add lesson: `/develop/unit/<unit_id>/lessons/add-new-lesson`
  (`#lesson-editor-form-title`, optional Lesson Date(s), `#lesson-editor-save-button`)
- Lesson editor: `/develop/lesson/<lesson_id>/view`
- Unit field block: `.template-renderer-category` (label + `.unit-text-content` Froala editor)
- Ch 1 lesson ids: 11149–11156 (Day 1–8)

## Status

- **All 18 units created + filled in Atlas** (fields 1/2/3/5). Unit ids in `config.yaml`:
  Ch 1 = 2224, Ch 2–18 = 2225–2241 (sequential).
- **Ch 1:** unit fields + all 8 daily lessons — done.
- **Daily lessons for Ch 2–18:** not started. Author `lessons/chNN-lessons.md` per chapter, then
  push with `lesson_fill.py <file> <unit_id>`.

## TODO

- Author + push daily lessons for Ch 2–18 (`lessons/chNN-lessons.md` → `lesson_fill.py`).
- Solve Faith Learning Integration (Standards picker) or confirm it's set manually.
- After Aug 1, 2026: set unit + lesson dates from `config.yaml` / the teaching map (all units
  currently sit on the placeholder Week 1 / Aug 2025 slot until dates are set).
- Note: `create_unit.py` now scripts "Add New Unit"; `fill_unit.py` still fills whatever page the
  browser is on, so navigate to the unit planner first if running it standalone.

## Security

`.auth/` (live session cookies), `.venv/`, and `probe-output/` are gitignored. Never commit them.
