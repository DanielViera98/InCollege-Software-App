from AccountSystem import AccountSystem
from Profiles import Profile_manager
from UsefulLinks import useful_links
from ImportantLinks import links
from Helpers import print_options, print_toggle_options
from Profiles import Profile_manager
from Messaging import Messaging
import os
import json
class InCollege:

  # Constructor
  def __init__(self):
    self.skills = [
     "Learn C", "Learn C#", "Learn Python", "Learn Java", "Learn HTML"
    ]
    self.menu_options = ["Login", "Register", "Why join InCollege", "Useful Links", "Important Links"]
    self.options = ["Job Search/Internship", "Network", "Learn a new skill", "Important Links", "Profile Options"]
    self.guest_control_options = ["Toggle Email", "Toggle SMS", "Toggle Targeted Advertising"]
    self.job_options = ["Display Jobs Options", "Search for jobs", "Post a job","Delete job"]
    self.lang_options = ["English", "Spanish"]
    self.network_options = ["Send Friend Request", "Check Pending Requests", "Manage Friends List", "Inbox & Messaging"]
    self.request_options = ["Accept Friend Request", "Deny Friend Request"]
    self.friends_options = ["Remove Friend", "View Profile"]
    self.profile_options = ["View Profile", "Edit Profile"]
    self.display_jobs_options = ["View All Jobs", "View Saved Jobs", "View Applied Jobs", "View Non-Applied Jobs"]
    self.displayed_jobs_options = ["View Job Info"]
    self.inbox_messaging_options = ["View Inbox", "Send Message to Friend", "Send Message to Anyone"]
    self.message_options = ["View Message", "Reply to Message", "Delete Message"]
    self.jobs_save_apply = ["Save Job","Apply for Job"]
    self.system = AccountSystem()
    self.user = False
    self.profile = Profile_manager()
    self.jobs = self.load_job_postings()
    
  # Engine
  def run(self):
    self.menu()
    os.system("clear")
    print("Thank you for using inCollege. Goodbye!")
  
  #Allows user to swap language preference between English & Spanish. Doesn't actually do anything
  #except change language value between 'es' and 'en'
  def set_language(self):
    if (self.user == False):
        os.system("clear")
        input("Not logged in")
        return
    option = -1
    back_option = len(self.lang_options) + 1
    
    while option != back_option:
      os.system("clear")
      print("Language:\n")
      print_options(self.lang_options)
      accounts = self.system.load_accounts()
      
      try:
        option = int(input("> "))
        match option:
          case 1:
            accounts[self.user]['language'] = 'en'
            input("Language changed to English...")
          case 2:
            accounts[self.user]['language'] = 'es'
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
          
      with open('students.json', 'w') as file:
              json.dump(accounts, file, indent=2)
          
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
              username = self.system.register()
              if username:
                self.user = username
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
      accounts = self.system.load_accounts()
      os.system("clear")
      #If user has requests, print alert message
      if (accounts[self.user]['requests']):
        print(f">>>      You have {len(accounts[self.user]['requests'])} Friend Requests. To view them, go to Network      <<<")
      
      print("Choose a task:\n")
      print_options(self.options)  
      try:
        option = int(input("> "))
        match option:
          case 1:
            self.jobs_info()
          case 2:
            self.network()
          case 3:
            self.learn_skills()
          case 4:
            self.important_links()
          case 5:
            self.profile_controls()
          case 6:
            self.user = False
            return
          case _:
            raise Exception()
          
      except Exception as e:
        if type(e) == ValueError:
          input("Invalid input...")
        else:
          input(f"Error: {e} {type(e)}")

  #Manages Jobs options, both search & post
  def jobs_info(self):
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
            self.display_jobs()
          case 2:
            self.search_jobs()
          case 3:
            self.post_jobs()
          case 4:
            self.delete_job()
          case 5:
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
        f.write('[]')  
        
    with open(filename, 'r') as file:
      jobs = json.load(file)
    
    return jobs

  def display_jobs(self):
    option = -1
    back_option = len(self.display_jobs_options) + 1
    
    while option != back_option:
      os.system("clear")
      if self.jobs == []:
        input("No jobs posted, press ENTER to return. ")
        return "Empty"
      
      try:
        os.system("clear")
        print_options(self.display_jobs_options)
        option = int(input("> "))
        accounts = self.system.load_accounts()
        match option:
          case 1:
            self.view_all_jobs()
          case 2:
            if accounts[self.user]['saved_jobs'] == []:
              input("No saved jobs. Hit ENTER to continue. ")
              break
            self.view_selected_jobs(accounts[self.user]['saved_jobs'])
          case 3:
            self.view_selected_jobs(accounts[self.user]['applied_jobs'])
          case 4:
            jobs = self.load_job_postings()
            non_applied_jobs = []
            for job in jobs:
              match = False
              for applied in accounts[self.user]['applied_jobs']:
                if applied == job['title']:
                  match = True
              if match == False:
                non_applied_jobs.append(job['title'])
            self.view_selected_jobs(non_applied_jobs)
          case 5:
            return
          case _:
            raise Exception()
          
      except Exception as e:
          if type(e) == ValueError:
            input("Invalid input...")
          else:
            input(f"Error: {e} {type(e)}")
  
  def view_all_jobs(self):
    option = -1
    back_option = len(self.displayed_jobs_options) + 1
    
    while option != back_option:
      os.system("clear")
      
      i = 0
      print("Job Listings:\n------------------------")
      for job in self.jobs:
        print(i+1, ". ",  job['title'])
        i += 1
      print("------------------------")
      print("Choose a task:\n")
      print_options(self.displayed_jobs_options)
      
      try:
        
        option = int(input("> "))
        
        match option:
          case 1:
            choice = int(input("Which job would you like to display? ")) - 1
            self.show_job_info(self.jobs[choice])
          case 2:
            return
          case _:
            raise Exception()
          
      except Exception as e:
          if type(e) == ValueError:
            input("Invalid input...")
          else:
            input(f"Error: {e} {type(e)}")

  def view_selected_jobs(self, jobs_list):
    option = -1
    back_option = len(self.displayed_jobs_options) + 1
    
    while option != back_option:
      os.system("clear")
      self.jobs = self.load_job_postings()
      i = 0
      print("Job Listings:\n------------------------")
      for job in self.jobs:
        for item in jobs_list:
          if job['title'] == item:
            print(i+1, ". ",  job['title'])
            i += 1
      print("------------------------")
    
      print("Choose a task:\n")
      print_options(self.displayed_jobs_options)
      
      try:
        option = int(input("> "))
        match option:
          case 1:
            choice = int(input("Which job would you like to display? ")) - 1
            self.show_job_info(self.jobs[choice])
          case 2:
            return
          case _:
            raise Exception()
          
      except Exception as e:
          if type(e) == ValueError:
            input("Invalid input...")
          else:
            input(f"Error: {e} {type(e)}")    

  def show_job_info(self, job):
    os.system("clear")
    accounts = self.system.load_accounts()
    print(job['title'], ":")
    print("\tPoster: ", job['poster'])
    print("\tDescription:", job['description'])
    print("\tEmployer:", job['employer'])
    print("\tLocation:", job['location'])
    print("\tSalary:", job['salary'])

    if job['title'] not in accounts[self.user]['saved_jobs']:
      print("1. Save Job")
      save = True
    else:
      print("1. Unsave Job")
      save = False

    if job['title'] not in accounts[self.user]['applied_jobs']:
      print("2. Submit Application")
      submit = True
    else:
      print("2. Cancel Application")
      submit = False
    print("3. Return")
    choice = int(input("> "))
    
    print(choice)
    match choice: 
      case 1:
        if save == True:
          accounts[self.user]['saved_jobs'].append(job['title'])
          input("Job Saved! Press Enter to return. ")
          saved = "Saved"
        else:
          accounts[self.user]['saved_jobs'].remove(job['title'])
          input("Job Unsaved! Press Enter to return. ")
          saved = "Unsaved"
        with open('students.json', 'w') as file:
          json.dump(accounts, file, indent=2)
        return saved
      case 2:
        if submit == True:
          accounts[self.user]['applied_jobs'].append(job['title'])
          input("Application Submitted! Press Enter to return. ")
        else:
          accounts[self.user]['applied_jobs'].remove(job['title'])
          input("Application Canceled. Press Enter to return. ")
        with open('students.json', 'w') as file:
          json.dump(accounts, file, indent=2)
        return
      case 3:
        return
      
  def job_select(self):
    os.system("clear")
    job = input("Which job would you like to apply for: ")
    return job
  
  def job_apply(self,job):
    os.system("clear")
    accounts = self.system.load_accounts()
    accounts[self.user]['applied jobs'].append(job['title'])

  def search_jobs(self):
    input("Under construction...")
  
  # Handles job posting
  def update_jobs(self,name,job_title,description,employer,location,salary):
    jobs = self.load_job_postings()
    #adding a new job
    new_job = {
    "poster": name,
    "title": job_title,
    "description": description,
    "employer": employer,
    "location": location,
    "salary": salary
    }
    jobs.append(new_job)
    # Write the updated data back to the file
    with open('job_postings.json', 'w') as file:
      json.dump(jobs, file, indent=2)
    self.jobs = self.load_job_postings()

  def post_jobs(self):
    success = False
    jobs = self.load_job_postings()
    
    if len(jobs) >= 10:
      input(
        "\nAll permitted jobs have been created, please come back later..."
      )
          
    else:
      while success==False:
        job_title = input("Job Title: ")
        description = input("Description: ")
        employer = input("Employer: ")
        location = input("Location: ")
        salary = input("Salary: ")

        name = self.system.get_account_name(self.user)
        full_name = ' '.join(name)
        self.update_jobs(full_name,job_title,description,employer,location,salary)
        input("Job posting created...")
        success = True
      
    return success
  
  def delete_job(self):
    jobs =  self.load_job_postings()
    name = self.system.get_account_name(self.user)
    full_name = ' '.join(name)
    count = 0
    for job in jobs:
      if full_name == job['poster']:
        print(job['title'])
        count+=1
    
    if(count == 0):
      input("You have not yet posted any jobs to be deleted")
      return False
    
    job_del=input("Which job would you like to delete?")
    for job in jobs:
      if (job['title'] == job_del):
        if(job['poster']==full_name):
          jobs.remove(job)
          print("DONE")
          with open('job_postings.json', 'w') as file:
            json.dump(jobs, file, indent=2)
          self.jobs = self.load_job_postings()
          return True
        else:
          input("You did not post this job")
          return False

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
            self.inbox_and_messaging()
          case 5:
            return
          case _:
            raise Exception()
          
      except Exception as e:
        if type(e) == ValueError:
          input("Invalid input...")
        else:
          input(f"Error: {e} {type(e)}")
  
  #Adds username to "requests" array of searched user if present
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

  #If user has requests, print. Else, show "No Friend Requests and return."
  def pending_requests(self):
    accounts = self.system.load_accounts()
    option = -1
    back_option = len(self.options) + 1
    
    while option != back_option:
      os.system("clear")
      requests = []
      i = int(0)
      for u in accounts[self.user]['requests']:
        requests.append(u)
        print(f"{i+1}. {u}")
      if (len(requests) == 0):
        input("No Friend Requests")
        return
      print("\nChoose a task:\n")
      print_options(self.request_options)
      
      try:
        option = int(input("> "))
        
        match option:
          case 1:
            self.accept_request(accounts, requests)
          case 2:
            self.delete_request(accounts, requests)
          case 3:
            return
          case _:
            raise Exception()
          
      except Exception as e:
        if type(e) == ValueError:
          input("Invalid input...")
        else:
          input(f"Error: {e} {type(e)}")

  #accepts pending friend from 'requests' list of self.user
  def accept_request(self, accounts, requests):
    option = -1
    back_option = len(requests) + 1
    
    while option != back_option:
      os.system("clear")
      print("Pending Requests:")
      requests = accounts[self.user]['requests']
      back_option = len(requests) + 1

      if (len(requests) == 0):  #If no more requests, print so and return
        input("No Friend Requests")
        return
      print_options(requests)
      
      try:
        option = int(input(f"\nChoose a request to accept, or enter {back_option} to exit\n> "))
        if (option == back_option):
          return
        choice = requests[option-1]
        
        #Accepts request, adds sender to reciever's friends list and vice versa
        if (requests[option-1]):
          accounts[self.user]['friends_list'].append(choice)
          accounts[choice]['friends_list'].append(self.user)
          accounts[self.user]['requests'].remove(choice)
          
          with open('students.json', 'w') as file:
            json.dump(accounts, file, indent=2)
          input(f"Accepted {choice}!")
        else:  
          raise Exception()
          
      except Exception as e:
        if type(e) == ValueError:
          input("Invalid input...")
        else:
          input(f"Error: {e} {type(e)}")
          
  #denies pending friend from 'requests' list of self.user
  def delete_request(self, accounts, requests):
    option = -1
    back_option = len(requests) + 1

    while option != back_option:
      os.system("clear")
      print("Pending Requests:")
      requests = accounts[self.user]['requests']
      if (len(requests) == 0):      #If no more requests, print so and return
        input("No Friend Requests")
        return
      back_option = len(requests) + 1
      print_options(requests)
      
      try:
        option = int(input(f"\nChoose a request to deny, or enter {back_option} to exit\n> "))
        if (option == back_option):
          return
        choice = requests[option-1]
  
        if (requests[option-1]):
          accounts[self.user]['requests'].remove(choice)
          
          with open('students.json', 'w') as file:
            json.dump(accounts, file, indent=2)
          input(f"Denied {choice}!")
        else:  
          raise Exception()
          
      except Exception as e:
        if type(e) == ValueError:
          input("Invalid input...")
        else:
          input(f"Error: {e} {type(e)}")
    
  #Prints friends if exist, gives user option to delete friend or return
  def manage_friends(self):
    accounts = self.system.load_accounts()
    option = -1
    back_option = len(self.friends_options) + 1
    while option != back_option:
      os.system("clear")
      if len(accounts[self.user]['friends_list']) == 0:
        input("Nobody here, go to \"Network -> Send Friend Request\" to find a friend! ")
        return
      i = 0
      for u in accounts[self.user]['friends_list']:
        if self.profile.get_profile(u) == False:
          print(f"{i+1}. {u} - No Profile Created") 
        else:
          print(f"{i+1}. {u} - Profile Created!")
        i = i+1
      print("\nChoose a task:\n")
      print_options(self.friends_options)
      
      try:
        option = int(input("> "))
        
        match option:
          case 1:
            remove = int(input("Which friend would you like to remove? "))
            username = accounts[self.user]['friends_list'][remove-1]
            accounts[self.user]['friends_list'].remove(username)
            accounts[username]['friends_list'].remove(self.user)
            input("Friend Removed.")
            with open('students.json', 'w') as file:
              json.dump(accounts, file, indent=2)
          case 2:
            view = int(input("Which friend's profile would you like to view? "))
            username = accounts[self.user]['friends_list'][view-1]
            self.profile.view_profile(username)
            input("Press ENTER to return to friend's list. ")
          case 3:
            return
          case _:
            raise Exception()
          
      except Exception as e:
        if type(e) == ValueError:
          input("Invalid input...")
        else:
          input(f"Error: {e} {type(e)}")

  #Lets user navigate to inbox or send a message to friends, or anyone if premium
  def inbox_and_messaging(self):
    option = -1
    back_option = len(self.inbox_messaging_options) + 1
    while option != back_option:
      os.system("clear")
      print("\nChoose a task:\n")
      print_options(self.inbox_messaging_options)
      try:
        option = int(input("> "))
        match option:
          case 1:
            self.view_inbox()
          case 2:
            self.send_message_friend()
          case 3:
            self.send_message_anyone()
          case 4:
            return
          case _:
            raise Exception()
          
      except Exception as e:
        if type(e) == ValueError:
          input("Invalid input...")
        else:
          input(f"Error: {e} {type(e)}")
    
  #Lets user view inbox and either view a message, reply, or delete messages
  def view_inbox(self):
    
    option = -1
    back_option = len(self.message_options) + 1
    while option != back_option:
      accounts = self.system.load_accounts()
      os.system("clear")
      if accounts[self.user]['message_inbox'] == []:
        print("You have no messages!")
        input("Press ENTER to return. ")
        return "Empty"
      print("INBOX: ")
      i = 1
      for item in accounts[self.user]['message_inbox']:
        print("Message", i, ", from", item[0], ":\n[", item[1][:15], "]...\n")
      
      print("\nChoose a task:\n")
      print_options(self.message_options)
      try:
        option = int(input("> "))
        match option:
          case 1:
            choice = int(input("Which message would you like to view? "))
            self.view_message(accounts[self.user]['message_inbox'][choice-1], choice-1)
          case 2:
            num = int(input("Which message would you like to reply to?"))
            reply = input("Enter reply: ")
            new_message = Messaging(self.user, accounts[self.user]['message_inbox'][num-1][0])
            new_message.send_message(reply)
          case 3:
            num = int(input("Which message would you like to delete? "))
            self.delete_message(num-1)
          case 4:
            return
          case _:
            raise Exception()
          
      except Exception as e:
        if type(e) == ValueError:
          input("Invalid input...")
        else:
          input(f"Error: {e} {type(e)}")
  
  #View full message and reply or delete
  def view_message(self, message, num):
    option = -1
    back_option = len(self.message_options) + 1
    while option != back_option:
      os.system("clear")
      print("FULL MESSAGE")
      print("Sender,", message[0])
      print("Message:", message[1])
      print("\nChoose a task:\n")
      print_options(self.message_options[1:])
      try:
        option = int(input("> "))
        match option:
          case 1:
            reply = input("Enter reply: ")
            new_message = Messaging(self.user, message[0])
            new_message.send_message(reply)
          case 2:
            return self.delete_message(num)
          case 3:
            return
          case _:
            raise Exception()
      except Exception as e:
        if type(e) == ValueError:
          input("Invalid input...")
        else:
          input(f"Error: {e} {type(e)}")
  
  #deletes message from user inbox
  def delete_message(self, number):
    accounts = self.system.load_accounts()
    accounts[self.user]['message_inbox'].pop(number)
    with open('students.json', 'w') as f:
      json.dump(accounts, f, indent=2)
    input("Message Deleted!")
    return True
    
  #prompts user to send a messsage to a friend
  def send_message_friend(self):
    accounts = self.system.load_accounts()
    os.system("clear")
    print("FRIENDS")
    if len(accounts[self.user]['friends_list']) == 0:
        input("Nobody here, go to \"Network -> Send Friend Request\" to find a friend! ")
        return False
    i = 0
    for u in accounts[self.user]['friends_list']:
      print(f"{i+1}. {u}")
      i = i+1
    
    choice = int(input("Which friend would you like to message? "))
    friend = accounts[self.user]['friends_list'][choice-1]
    new_message = Messaging(self.user, friend)
    
    message = input("Send a message: ")
    new_message.send_message(message)
    input("Press ENTER to return. ")
    return True
    
  def send_message_anyone(self):
    os.system("clear")
    accounts = self.system.load_accounts()
    if accounts[self.user]['plus_status'] == False:
      input("Function only available to InCollege Plus members. ")
      return False
    print("USERS")
    i = 0
    for u in accounts:
      print(f"{i+1}. {u}")
      i = i+1
    
    choice = int(input("Which user would you like to message? "))
    i = 0
    for u in accounts:
      if i == choice-1:
        recipient = u
        break
      i = i+1
    new_message = Messaging(self.user, recipient)
    
    message = input("Send a message: ")
    new_message.send_message(message)
    input("Press ENTER to return. ")
    return True
    
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

  #Sends user to privacy policy or set language
  def important_links(self):
    value = None
    value = links()
    if value == "privacy":
      self.privacy_policy()
    if value == "language":
      self.set_language()
  
  #Prints privacy policy, sends user to guest controls if chosen
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
  
  #Gives user option to toggle email, sms, and targeted advertising
  def guest_controls(self):
    if (self.user == False):
        os.system("clear")
        input("Not logged in")
        return
    option = -1
    back_option = len(self.skills) + 1
    
    while option != back_option:
      email = self.system.get_email(self.user)
      sms = self.system.get_SMS(self.user)
      targeted_advertising = self.system.get_targeted_advertising(self.user)
      
      toggle_options = [email, sms, targeted_advertising]
      options = zip(self.guest_control_options, toggle_options)
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

  def profile_controls(self):
    option = -1
    back_option = len(self.profile_options) + 1
    while option != back_option:
      self.profile = Profile_manager()
      os.system("clear")
      print("Choose a task:\n")
      print_options(self.profile_options)
      try:
        option = int(input("> "))
        match option:
          case 1:
            self.profile.view_profile(self.user)
            input("Press ENTER to return to profile options. ")
          case 2:
            self.profile.edit_profile(self.user)
          case 3:
            return
          case _:
            raise Exception()
          
      except Exception as e:
        if type(e) == ValueError:
          input("Invalid input...")
        else:
          input(f"Error: {e} {type(e)}")
