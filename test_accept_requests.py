import pytest
from io import StringIO
from AccountSystem import AccountSystem
from App import InCollege

system = AccountSystem()
college = InCollege()

def empty_students():
  student = open("students.json", "w")
  student.write("{\n}")

empty_students()

def test_accept_requests()