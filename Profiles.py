import json
import os

from Helpers import print_options

class Profile_manager:
    def __init__(self):
        self.filename = "profiles.json"
        self.num_profiles = 0
        self.profiles = self.load_profiles()

    def load_profiles(self):
        if not os.path.exists(self.filename):
            with open(self.filename, 'w') as f:
                f.write('[]')
            
        with open(self.filename, 'r') as file:
            profiles = json.load(file)

        self.num_profiles = len(profiles)
        return profiles

    def update_profiles(self, username, title, major, university, info, experience, education):
        new_profile = {
            "username": username,
            "title": title,
            "major": major,
            "university": university,
            "info": info,
            "experience": [],
            "education": []
        }
        self.profiles.append(new_profile)
        self.num_profiles += 1
        with open(self.filename, 'w') as file:
            json.dump(self.profiles, file, indent=2)

    def get_profile(self, username):
        for profile in self.profiles:
            if profile['username'] == username:
                return profile
        return False
        
    def view_profile(self, username):
        os.system("clear")
        profile = self.get_profile(username)
        if profile == False:
            input("No Profile for user. ")
            return
        print("Username: ", profile['username'], "\nTitle: ", profile['title'], "\nMajor: ", profile['major'],
              "\nUniversity: ", profile['university'], "\nInfo: ", profile['info'])
        self.view_experiences(profile)
        print("\nEducation: ", "NOT IMPLEMENTED")
        
    def search_profiles(self, keyword):
        results = []
        for profile in self.profiles:
            if keyword in profile.values():
                results.append(profile)
        return results
    
    def edit_profile(self, username):
        os.system("clear")
        profile = self.get_profile(username)
        if profile == False:
            self.update_profiles(username,"-","-","-","-","-","-")
            profile = self.get_profile(username)
        
        print("Current profile information:")
        self.view_profile(username)

        # Prompt user for new information
        new_title = input("Enter new title (press enter to skip): ")
        new_major = input("Enter new major (press enter to skip): ").title()
        new_university = input("Enter new university (press enter to skip): ").title()
        new_info = input("Enter new info (press enter to skip): ")
        test = input("Would you like to add an Experience (y/n)? ")
        if test == "y":
            self.get_experience(profile)
        new_education = input("Would you like to add an Education (y/n)? ")
        if new_education == "y":
            self.add_education(profile)

        # Update profile with new information
        if new_title:
            profile['title'] = new_title
        if new_major:
            profile['major'] = new_major
        if new_university:
            profile['university'] = new_university
        if new_info:
            profile['info'] = new_info

        # Write updated profiles to file
        with open(self.filename, 'w') as file:
            json.dump(self.profiles, file, indent=2)
        
        print("Profile updated successfully!")
        question = input("Would you like to view your finished profile?(y/n)")
        if question == 'y':
            self.view_profile(username)
            input("Press ENTER to continue. ")
        return
        
    def get_experience(self, profile):
        self.options = ["Add Experience (Max of Three)", "Edit Experience"]
        
        option = -1
        back_option = len(self.options) + 1
    
        while option != back_option:
            os.system("clear")
            print("Experience:")
            print_options(self.options)
            try:
                option = int(input("> "))
                match option:
                    case 1:
                        if len(profile['experience']) < 3:
                            self.add_experience(profile)
                        else:
                            input("Already have max number of Experiences. ")
                    case 2:
                        self.edit_experience(profile)
                    case 3:
                        return
                    case _:
                        raise Exception() 
                    
            except Exception as e:
                if type(e) == ValueError:
                    input("Invalid input...")
                else:
                    input(f"Error: {e} {type(e)}")

    def add_experience(self, profile):
        add = True
        while (len(profile['experience']) < 3 and add == True):
            os.system("clear")
            print("--------Adding Experience--------\n")
            counter = len(profile['experience'])
            profile['experience'].append(["-", "-", "-", "-", "-", "-"])
            self.view_experiences(profile)

            temp = ""
            temp = input("Enter job title (press enter to skip): ") 
            if (temp):
                profile['experience'][counter][0] = temp
            temp = input("Enter Employer (press enter to skip): ") 
            if (temp):
                profile['experience'][counter][1] = temp
            temp = input("Enter Date Started (press enter to skip): ") 
            if (temp):
                profile['experience'][counter][2] = temp
            temp = input("Enter Date Ended (press enter to skip): ") 
            if (temp):
                profile['experience'][counter][3] = temp
            temp = input("Enter Location (press enter to skip): ") 
            if (temp):
                profile['experience'][counter][4] = temp
            temp = input("Enter Description (press enter to skip): ") 
            if (temp):
                profile['experience'][counter][5] = temp
                
            with open(self.filename, 'w') as file:
                    json.dump(self.profiles, file, indent=2)
            
            if len(profile['experience']) < 3:
                temp = input("Would you like to add another Experience(y/n)? ")
                if temp == 'y':
                    add = True
                else:
                    add = False
            else:
                input("You've reached the max number of experiences, returning. ")
                
    def edit_experience(self, profile):
        os.system("clear")
        if len(profile['experience']) < 1:
            input("No experiences to edit, press enter to return. ")
            return
        print("--------Editing Experience--------\n")
        num = 1
        for i in profile['experience']:
            print("Experience ", num, ":")
            print("\tJob Title: ", i[0])
            print("\tDescription:\n\t\t", i[5], "\n")
            num = num + 1
        edit_num = int(input("Which Experience would you like to edit (Enter the number): "))
        edit_num = edit_num - 1
        self.edit_options = ["Job Title", "Employer", "Date Started", "Date Ended", "Location", "Description"]
        option = -1
        back_option = len(self.edit_options) + 1
        
        while option != back_option:
            os.system("clear")
            edit = profile['experience'][edit_num]
            print("Experience: ", edit_num+1, ":")
            print("\tJob Title: ", edit[0])
            print("\tEmployer: ", edit[1])
            print("\tDate Started: ", edit[2])
            print("\tDate Ended: ", edit[3])
            print("\tLocation: ", edit[4])
            print("\tDescription:\n\t\t", edit[5], "\n")
            
            print("Choose what to change: ")
            print_options(self.edit_options)
            choice = int(input("> "))
            match choice:
                case 1:
                    profile['experience'][edit_num][0] = input("New Job Title: ")
                case 2:
                    profile['experience'][edit_num][1] = input("New Employer: ")
                case 3:
                    profile['experience'][edit_num][2] = input("New Date Started: ")
                case 4:
                    profile['experience'][edit_num][3] = input("New Date Ended: ")
                case 5:
                    profile['experience'][edit_num][4] = input("New Location: ")
                case 6:
                    profile['experience'][edit_num][5] = input("New Description: ")
                case 7: 
                    option = back_option
                case _:
                    input("ERROR, RETURN")
                    option = back_option
            
            with open(self.filename, 'w') as file:
                json.dump(self.profiles, file, indent=2)
    
    def view_experiences(self, profile):
        if len(profile['experience']) == 0:
            print("Experience: -")
        for i in profile['experience']:
            print("Experience:")
            print("\tJob Title: ", i[0])
            print("\tEmployer: ", i[1])
            print("\tDate Started: ", i[2])
            print("\tDate Ended: ", i[3])
            print("\tLocation: ", i[4])
            print("\tDescription:\n\t\t", i[5], "\n")

    def add_education(self,profile):
        add = True
        if (len(profile['education']) >= 1):
            input("Education already exists(enter to continue)")
            add = False
        while (len(profile['education']) < 1 and add == True):
            os.system("clear")
            print("--------Adding Experience--------\n")
            counter = len(profile['education'])
            profile['education'].append(["-", "-", "-"])
            for i in profile['education']:
                print("Education:")
                print("\tSchool Name: ", i[0])
                print("\tDegree: ", i[1])
                print("\tYears Attended: ", i[2],"\n")
                
            temp = ""
            temp = input("Enter School Name (press enter to skip): ") 
            if (temp):
                profile['education'][counter][0] = temp
            temp = input("Enter Degree (press enter to skip): ") 
            if (temp):
                profile['education'][counter][1] = temp
            temp = input("Enter Years Attended (press enter to skip): ") 
            if (temp):
                profile['education'][counter][2] = temp
                
            with open(self.filename, 'w') as file:
                    json.dump(self.profiles, file, indent=2)
            
            add = False
            
                