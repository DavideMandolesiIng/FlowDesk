from datetime import date
from app.models.Habit import Habit, Weekday
from app.services.HabitService import HabitService

# --- fixtures ---

def make_habit(title: str, frequency: list[Weekday]) -> Habit:
    return Habit(title=title, frequency=frequency)

# lunedì=0, mercoledì=2, venerdì=4
MON_WED_FRI = [Weekday.MON, Weekday.WED, Weekday.FRI]
# tutti i giorni
DAILY = [Weekday.MON, Weekday.TUE, Weekday.WED, Weekday.THU, Weekday.FRI, Weekday.SAT, Weekday.SUN]
# solo weekend
WEEKEND = [Weekday.SAT, Weekday.SUN]

HABITS = [
    make_habit("Study Python",  MON_WED_FRI),
    make_habit("Morning run",   DAILY),
    make_habit("Read a book",   WEEKEND),
    make_habit("Meditate",      MON_WED_FRI),
]

service = HabitService()

# --- findByDate ---

def test_findByDate_returns_habits_scheduled_for_that_day():
    monday = date(2025, 6, 2)   # lunedì
    result = service.findByDate(HABITS, monday)
    assert all(Weekday(monday.weekday()) in h.frequency for h in result)
    assert len(result) == 3     # Study Python, Morning run, Meditate

def test_findByDate_excludes_habits_not_scheduled():
    monday = date(2025, 6, 2)
    result = service.findByDate(HABITS, monday)
    titles = [h.title for h in result]
    assert "Read a book" not in titles

def test_findByDate_weekend_only_habit():
    saturday = date(2025, 5, 31)
    result = service.findByDate(HABITS, saturday)
    titles = [h.title for h in result]
    assert "Read a book" in titles
    assert "Study Python" not in titles

def test_findByDate_empty_list():
    assert service.findByDate([], date(2025, 6, 2)) == []

def test_findByDate_no_habits_scheduled():
    sunday = date(2025, 6, 1)
    only_weekday_habits = [make_habit("Work task", [Weekday.MON, Weekday.TUE])]
    result = service.findByDate(only_weekday_habits, sunday)
    assert result == []