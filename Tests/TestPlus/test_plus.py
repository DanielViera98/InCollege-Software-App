from io import StringIO
from Tests.helpers import empty_all, MockUser1
from App import AccountSystem
empty_all()

system = AccountSystem()
#Tests registration of a plus user
def test_register_plus(monkeypatch, capsys):  
  account1 = MockUser1()
  #Test register function on correct input 
  input = StringIO('Username\nTest1now*\nFirst\nLast\ny\nn\n\n')
  monkeypatch.setattr('sys.stdin', input)
  assert account1.system.register() == 'Username'
  assert account1.plus_status == True
  
  