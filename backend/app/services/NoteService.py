from app.models.Note import Note

class NoteService:
    def __init__(self) -> None:
        pass

    def filterByTag(self, notes: list[Note], tag: str) -> list[Note]:
        return [n for n in notes if n.tags.__contains__(tag)]