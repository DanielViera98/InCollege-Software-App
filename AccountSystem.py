import json
import os
from AccountAuth import is_secure_password, verify_login_info, is_valid_username
from Profiles import Profile_manager

MAX_ACCOUNTS = 10

class AccountSystem():

  #Initialize
  def __init__(self):
    self.filename = 'students.json'
    self.accounts = self.load_accounts()
    self.num_accounts = len(self.accounts)

  #Pull accounts from students.json and return them. If .json doesn't exist, create empty .json
  def load_accounts(self):
    if not os.path.exists(self.filename):
      input("DELETING STUDENTS")    #Trying to catch account removal
      with open(self.filename, 'w') as f:
        f.write('{}')  
        
    with open(self.filename, 'r') as f:
      data = json.load(f)

    return data

  def update_accounts(self):
    data = self.load_accounts()

    self.num_accounts = len(data)
    self.accounts = data

  #Create an account with all user entered input and add to .json
  def add_account(self, username, password, first_name, last_name):
    # Load the contents of the JSON file into a Python dictionary
    with open('students.json', 'r') as file:
      data = json.load(file)

    # Add a new object
    data[username] = {
      "password": password,
      "first_name": first_name,
      "last_name": last_name,
      "plus_status": False,
      "language": "en",
      "email" : True,
      "SMS" : True,
      "targeted_advertising" : True,
      "friends_list" : [],
      "requests" : [],
      "saved_jobs" : [],
      "applied_jobs" : [],
      "message_inbox" : []
    }


    # #asking if you want to sign up for InCollege+
    question = input("Do you want to sign up for InColege+ (y/n)")
    if(question == "y"):
      data[username]['plus_status'] = True
      
    # # Write the updated data back to the file
    with open('students.json', 'w') as file:
      json.dump(data, file, indent=2)

    # #asking if they want to edit profile:
    question = input("Would you like to customize your profile?(y/n)")
    if(question == "y"):
      new_profile = Profile_manager()
      new_profile.edit_profile(username)
      
    
    self.update_accounts()
 
  #Returns full name ("first" + " " + "last") of user "username"
  def get_account_name(self, username):
    accounts = self.load_accounts()
    name = [accounts[username]["first_name"], accounts[username]["last_name"]]
    return name
  
  #The following seven functions get and toggle user guest controls
  def get_plus_status(self,username):
    accounts = self.load_accounts()
    plus_status = accounts[username]["plus_status"]
    return plus_status
  
  def get_targeted_advertising(self, username):
    accounts = self.load_accounts()
    targeted_advertising = accounts[username]["targeted_advertising"]
    return targeted_advertising
  
  def get_email(self, username):
    accounts = self.load_accounts()
    email = accounts[username]["email"]
    return email
  
  def get_SMS(self, username):
    accounts = self.load_accounts()
    SMS = accounts[username]["SMS"]
    return SMS

  def toggle_email(self, user):
    accounts = self.load_accounts()
    accounts[user]['email'] = not accounts[user]['email']
    
    with open('students.json', 'w') as file:
      json.dump(accounts, file, indent=2)
    
  def toggle_SMS(self, user):
    accounts = self.load_accounts()
    accounts[user]['SMS'] = not accounts[user]['SMS']
    
    with open('students.json', 'w') as file:
      json.dump(accounts, file, indent=2)

  def toggle_targeted_advertising(self, user):
    accounts = self.load_accounts()
    accounts[user]['targeted_advertising'] = not accounts[user]['targeted_advertising']
    
    with open('students.json', 'w') as file:
      json.dump(accounts, file, indent=2)
  
  # Handles login, returns username if login succeeded
  def login(self):

    retry = True
    success = False
    while success == False and retry == True:
      os.system("clear")
      print("Login:\n")
      username = input("Username: ")
      password = input("Password: ")

      if verify_login_info(self.accounts, username, password):
        success = True
        input("\nYou have successfully logged in...")
      else:
        success, is_invalid_input = False, True
        input("\nIncorrect username or password. Please try again...")

        while is_invalid_input:
          os.system("clear")
          retry = input("Keep trying? (Y/N): ")

          if retry in ['y', 'n', 'Y', 'N']:
            retry = True if retry.lower() == "y" else False
            is_invalid_input = False if retry == True else False
          else:
            input("Invalid input...")

    if success: 
      return username
    else: 
      return False

  # Handles registration, returns username if registration succeeded
  def register(self):
    success = False
    if self.num_accounts >= MAX_ACCOUNTS:
      input(
        "\nAll permitted accounts have been created, please come back later..."
      )

    else:
      username, password = "", ""
      while not is_valid_username(username) and not is_secure_password(password):
        os.system("clear")
        print(
          f"Account Registration (# of Accounts Available - {MAX_ACCOUNTS - self.num_accounts}:\n"
        )
        print(
          "Password Requirements -\n\tMinimum of 8 characters\n\tMaximum of 12 characters\n\tAt least one capital letter\n\tOne digit\n\tOne special character\n"
        )
        
        username = input("Username: ")
        if is_valid_username(username): 

          if username not in self.accounts:  # If username does not exist in the database
            password = input("Password: ")
            if is_secure_password(password):
              first_name = input("First name: ").capitalize()
              last_name = input("Last name: ").capitalize()
              self.add_account(username, password, first_name, last_name)
              success = True
              input("\nAccount registered...")
            else:
              input("Invalid password...")

          else:
            input("Username taken...")
        
        else:
          input("Invalid username...")

    if success:
      return username
    else:
      return False
    
  def get_notifications(self, user):
    accounts = self.load_accounts()
    notifications = []
    if accounts[user]['apply_notif']:
      notifications.append("Remember – you're going to want to have a job when you graduate. \
                           Make sure that you start to apply for jobs today!")
    if accounts[user]['is_profile_created']:
      notifications.append("Don't forget to create a profile")
    if accounts[user]['message_inbox']:
      notifications.append("You have messages waiting for you")
    if accounts[user]['applied_jobs']:
      notifications.append(f"You have currently applied for {len(accounts[user]['applied_jobs'])} jobs")
    if accounts[user]['new_jobs']:
      for item in accounts[user]['new_jobs']:
        notifications.append(f"A new job {item} has been posted.")
    if accounts[user]['removed_jobs']:
      for item in accounts[user]['removed_jobs']:
        notifications.append(f"A job you have applied for({item}) has been deleted. ")
      