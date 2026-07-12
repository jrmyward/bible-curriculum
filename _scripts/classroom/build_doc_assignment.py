#!/usr/bin/env python3
"""Turn a markdown worksheet into a Google Doc and attach it to a Classroom ASSIGNMENT
as a per-student copy (shareMode STUDENT_COPY) — each student gets their own editable
copy to fill in and submit. Reuses make_doc() from create_doc_material.py.

    build_doc_assignment.py --md <path> --topic "01: Introduction" \
        --title "Video Questions & Reflection — Chapter 1" --points 20 \
        [--desc <txt-file-or-literal>] [--replace "Old Title"] [--force]

Idempotent: skips if the assignment already has a Doc material, unless --force.
"""
import argparse, pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import cl
from create_doc_material import make_doc


def read_desc(val):
    if not val:
        return ""
    p = pathlib.Path(val)
    return p.read_text().rstrip("\n") if p.exists() else val


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--md", required=True)
    ap.add_argument("--topic", required=True)
    ap.add_argument("--title", required=True)
    ap.add_argument("--points", type=int, required=True)
    ap.add_argument("--desc", default="")
    ap.add_argument("--replace", help="title of an existing draft assignment to delete first")
    ap.add_argument("--course", default=None, help="repo class key (courses.json); default = config default")
    ap.add_argument("--force", action="store_true")
    a = ap.parse_args()

    svc = cl.service(); cid = cl.course_id(svc, a.course); tid = cl.topics(svc, cid)[a.topic]
    drive = cl.drive_service()

    work = svc.courses().courseWork().list(
        courseId=cid, courseWorkStates=["PUBLISHED", "DRAFT"], pageSize=100).execute().get("courseWork", [])
    same = next((w for w in work if w["title"] == a.title), None)
    if same and any("driveFile" in m for m in same.get("materials", [])) and not a.force:
        print(f"skip: assignment {a.title!r} already has a Doc material (use --force)")
        return

    to_delete = set(filter(None, [a.replace]))
    if same and a.force:
        to_delete.add(a.title)
    for tt in to_delete:
        t = next((w for w in work if w["title"] == tt), None)
        if not t:
            continue
        if t["state"] != "DRAFT" and not a.force:
            raise SystemExit(f"refusing to delete PUBLISHED assignment {tt!r} without --force")
        svc.courses().courseWork().delete(courseId=cid, id=t["id"]).execute()
        print(f"deleted existing {t['state']} assignment {tt!r}")

    unit_folder = cl.ensure_folder(drive, a.topic, cl.teacher_folder(svc, cid))
    file_id, link = make_doc(drive, a.title, pathlib.Path(a.md).read_text(), parent=unit_folder)
    print(f"created worksheet Doc: {a.title}  ({link})")

    body = {
        "title": a.title, "description": read_desc(a.desc),
        "state": "DRAFT", "topicId": tid,
        "workType": "ASSIGNMENT", "maxPoints": a.points,
        "materials": [{"driveFile": {"driveFile": {"id": file_id}, "shareMode": "STUDENT_COPY"}}],
    }
    r = svc.courses().courseWork().create(courseId=cid, body=body).execute()
    print(f"created assignment {a.title!r} (id={r['id']}, state={r['state']}) — worksheet as per-student copy")


if __name__ == "__main__":
    main()
