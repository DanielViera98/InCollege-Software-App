from io import StringIO
from Tests.helpers import empty_all, MockUser1, MockUser2
from Messaging import Messaging
empty_all()

def create_account(num, input, monkeypatch):
  if num == 1:
    account = MockUser1()
  else:
    account = MockUser2()
  input = StringIO(input)
  monkeypatch.setattr('sys.stdin', input)
  account.system.add_account(account.username, account.password, account.first_name[0], account.last_name[0])
  return account

def test_message(monkeypatch):
  input = ('y\nn\nn\n\n')
  account1 = create_account(1, input, monkeypatch)
  input = ('n\nn\nn\n\n')
  account2 = create_account(2, input, monkeypatch)
  account1
  
  
  
  
  