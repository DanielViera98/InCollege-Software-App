import pytest
from io import StringIO
from AccountSystem import AccountSystem
from App import InCollege


class MockSystem1():
    def __init__(self):
        self.user = "Username"
        self.username = "Username"
        self.password = "I234567&"
        self.first_name =  "Nobody",
        self.last_name =  "Here",
        self.language = "en",
        self.email = True,
        self.SMS = True,
        self.targeted_advertising = True,
        self.friends_list = [],
        self.requests = []
        self.system = AccountSystem()
        self.college = InCollege()
        self.college.user = "Username"

class MockSystem2():
    def __init__(self):
        self.user = "Username2"
        self.username = "Username2"
        self.password = "I234567&"
        self.first_name =  "Nobody2",
        self.last_name =  "Here2",
        self.language = "es",
        self.email = True,
        self.SMS = True,
        self.targeted_advertising = True,
        self.friends_list = [],
        self.requests = []
        self.system = AccountSystem()
        self.college = InCollege()
        self.college.user = "Username2"

def empty_students():
  student = open("students.json", "w")
  student.write("{\n}")

empty_students()

#Test search
def test_request_reg(capsys, monkeypatch):
    acc1 = MockSystem1()
    acc2 = MockSystem2()
    
    input = ('n\nn\n')
    input = StringIO(input)
    monkeypatch.setattr('sys.stdin', input)
    
    acc1.system.add_account(acc1.username, acc1.password, acc1.first_name[0], acc1.last_name[0], acc1.email[0], acc1.SMS[0], acc1.targeted_advertising[0], acc1.friends_list[0], acc1.requests)
    acc2.system.add_account(acc2.username, acc2.password, acc2.first_name[0], acc2.last_name[0], acc2.email[0], acc2.SMS[0], acc2.targeted_advertising[0], acc2.friends_list[0], acc2.requests)    
    
    input = ('Nobody2\nHere2\n\n')
    input = StringIO(input)
    monkeypatch.setattr('sys.stdin', input)
    
    assert acc1.college.send_request() == True