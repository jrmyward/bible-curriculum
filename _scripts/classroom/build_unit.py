#!/usr/bin/env python3
"""Create a unit's text materials (Start Here, Readings, …) as DRAFTS under its topic,
for any course. Reads a per-unit materials.json manifest. Idempotent (skips existing titles).

    build_unit.py --course foundations --topic "02: What the Bible Is and Isn't" \
        --dir content/foundations/unit02

materials.json format:  [{"title": "...", "file": "start-here.txt"}, ...]
Graded work (video worksheet, chapter test) is built by build_doc_assignment.py / build_form.py.
Doc references (study guide, etc.) by create_doc_material.py.
"""
import argparse, json, pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import cl

HERE = pathlib.Path(__file__).parent


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--course", default=None, help="repo class key (courses.json); default = config default")
    ap.add_argument("--topic", required=True, help='exact Classroom topic name, e.g. "02: What the Bible Is and Isn\'t"')
    ap.add_argument("--dir", required=True, help="unit content dir holding materials.json + the txt files")
    args = ap.parse_args()

    unit_dir = pathlib.Path(args.dir)
    manifest = json.loads((unit_dir / "materials.json").read_text())

    svc = cl.service()
    cid = cl.course_id(svc, args.course)
    topics = cl.topics(svc, cid)
    if args.topic not in topics:
        raise SystemExit(f"topic {args.topic!r} not found in course (have {len(topics)} topics). "
                         "Provision it with create_topics_api.py.")
    tid = topics[args.topic]
    existing = cl.existing_titles(svc, cid)

    for item in manifest:
        title, fname = item["title"], item["file"]
        if title in existing:
            print(f"skip (exists): {title}")
            continue
        body = {"title": title, "description": (unit_dir / fname).read_text().rstrip("\n"),
                "state": "DRAFT", "topicId": tid}
        r = svc.courses().courseWorkMaterials().create(courseId=cid, body=body).execute()
        print(f"created material: {title}  (id={r.get('id')}, state={r.get('state')})")
    print("done.")


if __name__ == "__main__":
    main()
