import pytest
from io import StringIO
from AccountSystem import AccountSystem
from App import InCollege

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
  