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

#Test register function on correct input 
def test_register_inputs(capsys, monkeypatch):
  input = StringIO('First\nTest1now*\nA\na\n\n')
  monkeypatch.setattr('sys.stdin', input)
  assert system.register() == 'First'
  
  input = StringIO('Second\n\nFail\nSecond\nB\nb\n')
  monkeypatch.setattr('sys.stdin', input)
  assert system.register() == False
  
#Test registering duplicate accounts - First return is a string, second is false
def test_register_duplicate(capsys, monkeypatch):
  test = StringIO("Duplicate\nI234567*\nFirst\nLast\n\n")
  monkeypatch.setattr('sys.stdin', test)
  assert type(system.register()) == str
  test = StringIO("Duplicate\nI234567*\nFirst\nLast\n\n")
  monkeypatch.setattr('sys.stdin', test)
  assert system.register() == False

#Test login failure
def test_login_fail(capsys, monkeypatch):
  input = StringIO("T\nI234567*\n\nn")
  monkeypatch.setattr('sys.stdin', input)
  assert system.login() == False



#Test login
def test_login(capsys, monkeypatch):
  register =  (("XASASDDASD\nI234567*\nNobody\nHere\n\n", True), ("TASDASDASD\nI234567*\nEmpty\nField\n\n", True))
  login = (("XASASDDASD\nI234567*\n\nN\n", False), ("TASDASDASD\nI234567*\n\nN\n", False))
  for i,r in register:
    test = StringIO(i)
    monkeypatch.setattr('sys.stdin', test)
    assert type(system.register()) == str
  for i, r in login:
    test = StringIO(i)
    monkeypatch.setattr('sys.stdin', test)
    assert system.login() != r
