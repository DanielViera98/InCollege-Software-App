class Student:
    
  def __init__(self,
  username=None,
  password=None,
  first_name=None,
  last_name=None,
  email=True,
  SMS=True,
  targeted_advertising=True,
  language = "English", #True = English, False = Spanish
  ):
    self.username = username
    self.password = password
    self.first_name = first_name
    self.last_name = last_name
  
  def record(self):
    info = {
    "username": self.username,
    "password": self.password,
    "first_name": self.first_name,
    "last_name": self.last_name,
    "job_postings": self.job_postings,
    }
  
    return info

  def add_job(self, job_posting):
    self.job_postings.append(job_posting)

  def toggle_option(self, option):
    self.option = not self.option
    
  def change_language(self, option):
    if option == "English":
      self.language = "English"
    else:
      self.language = "Spanish"
