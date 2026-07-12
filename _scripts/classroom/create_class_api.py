#!/usr/bin/env python3
"""Create (or find) a Classroom course via the API. Idempotent: skips if a course with the
same name already exists. Name/section come from courses.json via --course, or pass explicitly.

    create_class_api.py --course foundations
    create_class_api.py --name "Bible 10 Apologetics" --section "Grade 10-11"
"""
import argparse, pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import cl


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--course", default=None, help="repo class key (courses.json) → name + section")
    ap.add_argument("--name", default=None, help="override course name")
    ap.add_argument("--section", default=None, help="override section")
    args = ap.parse_args()

    if args.course and not args.name:
        cfg = cl.course_config(args.course)
        name, section = cfg["course_name"], cfg.get("section", "")
    else:
        name = args.name or cl.course_name(None)
        section = args.section or ""
    if not name:
        raise SystemExit("need --course (in courses.json) or --name")

    svc = cl.service()
    for c in svc.courses().list(teacherId="me").execute().get("courses", []):
        if c.get("name") == name:
            print(f"EXISTS course id={c['id']} code={c.get('enrollmentCode')} {c.get('alternateLink')}")
            return
    course = svc.courses().create(
        body={"name": name, "section": section, "ownerId": "me", "courseState": "ACTIVE"}
    ).execute()
    print(f"CREATED course id={course['id']} code={course.get('enrollmentCode')} {course.get('alternateLink')}")


if __name__ == "__main__":
    main()
