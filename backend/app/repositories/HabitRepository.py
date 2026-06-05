from pathlib import Path
from dataclasses import asdict
from app.repositories.BaseRepository import BaseRepository
from app.models.Habit import Habit,Weekday
from datetime import date,timedelta

class HabitRepository(BaseRepository):
    def __init__(self) -> None:
        super().__init__(Path("backend/data/habits.json"))

    def _toHabit(self, d:dict) -> Habit:
        h = Habit(
            title=d["title"],
            frequency=[Weekday(w) for w in d["frequency"]]
            )
        object.__setattr__(h,"creationDate",date.fromisoformat(d["creationDate"]))
        object.__setattr__(h,"habitLog", [date.fromisoformat(day) for day in d["habitLog"]] )

        return h
    
    #---------------------
    # ------- CRUD -------
    # --------------------
    def findAll(self) -> list[Habit]:
        return [self._toHabit(d) for d in self._readAll()]
    
    def save(self, habit:Habit) -> None:
        data=self._readAll()
        data.append(asdict(habit))
        self._writeAll(data)

    def delete(self, title:str) -> None:
        data=[d for d in self._readAll() if d["title"]!=title]
        self._writeAll(data)