#!/usr/bin/env python3
"""Turn a markdown handout into a Google Doc in the teacher's Drive, then attach it to
a Classroom topic as a Material (DRAFT by default). Reusable for any handout.

    create_doc_material.py --md <path> --topic "01: Introduction" \
        --title "Unit 1 · Study Guide" [--desc "..."] [--post]

Idempotent: skips if a courseWork/material with the same title already exists.
"""
import sys, pathlib
import markdown as md_lib
from googleapiclient.http import MediaInMemoryUpload
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import cl

def arg(flag, default=None):
    return sys.argv[sys.argv.index(flag) + 1] if flag in sys.argv else default

def make_doc(drive, name, md_text, parent=None):
    html = md_lib.markdown(md_text, extensions=["extra", "sane_lists"])
    html = f"<html><body>{html}</body></html>"
    media = MediaInMemoryUpload(html.encode("utf-8"), mimetype="text/html", resumable=False)
    body = {"name": name, "mimeType": "application/vnd.google-apps.document"}
    if parent:
        body["parents"] = [parent]
    f = drive.files().create(
        body=body, media_body=media, fields="id,webViewLink").execute()
    return f["id"], f.get("webViewLink")

def main():
    md_path = arg("--md"); topic = arg("--topic"); title = arg("--title")
    desc = arg("--desc", ""); post = "--post" in sys.argv
    if not (md_path and topic and title):
        print("need --md, --topic, --title"); sys.exit(1)

    svc = cl.service(); cid = cl.course_id(svc); tid = cl.topics(svc, cid)[topic]
    if title in cl.existing_titles(svc, cid):
        print(f"skip (exists): {title}"); return

    drive = cl.drive_service()
    unit_folder = cl.ensure_folder(drive, topic, cl.teacher_folder(svc, cid))  # Classroom/<course>/<unit>/
    file_id, link = make_doc(drive, title, pathlib.Path(md_path).read_text(), parent=unit_folder)
    print(f"created Google Doc in unit folder: {title}  ({link})")

    body = {
        "title": title, "description": desc,
        "state": "PUBLISHED" if post else "DRAFT", "topicId": tid,
        "materials": [{"driveFile": {"driveFile": {"id": file_id}, "shareMode": "VIEW"}}],
    }
    m = svc.courses().courseWorkMaterials().create(courseId=cid, body=body).execute()
    print(f"attached material: {title}  (id={m.get('id')}, state={m.get('state')})")

if __name__ == "__main__":
    main()
