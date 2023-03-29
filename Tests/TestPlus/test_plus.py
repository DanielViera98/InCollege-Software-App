from io import StringIO
from Tests.helpers import empty_all, MockUser1
from App import AccountSystem
empty_all()

sys = AccountSystem()
#Tests registration of a plus user
def test_register_plus(monkeypatch, capsys):  
  input = StringIO('Username\nTest1now*\nFirst\nLast\ny\nn\n\n')
  monkeypatch.setattr('sys.stdin', input)
  #Test register function on correct input 
  assert sys.register() == 'Username'
  print(sys.accounts['Username'])     #use -s to view print statements in output
  assert sys.accounts['Username']['plus_status'] == True

  
  