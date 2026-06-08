import pytest
from datetime import datetime,date
from app.models.Note import Note

def testDefaultValues():
    n = Note("","",[])
    assert n.updatedAt.date()==date.today()
    assert len(n.tags)==0

def testUpdateTags():
    n = Note("","",[])
    t=["tag1","tag2"]
    n.updateTags(t)
    assert len(n.tags)==2