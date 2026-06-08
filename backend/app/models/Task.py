from datetime import datetime, date
from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

class Priority(Enum):
    '''Enum that represent the possible task priorities'''
    NORMAL = 0
    HIGH = 1
    URGENT = 2

class Status(Enum):
    '''Enum that represents the possible task statuses'''
    TODO = 0
    IN_PROGRESS = 1
    COMPLETED = 2

@dataclass
class Task:
    '''This class models a task in the user's task list. It represents an activity.'''

    # class atributes with type hinting included in the constructor __init__ as arguments
    # by the @dataclass decorator  
    title: str
    dueDate: date
    description: str = "No description"
    priority: Priority = Priority.NORMAL
    status: Status = Status.TODO

    # Dynamic starting value, shouldn't be included in the __init__ as an agument
    # populated by the default_factory for every class instance
    creationDate: datetime = field(init=False, default_factory=datetime.now)

    # "static" starting value, shouldn't be included in the __init__ as an argument, defaults to None
    completionDate: Optional[datetime] = field(init=False, default=None)
    

    def updateStatus(self, newStatus: Status) -> None:
        self.status = newStatus
        if newStatus == Status.COMPLETED:
            self.completionDate = datetime.now()

    def updatePriority(self, newPriority: Priority) -> None:
        self.priority=newPriority

    def __str__(self) -> str:
        '''should be readable by the user'''
        return (
            f"Task '{self.title}' "
            f"with priority '{self.priority.name}', "
            f"due to {self.dueDate}, "
            f"has status='{self.status.name}'."
        )