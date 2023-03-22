import pytest
from io import StringIO
from App import InCollege
from Tests.helpers import MockSystem1, MockSystem2, empty_all

#create mock account to add jobs from
def test_nonexistent_accounts(capsys, monkeypatch):
    account1 = MockSystem1()
    inp = ('n\nn\n')
    inp = StringIO(input)
    monkeypatch.setattr('sys.stdin', inp)
    account1.system.add_account(account1.username, account1.password, account1.first_name[0], account1.last_name[0], account1.email[0], account1.SMS[0], account1.targeted_advertising[0], account1.friends_list[0], account1.requests, [], [])
    
    account2 = MockSystem2()
    inp = ('n\nn\n')
    inp = StringIO(input)
    monkeypatch.setattr('sys.stdin',inp)
    account2.system.add_account(account2.username, account2.password, account2.first_name[0], account2.last_name[0], account2.email[0], account2.SMS[0], account2.targeted_advertising[0], account2.friends_list[0], account2.requests, [], [])
    
    input = StringIO('Nobody2\nHere2\n\n')
    monkeypatch.setattr('sys.stdn',input)
    account1.college.send_request()
    print(dir(account1))
    
    input = StringIO('1\n1\n\n\n\n')
    monkeypatch.setattr('sys.stdin', input)
    account2.college.pending_requests()
    print(dir(account2))
    
    try:
        input = StringIO('2\n1\n\n\n3\n')
        monkeypatch.setattr('sys.stdin', input)
        account1.college.manage_friends()
    except:
        assert False, "error unable to view profile"