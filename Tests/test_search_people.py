import pytest
from io import StringIO
from AccountSystem import AccountSystem
from App import InCollege

system = AccountSystem()
college = InCollege()

def empty_students():
  student = open("students.json", "w")
  student.write("{\n}")

empty_students()

#Test search
def test_search(capsys, monkeypatch):
    register =  ("XASASDDASD\nI234567*\nNobody\nHere\n\n", "TASDASDASD\nI234567*\nEmpty\nField\n\n")
    for i in register:
        test = StringIO(i)
        monkeypatch.setattr('sys.stdin', test)
        assert type(system.register()) == str

    assert type(college.search_people("Nobody", "Here")) == str
    assert college.search_people("Nobodi","here") == False

        