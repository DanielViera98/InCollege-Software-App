import pytest
from io import StringIO
from App import InCollege

college = InCollege()

#search_jobs To Be Implemented
def test_search_jobs(capsys, monkeypatch):
  input = StringIO("\n")
  monkeypatch.setattr('sys.stdin', input)
  assert college.search_jobs() == None

#Username, username, job_title, description, employer, location, salary.
#Tests correct input, every empty field, all empty fields, long input
@pytest.mark.parametrize("input, results", [('First\nRecruiter\nRecruit people\nDaniel Viera\nFlorida\n10$\n', True), ('\nRecruiter\nRecruit people\nDaniel Viera\nFlorida\n10$\n', False), ('Third\n\nRecruit people\nDaniel Viera\nFlorida\n10$\n', False), ('Fourth\nRecruiter\n\nDaniel Viera\nFlorida\n10$\n', False), ('Fifth\nRecruiter\nRecruit people\n\nFlorida\n10$\n', False), ('Sixth\nRecruiter\nRecruit people\nDaniel Viera\n\n10$\n', False), ('Seventh\nRecruiter\nRecruit people\nDaniel Viera\nFlorida\n\n', False), ('\n\n\n\n\n\n\n', False), ('\'None\'\nRecruiter\nRecruit people\nDaniel Viera\nFlorida\n10$\n', False), ('Firstttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttt\nRecruiter\nRecruit people\nDaniel Viera\nFlorida\n10$\n', False)])
def test_job_updater(capsys, monkeypatch, input, results):
  input = StringIO(input)
  monkeypatch.setattr('sys.stdin', input)
  assert college.job_updater() == results

#Tests for adding more than required five accounts. Currently not implemented correctly
@pytest.mark.parametrize("input, results", [("First\n\n\n\n\n\n\n", True), ("Second\n\n\n\n\n\n\n", True), ("Third\n\n\n\n\n\n\n", True), ("Fourth\n\n\n\n\n\n\n", True), ("Fifth\n\n\n\n\n\n\n", True), ("Sixth\n\n\n\n\n\n\n", False)])
def test_job_updater_max_five(capsys, monkeypatch, input, results):
  input = StringIO(input)
  monkeypatch.setattr('sys.stdin', input)
  assert college.job_updater() == results