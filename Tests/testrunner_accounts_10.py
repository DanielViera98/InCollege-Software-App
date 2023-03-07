import pytest
from io import StringIO
from App import InCollege

college = InCollege()

#Tests for adding up to 10 accounts. 
@pytest.mark.parametrize("input, results", [("D1\nI234567*\nA\na\n\n", True), ("D2\nI234567*\nB\nb\n\n", True),
         ("D3\nI234567*\nC\nc\n\n", True), ("D4\nI234567*\nD\nd\n\n", True),
         ("D5\nI234567*\nE\ne\n\n", True), ("D6\nI234567*\nF\nf\n\n", True), ("D7\nI234567*\nG\ng\n\n", True),("D8\nI234567*\nH\nh\n\n", True),
         ("D9\nI234567*\nI\ni\n\n", True),("D10\nI234567*\nJ\nj\n\n", True),("D11\nI234567*\nK\nk\n\n", False)])

def test_10_users(capsys,monkeypatch, input, results):
    input = StringIO(input)
    monkeypatch.setattr('sys.stdin', input)
    assert college.register() == results