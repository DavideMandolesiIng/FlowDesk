import pytest
from datetime import datetime, date,timedelta
from app.models.Task import Task, Status, Priority

def testDefaultValues():
    t=Task("",date.today()+timedelta(days=1))
    assert t.status==Status.TODO
    assert t.priority==Priority.NORMAL
    assert t.completionDate==None
    assert t.creationDate.date()==date.today()

def testUpdateStatusToInProgressDontUpdatesCompletionDate():
    t=Task("",date.today()+timedelta(days=1))
    t.updateStatus(Status.IN_PROGRESS)
    assert t.completionDate==None

def testUpdateStatusToCompleteUpdatesCompletionDate():
    t=Task("",date.today()+timedelta(days=1))
    t.updateStatus(Status.COMPLETED)
    assert t.completionDate!=None
    assert t.completionDate.date()==date.today()

def testUpdatePriority():
    t=Task("",date.today()+timedelta(days=1))
    t.updatePriority(Priority.HIGH)
    assert t.priority==Priority.HIGH