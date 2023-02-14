import pytest
from io import StringIO
from App import InCollege

college = InCollege()

#Network func to be implemented
def test_network(capsys, monkeypatch):
  input = StringIO("\n")
  monkeypatch.setattr('sys.stdin', input)
  assert college.network() == None