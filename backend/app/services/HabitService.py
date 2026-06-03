from app.models.Habit import Habit
from datetime import date

class HabitService:
    def __init__(self) -> None:
        pass

    def findByDate(self, habits: list[Habit], day: date) -> list[Habit]:
        return [h for h in habits if h.frequency.__contains__(day.weekday())]