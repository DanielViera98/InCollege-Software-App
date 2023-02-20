import json
import os
from AccountAuth import is_secure_password, verify_login_info

MAX_ACCOUNTS = 5

class AccountSystem():

  # Handles login, returns True if login succeeded
  def __init__(self):

    self.accounts = self.load_accounts()
    self.num_accounts = len(self.accounts)

  def load_accounts(self):
    with open('students.json', 'r') as f:
      data = json.load(f)

    return data

  def update_accounts(self):
    data = self.load_accounts()

    self.num_accounts = len(data)
    self.accounts = data

  def add_account(self, username, password, first_name, last_name):
    # Load the contents of the JSON file into a Python dictionary
    with open('students.json', 'r') as file:
      data = json.load(file)

    # Add a new object
    data[username] = {
      "password": password,
      "first_name": first_name,
      "last_name": last_name,
      "language": "en"
    }

    # Write the updated data back to the file
    with open('students.json', 'w') as file:
      json.dump(data, file, indent=2)

    self.update_accounts()


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
          retry = input("Keep trying? (Y/N): ")

          if retry in ['y', 'n', 'Y', 'N']:
            retry = True if retry.lower() == "y" else False
            is_invalid_input = False if retry == True else False

    return success

  # Handles registration, returns True if registration succeeded
  def register(self):
    success = False
    if self.num_accounts >= MAX_ACCOUNTS:
      input(
        "\nAll permitted accounts have been created, please come back later..."
      )

    else:

      os.system("clear")
      print(
        f"Account Registration (# of Accounts Available - {MAX_ACCOUNTS} - {self.num_accounts}:\n"
      )
      print(
        "Password Requirements -\n\tMinimum of 8 characters\n\tMaximum of 12 characters\n\tAt least one capital letter\n\tOne digit\n\tOne special character\n"
      )
      while success == False:
        username = input("Username: ")
        password = input("Password: ")
        first_name = input("First name: ").capitalize()
        last_name = input("Last name: ").capitalize()

        if username not in self.accounts:  # If username does not exist in the database

          if is_secure_password(password):
            success = True
            self.add_account(username, password, first_name, last_name)
            input("\nYou have successfully created an account...")
          else:
            input("Invalid password...")
            return success

        else:
          input("Username taken...")
          return success

    return success