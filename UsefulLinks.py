
import os
from Helper import print_options
from AccountSystem import AccountSystem

useful_links_list = ["General", "Browse InCollege", "Business Solutions", "Directories"]
general_links = ["Sign up", "Help Center", "About", "Press", "Blog", "Careers", "Developers"]

def useful_links():
  option = -1
  back_option = len(useful_links_list) + 1

  while option != back_option:
    os.system("clear")
    print("Useful Links:\n")
    print_options(useful_links_list)
    
    try:
      option = int(input("> "))
      
      match option:
        case 1:
          general()
        case 2:
          browse()
        case 3:
          solutions()
        case 4:
          directories()
        case 5:
          return
        case _:
          raise Exception()
      
    except:
      input("Invalid Input")
        
def general():
  option = -1
  back_option = len(general_links) + 1

  while option != back_option:
    os.system("clear")
    print("General Links:\n")
    print_options(general_links)
    
    try:
      option = int(input("> "))
      
      match option:
        case 1:
          system = AccountSystem()
          system.register()
        case 2:
          input("We're here to help...")
        case 3:
          input("In College: Welcome to In College, the world's largest college student network with many users in many countries and territories worldwide...")
        case 4:
          input("In College Pressroom: Stay on top of the latest news, updates, and reports...")
        case 5:
          input("Under construction...")
        case 6:
          input("Under construction...")
        case 7:
          input("Under construction...")
        case 8:
          return
        case _:
          raise Exception()
      
    except:
      input("Invalid Input")

def browse():
  input("Under construction...")

def solutions():
  input("Under construction...")

def directories():
  input("Under construction...")