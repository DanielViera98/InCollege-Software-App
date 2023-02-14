import pytest
from io import StringIO
from App import InCollege

college = InCollege()

#Tests for adding more than required five accounts. 
@pytest.mark.parametrize("input, results", [("First\n\n\n\n\n\n\n", True), ("Second\n\n\n\n\n\n\n", True), ("Third\n\n\n\n\n\n\n", True), ("Fourth\n\n\n\n\n\n\n", True), ("Fifth\n\n\n\n\n\n\n", True), ("Sixth\n\n\n\n\n\n\n", False)])
def test_post_jobs_max_five(capsys, monkeypatch, input, results):
  input = StringIO(input)
  monkeypatch.setattr('sys.stdin', input)
  assert college.post_jobs() == results