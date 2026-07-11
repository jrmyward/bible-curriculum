#!/usr/bin/env python3
"""One-time OAuth for the Google Classroom API (path B). Reads credentials.json
(a Desktop OAuth client from Google Cloud — see README step B), runs the consent
flow in a browser, and saves token.json (gitignored) for the other API scripts."""
import pathlib
from google_auth_oauthlib.flow import InstalledAppFlow

HERE = pathlib.Path(__file__).parent
SCOPES = [
    "https://www.googleapis.com/auth/classroom.courses",             # create/manage the class
    "https://www.googleapis.com/auth/classroom.topics",              # unit topics
    "https://www.googleapis.com/auth/classroom.courseworkmaterials", # materials (Start Here, Readings)
    "https://www.googleapis.com/auth/classroom.coursework.students", # assignments (reflection, test)
    "https://www.googleapis.com/auth/drive",                         # organize Drive to mirror Classroom (rename/move the Classroom-made folder)
    "https://www.googleapis.com/auth/forms.body",                    # create/edit Google Form quizzes (chapter tests) — see build_form.py
]

def main():
    creds_path = HERE / "credentials.json"
    if not creds_path.exists():
        raise SystemExit("Missing credentials.json — see README step B.4 (Desktop OAuth client).")
    flow = InstalledAppFlow.from_client_secrets_file(str(creds_path), SCOPES)
    creds = flow.run_local_server(port=0)
    (HERE / "token.json").write_text(creds.to_json())
    print("Saved token.json. You can now run create_class_api.py.")

if __name__ == "__main__":
    main()
