import pytest
from datetime import datetime, date,timedelta
from app.models.Task import Task, Status, Priority

def testDefaultValues():
    t=Task("",datetime.now()+timedelta(days=1))
    assert t.status==Status.TODO
    assert t.priority==Priority.NORMAL
    assert t.completedAt==None
    assert t.createdAt.date()==date.today()

def testUpdateStatusToInProgressDontUpdatesCompletionDate():
    t=Task("",datetime.now()+timedelta(days=1))
    t.updateStatus(Status.IN_PROGRESS)
    assert t.completedAt==None

def testUpdateStatusToCompleteUpdatesCompletionDate():
    t=Task("",datetime.now()+timedelta(days=1))
    t.updateStatus(Status.COMPLETED)
    assert t.completedAt!=None
    assert t.completedAt.date()==date.today()

def testUpdatePriority():
    t=Task("",datetime.now()+timedelta(days=1))
    t.updatePriority(Priority.HIGH)
    assert t.priority==Priority.HIGH