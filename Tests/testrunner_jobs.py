import pytest
from io import StringIO
from Tests.helpers import MockSystem2, empty_jobs

empty_jobs()

#search_jobs To Be Implemented
def test_search_jobs(capsys, monkeypatch):
  account = MockSystem2()
  input = StringIO("\n")
  monkeypatch.setattr('sys.stdin', input)
  assert account.college.search_jobs() == None


@pytest.mark.parametrize("input, results", 
                         [('Recruiter\nRecruit people\nDaniel Viera\nFlorida\n10$\n\n', True), 
                          ('Recruiter\nRecruit people\nDaniel Viera\nFlorida\n10$\n\n', False), 
                          ('\nRecruit people\nDaniel Viera\nFlorida\n10$\n\n', False), 
                          ('Recruiter\n\nDaniel Viera\nFlorida\n10$\n\n', False), 
                          ('Recruiter\nRecruit people\n\nFlorida\n10$\n\n', False), 
                          ('Recruiter\nRecruit people\nDaniel Viera\n\n10$\n\n', False), 
                          ('Recruiter\nRecruit people\nDaniel Viera\nFlorida\n\n\n', False), 
                          ('\n\n\n\n\n\n\n', False), 
                          ('\'None\'\nRecruit people\nDaniel Viera\nFlorida\n10$\n\n', False), 
                          ('Firstttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttt\nRecruiter\nRecruit people\nDaniel Viera\nFlorida\n10$\n\n', False)])
#job_title, description, employer, location, salary.
#Tests correct input, every empty field, all empty fields, long input
#Empty fields will fail because checks currently not implemented due to not being required
def test_post_jobs(capsys, monkeypatch, input, results):
  account = MockSystem2()
  inp = ('n\nn\n')
  inp = StringIO(input)
  monkeypatch.setattr('sys.stdin', inp)
  account.system.add_account(account.username, account.password, account.first_name[0], account.last_name[0], account.email[0], account.SMS[0], account.targeted_advertising[0], account.friends_list[0], account.requests, [], [])
  input = StringIO(input)
  monkeypatch.setattr('sys.stdin', input)
  assert account.college.post_jobs() == results