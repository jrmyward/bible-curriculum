#!/usr/bin/env python3
"""Generate a Google Slides deck for each day's lesson plan. Slide 1 is a styled
"Start Slide" (Do Now / Objective / Agenda / Reminders, with a "today is ..." header)
that mimics the classroom start-slide template; the rest of the deck is one slide per
item in that day's "Slide-Deck Outline". The day .md file is the source of truth.

    _scripts/classroom/.venv/bin/python _scripts/classroom/build_slides.py \
        classes/foundations/lesson-plans-2026-27/week-01-aug-24/1-monday.md ...

Files each deck into Classroom/<course>/<unit>/Slides/ in Drive. Prints the edit links.
Requires the presentations scope (re-run auth_api.py) + the Slides API enabled.

NOTE: approximates the template's layout + accent colors, not its hand-lettered fonts.
Verify the first deck in the Slides UI.
"""
import argparse, pathlib, re, sys
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import cl
from googleapiclient.errors import HttpError

EMU = 914400  # per inch
TERRACOTTA = {"red": 0.85, "green": 0.53, "blue": 0.36}
DARK = {"red": 0.17, "green": 0.17, "blue": 0.17}
BORDER = {"red": 0.20, "green": 0.20, "blue": 0.20}


# ---------- parsing the day .md ----------

def strip_md(s):
    s = re.sub(r"\*\*(.+?)\*\*", r"\1", s)
    s = re.sub(r"\*(.+?)\*", r"\1", s)
    s = s.replace("`", "").strip()
    return s


def section(md, heading_contains):
    """Return the lines of the '## ...' section whose heading contains the substring."""
    lines = md.splitlines()
    out, capturing = [], False
    for ln in lines:
        if ln.startswith("## "):
            capturing = heading_contains.lower() in ln.lower()
            if capturing:
                out.append(ln)
            continue
        if capturing:
            out.append(ln)
    return "\n".join(out)


def parse_day(md):
    h1 = next((l[2:].strip() for l in md.splitlines() if l.startswith("# ")), "Lesson")
    cm = re.search(r"\*\*Chapter:\*\*\s*Ch\s*(\d+)", md)
    chapter = int(cm.group(1)) if cm else None
    start = section(md, "Start Slide")

    m = re.search(r"Today is\s+([A-Za-z]+)\s*·\s*([^*\n]+)", start)
    weekday = m.group(1).strip() if m else ""
    date = strip_md(m.group(2)).strip() if m else ""

    def field(name):
        mm = re.search(rf"^\*\*{name}\*\*\s*[—-]\s*(.+)$", start, re.MULTILINE)
        return strip_md(mm.group(1)) if mm else ""

    do_now, objective, reminders = field("Do Now"), field("Objective"), field("Reminders")

    agenda = []
    grab = False
    for ln in start.splitlines():
        if re.match(r"^\*\*Agenda\*\*", ln):
            grab = True
            continue
        if grab:
            mm = re.match(r"^\d+\.\s+(.*)$", ln.strip())
            if mm:
                agenda.append(strip_md(mm.group(1)))
            elif ln.strip() and not ln.startswith(" "):
                break

    # content slides from the Slide-Deck Outline
    outline_block = section(md, "Slide-Deck Outline")
    slides = []
    for ln in outline_block.splitlines():
        mm = re.match(r"^\d+\.\s+\*\*(.+?)\*\*\s*(?:[—-]\s*(.*))?$", ln.strip())
        if not mm:
            continue
        title = strip_md(mm.group(1))
        if title.lower().startswith("start slide"):
            continue  # slide 1 is the styled Start Slide, built separately
        bullets = [strip_md(b) for b in (mm.group(2) or "").split("·") if strip_md(b)]
        slides.append((title, bullets))

    return {"h1": h1, "chapter": chapter, "weekday": weekday, "date": date, "do_now": do_now,
            "objective": objective, "reminders": reminders, "agenda": agenda, "slides": slides}


# ---------- Slides request builders ----------

def _size_xf(x, y, w, h, page_id):
    return {"pageObjectId": page_id,
            "size": {"width": {"magnitude": w * EMU, "unit": "EMU"},
                     "height": {"magnitude": h * EMU, "unit": "EMU"}},
            "transform": {"scaleX": 1, "scaleY": 1, "translateX": x * EMU,
                          "translateY": y * EMU, "unit": "EMU"}}


def rect(page_id, oid, x, y, w, h, fill=None, weight=1.5):
    reqs = [{"createShape": {"objectId": oid, "shapeType": "RECTANGLE",
                             "elementProperties": _size_xf(x, y, w, h, page_id)}}]
    props, fields = {"outline": {"outlineFill": {"solidFill": {"color": {"rgbColor": BORDER}}},
                                 "weight": {"magnitude": weight, "unit": "PT"}, "dashStyle": "SOLID"}}, \
                    "outline.outlineFill.solidFill.color,outline.weight,outline.dashStyle"
    if fill is not None:
        props["shapeBackgroundFill"] = {"solidFill": {"color": {"rgbColor": fill}}}
        fields += ",shapeBackgroundFill.solidFill.color"
    reqs.append({"updateShapeProperties": {"objectId": oid, "shapeProperties": props, "fields": fields}})
    return reqs


