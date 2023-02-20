from AccountSystem import AccountSystem
import os
import json


class InCollege:

  # Constructor
  def __init__(self):
    self.skills = [
     "Learn C", "Learn C#", "Learn Python", "Learn Java", "Learn HTML"
    ]
    self.menu_options = ["Login","Why join InCollege", "Register", "Useful Links"]
    self.options = ["Search for jobs", "Find someone you know", "Learn a new skill"]
    self.job_options = ["Search for jobs", "Post a job"]
    self.useful_links = ["General", "Browse InCollege", "Business Solutions", "Directories"]
    self.general_links = ["Sign up", "Help Center", "About", "Press", "Blog", "Careers", "Developers"]
    self.system = AccountSystem()

  # Helper method to print options
  def print_options(self, options, label="Back"):
    for i, option in enumerate(options):
      print(f"{i+1}. {option}")
    print(f"{len(options)+1}. {label}")
    
  # Engine
  def run(self):
    self.menu()
    os.system("clear")
    print("Thank you. Goodbye!")

  # Displays the menu
  def menu(self):
    option = -1
    
    while option != len(self.menu_options) + 1: 
      os.system("clear")
      print("Welcome to inCollege!\n")
      print('"InCollege helped me find a job while in college"-student')
      self.print_options(self.menu_options, "Exit")
      
      option = int(input("> "))
      match option:
        case 1:
          if self.system.login(): 
            self.show_options()
        case 2: 
          print("Video is now playing:")
          input("('press ENTER when done')")
        case 3: 
          if self.system.register(): 
            self.show_options()
        case 4:  
          self.useful_links()
        case 5:
          return
  
  def useful_links(self):
    os.system("clear")
    print("Useful Links:\n")
    self.print_options(self.useful_links)
    option = int(input("> "))

  # The options shown after successfully logging in
  def show_options(self):
    option = -1
    
    while option != 4:
      os.system("clear")
      print("Choose a task:\n")
      self.print_options(self.options)
      
      option = int(input("> "))
      match option:
        case 1:
          self.search_opportunities()
        case 2:
          self.network()
        case 3:
          self.learn_skills()
        case 4:
          return

  def search_opportunities(self):
    option = -1

    while option !=3:
      os.system("clear")
      print("Choose a task:\n")
      self.print_options(self.job_options)

      option = int(input("> "))
      match option:
        case 1:
          self.search_jobs()
        case 2:
          self.post_jobs()
        case 3:
          return  
    
  def load_job_postings(self):
    with open('job_postings.json', 'r') as file:
      jobs = json.load(file)
      
    return jobs

  def search_jobs(self):
    input("Under construction...")
  
  # Handles job posting
  def update_jobs(self,username,job_title,description,employer,location,salary):
    jobs = self.load_job_postings()

      #adding a new job
    jobs[username] = {
    "title": job_title,
    "description": description,
    "employer": employer,
    "location": location,
    "salary": salary
    }
    # Write the updated data back to the file
    with open('job_postings.json', 'w') as file:
      json.dump(jobs, file, indent=2)

  def post_jobs(self):
    success = False
    jobs = self.load_job_postings()
    
    if len(jobs) >= 5:
      input(
        "\nAll permitted jobs have been created, please come back later..."
      )
          
    else:

      while success==False:
        username = input("Username: ")
        job_title = input("Job Title: ")
        description = input("Description: ")
        employer = input("Employer: ")
        location = input("Location: ")
        salary = input("salary: ")

        self.update_jobs(username,job_title,description,employer,location,salary)
        success = True
      
    return success

  def search_people(self,first_name,last_name):
    success = False
    with open('students.json', 'r') as f:
      data = json.load(f)
    for username in data:
      if((data[username]['first_name']==first_name)and (data[username]['last_name']==last_name)):
        success = True
        return success
    return success
    

  # Handles networking
  def network(self):
    first_name = input("First Name: ").capitalize()
    last_name = input("Last Name: ").capitalize()
    if(self.search_people(first_name,last_name)):
      print("They are a part of the InCollege system")
      input(f"A message has been sent to {first_name} {last_name} to log in and connect with you")     
      return True
    else:
      print("They are not a part of the InCollege system")
      input(f"An invite has been sent to {first_name} {last_name} to join InCollege")
      return False

  # Handles learning new skills
  def learn_skills(self):
    option = -1
    
    while option != len(self.skills) + 1:
      os.system("clear")
      print("Select a skill to learn:\n")
      self.print_options(self.skills)
  
      option = int(input("> "))
      match option:
        case option if option in [1,2,3,4,5]:
          input("\nUnder construction...")
        case 6: 
          return
  
      
