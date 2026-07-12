#!/usr/bin/env python3
"""Build Unit 02's text materials as DRAFTS under the '02: What the Bible Is and Isn't'
topic. Idempotent (skips existing titles).

    _scripts/classroom/.venv/bin/python _scripts/classroom/build_unit02.py

The graded work is built by dedicated scripts so it carries the right attachments:
  - "Video Questions — Chapter 2"  → build_doc_assignment.py (per-student Doc copy)
  - "Chapter 2 Test"               → build_form.py (Google Form quiz)
The Study Guide + Key Concepts references are Doc materials, added via create_doc_material.py.
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import cl

HERE = pathlib.Path(__file__).parent
TOPIC = "02: What the Bible Is and Isn't"
# (kind, title, description-file, points)
ITEMS = [
    ("material", "Unit 2 · Start Here: What the Bible Is and Isn't", "content/unit02/start-here.txt", None),
    ("material", "Unit 2 · Readings",                                 "content/unit02/readings.txt",   None),
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
