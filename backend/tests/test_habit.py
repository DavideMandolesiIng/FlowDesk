import pytest
from datetime import date,datetime,timedelta
from app.models.Habit import Habit, Weekday

def testDefaultValues():
    h = Habit("",[])
    assert h.createdAt.date()==date.today()
    assert h.habitLog==[]

def testEmptyLog():
    h=Habit("",[])
    
    assert len(h.habitLog)==0

def testUpdateLogToday():
    today = datetime.now()
    h=Habit("",[Weekday(today.weekday())])
    h.updateHabitLog()
    
    assert any(log.date() == today.date() for log in h.habitLog)

def testUpdateLogTwice():
    today = date.today()
    h=Habit("",[Weekday(today.weekday())])

    h.updateHabitLog()
    h.updateHabitLog()

    assert len(h.habitLog)==1

def testEvaluateCurrentStreakOfLenght0():
    h = Habit("",[Weekday.MON])

    assert h.evaluateCurrentStreak()==0

def testEvaluateCurrentStreakOfLenght1():
    h=buildHabitAndLogOnModay()
    assert h.evaluateCurrentStreak()==1

def testEvaluateCurrentStreakStopsWhenMissing():
    h=buildHabitAndLogTwoMondaysAgo()
    h.frequency.append(Weekday.WED)
    #missing wednesday
    h.habitLog.append(findLastMonday())

    assert h.evaluateCurrentStreak()<2

def testEvaluetMaxStreak():
    h = buildHabitAndLogTwoMondaysAgo()
    h.frequency.append(Weekday.TUE)
    h.frequency.append(Weekday.WED)
    #log: Mon:V, Tue:V, Wed:x, Mon:V 
    h.habitLog.append(h.habitLog[0]+timedelta(days=1))

    h.habitLog.append(findLastMonday())

    assert h.maxStreak()==2



def findLastMonday() -> datetime:
    d = datetime.now()
    while d.weekday() != Weekday.MON.value:
        d -= timedelta(days=1)
    return d

def buildHabitAndLogOnModay() -> Habit:
    '''Builds a Habit last Monday. Log includes starting day'''
    d = findLastMonday()
    h = Habit("",[Weekday.MON])
    h.createdAt = d
    h.habitLog.append(d)

    return h

def buildHabitAndLogTwoMondaysAgo() -> Habit:
    '''Builds a Habit two Mondays ago. Log includes starting day'''
    d = findLastMonday()-timedelta(days=7)#two modays ago
    h = Habit("",[Weekday.MON])
    h.createdAt = d

    h.habitLog.append(d)
    
    return h
