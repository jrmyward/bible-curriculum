#!/usr/bin/env python3
"""Build Unit 01 coursework in Google Classroom via the API (path B), as DRAFTS under
the '01: Introduction' topic. Idempotent: skips items whose title already exists
(so the browser-made 'Start Here' material is left as-is, not duplicated).

    _scripts/classroom/.venv/bin/python _scripts/classroom/build_unit01.py
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import cl

HERE = pathlib.Path(__file__).parent
TOPIC = "01: Introduction"
# (kind, title, description-file, points)
# Only the two text materials live here. The graded work is built by dedicated scripts so it
# carries the right attachments:
#   - "Video Questions & Reflection — Chapter 1"  → build_doc_assignment.py (per-student Doc copy)
#   - "Chapter 1 Test"                            → build_form.py (Google Form quiz)
# The "Six Acts" reference is a Doc material, added via create_doc_material.py (see README recipes).
ITEMS = [
    ("material",   "Unit 1 · Start Here: Finding Direction", "content/unit01/start-here.txt",      None),
    ("material",   "Unit 1 · Readings",                       "content/unit01/readings.txt",        None),
]

def desc(rel):
    return (HERE / rel).read_text().rstrip("\n")

def main():
    svc = cl.service()
    cid = cl.course_id(svc)
    tid = cl.topics(svc, cid)[TOPIC]
    existing = cl.existing_titles(svc, cid)
    for kind, title, rel, points in ITEMS:
        if title in existing:
            print(f"skip (exists): {title}")
            continue
        body = {"title": title, "description": desc(rel), "state": "DRAFT", "topicId": tid}
        if kind == "material":
            r = svc.courses().courseWorkMaterials().create(courseId=cid, body=body).execute()
        else:
            body.update({"workType": "ASSIGNMENT", "maxPoints": points})
            r = svc.courses().courseWork().create(courseId=cid, body=body).execute()
        print(f"created {kind}: {title}  (id={r.get('id')}, state={r.get('state')})")
    print("done.")

if __name__ == "__main__":
    main()
