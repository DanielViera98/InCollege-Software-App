import pytest
from io import StringIO
from App import InCollege
from Tests.helpers import MockSystem1, empty_all

empty_all()

#Tests for adding more than required ten accounts. 
@pytest.mark.parametrize("input, results", [("First\n\n\n\n\n\n\n", True), 
                      ("Second\n\n\n\n\n\n\n", True), ("Third\n\n\n\n\n\n\n", True), 
                      ("Fourth\n\n\n\n\n\n\n", True), ("Fifth\n\n\n\n\n\n\n", True), 
                      ("Sixth\n\n\n\n\n\n\n", True), ("Seventh\n\n\n\n\n\n\n", True), 
                      ("Eighth\n\n\n\n\n\n\n", True), ("Ninth\n\n\n\n\n\n\n", True), 
                      ("Tenth\n\n\n\n\n\n\n", True), ("Eleventh\n\n\n\n\n\n\n", False),])
def test_post_jobs_max_five(capsys, monkeypatch, input, results):
  #create mock account to add jobs from
  account = MockSystem1()
  inp = ('n\nn\n')
  inp = StringIO(input)
  monkeypatch.setattr('sys.stdin', inp)
  account.system.add_account(account.username, account.password, account.first_name[0], account.last_name[0], 
                             account.email[0], account.SMS[0], account.targeted_advertising[0], 
                             account.friends_list[0], account.requests, [], [])
  
  input = StringIO(input)
  monkeypatch.setattr('sys.stdin', input)
  assert account.college.post_jobs() == results
  
empty_all()