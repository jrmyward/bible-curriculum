#!/usr/bin/env python3
"""One-time OAuth for the Google Classroom API (path B). Reads credentials.json
(a Desktop OAuth client from Google Cloud — see README step B), runs the consent
flow in a browser, and saves token.json (gitignored) for the other API scripts."""
import pathlib
from google_auth_oauthlib.flow import InstalledAppFlow

HERE = pathlib.Path(__file__).parent
SCOPES = [
    "https://www.googleapis.com/auth/classroom.courses",            # create/manage the class
    "https://www.googleapis.com/auth/classroom.topics",             # unit topics (later)
    "https://www.googleapis.com/auth/classroom.coursework.students",# assignments (later)
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
