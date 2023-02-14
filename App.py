from AccountSystem import AccountSystem
import os


class InCollege:

  # Constructor
  def __init__(self):
    self.skills = [
     "Learn C", "Learn C#", "Learn Python", "Learn Java", "Learn HTML"
    ]
    self.menu_options = ["Login","Why join InCollege", "Register"]
    self.options = ["Search for jobs", "Find someone you know", "Learn a new skill"]
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
          return

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
          self.search_jobs()
        case 2:
          self.network()
        case 3:
          self.learn_skills()
        case 4:
          return

  # Handles job searches
  def search_jobs(self):
    input("\nUnder construction...")

  # Handles networking
  def network(self):
    input("\nUnder construction...")

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
  
      
