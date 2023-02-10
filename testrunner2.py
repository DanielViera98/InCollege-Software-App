import pytest
from AccountSystem import AccountSystem
from replit import db
from debug import reset_db
from io import StringIO

system = AccountSystem()
reset_db()
#Test register function for atleast 6 entries
input = (("D1\nI234567*\n", True), ("D2\nI234567*\n\n", True),
         ("D3\nI234567*\n\n", True), ("D4\nI234567*\n\n", True),
         ("D5\nI234567*\n\n", True), ("D6\nI234567*\n\n", False))


def test_register_max_entries(capsys, monkeypatch):
	for i, r in input:
		print(i, r)
		test = StringIO(i)
		monkeypatch.setattr('sys.stdin', test)
		assert system.register() == r
