from app.models.Note import Note
from app.services.NoteService import NoteService

# --- fixtures ---

NOTES = [
    Note(title="Python basics",   body="...", tags=["python", "study"]),
    Note(title="FastAPI intro",   body="...", tags=["python", "backend"]),
    Note(title="React hooks",     body="...", tags=["typescript", "frontend"]),
    Note(title="Docker basics",   body="...", tags=["devops"]),
    Note(title="JWT auth",        body="...", tags=["backend", "security"]),
]

service = NoteService()

# --- filterByTag ---

def test_filterByTag_returns_correct_notes():
    result = service.filterByTag(NOTES, "python")
    assert all("python" in n.tags for n in result)
    assert len(result) == 2

def test_filterByTag_empty_list():
    assert service.filterByTag([], "python") == []

def test_filterByTag_no_match():
    result = service.filterByTag(NOTES, "rust")
    assert result == []

def test_filterByTag_single_match():
    result = service.filterByTag(NOTES, "security")
    assert len(result) == 1
    assert result[0].title == "JWT auth"