import pytest
from io import StringIO
from AccountSystem import AccountSystem
from App import InCollege
from Messaging import Messaging
class MockUser1():
    def __init__(self):
        self.user = "Username"
        self.username = "Username"
        self.password = "I234567&"
        self.first_name = "Nobody",
        self.last_name =  "Here",
        self.language = "en",
        self.email = True,
        self.SMS = True,
        self.targeted_advertising = True,
        self.friends_list = [],
        self.requests = []
        self.system = AccountSystem()
        self.college = InCollege()
        self.college.user = "Username"
        self.plus_status = False
        self.message_inbox = []
      
class MockUser2():
    def __init__(self):
        self.user = "Username2"
        self.username = "Username2"
        self.password = "I234567&"
        self.first_name =  "Nobody2",
        self.last_name =  "Here2",
        self.language = "es",
        self.email = True,
        self.SMS = True,
        self.targeted_advertising = True,
        self.friends_list = [],
        self.requests = []
        self.system = AccountSystem()
        self.college = InCollege()
        self.college.user = "Username2"
        self.plus_status = False
        self.message_inbox = []

class MockUser3():
    def __init__(self):
        self.user = "Username3"
        self.username = "Username3"
        self.password = "I234567&"
        self.first_name =  "Nobody3",
        self.last_name =  "Here3",
        self.language = "es",
        self.email = True,
        self.SMS = True,
        self.targeted_advertising = True,
        self.friends_list = [],
        self.requests = []
        self.system = AccountSystem()
        self.college = InCollege()
        self.college.user = "Username3"
        self.plus_status = True
        self.message_inbox = []

def empty_students():
  student = open("students.json", "w")
  student.write("{\n}")
  
def empty_jobs():
  f = open("job_postings.json", "w")
  f.write("[\n]")
 
def empty_profiles():
  f = open("profiles.json", "w")
  f.write("[\n]")
  
def empty_all():
    empty_students()
    empty_jobs()
    empty_profiles()
  
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