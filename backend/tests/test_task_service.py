from datetime import date
from app.models.Task import Task, Priority, Status
from app.services.TaskService import TaskService

# --- fixtures ---

def make_task(title: str, priority: Priority, status: Status, dueDate: date) -> Task:
    t = Task(title=title, dueDate=dueDate, priority=priority)
    t.updateStatus(status)
    return t

TASKS = [
    make_task("Task A", Priority.NORMAL,  Status.TODO,        date(2025, 6, 1)),
    make_task("Task B", Priority.HIGH,    Status.IN_PROGRESS, date(2025, 6, 1)),
    make_task("Task C", Priority.URGENT,  Status.COMPLETED,   date(2025, 6, 3)),
    make_task("Task D", Priority.HIGH,    Status.TODO,        date(2025, 6, 5)),
    make_task("Task E", Priority.NORMAL,  Status.COMPLETED,   date(2025, 6, 5)),
]

service = TaskService()

# --- filterByPriority ---

def test_filterByPriority_returns_correct_tasks():
    result = service.filterByPriority(TASKS, Priority.HIGH)
    assert all(t.priority == Priority.HIGH for t in result)
    assert len(result) == 2

def test_filterByPriority_empty_list():
    assert service.filterByPriority([], Priority.HIGH) == []

def test_filterByPriority_no_match():
    result = service.filterByPriority(TASKS, Priority.URGENT)
    assert len(result) == 1

# --- filterByStatus ---

def test_filterByStatus_returns_correct_tasks():
    result = service.filterByStatus(TASKS, Status.TODO)
    assert all(t.status == Status.TODO for t in result)
    assert len(result) == 2

def test_filterByStatus_empty_list():
    assert service.filterByStatus([], Status.TODO) == []

def test_filterByStatus_no_match():
    result = service.filterByStatus(TASKS, Status.IN_PROGRESS)
    assert len(result) == 1

# --- groupByDueDate ---

def test_groupByDueDate_groups_correctly():
    result = service.groupTaskByDueDate(TASKS)
    assert date(2025, 6, 1) in result
    assert len(result[date(2025, 6, 1)]) == 2
    assert len(result[date(2025, 6, 5)]) == 2

def test_groupByDueDate_empty_list():
    assert service.groupTaskByDueDate([]) == {}

def test_groupByDueDate_single_task():
    single = [make_task("Solo", Priority.NORMAL, Status.TODO, date(2025, 6, 10))]
    result = service.groupTaskByDueDate(single)
    assert len(result) == 1
    assert len(result[date(2025, 6, 10)]) == 1