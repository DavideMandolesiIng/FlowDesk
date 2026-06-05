from dataclasses import dataclass,field
from datetime import datetime

@dataclass
class Note:
    '''This class models a note taken by the user. It could be a reminder, an annotation
      or any other detail worthy of being written down.'''
    
    # class atributes with type hinting included in the constructor __init__ as arguments
    # by the @dataclass decorator
    title: str
    body: str = ""
    tags: list[str] = field(default_factory=list[str])

    # Dynamic starting value, shouldn't be included in the __init__ as an agument
    # populated by the default_factory for every class instance
    updatedAt: datetime = field(init=False, default_factory=datetime.now)
    

    def updateTitle(self, newTitle: str) -> None:
        self.title = newTitle
        self.updateTimestamp()

    def updateBody(self, newBody: str) -> None:
        self.body = newBody
        self.updateTimestamp()

    def updateTags(self, newTags: list[str]) -> None:
        self.tags = newTags
        self.updateTimestamp()

    def updateTimestamp(self) -> None:
        self.updatedAt = datetime.now()


    def __str__(self) -> str:
        return (
            f"Note '{self.title}' "
            f"was last updated on {self.updatedAt}."
        )