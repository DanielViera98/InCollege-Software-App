class Student:
    
  def __init__(self,
  username=None,
  password=None,
  first_name=None,
  last_name=None,
  plus_status = False,
  email=True,
  SMS=True,
  targeted_advertising=True,
  language=None, 
  friends=[],
  requests=[],
  saved_jobs=[],
  applied_jobs=[],
  inbox=[],
  is_profile_created=False,
  new_jobs=[],
  removed_jobs=[],
  is_new_account=[]
  ):
    self.username = username
    self.password = password
    self.first_name = first_name
    self.last_name = last_name
    self.plus_status = plus_status
    self.email = email
    self.SMS = SMS
    self.targeted_advertising = targeted_advertising
    self.language = language
    self.friends = friends
    self.requests = requests
    self.saved_jobs= saved_jobs
    self.applied_jobs= applied_jobs
    self.inbox=inbox
    self.is_profile_created = is_profile_created
    self.new_jobs = new_jobs
    self.removed_jobs = removed_jobs
    self.is_new_account = is_new_account
  
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

