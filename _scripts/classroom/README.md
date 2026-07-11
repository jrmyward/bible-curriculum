# Google Classroom + Google Drive integration

Tooling that publishes the **Bible 9 Foundations** course into Google Classroom and mirrors it in
Google Drive, driven from this repo. Owner account: **jward@waterspringsschool.net**.

Everything runs through the **official Google APIs** (Classroom + Drive) via a single OAuth token.
An earlier browser-automation approach was used once to create the class and the 18 topics; those
scripts are kept as reference (see [Legacy](#legacy-browser-automation)) but coursework, handouts,
and Drive organization all go through the API now — it is deterministic and idempotent.

## Architecture

```
this repo (source of truth)                Google (via API, as jward@waterspringsschool.net)
──────────────────────────                 ─────────────────────────────────────────────────
classes/foundations/
  lesson-plans-2026-27/   ─┐
  rubicon-atlas/unit-*.md  ├─ (authored) ─▶ Classroom  Bible 9 Foundations
  handouts/*.md            ─┘                 ├─ 18 Topics  (= units, "01: Introduction" …)
_scripts/classroom/                           └─ per topic: Materials + Assignments (drafts)
  content/<unit>/*.txt  (item copy)
  cl.py + build/create scripts ───────────▶ Drive  Classroom/Bible 9 Foundations/
                                              └─ one subfolder per unit  ← handout Google Docs
```

**Mapping.** 1 Classroom class = the course · 1 Topic = 1 unit (chapter) · Materials/Assignments =
the unit's coursework · Drive mirrors it (a folder per unit holding that unit's Docs).

**Source-of-truth model.** The repo markdown is what we *generate from*. Handouts become **Google
Docs** in Drive (editable by the teacher, and what students download). Small edits happen in the
Doc; substantive/bulk changes happen in the repo markdown and are re-generated.

## Current state

- **Course:** Bible 9 Foundations · Section Grade 9 · course id `855510334007` ·
  class code `kegl4xsb` · <https://classroom.google.com/c/ODU1NTEwMzM0MDA3>
- **Topics:** 18, named exactly like the Atlas units (`01: Introduction` … `18: Conclusion`).
- **Unit 01 built** (all **drafts**, hidden from students until posted):
  - Materials: *Unit 1 · Start Here: Finding Direction*, *Unit 1 · Readings*, *Unit 1 · Study Guide*
    (an editable Google Doc, test-aligned to `TR 1.10A`)
  - Assignments: *Video Reflection — Chapter 1* (20 pts), *Chapter 1 Test* (87 pts)
- **Drive:** `Classroom/Bible 9 Foundations/` (Google-created course folder) now holds an
  `01: Introduction/` … `18: Conclusion/` subfolder each; the Ch 1 study-guide Doc lives in
  `01: Introduction/`. New handout Docs auto-file into their unit folder.
- **Dates:** deferred — Classroom exposes 2026-27 week dates only after Aug 1, 2026.

## Setup (one-time, already done)

Google Cloud project **Watersprings Teaching** (`watersprings-teaching`, in the
`waterspringsschool.net` org):

1. Enabled APIs: **Google Classroom API**, **Google Drive API**.
2. OAuth consent screen: **Internal** (Workspace org → no Google verification needed).
3. Credential: **OAuth client ID → Desktop app**, downloaded to `credentials.json` (gitignored).
4. Python env + authorization:

   ```bash
   python3 -m venv _scripts/classroom/.venv
   _scripts/classroom/.venv/bin/pip install -r _scripts/classroom/requirements.txt
   _scripts/classroom/.venv/bin/python _scripts/classroom/auth_api.py   # browser consent → token.json
   ```

Re-run `auth_api.py` whenever the scope list changes (it re-consents and overwrites `token.json`).

### Scopes (`auth_api.py`)
- `classroom.courses` — the class
- `classroom.topics` — unit topics
- `classroom.courseworkmaterials` — materials (Start Here, Readings, Study Guide)
- `classroom.coursework.students` — assignments (reflection, test)
- `drive` (full) — organize Drive into the Classroom-created course folder (the folder was made by
  Classroom, not this app, so `drive.file` can't reach it — full `drive` is required to add the
  unit subfolders and move Docs in)

## Scripts

Run everything with the venv: `_scripts/classroom/.venv/bin/python _scripts/classroom/<script>.py`

| Script | Purpose |
| --- | --- |
| `auth_api.py` | One-time OAuth consent (`credentials.json` → `token.json`). |
| `cl.py` | Shared helpers: `service()` / `drive_service()`, `course_id()`, `topics()`, `existing_titles()`, `teacher_folder()`, `ensure_folder()`, `move_file()`. |
| `create_class_api.py` | Create (or find) the course. Idempotent by name. |
| `build_unit01.py` | Create Unit 01's materials + assignments as drafts under `01: Introduction`. Idempotent (skips existing titles). The item list + points live at the top; `content/unit01/*.txt` holds the copy. |
| `create_doc_material.py` | `--md <file> --topic "<unit>" --title "<name>" [--desc …] [--post]`. Renders markdown → a **Google Doc** in the unit's Drive folder → attaches it to the topic as a material (draft by default). Reusable for any handout. |
| `organize_drive.py` | Create the per-unit Drive subfolders inside the course folder and move listed Docs into their unit folder. Idempotent. |

### Recipes

Add a handout (e.g. a study guide) — author `classes/foundations/handouts/<name>.md`, then:

```bash
_scripts/classroom/.venv/bin/python _scripts/classroom/create_doc_material.py \
  --md classes/foundations/handouts/ch01-study-guide.md \
  --topic "01: Introduction" --title "Unit 1 · Study Guide" \
  --desc "Downloadable study guide for the Chapter 1 Test."
```

Build a unit's coursework — copy `build_unit01.py`, edit the `ITEMS` list + `content/<unit>/`
copy, run it. (Generalizing this into one `build_unit.py` that reads a per-unit manifest is the
next step for the 02–18 rollout.)

## Legacy (browser automation)

Used once, over a persistent authenticated Chrome on CDP `:9222`, to create the class and the 18
topics before the API path existed. Kept for reference; not needed for ongoing work.

- `open_signin.py` — point the watchable Chrome at Google sign-in.
- `check_login.py` — report the signed-in account / Classroom state (read-only).
- `create_class.py` — create the class via the "Create class" UI.
- `create_topics.py` — create the 18 topics (reads names from the Atlas `unit-*.md` files).

These use the Atlas venv's Playwright: `_scripts/atlas/.venv/bin/python …`.

## Security

`credentials.json`, `token.json`, `.venv/`, and `probe-output/` (screenshots can show the account)
are gitignored — never commit them. The token grants access to the teacher's Google account; treat
it like a password.
