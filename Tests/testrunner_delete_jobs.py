import pytest
from io import StringIO
from App import InCollege
from Tests.helpers import MockUser1, MockUser2, empty_all

empty_all()


def test_delete_job(capsys, monkeypatch):
  account1 = MockUser1()
  account2 = MockUser2()
  inp = ('n\nn\n')
  inp = StringIO(inp)
  monkeypatch.setattr('sys.stdin', inp)
  account1.system.add_account(account1.username, account1.password, account1.first_name[0], account1.last_name[0])
  account2.system.add_account(account2.username, account2.password, account2.first_name[0], account2.last_name[0])
  
  #Attempt to delete job when it doesn't exist
  input = StringIO("First\n\n")
  monkeypatch.setattr('sys.stdin', input)
  assert account1.college.delete_job() == False
  
  #Attempt to create job
  input = StringIO("First\n\n\n\n\n\n\n")
  monkeypatch.setattr('sys.stdin', input)
  assert account1.college.post_jobs() == True
  
  #Attempt to delete account's created job with account2
  input = StringIO("First\n\n")
  monkeypatch.setattr('sys.stdin', input)
  assert account2.college.delete_job() == False
  
  #Attempt to delete created job
  input = StringIO("First\n\n")
  monkeypatch.setattr('sys.stdin', input)
  assert account1.college.delete_job() == True

empty_all()