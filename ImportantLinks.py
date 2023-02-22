import os
from Helpers import print_options

important_links_list = ["A Copyright Notice", "About", "Accessibility", "User Agreement", 
                        "Privacy Policy", "Cookie Policy", "Copyright Policy", "Brand Policy",
                        "Languages"]


def links():
    option = -1
    back_option = len(important_links_list) + 1
    
    while option != back_option:
        os.system("clear")
        print("InCollege Important Links:\n")
        print_options(important_links_list)
        
        try:
            option = int(input("> "))
            match option:
                case 1:
                    copyright_notice()
                case 2:
                    about()
                case 3:
                    accessibility()
                case 4:
                    user_agreement()
                case 5:
                    return "privacy"
                    #privacy_policy(self)
                case 6:
                    cookie_policy()
                case 7:
                    copyright_policy()
                case 8:
                    brand_policy()
                case 9:
                    return "language"
                case 10:
                    return
                case _:
                    raise Exception()
                
        except Exception as e:
            if type(e) == ValueError:
                input("Invalid input...")
            else:
                input(f"Error: {e} {type(e)}")

def copyright_notice():
    file = open("Misc Files/copyright.txt", "r")
    os.system("clear")
    print("Copyright Notice: ")
    print(file.read())
    input("> Hit enter to return: ")
    file.close()
    
def about():
    file = open("Misc Files/about.txt", "r")
    os.system("clear")
    print("About: ")
    print(file.read())
    input("> Hit enter to return: ")
    file.close()
    
def accessibility():
    file = open("Misc Files/accessibility.txt", "r")
    os.system("clear")
    print("Accessibility: ")
    print(file.read())
    input("> Hit enter to return: ")
    file.close()
    
def user_agreement():
    file = open("Misc Files/user agreement.txt", "r")
    os.system("clear")
    print("User Agreement: ")
    print(file.read())
    input("> Hit enter to return: ")
    file.close()
    
def privacy_policy(self):
    file = open("Misc Files/privacy policy.txt", "r")
    os.system("clear")
    print("Privacy Policy: ")
    print(file.read())
    privacy_options = ["Guest Controls"]
    print_options(privacy_options)
    option = int(input(">"))
    try:    
        if option == 1:
            guest_controls(self)
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
    
def cookie_policy():
    file = open("Misc Files/cookie policy.txt", "r")
    os.system("clear")
    print("Cookie Policy: ")
    print(file.read())
    input("> Hit enter to return: ")
    file.close()
    
def copyright_policy():
    file = open("Misc Files/copyright policy.txt", "r")
    os.system("clear")
    print("Copyright Policy: ")
    print(file.read())
    input("> Hit enter to return: ")
    file.close()
    
def brand_policy():
    file = open("Misc Files/brand policy.txt", "r")
    os.system("clear")
    print("Brand Policy: ")
    print(file.read())
    input("> Hit enter to return: ")
    file.close()
    
def guest_controls(self):
    os.system("clear")
    options = [("1: Toggle Email: ", self.email), ("2: Toggle SMS: ", self.SMS),
               ("3: Toggle Targeted Advertising: ", self.targeted_advertising), ("4: Return: ")]
    
    for u, v in options:
        print(u, v)
    option = int(input("> "))    
    try:    
        match option:
            case 1:
                self.toggle_options("Email")
        match option:
            case 2:
                self.toggle_options("SMS")
        match option:
            case 3:
                self.toggle_options("targeted_advertising")
            case 4:
                return
            case _:
                raise Exception()
    
    except Exception as e:
            if type(e) == ValueError:
                input("Invalid input...")
                guest_controls()
            else:
                input(f"Error: {e} {type(e)}")
                guest_controls()