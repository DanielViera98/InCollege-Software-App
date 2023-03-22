import pytest
from io import StringIO
from Tests.helpers import MockUser1, empty_all
empty_all()

def test_display_jobs(capsys, monkeypatch):
  account = MockUser1()
  inp = ('n\nn\n')
  inp = StringIO(inp)
  monkeypatch.setattr('sys.stdin', inp)
  account.system.add_account(account.username, account.password, account.first_name[0], 
                             account.last_name[0], account.email[0], account.SMS[0], 
                             account.targeted_advertising[0], account.friends_list[0], account.requests, [], [])
  
  #Attempt to view jobs without any there
  input = StringIO("\n")
  monkeypatch.setattr('sys.stdin', input)
  assert account.college.display_jobs() == "Empty"
  
  #Attempt to create job
  input = StringIO("First\n\n\n\n\n\n\n")
  monkeypatch.setattr('sys.stdin', input)
  assert account.college.post_jobs() == True
  
  #Attempt to view ALL jobs, display Job 1, then save it. 
  input = StringIO("\n1\n1\n1\n1\n1\n\n2\n")
  monkeypatch.setattr('sys.stdin', input)
  assert account.college.display_jobs() == "Saved"
  
  
  