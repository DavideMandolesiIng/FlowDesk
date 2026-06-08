from dataclasses import dataclass,field
from datetime import date,timedelta
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
    creationDate: date = field(init=False, default_factory=date.today)

    # "static" starting value, shouldn't be included in the __init__ as an argument, defaults to None
    habitLog: list[date] = field(init=False, default_factory=list[date])

    def updateHabitLog(self) -> None:
        # depending on implementation logic, today's date can be checked to be contained in frequency
        today = date.today()
        if self.frequency.__contains__(Weekday(today.weekday())) and (not self.habitLog.__contains__(today)):
            self.habitLog.append(today)

    def evaluateCurrentStreak(self) -> int:
        '''Returns the current streak for this habit.'''
        # Starting from today, the method iterate backwards through days.
        # It only updates the count if the current day is a habit day and appears in habitLog
        # Cycle (and count) stops at the first habit day missing in the habitLog

        isOnStreak=True
        streakCount=0
        d=date.today()

        while isOnStreak and d >= self.creationDate:
            if self.frequency.__contains__(Weekday(d.weekday())):
                #current day is a habit day
                if self.habitLog.__contains__(d):
                    streakCount+=1
                else:
                    isOnStreak=False
            #go to previous day
            d=d-timedelta(days=1)

        return streakCount
    
    def maxStreak(self) -> int:
        '''Returns the maximum streak for this habit's history.'''
        maxCount=0
        streakCount=0
        d=date.today()
        while d >= self.creationDate:
            if self.frequency.__contains__(Weekday(d.weekday())):
                #current day is a habit day
                if self.habitLog.__contains__(d):
                    streakCount+=1
                else:
                    streakCount=0
            maxCount=max(streakCount,maxCount)
            #go to previous day
            d=d-timedelta(days=1)

        return maxCount