#!/usr/bin/env python3
"""Build a Chapter Test as a Google Form *quiz* from a JSON spec, then attach it to
the matching Classroom assignment (as a link, so Classroom offers "Import grades").

    _scripts/classroom/.venv/bin/python _scripts/classroom/build_form.py \
        --spec _scripts/classroom/content/unit01/chapter-1-test.form.json \
        [--desc _scripts/classroom/content/unit01/chapter-test.txt] \
        [--force]

What it does:
  1. Creates the Form, marks it a quiz, and adds every item with point values +
     correct answers (auto-graded: matching, multiple choice, true/false, fill-in;
     manually graded: short answer, essay).
  2. Files the Form into the unit's Drive folder (Classroom/<course>/<unit>/).
  3. Finds the Classroom assignment named by the spec ("Chapter 1 Test"). If it is a
     DRAFT stub, it is deleted and recreated with the Form attached as a link material
     (Classroom auto-detects Forms links and shows the grade-import control).

Requires the forms.body scope — re-run auth_api.py once after it was added, and enable
the Google Forms API in the Cloud project. Idempotent: skips if the assignment already
has a link material, unless --force.

NOTE: first run against Google should be verified in the Classroom/Forms UI (grade
import, question rendering). This script has not been round-tripped in this environment.
"""
import argparse, json, pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import cl
from googleapiclient.errors import HttpError

HERE = pathlib.Path(__file__).parent

CHOICE_TYPE = {"dropdown": "DROP_DOWN", "checkbox": "CHECKBOX", "radio": "RADIO"}


def load_spec(path):
    spec = json.loads(pathlib.Path(path).read_text())
    # Verify the point total matches the declared total — a cheap guard against drift.
    total = sum(q["points"] for s in spec["sections"] for q in s["questions"])
    declared = spec.get("totalPoints")
    if declared is not None and total != declared:
        raise SystemExit(f"point total mismatch: questions sum to {total}, spec says {declared}")
    print(f"spec ok: {total} points across "
          f"{sum(len(s['questions']) for s in spec['sections'])} questions")
    return spec, total


def question_item(q, matching_options):
    """Build a Forms `questionItem` body for one question in the spec."""
    grading = {"pointValue": q["points"]}
    if q["type"] in CHOICE_TYPE:
        options = matching_options if q.get("useMatchingOptions") else q["options"]
        question = {"choiceQuestion": {"type": CHOICE_TYPE[q["type"]],
                                       "options": [{"value": o} for o in options]}}
        grading["correctAnswers"] = {"answers": [{"value": c} for c in q["correct"]]}
    elif q["type"] == "short_text":
        question = {"textQuestion": {"paragraph": False}}
        grading["correctAnswers"] = {"answers": [{"value": c} for c in q["correct"]]}
    elif q["type"] == "paragraph":
        question = {"textQuestion": {"paragraph": True}}  # manually graded (no correctAnswers)
    else:
        raise SystemExit(f"unknown question type: {q['type']}")
    question["required"] = bool(q.get("required"))
    question["grading"] = grading
    return {"questionItem": {"question": question}}


def build_requests(spec):
    """Ordered list of createItem requests: a text header per section, then its questions."""
    reqs, idx = [], 0
    mopts = spec.get("matchingOptions", [])
    for s in spec["sections"]:
        reqs.append({"createItem": {
            "item": {"title": s["heading"], "description": s.get("instructions", ""), "textItem": {}},
            "location": {"index": idx}}})
        idx += 1
        for q in s["questions"]:
            reqs.append({"createItem": {
                "item": dict({"title": q["text"]}, **question_item(q, mopts)),
                "location": {"index": idx}}})
            idx += 1
    return reqs


def create_form(forms, spec):
    form = forms.forms().create(body={"info": {
        "title": spec["title"],
        "documentTitle": spec.get("documentTitle", spec["title"])}}).execute()
    fid = form["formId"]
    # Description + quiz mode must go through batchUpdate (create ignores them).
    forms.forms().batchUpdate(formId=fid, body={"requests": [
        {"updateFormInfo": {"info": {"description": spec.get("description", "")},
                            "updateMask": "description"}},
        {"updateSettings": {"settings": {"quizSettings": {"isQuiz": True}},
                            "updateMask": "quizSettings.isQuiz"}},
    ]}).execute()
    forms.forms().batchUpdate(formId=fid, body={"requests": build_requests(spec)}).execute()
    info = forms.forms().get(formId=fid).execute()
    return fid, info.get("responderUri", f"https://docs.google.com/forms/d/{fid}/viewform")


def file_into_unit_folder(drive, svc, cid, form_id, topic_name):
    try:
        course_folder = cl.teacher_folder(svc, cid)
        unit_folder = cl.ensure_folder(drive, topic_name, course_folder)
        cl.move_file(drive, form_id, unit_folder)
        print(f"filed Form into Drive: {topic_name}/")
    except HttpError as e:
        print(f"warning: could not move Form into the unit folder ({e}); it's in Drive root.")


def attach_assignment(svc, cid, spec, responder_uri, desc_text, force):
    title = spec["assignmentTitle"]
    tid = cl.topics(svc, cid)[spec["topic"]]
    existing = svc.courses().courseWork().list(
        courseId=cid, courseWorkStates=["PUBLISHED", "DRAFT"], pageSize=100).execute().get("courseWork", [])
    match = next((w for w in existing if w["title"] == title), None)
    if match:
        has_link = any("link" in m for m in match.get("materials", []))
        if has_link and not force:
            print(f"skip: assignment {title!r} already has a link material (use --force to rebuild)")
            return
        if match["state"] != "DRAFT" and not force:
            raise SystemExit(f"refusing to replace PUBLISHED assignment {title!r} without --force")
        svc.courses().courseWork().delete(courseId=cid, id=match["id"]).execute()
        print(f"deleted existing {match['state']} assignment {title!r} to reattach the Form")
    body = {
        "title": title,
        "description": desc_text,
        "state": "DRAFT",
        "topicId": tid,
        "workType": "ASSIGNMENT",
        "maxPoints": spec["totalPoints"],
        "materials": [{"link": {"url": responder_uri}}],
    }
    r = svc.courses().courseWork().create(courseId=cid, body=body).execute()
    print(f"created assignment {title!r} (id={r['id']}, state={r['state']}) with the Form attached")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--spec", required=True)
    ap.add_argument("--desc", help="text file for the assignment description")
    ap.add_argument("--course", default=None, help="repo class key (courses.json); default = config default")
    ap.add_argument("--force", action="store_true")
    args = ap.parse_args()

    spec, _ = load_spec(args.spec)
    desc_text = pathlib.Path(args.desc).read_text().rstrip("\n") if args.desc else spec.get("description", "")

    try:
        forms = cl.forms_service()
        svc = cl.service()
        drive = cl.drive_service()
        cid = cl.course_id(svc, args.course)

        fid, responder = create_form(forms, spec)
        print(f"created Form: {fid}\n  edit:   https://docs.google.com/forms/d/{fid}/edit\n  fill:   {responder}")
        file_into_unit_folder(drive, svc, cid, fid, spec["topic"])
        attach_assignment(svc, cid, spec, responder, desc_text, args.force)
        print("done.")
    except HttpError as e:
        if e.resp.status in (401, 403):
            raise SystemExit(
                f"{e}\n\nLikely missing scope/API. Enable the Google Forms API in the Cloud "
                "project, then re-run auth_api.py to consent to forms.body.")
        raise


if __name__ == "__main__":
    main()
