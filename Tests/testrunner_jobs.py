import pytest
from io import StringIO
from App import InCollege

college = InCollege()

#search_jobs To Be Implemented
def test_search_jobs(capsys, monkeypatch):
  input = StringIO("\n")
  monkeypatch.setattr('sys.stdin', input)
  assert college.search_jobs() == None

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
  input = StringIO(input)
  monkeypatch.setattr('sys.stdin', input)
  assert college.post_jobs() == results