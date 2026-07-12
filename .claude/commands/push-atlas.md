---
name: push-atlas
description: Push a chapter's unit fields + daily lessons to Rubicon Atlas via Playwright
args: "<class-name> <chapter-number>"
---

# Push to Rubicon Atlas

Push a chapter's authored data models to **Rubicon Atlas** (`watersprings.rubiconatlas.org`) using
Playwright over a persistent, watchable Chrome. Fills the **unit's four free-text fields** and creates
+ fills the **daily lessons** (Madeline Hunter template).

## Usage

```bash
/push-atlas foundations 3
```

## Prerequisites

- ✅ Data models authored + reviewed: `classes/<class>/rubicon-atlas/unit-NN-*.md` and
  `classes/<class>/rubicon-atlas/lessons/chNN-lessons.md` (run `/build-atlas` first).
- ✅ Atlas session + persistent Chrome running (one-time setup below).
- ⚠️ **Playwright / live browser required — this cannot run headless.** The push drives a real Chrome
  the teacher can watch. Confirm the browser is up before running.

## One-time setup (per machine / expired session)

```bash
PY=_scripts/atlas/.venv/bin/python
$PY _scripts/atlas/auth.py "https://watersprings.rubiconatlas.org/"   # interactive login → .auth/state.json
_scripts/atlas/launch-browser.sh &                                     # persistent CDP Chrome on :9222
```

## Process

1. **Confirm the browser is running** (CDP :9222) and authenticated. If not, run the setup above.
2. **Resolve the unit id.** Atlas unit ids live in [`_scripts/atlas/config.yaml`](../../_scripts/atlas/config.yaml)
   (Foundations Ch 1 = 2224, Ch 2–18 = 2225–2241). For a new class/unit, create it with
   `create_unit.py` (Add New Unit form) and record the new `/unit-planner/<id>` id.
3. **Push the unit fields** — navigate the browser to the unit planner, then:
   ```bash
   $PY _scripts/atlas/fill_unit.py classes/<class>/rubicon-atlas/unit-NN-*.md
   ```
4. **Push the daily lessons** (creates missing lessons by title, inserts the default template, fills
   cells; idempotent-ish):
   ```bash
   $PY _scripts/atlas/lesson_fill.py classes/<class>/rubicon-atlas/lessons/chNN-lessons.md <unit_id>
   ```
5. **Watch + verify** in the Chrome window; spot-check a lesson's cells.

## Known limits (from the runbook)

- **Faith Learning Integration** is a Standards picker, not free text — `fill_unit.py` skips it; set
  it manually or solve the standards modal.
- **Dates** are parked until after Aug 1, 2026 (Atlas exposes 2026-27 week dates only then); target
  dates live in `config.yaml`.
- macOS clear is `Meta+A`; Froala table cells are set via JS (don't click them). Full details +
  selectors: [`_scripts/atlas/README.md`](../../_scripts/atlas/README.md).

## Reference

The **atlas runbook** [`_scripts/atlas/README.md`](../../_scripts/atlas/README.md) is authoritative for
architecture, scripts, selectors, and gotchas. Read it before pushing.