def textbox(page_id, oid, x, y, w, h, text, size, bold=False, color=DARK,
            align="START", valign="TOP"):
    reqs = [{"createShape": {"objectId": oid, "shapeType": "TEXT_BOX",
                             "elementProperties": _size_xf(x, y, w, h, page_id)}}]
    reqs.append({"updateShapeProperties": {"objectId": oid,
        "shapeProperties": {"contentAlignment": valign}, "fields": "contentAlignment"}})
    if text:
        reqs.append({"insertText": {"objectId": oid, "text": text}})
        reqs.append({"updateTextStyle": {"objectId": oid,
            "style": {"fontSize": {"magnitude": size, "unit": "PT"}, "bold": bold,
                      "foregroundColor": {"opaqueColor": {"rgbColor": color}}},
            "textRange": {"type": "ALL"}, "fields": "fontSize,bold,foregroundColor"}})
        reqs.append({"updateParagraphStyle": {"objectId": oid,
            "style": {"alignment": align}, "textRange": {"type": "ALL"}, "fields": "alignment"}})
    return reqs


def zone(page_id, tag, label, body, x, y, w, h):
    """A bordered box + accent title chip text + body text."""
    reqs = rect(page_id, f"{tag}_box", x, y, w, h, fill={"red": 1, "green": 1, "blue": 1})
    reqs += textbox(page_id, f"{tag}_ttl", x + 0.15, y + 0.1, w - 0.3, 0.4,
                    label, 15, bold=True, color=TERRACOTTA)
    reqs += textbox(page_id, f"{tag}_bod", x + 0.15, y + 0.6, w - 0.3, h - 0.7,
                    body, 11, color=DARK)
    return reqs


def start_slide_requests(page_id, d):
    reqs = []
    # header
    reqs += textbox(page_id, "hdr_l", 0.4, 0.2, 5.6, 0.7,
                    f"today is {d['weekday'].upper()}", 26, bold=True, color=DARK, valign="MIDDLE")
    reqs += textbox(page_id, "hdr_r", 6.0, 0.2, 3.6, 0.7,
                    d["date"], 26, bold=True, color=TERRACOTTA, align="END", valign="MIDDLE")
    # zones: DO NOW (top-left), OBJECTIVE (top-mid), AGENDA (tall right), REMINDERS (bottom span)
    agenda = "\n".join(f"{i}. {a}" for i, a in enumerate(d["agenda"], 1))
    reqs += zone(page_id, "don", "DO NOW", d["do_now"], 0.4, 1.05, 2.9, 2.35)
    reqs += zone(page_id, "obj", "OBJECTIVE", d["objective"], 3.45, 1.05, 3.0, 2.35)
    reqs += zone(page_id, "agd", "AGENDA", agenda, 6.6, 1.05, 3.0, 4.15)
    reqs += zone(page_id, "rem", "REMINDERS", d["reminders"], 0.4, 3.55, 6.05, 1.65)
    return reqs


def content_slide(page_id, title_id, body_id, title, bullets):
    reqs = [{"createSlide": {"objectId": page_id,
        "slideLayoutReference": {"predefinedLayout": "TITLE_AND_BODY"},
        "placeholderIdMappings": [
            {"layoutPlaceholder": {"type": "TITLE", "index": 0}, "objectId": title_id},
            {"layoutPlaceholder": {"type": "BODY", "index": 0}, "objectId": body_id}]}}]
    reqs.append({"insertText": {"objectId": title_id, "text": title}})
    if bullets:
        reqs.append({"insertText": {"objectId": body_id, "text": "\n".join(bullets)}})
        reqs.append({"createParagraphBullets": {"objectId": body_id,
            "textRange": {"type": "ALL"}, "bulletPreset": "BULLET_DISC_CIRCLE_SQUARE"}})
    return reqs


# ---------- build one deck ----------

def unit_slides_folder(drive, topics_map, course_folder, chapter):
    """Resolve (or create) <NN: Topic>/Slides/ in Drive for the given chapter number."""
    prefix = f"{chapter:02d}:"
    topic_name = next((n for n in topics_map if n.startswith(prefix)), None)
    if not topic_name:
        return None
    unit = cl.ensure_folder(drive, topic_name, course_folder)
    return cl.ensure_folder(drive, "Slides", unit)


def build_deck(slides, drive, topics_map, course_folder, day_file):
    d = parse_day(pathlib.Path(day_file).read_text())
    ch = d["chapter"]
    title = f"Foundations Ch {ch if ch else '?'} · {strip_md(d['h1'])}"
    pres = slides.presentations().create(body={"title": title}).execute()
    pid = pres["presentationId"]
    default_slide = pres["slides"][0]["objectId"]

    reqs = [{"deleteObject": {"objectId": default_slide}}]
    reqs.append({"createSlide": {"objectId": "start", "slideLayoutReference": {"predefinedLayout": "BLANK"}}})
    reqs += start_slide_requests("start", d)
    for i, (t, bl) in enumerate(d["slides"]):
        reqs += content_slide(f"cslide{i:02d}", f"ctitle{i:02d}", f"cbody{i:02d}", t, bl)
    slides.presentations().batchUpdate(presentationId=pid, body={"requests": reqs}).execute()

    folder = unit_slides_folder(drive, topics_map, course_folder, ch) if ch else None
    if folder:
        cl.move_file(drive, pid, folder)
    return title, len(d["slides"]) + 1, f"https://docs.google.com/presentation/d/{pid}/edit"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("day_files", nargs="+")
    ap.add_argument("--course", default=None, help="repo class key (courses.json); default = config default")
    args = ap.parse_args()
    try:
        slides = cl.slides_service()
        svc = cl.service()
        drive = cl.drive_service()
        cid = cl.course_id(svc, args.course)
        topics_map = cl.topics(svc, cid)
        course_folder = cl.teacher_folder(svc, cid)
        for f in args.day_files:
            title, n, link = build_deck(slides, drive, topics_map, course_folder, f)
            print(f"built {n:2} slides: {title}\n            {link}")
        print("done.")
    except HttpError as e:
        if e.resp.status in (401, 403):
            raise SystemExit(f"{e}\n\nEnable the Google Slides API and re-run auth_api.py "
                             "to consent to the presentations scope.")
        raise


if __name__ == "__main__":
    main()
