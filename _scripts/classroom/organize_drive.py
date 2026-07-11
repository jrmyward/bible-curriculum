#!/usr/bin/env python3
"""Mirror Classroom in Drive: inside the Classroom-created course folder
(Classroom/Bible 9 Foundations/), create one subfolder per unit named exactly
like the Classroom topics (01: Introduction ... 18: Conclusion), and move any
existing unit handout Docs into their unit folder. Idempotent.

    _scripts/classroom/.venv/bin/python _scripts/classroom/organize_drive.py
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import cl

# Docs already created that should live in a unit folder: {doc_id: "topic name"}
PLACE = {"1q35VonwmqLMbThkCGPBUR1Z0NIXFrvAr2f_u21P36XE": "01: Introduction"}

def main():
    svc = cl.service(); cid = cl.course_id(svc)
    drive = cl.drive_service()
    tf = cl.teacher_folder(svc, cid)
    if not tf:
        print("! no teacherFolder on the course"); sys.exit(1)
    print(f"course folder (Classroom/Bible 9 Foundations): {tf}")

    folders = {}
    for name in sorted(cl.topics(svc, cid).keys()):
        fid = cl.ensure_folder(drive, name, tf)
        folders[name] = fid
        print(f"  folder ready: {name}")

    for doc_id, topic in PLACE.items():
        cl.move_file(drive, doc_id, folders[topic])
        print(f"  moved {doc_id} -> {topic}")
    print("done.")

if __name__ == "__main__":
    main()
