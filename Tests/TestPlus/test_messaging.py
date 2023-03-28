from io import StringIO
from Tests.helpers import empty_all, MockUser1, MockUser2, MockUser3
from Messaging import Messaging
import time
empty_all()

def create_account(num, input, monkeypatch):
  if num == 1:
    account = MockUser1()
  elif num == 2:
    account = MockUser2()
  elif num == 3:
    account = MockUser3()
  input = StringIO(input)
  monkeypatch.setattr('sys.stdin', input)
  account.system.add_account(account.username, account.password, account.first_name[0], account.last_name[0])
  return account

#Works but only checks send_message
def test_message(monkeypatch):
  input = ('y\nn\nn\n\n')
  account1 = create_account(1, input, monkeypatch)
  input = ('n\nn\nn\n\n')
  account2 = create_account(2, input, monkeypatch)
  input = ('\n')
  input = StringIO(input)
  monkeypatch.setattr('sys.stdin', input)
  new_message = Messaging(account1.user, account2.user)
  assert new_message.send_message("Message") == True
  accounts = new_message.system.load_accounts()
  print("\nMessage:", accounts["Username2"]["message_inbox"][0]) #use -s to see
  assert accounts["Username2"]["message_inbox"][0] == "Message"
  
#Check to make sure you can't send friend request to someone you aren't friends with
def test_message2(monkeypatch):
  input = ('y\nn\nn\n\n')
  account1 = create_account(1, input, monkeypatch)
  input = ('n\nn\nn\n\n')
  account2 = create_account(2, input, monkeypatch)
  account3 = create_account(3, input, monkeypatch)
  input = ('3\n')
  input = StringIO(input)
  monkeypatch.setattr('sys.stdin', input)
  
  assert account1.college.manage_friends()
  
  
  
  