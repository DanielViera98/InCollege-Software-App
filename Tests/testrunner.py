import pytest
from io import StringIO
from debug import reset_db
from AccountSystem import AccountSystem

system = AccountSystem()


reset_db()
#Test for minimum 8 characters, maximum 12 characters, an uppercase letter, a digit, and special character
@pytest.mark.parametrize("passwords, results", [("Test1*", False), ("Test1*extralong", False), ("test1*low", False), ("Testa*alpha", False), ("Test1nospec", False), ("Works1*as", True), ("WORKS123*_", True), ("W0463123*_$", True)])
def test_verify_password(passwords, results): 
  assert system.is_secure_password(passwords) == results

reset_db()
#Test register function on correct input, failing input, empty username, empty password, and empty username and password.
@pytest.mark.parametrize("input, results", [('First\nTest1now*\n', True), ('Second\nFail\nSecond\n\n', False), ('\nFail\n\n', False), ('Fourth\n\n\n', False), ('\n\n\n', False)])
def test_register_inputs(capsys, monkeypatch, input, results):
  input = StringIO(input)
  monkeypatch.setattr('sys.stdin', input)
  assert system.register() == results

#Test register function for duplicate usernames

#Clear database for login functions

input = (("D\nI234567*\n", True), ("D\nI234567*\n\n", False))
#Test registering duplicate accounts
def test_register_duplicate(capsys, monkeypatch):
  reset_db()
  for i,r in input:
    print(i,r)
    test = StringIO(i)
    monkeypatch.setattr('sys.stdin', test)
    assert system.register() == r


#Test login failure
def test_login_fail(capsys, monkeypatch):
  reset_db()
  input = StringIO("T\nI234567*\n\nn")
  monkeypatch.setattr('sys.stdin', input)
  assert system.login() == False



#Test login
input = (("XASASDDASD\nI234567*\n\n", True), ("TASDASDASD\nI234567*\n\n", True))
def test_login(capsys, monkeypatch):
  reset_db()
  for i,r in input:
    test = StringIO(i)
    monkeypatch.setattr('sys.stdin', test)
    assert system.register() == r
    
  for i, r in input:
    test = StringIO(i)
    monkeypatch.setattr('sys.stdin', test)
    assert system.login() == r
reset_db()

