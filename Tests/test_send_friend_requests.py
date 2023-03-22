import pytest
from io import StringIO
from AccountSystem import AccountSystem
from App import InCollege
from helpers import MockUser1, MockUser2, empty_students

empty_students()

#Test search
def test_request_reg(capsys, monkeypatch):
    acc1 = MockUser1()
    acc2 = MockUser2()
    
    input = ('n\nn\n')
    input = StringIO(input)
    monkeypatch.setattr('sys.stdin', input)
    
    acc1.system.add_account(acc1.username, acc1.password, acc1.first_name[0], acc1.last_name[0], acc1.email[0], acc1.SMS[0], acc1.targeted_advertising[0], acc1.friends_list[0], acc1.requests)
    acc2.system.add_account(acc2.username, acc2.password, acc2.first_name[0], acc2.last_name[0], acc2.email[0], acc2.SMS[0], acc2.targeted_advertising[0], acc2.friends_list[0], acc2.requests)    
    
    input = ('Nobody2\nHere2\n\n')
    input = StringIO(input)
    monkeypatch.setattr('sys.stdin', input)
    
    assert acc1.college.send_request() == True