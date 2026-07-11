# Google Classroom Automation — Runbook

Create + populate the Google Classroom class for **Bible 9 Foundations**, owned by the teacher
account **jward@waterspringsschool.net** (confirm exact domain). Two paths, by design:

- **A · Browser automation (now).** Drive the persistent watchable Chrome (`:9222`, the same one
  the Atlas tooling uses) to `classroom.google.com` and click through "Create class." Fastest, no
  Google Cloud setup. Requires the teacher to be **signed into that Chrome window** first.
- **B · Classroom API (long-term).** Official `classroom.googleapis.com` via OAuth. Robust and
  repeatable — the right tool for pushing unit topics and daily lessons as topics/coursework later.
  Needs a one-time Google Cloud setup (below).

Mapping we're building toward: **1 class = Bible 9 Foundations · Atlas unit → Classroom Topic ·
daily lesson → Classroom assignment/material** (due dates deferred until after Aug 1, 2026).
For now the scope is **just the class shell.**

## Status

- **Class shell created** (via path A, browser automation) on `jward@waterspringsschool.net`:
  - Name **Bible 9 Foundations** · Section **Grade 9**
  - Course id `ODU1NTEwMzM0MDA3` · class code `kegl4xsb`
  - Link: <https://classroom.google.com/c/ODU1NTEwMzM0MDA3>
- **Path B (API):** scripts scaffolded; awaiting the one-time Google Cloud setup below. When run,
  `create_class_api.py` will find this existing class (same name) and not duplicate it.
- **Next:** topics per Atlas unit, then coursework from the daily lessons (after those are authored
  and after dates unlock on Aug 1, 2026).

---

## A · Browser automation (do this now)

1. **Sign in.** In the watchable Chrome window, sign into `classroom.google.com` as
   `jward@waterspringsschool.net`. (`open_signin.py` navigates that window to the sign-in page.)
   First-time Classroom use will prompt for a role — choose **"I'm a Teacher."**
2. **Verify** the session: `python check_login.py` (reports the signed-in account; screenshots the
   Classroom home).
3. **Create the class:** `python create_class.py` (probes the live "Create class" dialog and fills
   Class name = "Bible 9 Foundations", Section = "Grade 9"). Written after login so the selectors
   match the real logged-in UI.

Run with the Atlas venv (Playwright is already installed there):
`_scripts/atlas/.venv/bin/python _scripts/classroom/<script>.py`

## B · Classroom API (one-time setup, then reusable)

**You do the Google Cloud steps once; the scripts handle the rest.**

1. **Google Cloud project.** At <https://console.cloud.google.com/> create (or pick) a project.
2. **Enable the API:** APIs & Services → Library → **Google Classroom API** → Enable.
3. **OAuth consent screen:** User type **Internal** (if waterspringsschool.net is a Workspace org)
   or External. App name e.g. "Foundations Classroom Automation." Add your account as a test user
   if External.
4. **Credentials:** Create Credentials → **OAuth client ID** → Application type **Desktop app** →
   download the JSON as `_scripts/classroom/credentials.json` (gitignored).
5. **Workspace admin note:** if the domain restricts third-party API access, an admin may need to
   trust this OAuth client (Admin console → Security → API controls).
6. **Install deps + authorize** (one-time browser consent, saves `token.json`, gitignored):

   ```bash
   python3 -m venv _scripts/classroom/.venv
   _scripts/classroom/.venv/bin/pip install -r _scripts/classroom/requirements.txt
   _scripts/classroom/.venv/bin/python _scripts/classroom/auth_api.py
   ```

7. **Create the class:**

   ```bash
   _scripts/classroom/.venv/bin/python _scripts/classroom/create_class_api.py \
     --name "Bible 9 Foundations" --section "Grade 9"
   ```

   Prints the new course id; record it here and in future scripts. Topic/coursework helpers build
   on the same `service` (see `create_class_api.py`).

### Scopes requested
`classroom.courses` (create/manage the class) · `classroom.topics` (unit topics later) ·
`classroom.coursework.students` (assignments later). Trim in `auth_api.py` if you want least
privilege for just the shell (`classroom.courses` alone is enough to create the class).

## Files
- `open_signin.py` — point the watchable Chrome at Google sign-in (path A).
- `check_login.py` — report the signed-in Google account / Classroom state (read-only).
- `create_class.py` — browser-automation create-class (path A; added after login).
- `requirements.txt`, `auth_api.py`, `create_class_api.py` — path B (API).

## Security
`credentials.json`, `token.json`, `.venv/`, and `probe-output/` (screenshots may show the account)
are gitignored. Never commit them.
