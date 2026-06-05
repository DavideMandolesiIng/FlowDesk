from pathlib import Path
from dataclasses import asdict
from app.repositories.BaseRepository import BaseRepository
from app.models.Task import Task,Priority,Status
from datetime import date,datetime

class TaskRepository(BaseRepository):
    def __init__(self) -> None:
        super().__init__(Path("backend/data/tasks.json"))

    def _toTask(self, d: dict) -> Task:
        '''dict -> Task, reconverts a json formatted dict into a Task obj'''
        t = Task(
            title=d["title"],
            dueDate=date.fromisoformat(d["dueDate"]),
            description=d["description"],
            priority=Priority(d["priority"]),
            status=Status(d["status"])
        )
        # populate attributes that have (init=False)
        object.__setattr__(t,"creationDate", datetime.fromisoformat(d["creationDate"]))
        object.__setattr__(t,"completionDate", datetime.fromisoformat(d["completionDate"]) if d["completionDate"] else None)
        return t
    
    #---------------------
    # ------- CRUD -------
    # --------------------
    def findAll(self)->list[Task]:
        return [self._toTask(d) for d in self._readAll()]
    
    def save(self, task:Task) -> None:
        #get current state
        data=self._readAll()
        #add task you want to save (asdict returns the fields of a given @dataclass as dict)
        data.append(asdict(task))
        #actually save data
        self._writeAll(data)

    def delete(self, title:str) -> None:
        data=[d for d in self._readAll() if d["title"] != title]
        self._writeAll(data)
