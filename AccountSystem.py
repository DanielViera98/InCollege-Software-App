from replit import db
import os

MAX_ACCOUNTS = 5

class AccountSystem():

	# Handles login, returns True if login succeeded
	def login(self):

		retry = True
		success = False
		while success == False and retry == True:
			os.system("clear")
			print("Login:\n")
			username = input("Username: ")
			password = input("Password: ")

			try:

				if db[username] == password:
					success = True
					input("\nYou have successfully logged in...")
				else:
					raise Exception()

			except:
				success = False
				input("\nIncorrect username or password. Please try again...")
				retry = input("Keep trying? (Y/N): ")
				retry = True if retry.lower() == "y" else False

		return success

	# Handles registration, returns True if registration succeeded
	def register(self):
		success = False
		if len(db) >= MAX_ACCOUNTS:
			input(
			 "\nAll permitted accounts have been created, please come back later...")

		else:

			os.system("clear")
			print(f"Account Registration (# of Accounts Available - {MAX_ACCOUNTS - len(db)}):\n")
			print(
			 "Password Requirements -\n\tMinimum of 8 characters\n\tMaximum of 12 characters\n\tAt least one capital letter\n\tOne digit\n\tOne special character\n"
			)
			while success == False:
				username = input("Username: ")
				password = input("Password: ")

				if not username in db:  # If username does not exist in the database

					if self.is_secure_password(password):
						success = True
						db[username] = password
						input("\nYou have successfully created an account...")
					else:
						input("Invalid password...")
						return success

				else:
					input("Username taken...")
					return success

		return success

	### Handles checking if registered password is secure ###

	def has_capital_letter(self, password):
		for char in password:
			if char.isupper(): return True
		return False

	def has_min_char(self, password):
		return len(password) >= 8

	def has_max_char(self, password):
		return len(password) <= 12

	def has_digit(self, password):
		for char in password:
			if char.isdigit(): return True
		return False

	def has_special_char(self, password):
		for char in password:
			if not char.isalnum(): return True
		return False

	def is_secure_password(self, password):
		return self.has_capital_letter(password) and\
      self.has_min_char(password) and\
      self.has_max_char(password) and\
      self.has_max_char(password) and\
      self.has_digit(password) and\
      self.has_special_char(password)
