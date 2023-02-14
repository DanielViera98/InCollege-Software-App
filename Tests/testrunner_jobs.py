import pytest
from io import StringIO
from App import InCollege


college = InCollege()

def test_search_jobs(capsys, monkeypatch):
  input = StringIO("\n")
  monkeypatch.setattr('sys.stdin', input)
  assert college.search_jobs() == None

#Username, username, job_title, description, employer, location, salary
@pytest.mark.parametrize("input, results", [('First\nRecruiter\nRecruit people\nDaniel Viera\nFlorida\n10$\n', True), ('\nRecruiter\nRecruit people\nDaniel Viera\nFlorida\n10$\n', False), ('First\\nRecruit people\nDaniel Viera\nFlorida\n10$\n', False), ('First\nRecruiter\\nDaniel Viera\nFlorida\n10$\n', False), ('First\nRecruiter\nRecruit people\\nFlorida\n10$\n', False), ('First\nRecruiter\nRecruit people\nDaniel Viera\\n10$\n', False), ('First\nRecruiter\nRecruit people\nDaniel Viera\nFlorida\n\n', False), ('\n\n\n\n\n\n\n', False), ('\'None\'\nRecruiter\nRecruit people\nDaniel Viera\nFlorida\n10$\n', False), ('Firstttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttt\nRecruiter\nRecruit people\nDaniel Viera\nFlorida\n10$\n', False)])
def test_job_updater(capsys, monkeypatch, input, results):
  for i,r in input:
    input = StringIO(i)
    monkeypatch.setattr('sys.stdin', input)
    assert college.job_updater() == r
  