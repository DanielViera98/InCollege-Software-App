import pytest
from io import StringIO
from App import InCollege
from Tests.helpers import MockSystem1, MockSystem2, empty_all

empty_all()


def test_delete_job(capsys, monkeypatch):
  account = MockSystem1()
  account2 = MockSystem2()
  inp = ('n\nn\n')
  inp = StringIO(inp)
  monkeypatch.setattr('sys.stdin', inp)
  account.system.add_account(account.username, account.password, account.first_name[0], 
                             account.last_name[0], account.email[0], account.SMS[0], 
                             account.targeted_advertising[0], account.friends_list[0], account.requests, [], [])
  account2.system.add_account(account2.username, account2.password, account2.first_name[0], 
                              account2.last_name[0], account2.email[0], account2.SMS[0], 
                              account2.targeted_advertising[0], account2.friends_list[0], account2.requests, [], [])
  
  #Attempt to delete job when it doesn't exist
  input = StringIO("First\n\n")
  monkeypatch.setattr('sys.stdin', input)
  assert account.college.delete_job() == False
  
  #Attempt to create job
  input = StringIO("First\n\n\n\n\n\n\n")
  monkeypatch.setattr('sys.stdin', input)
  assert account.college.post_jobs() == True
  
  #Attempt to delete account's created job with account2
  input = StringIO("First\n\n")
  monkeypatch.setattr('sys.stdin', input)
  assert account2.college.delete_job() == False
  
  #Attempt to delete created job
  input = StringIO("First\n\n")
  monkeypatch.setattr('sys.stdin', input)
  assert account.college.delete_job() == True

empty_all()