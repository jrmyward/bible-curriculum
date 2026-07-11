"""Shared Google Classroom API helpers (path B). Reads token.json from auth_api.py."""
import pathlib
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

HERE = pathlib.Path(__file__).parent
COURSE_NAME = "Bible 9 Foundations"

def _creds():
    return Credentials.from_authorized_user_file(str(HERE / "token.json"))

def service():
    return build("classroom", "v1", credentials=_creds())

def drive_service():
    return build("drive", "v3", credentials=_creds())

def forms_service():
    # static_discovery=False: the Forms API isn't in the client library's baked-in
    # discovery cache, so fetch it at runtime.
    return build("forms", "v1", credentials=_creds(), static_discovery=False)

def slides_service():
    return build("slides", "v1", credentials=_creds(), static_discovery=False)

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

def teacher_folder(svc, cid):
    """Drive id of the Classroom-created course folder (Classroom/<Course Name>/)."""
    return svc.courses().get(id=cid).execute().get("teacherFolder", {}).get("id")

def ensure_folder(drive, name, parent):
    """Find (or create) a subfolder `name` under `parent`; return its id. Idempotent."""
    esc = name.replace("'", "\\'")
    q = ("mimeType='application/vnd.google-apps.folder' and trashed=false "
         f"and name='{esc}' and '{parent}' in parents")
    hit = drive.files().list(q=q, fields="files(id)").execute().get("files", [])
    if hit:
        return hit[0]["id"]
    return drive.files().create(
        body={"name": name, "mimeType": "application/vnd.google-apps.folder", "parents": [parent]},
        fields="id").execute()["id"]

def move_file(drive, file_id, new_parent):
    prev = ",".join(drive.files().get(fileId=file_id, fields="parents").execute().get("parents", []))
    drive.files().update(fileId=file_id, addParents=new_parent,
                         removeParents=prev, fields="id").execute()

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
