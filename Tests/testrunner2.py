import pytest
from AccountSystem import AccountSystem
from io import StringIO
from MetaTests import empty_students
system = AccountSystem()

empty_students()
#Test register function for atleast 10 entries
input = (("Account1\nI234567*\nA\na\n\n", True), ("Account2\nI234567*\nB\nb\n\n", True),
         ("Account3\nI234567*\nC\nc\n\n", True), ("Account4\nI234567*\nD\nd\n\n", True),
         ("Account5\nI234567*\nE\ne\n\n", True), ("Account6\nI234567*\nF\nf\n\n", True),
         ("Account7\nI234567*\nA\na\n\n", True), ("Account8\nI234567*\nB\nb\n\n", True),
         ("Account9\nI234567*\nC\nc\n\n", True), ("Account10\nI234567*\nD\nd\n\n", True))
def test_register_max_entries(capsys, monkeypatch):
    #First ten entries return type is string (returning username), eleventh return is False because of failure
    for i, r in input:
        print(i, r)
        test = StringIO(i)
        monkeypatch.setattr('sys.stdin', test)
        assert type(system.register()) == str
    test = StringIO("Account11\nI234567*\nC\nc\n\n")
    monkeypatch.setattr('sys.stdin', test)
    assert system.register() == False