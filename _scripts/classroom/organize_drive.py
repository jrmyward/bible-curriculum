#!/usr/bin/env python3
"""Mirror Classroom in Drive: inside the Classroom-created course folder, create one
subfolder per unit named exactly like the Classroom topics (01: … … 18: …). Idempotent.
(create_doc_material.py / build_slides.py already file new content into these folders; this
just ensures they all exist up front.)

    build_unit … ; then:
    _scripts/classroom/.venv/bin/python _scripts/classroom/organize_drive.py --course foundations
"""
import argparse, sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import cl

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--course", default=None, help="repo class key (courses.json); default = config default")
    args = ap.parse_args()

    svc = cl.service(); cid = cl.course_id(svc, args.course)
    drive = cl.drive_service()
    tf = cl.teacher_folder(svc, cid)
    if not tf:
        print("! no teacherFolder on the course"); sys.exit(1)
    print(f"course folder: {tf}")

    for name in sorted(cl.topics(svc, cid).keys()):
        cl.ensure_folder(drive, name, tf)
        print(f"  folder ready: {name}")
    print("done.")

if __name__ == "__main__":
    main()
