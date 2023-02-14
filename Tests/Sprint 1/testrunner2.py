import pytest
from AccountSystem import AccountSystem
from io import StringIO

system = AccountSystem()

#Test register function for atleast 6 entries
input = (("D1\nI234567*\nA\na\n\n", True), ("D2\nI234567*\nB\nb\n\n", True),
         ("D3\nI234567*\nC\nc\n\n", True), ("D4\nI234567*\nD\nd\n\n", True),
         ("D5\nI234567*\nE\ne\n\n", True), ("D6\nI234567*\nF\nf\n\n", False))


def test_register_max_entries(capsys, monkeypatch):
	for i, r in input:
		print(i, r)
		test = StringIO(i)
		monkeypatch.setattr('sys.stdin', test)
		assert system.register() == r
