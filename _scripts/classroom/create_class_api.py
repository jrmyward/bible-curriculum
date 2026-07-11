#!/usr/bin/env python3
"""Create (or find) the Classroom course via the official API (path B).
Requires token.json from auth_api.py. Idempotent: skips if a course with the same
name already exists on this account (including one created via the browser path).

Usage:
    create_class_api.py [--name "Bible 9 Foundations"] [--section "Grade 9"]
"""
import sys, pathlib
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

HERE = pathlib.Path(__file__).parent

def arg(flag, default):
    return sys.argv[sys.argv.index(flag) + 1] if flag in sys.argv else default

def service():
    tok = HERE / "token.json"
    if not tok.exists():
        raise SystemExit("Missing token.json — run auth_api.py first.")
    return build("classroom", "v1", credentials=Credentials.from_authorized_user_file(str(tok)))

def main():
    name = arg("--name", "Bible 9 Foundations")
    section = arg("--section", "Grade 9")
    svc = service()
    existing = svc.courses().list(teacherId="me").execute().get("courses", [])
    for c in existing:
        if c.get("name") == name:
            print(f"EXISTS course id={c['id']} code={c.get('enrollmentCode')} {c.get('alternateLink')}")
            return
    course = svc.courses().create(
        body={"name": name, "section": section, "ownerId": "me", "courseState": "ACTIVE"}
    ).execute()
    print(f"CREATED course id={course['id']} code={course.get('enrollmentCode')} {course.get('alternateLink')}")

if __name__ == "__main__":
    main()
