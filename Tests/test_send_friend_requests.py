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
def test_request_reg(capsys, monkeypatch):
    register =  ("XASASDDASD\nI234567*\nNobody\nHere\n\n\n", "TASDASDASD\nI234567*\nEmpty\nField\n\n\n")
    for i in register:
        test = StringIO(i)
        monkeypatch.setattr('sys.stdin', test)
        assert type(system.register()) == str

    assert type(college.search_people("Nobody", "Here")) == str
    assert college.search_people("Nobodi","here") == False

empty_students()

#Test Requests
@pytest.mark.parametrize("input, results", 
                         [('Nobody\nHere\n\n', True), 
                          ('Empty\nField\n\n', True),
                          ('Not\nInside\n\n', False)])
#Works, but sends False as request since self.user is initialized to False
def test_send_request(capsys, monkeypatch, input, results):
    input = StringIO(input)
    monkeypatch.setattr('sys.stdin', input)
    assert college.send_request() == results

#def test_receive_request():
    