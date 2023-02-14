import pytest
from io import StringIO
from AccountSystem import AccountSystem
from AccountAuth import is_secure_password
from App import InCollege

system = AccountSystem()
college = InCollege()

#Test for minimum 8 characters, maximum 12 characters, an uppercase letter, a digit, and special character
@pytest.mark.parametrize("passwords, results", [("Test1*", False), ("Test1*extralong", False), ("test1*low", False), ("Testa*alpha", False), ("Test1nospec", False), ("Works1*as", True), ("WORKS123*_", True), ("W0463123*_$", True)])
def test_verify_password(passwords, results): 
  assert is_secure_password(passwords) == results


@pytest.mark.parametrize("input, results", [('First\nTest1now*\nA\na\n\n', True), ('Second\n\nFail\nSecond\nB\nb\n', False), ('\nC\nc\nFail\n\n', False), ('Fourth\nD\nd\n\n\n', False), ('\nE\ne\n\n\n', False), ('\n\ne\n\n\n', False), ('\nE\n\n\n\n', False), ('\n\n\n\n\n', False)])
#Test register function on correct input, failing input, empty username, empty password, and empty username and password.
def test_register_inputs(capsys, monkeypatch, input, results):
  input = StringIO(input)
  monkeypatch.setattr('sys.stdin', input)
  assert system.register() == results
  

#Test register function for duplicate usernames

#Clear database for login functions

input = (("Dup\nI234567*\nFirst\nLast\n\n", True), ("Dup\nI234567*\nFirst\nLast\n\n", False))
#Test registering duplicate accounts
def test_register_duplicate(capsys, monkeypatch):
    for i,r in input:
      test = StringIO(i)
      monkeypatch.setattr('sys.stdin', test)
      assert system.register() == r


#Test login failure
def test_login_fail(capsys, monkeypatch):
  input = StringIO("T\nI234567*\n\nn")
  monkeypatch.setattr('sys.stdin', input)
  assert system.login() == False



#Test login
def test_login(capsys, monkeypatch):
  register =  (("XASASDDASD\nI234567*\nNobody\nHere\n\n", True), ("TASDASDASD\nI234567*\nEmpty\nField\n\n", True))
  login = (("XASASDDASD\nI234567*\n\nN\n", True), ("TASDASDASD\nI234567*\n\nN\n", True))
  for i,r in register:
    test = StringIO(i)
    monkeypatch.setattr('sys.stdin', test)
    assert system.register() == r
  for i, r in login:
    test = StringIO(i)
    monkeypatch.setattr('sys.stdin', test)
    assert system.login() == r

@pytest.mark.parametrize("input, results", [('First\nLast\n\n', True), ('A\na\n\n', True), ("Doesn't\nExist\n\n", False), ('\nLast\n\n', False), ('First\n\n\n', False), ('\n\n\n', False)])
def test_network(capsys, monkeypatch, input, results):
  input = StringIO(input)
  monkeypatch.setattr('sys.stdin', input)
  assert college.network() == results