from dataclasses import dataclass,field
from datetime import date,datetime,timedelta
from enum import Enum

class Weekday(Enum):
    MON = 0
    TUE = 1
    WED = 2
    THU = 3
    FRI = 4
    SAT = 5
    SUN = 6

@dataclass
class Habit:
    '''This class models a habit the user wants to track throughout certain weekdays.'''

    # class atributes with type hinting included in the constructor __init__ as arguments
    # by the @dataclass decorator
    title: str
    frequency: list[Weekday]

    # Dynamic starting value, shouldn't be included in the __init__ as an agument
    # populated by the default_factory for every class instance
    createdAt: datetime = field(init=False, default_factory=datetime.now)

    # "static" starting value, shouldn't be included in the __init__ as an argument, defaults to None
    habitLog: list[datetime] = field(init=False, default_factory=list[datetime])

    def updateHabitLog(self) -> None:
        # depending on implementation logic, today's date can be checked to be contained in frequency
        now = datetime.now()
        if Weekday(now.weekday()) in self.frequency and not any(log.date() == now.date() for log in self.habitLog):
            self.habitLog.append(now)

    def evaluateCurrentStreak(self) -> int:
        '''Returns the current streak for this habit.'''
        # Starting from today, the method iterate backwards through days.
        # It only updates the count if the current day is a habit day and appears in habitLog
        # Cycle (and count) stops at the first habit day missing in the habitLog

        streakCount=0
        d=datetime.now()

        while d >= self.createdAt:
            if Weekday(d.weekday()) in self.frequency:
                if any(log.date() == d.date() for log in self.habitLog):
                    streakCount += 1
                else:
                    break

            d -= timedelta(days=1)

        return streakCount

    
    def maxStreak(self) -> int:
        '''Returns the maximum streak for this habit's history.'''
        maxCount = 0
        streakCount = 0
        d = datetime.now()

        while d >= self.createdAt:
            if Weekday(d.weekday()) in self.frequency:
                #current day is a habit day
                if any(log.date() == d.date() for log in self.habitLog):
                    streakCount += 1
                else:
                    streakCount=0
            maxCount=max(streakCount,maxCount)
            #go to previous day
            d-=timedelta(days=1)

        return maxCount