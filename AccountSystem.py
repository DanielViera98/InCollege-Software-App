import json
import os
from AccountAuth import is_secure_password, verify_login_info, is_valid_username

MAX_ACCOUNTS = 5

class AccountSystem():

  # Handles login, returns True if login succeeded
  def __init__(self):
    self.accounts = self.load_accounts()
    self.num_accounts = len(self.accounts)

  def load_accounts(self):
    filename = 'students.json'
    if not os.path.exists(filename):
      with open(filename, 'w') as f:
        f.write('{}')  
        
    with open(filename, 'r') as f:
      data = json.load(f)

    return data

  def update_accounts(self):
    data = self.load_accounts()

    self.num_accounts = len(data)
    self.accounts = data

  def add_account(self, username, password, first_name, last_name, email, SMS, targeted_advertising):
    # Load the contents of the JSON file into a Python dictionary
    with open('students.json', 'r') as file:
      data = json.load(file)

    # Add a new object
    data[username] = {
      "password": password,
      "first_name": first_name,
      "last_name": last_name,
      "language": "en",
      "email" : email,
      "SMS" : SMS,
      "targeted_advertising": targeted_advertising,
    }

    # Write the updated data back to the file
    with open('students.json', 'w') as file:
      json.dump(data, file, indent=2)

    self.update_accounts()
    
  def get_account_name(self, username):
    accounts = self.load_accounts()
    name = [accounts[username]["first_name"], accounts[username]["last_name"]]
    return name
  
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

  def toggle_email(self):
    self.email = not self.email
    
  def toggle_SMS(self):
    self.SMS = not self.SMS

  def toggle_targeted_advertising(self):
    self.targeted_advertising = not self.targeted_advertising

#NOT FINISHED
  def set_language(self, username, option):
    accounts = self.load_accounts()
    with open('students.json', 'r') as file:
      data = json.load(file)
    print("In set language")
    

    
    with open('students.json', 'w') as file:
      json.dump(data, file, indent=2)
    #[accounts[username]["language"]] = option
    
  # Handles login, returns True if login succeeded
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

  # Handles registration, returns True if registration succeeded
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
              self.add_account(username, password, first_name, last_name, True, True, True)
              success = True
              input("\nAccount registered...")
            else:
              input("Invalid password...")

          else:
            input("Username taken...")
        
        else:
          input("Invalid username...")

    return success