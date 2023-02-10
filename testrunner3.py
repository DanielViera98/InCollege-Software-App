import pytest
from io import StringIO
from App import InCollege

college = InCollege()

#Test Tasks to make sure user can access each function and return afterwards
input = "1\n\n2\n\n3\n1\n\n2\n\n3\n\n4\n\n5\n\n6\n4\n"


def test_Tasks(capsys, monkeypatch):
  test = StringIO(input)
  monkeypatch.setattr('sys.stdin', test)
  assert college.show_options() == None
