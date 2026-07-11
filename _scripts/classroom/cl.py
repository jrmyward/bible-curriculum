"""Shared Google Classroom API helpers (path B). Reads token.json from auth_api.py."""
import pathlib
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

HERE = pathlib.Path(__file__).parent
COURSE_NAME = "Bible 9 Foundations"

def service():
    return build("classroom", "v1",
                 credentials=Credentials.from_authorized_user_file(str(HERE / "token.json")))

def course_id(svc, name=COURSE_NAME):
    for c in svc.courses().list(teacherId="me").execute().get("courses", []):
        if c.get("name") == name:
            return c["id"]
    raise SystemExit(f"course {name!r} not found")

def topics(svc, cid):
    """Return {topic_name: topicId} for the course."""
    out, tok = {}, None
    while True:
        r = svc.courses().topics().list(courseId=cid, pageToken=tok, pageSize=100).execute()
        for t in r.get("topic", []):
            out[t["name"]] = t["topicId"]
        tok = r.get("nextPageToken")
        if not tok:
            break
    return out

def existing_titles(svc, cid):
    """Titles of all courseWork + courseWorkMaterials (incl. drafts), to skip duplicates."""
    titles = set()
    r = svc.courses().courseWork().list(
        courseId=cid, courseWorkStates=["PUBLISHED", "DRAFT"], pageSize=100).execute()
    titles |= {w["title"] for w in r.get("courseWork", [])}
    r = svc.courses().courseWorkMaterials().list(
        courseId=cid, courseWorkMaterialStates=["PUBLISHED", "DRAFT"], pageSize=100).execute()
    titles |= {m["title"] for m in r.get("courseWorkMaterial", [])}
    return titles
