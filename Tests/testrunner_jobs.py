import pytest
from io import StringIO
from App import InCollege

college = InCollege()

#search_jobs To Be Implemented
def test_search_jobs(capsys, monkeypatch):
  input = StringIO("\n")
  monkeypatch.setattr('sys.stdin', input)
  assert college.search_jobs() == None

@pytest.mark.parametrize("input, results", [('First\nRecruiter\nRecruit people\nDaniel Viera\nFlorida\n10$\n', True), ('\nRecruiter\nRecruit people\nDaniel Viera\nFlorida\n10$\n', False), ('Third\n\nRecruit people\nDaniel Viera\nFlorida\n10$\n', False), ('Fourth\nRecruiter\n\nDaniel Viera\nFlorida\n10$\n', False), ('Fifth\nRecruiter\nRecruit people\n\nFlorida\n10$\n', False), ('Sixth\nRecruiter\nRecruit people\nDaniel Viera\n\n10$\n', False), ('Seventh\nRecruiter\nRecruit people\nDaniel Viera\nFlorida\n\n', False), ('\n\n\n\n\n\n\n', False), ('\'None\'\nRecruiter\nRecruit people\nDaniel Viera\nFlorida\n10$\n', False), ('Firstttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttt\nRecruiter\nRecruit people\nDaniel Viera\nFlorida\n10$\n', False)])
#Username, job_title, description, employer, location, salary.
#Tests correct input, every empty field, all empty fields, long input
#Empty fields will fail because checks currently not implemented due to not being required
def test_post_jobs(capsys, monkeypatch, input, results):
  input = StringIO(input)
  monkeypatch.setattr('sys.stdin', input)
  assert college.post_jobs() == results