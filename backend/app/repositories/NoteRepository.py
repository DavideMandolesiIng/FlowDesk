from pathlib import Path
from dataclasses import asdict
from app.repositories.BaseRepository import BaseRepository
from app.models.Note import Note
from datetime import datetime

class NoteRepository(BaseRepository):
    def __init__(self) -> None:
        super().__init__(Path("backend/data/notes.json"))

    def _toNote(self, d: dict) -> Note:
        '''dict -> Note, reconverts a json formatted dict into a Note obj'''
        n = Note(
            title= d["title"],
            body=d["body"],
            tags=d["tags"]
        )
        # populate attributes that have (init=False)
        object.__setattr__(n,"updatedAt", datetime.fromisoformat(d["updatedAt"]))

        return n
    
    #---------------------
    # ------- CRUD -------
    # --------------------
    def findAll(self) -> list[Note]:
        return [self._toNote(d) for d in self._readAll()]
    
    def save(self, note:Note) -> None:
        data=self._readAll()
        data.append(asdict(note))
        self._writeAll(data)

    def delete(self, title:str) -> None:
        data=[d for d in self._readAll() if d["title"]!=title]
        self._writeAll(data)
        
