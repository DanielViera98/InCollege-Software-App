from io import StringIO
from Tests.helpers import empty_all, create_account
from App import AccountSystem
empty_all()

sys = AccountSystem()

#Test view_inbox with empty inbox returns empty
def test_empty_inbox(monkeypatch):
  input = ('y\nn\nn\n\n')
  account1 = create_account(1, input, monkeypatch)
  
  input = ('\n')
  input = StringIO(input)
  monkeypatch.setattr('sys.stdin', input)
  assert account1.college.view_inbox() == "Empty"

#Test sending message from premium to nonfriend and standard to nonfriend
def test_send_message_plus(monkeypatch):
  #test sending message in premium account
  input = ('y\nn\nn\n\n')
  account1 = create_account(1, input, monkeypatch)
  input = ('n\nn\nn\n\n')
  account2 = create_account(2, input, monkeypatch)
  
  #Attempt to send request in standard account to non-friend
  input = ('\n')
  input = StringIO(input)
  monkeypatch.setattr('sys.stdin', input)
  assert account2.college.send_message_anyone() == False
  
  #Attempt to send request in premium account to non-friend
  input = ('2\nMessage\n\n\n')
  input = StringIO(input)
  monkeypatch.setattr('sys.stdin', input)
  assert account1.college.send_message_anyone() == True

def test_send_message_friend(monkeypatch):
  #test sending message in premium account
  input = ('y\nn\nn\n\n')
  account1 = create_account(1, input, monkeypatch)
  input = ('n\nn\nn\n\n')
  account2 = create_account(2, input, monkeypatch)
  
  # input = StringIO('Nobody2\nHere2\n\n')
  # monkeypatch.setattr('sys.stdin', input)
  # account1.college.send_request()
  # input = StringIO('1\n\n')
  # monkeypatch.setattr('sys.stdin', input)
  # account2.college.accept_request(account2.system.load_accounts(), account2.requests)
  
  print(account2.friends_list)
  #Attempt to send request in standard account to friend
  input = ('1\n')
  input = StringIO(input)
  monkeypatch.setattr('sys.stdin', input)
  print("DO SOMETHING", account2.friends_list)
  account2.college.send_message_friend()
  print(account1.requests)
  
  #Attempt to send request in premium account to friend
  input = ('2\n\n\n\n\n\n\n\n')
  input = StringIO(input)
  monkeypatch.setattr('sys.stdin', input)
  assert account1.college.send_message_anyone() == True