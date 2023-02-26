from AccountSystem import AccountSystem
from UsefulLinks import useful_links
from ImportantLinks import links
from Helpers import print_options, print_toggle_options
import os
import json
class InCollege:

  # Constructor
  def __init__(self):
    self.skills = [
     "Learn C", "Learn C#", "Learn Python", "Learn Java", "Learn HTML"
    ]
    self.menu_options = ["Login", "Register", "Why join InCollege", "Useful Links", "Important Links"]
    self.options = ["Job Search/Internship", "Network", "Learn a new skill", "Important Links"]
    self.guest_control_options = ["Toggle Email", "Toggle SMS", "Toggle Targeted Advertising"]
    self.job_options = ["Search for jobs", "Post a job"]
    self.lang_options = ["English", "Spanish"]
    self.network_options = ["Send Friend Request", "Check Pending Requests", "Manage Friends List"]
    self.request_options = ["Accept Friend Request", "Deny Friend Request"]
    self.system = AccountSystem()
    self.user = False
    
  # Engine
  def run(self):
    self.menu()
    os.system("clear")
    print("Thank you for using inCollege. Goodbye!")

  
  def set_language(self):

    option = -1
    back_option = len(self.lang_options) + 1

    while option != back_option:
      os.system("clear")
      print("Language:\n")
      print_options(self.lang_options)

      try:
        option = int(input("> "))
        match option:
          case 1:
            self.system.set_language(self.user, "English")
            input("Language changed to English...")
          case 2:
            self.system.set_language(self.user, "Spanish")
            input("Language changed to Spanish...")
          case 3:
            return 
          case _:
            raise Exception() 
          
      except Exception as e:
        if type(e) == ValueError:
          input("Invalid input...")
        else:
          input(f"Error: {e} {type(e)}")
          
  # Displays the menu
  def menu(self):
    option = -1
    back_option = len(self.menu_options) + 1
    self.username = False
    
    while option != back_option: 
      os.system("clear")
      print("Welcome to inCollege!\n")
      print('"InCollege helped me find a job while in college"-student')
      print_options(self.menu_options, "Exit")
      
      try:
        option = int(input("> "))

        match option:
          case 1:
            username = self.system.login()
            if isinstance(username, str):
              self.user = username
              self.show_options()
          case 2: 
            if self.system.register(): 
              self.show_options()
          case 3: 
            print("Video is now playing:")
            input("('press ENTER when done')")
          case 4:  
            useful_links()
          case 5:
            self.important_links()
          case 6:
            return
          case _:
            raise Exception()
        
      except Exception as e:
        if type(e) == ValueError:
          input("Invalid input...")
        else:
          input(f"Error: {e} {type(e)}")
  
  # The options shown after successfully logging in
  def show_options(self):
    option = -1
    back_option = len(self.options) + 1
    
    while option != back_option:
      os.system("clear")
      print("Choose a task:\n")
      print_options(self.options)
      
      try:
        option = int(input("> "))
        
        match option:
          case 1:
            self.search_opportunities()
          case 2:
            self.network()
          case 3:
            self.learn_skills()
          case 4:
            self.important_links()
          case 5:
            return
          case _:
            raise Exception()
          
      except Exception as e:
        if type(e) == ValueError:
          input("Invalid input...")
        else:
          input(f"Error: {e} {type(e)}")


  def search_opportunities(self):
    option = -1
    back_option = len(self.job_options) + 1

    while option != back_option:
      os.system("clear")
      print("Job Search/Internship:\n")
      print_options(self.job_options)

      try:
        option = int(input("> "))
        
        match option:
          case 1:
            self.search_jobs()
          case 2:
            self.post_jobs()
          case 3:
            return 
          case _:
            raise Exception() 
          
      except Exception as e:
        if type(e) == ValueError:
          input("Invalid input...")
        else:
          input(f"Error: {e} {type(e)}")
          
    
  def load_job_postings(self):
    filename = "job_postings.json"
    if not os.path.exists(filename):
      with open(filename, 'w') as f:
        f.write('{}')  
        
    with open(filename, 'r') as file:
      jobs = json.load(file)
    
    return jobs

  def search_jobs(self):
    input("Under construction...")
  
  # Handles job posting
  def update_jobs(self,name,job_title,description,employer,location,salary):
    jobs = self.load_job_postings()
    
    #adding a new job
    jobs[len(jobs)+1] = {
    "poster": name,
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
        job_title = input("Job Title: ")
        description = input("Description: ")
        employer = input("Employer: ")
        location = input("Location: ")
        salary = input("salary: ")

        name = self.system.get_account_name(self.user)
        full_name = ' '.join(name)
        self.update_jobs(full_name,job_title,description,employer,location,salary)
        input("Job posting created...")
        success = True
      
    return success

  def search_people(self,first_name,last_name):
    success = False
    with open('students.json', 'r') as f:
      data = json.load(f)
    for username in data:
      if((data[username]['first_name']==first_name)and (data[username]['last_name']==last_name)):
        success = True
        return username
    return success
    

  # Handles networking
  def network(self):
    
    option = -1
    back_option = len(self.options) + 1
    
    while option != back_option:
      os.system("clear")
      print("Choose a task:\n")
      print_options(self.network_options)
      
      try:
        option = int(input("> "))
        
        match option:
          case 1:
            self.send_request()
          case 2:
            self.pending_requests()
          case 3:
            self.manage_friends()
          case 4:
            return
          case _:
            raise Exception()
          
      except Exception as e:
        if type(e) == ValueError:
          input("Invalid input...")
        else:
          input(f"Error: {e} {type(e)}")
          
  def send_request(self):
    first_name = input("First Name: ").capitalize()
    last_name = input("Last Name: ").capitalize()
    username = self.search_people(first_name, last_name)
    if(username != False):
      #Gets username of target, appends username of sender into requests
      print("They are a part of the InCollege system")
      accounts = self.system.load_accounts()
      accounts[username]['requests'].append(self.user)
      with open('students.json', 'w') as file:
        json.dump(accounts, file, indent=2)
      input(f"A message has been sent to {first_name} {last_name} to log in and connect with you")     
      return True
    else:
      print("They are not a part of the InCollege system")
      input(f"An invite has been sent to {first_name} {last_name} to join InCollege")
      return False

  def pending_requests(self):
    accounts = self.system.load_accounts()
    option = -1
    back_option = len(self.options) + 1
    
    while option != back_option:
      os.system("clear")
      for u in accounts[self.user]['requests']:
        print(u)
      
      print("\nChoose a task:\n")
      print_options(self.request_options)
      
      try:
        option = int(input("> "))
        
        match option:
          case 1:
            self.accept_friend(accounts)
          case 2:
            self.delete_friend(accounts)
          case 3:
            return
          case _:
            raise Exception()
          
      except Exception as e:
        if type(e) == ValueError:
          input("Invalid input...")
        else:
          input(f"Error: {e} {type(e)}")

  def accept_friend(self, accounts):
    delete = input("Enter the request to deny: ")
    
  # Handles learning new skills
  def learn_skills(self):
    option = -1
    back_option = len(self.skills) + 1
    
    while option != back_option:
      os.system("clear")
      print("Select a skill to learn:\n")
      print_options(self.skills)

      try:
        option = int(input("> "))
        match option:
          case option if option in [1,2,3,4,5]:
            input("Under construction...")
          case 6: 
            return
          case _:
            raise Exception()
          
      except Exception as e:
        if type(e) == ValueError:
          input("Invalid input...")
        else:
          input(f"Error: {e} {type(e)}")

  def important_links(self):
    value = None
    value = links()
    if value == "privacy":
      self.privacy_policy()
    if value == "language":
      self.set_language()
  
  def privacy_policy(self):
    file = open("Misc Files/privacy policy.txt", "r")
    os.system("clear")
    print("Privacy Policy: ")
    print(file.read())
    privacy_options = ["Guest Controls"]
    print_options(privacy_options)
    option = int(input("> "))
    try:    
        if option == 1:
            self.guest_controls()
        elif option == 2:
            file.close()
            return
        else:
            file.close()
            raise Exception()
        
    except Exception as e:
            if type(e) == ValueError:
                input("Invalid input...")
                privacy_options()
            else:
                input(f"Error: {e} {type(e)}")
                privacy_options()
    file.close()
    
  def guest_controls(self):
    option = -1
    back_option = len(self.skills) + 1
    email = self.system.get_email(self.user)
    sms = self.system.get_SMS(self.user)
    targeted_advertising = self.system.get_targeted_advertising(self.user)
    
    toggle_options = [email, sms, targeted_advertising]
    options = zip(self.guest_control_options, toggle_options)
    
    while option != back_option:
      os.system("clear")
      print("Select an option:\n")
      print_toggle_options(options)
        
      try:    
          option = int(input("> "))
          match option:
              case 1:
                  print("Try 1")
                  self.system.toggle_email(self.user)
              case 2:
                  print("Try 2")
                  self.system.toggle_SMS(self.user)
              case 3:
                  print("Try 3")
                  self.system.toggle_targeted_advertising(self.user)
              case 4:
                  return
              case _:
                  raise Exception()
      
      except Exception as e:
              if type(e) == ValueError:
                  input("Invalid input...")
              else:
                  input(f"Error guest: {e} {type(e)}")
