#!/usr/bin/env python3
"""Create a course's unit Topics via the API. Topic names come from the class's Atlas unit
files' H1s (`# Rubicon Atlas — Unit NN: Title`) so they match the units exactly. Idempotent
(skips topics that already exist). Replaces the legacy Playwright create_topics.py.

    create_topics_api.py --course foundations [--dry-run]

Note: the Classroom API doesn't control topic display order; new courses may need a one-time
manual reorder in the UI (or leave as-is — items still file under the right topic).
"""
import argparse, glob, pathlib, re, sys
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import cl

REPO = pathlib.Path(__file__).resolve().parents[2]


def unit_topic_names(class_key):
    names = []
    for f in sorted(glob.glob(str(REPO / "classes" / class_key / "rubicon-atlas" / "unit-*.md"))):
        m = re.search(r"^#\s+Rubicon Atlas\s+[—-]\s+Unit\s+(\d+:\s*.+?)\s*$",
                      pathlib.Path(f).read_text(), re.M)
        if m:
            names.append(m.group(1).strip())
    return names  # ascending 01..NN


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--course", required=True, help="repo class key (also the classes/<key>/ folder)")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    names = unit_topic_names(args.course)
    if not names:
        raise SystemExit(f"no unit-*.md files found under classes/{args.course}/rubicon-atlas/")
    print(f"{len(names)} unit topic(s) from Atlas files:")
    if args.dry_run:
        for n in names:
            print("  would ensure:", n)
        return

    svc = cl.service()
    cid = cl.course_id(svc, args.course)
    existing = set(cl.topics(svc, cid))
    created = 0
    for name in names:
        if name in existing:
            print(f"  skip (exists): {name}")
            continue
        svc.courses().topics().create(courseId=cid, body={"name": name}).execute()
        created += 1
        print(f"  created: {name}")
    print(f"done. Created {created} this run.")


if __name__ == "__main__":
    main()
