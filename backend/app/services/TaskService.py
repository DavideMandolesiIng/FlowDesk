from backend.app.models.Task import Task, Priority, Status
from datetime import date


class TaskService:
    def __init__(self) -> None:
        pass
    
    def filterByPriority(self, tasks: list[Task], priority: Priority) -> list[Task]:
        return [t for t in tasks if t.priority==priority]
    
    def filterByStatus(self, tasks:list[Task], status:Status) -> list[Task]:
        return [t for t in tasks if t.status==status]

    def groupTaskByDueDate(self, tasks: list[Task]) -> dict[date,list[Task]]:
        result = dict()
        for t in tasks:
            if not (t.dueDate in result):
                #create new list
                result[t.dueDate]=[t]
            else:
                #add this task to the existing list
                result[t.dueDate].append(t)

        return result