import json
import os

import json
import os

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
            "education": education
        }
        self.profiles.append(new_profile)
        self.num_profiles += 1
        with open(self.filename, 'w') as file:
            json.dump(self.profiles, file, indent=2)

    def search_profiles(self, keyword):
        results = []
        for profile in self.profiles:
            if keyword in profile.values():
                results.append(profile)
        return results
    
    def edit_profile(self, username):
        os.system("clear")
        for profile in self.profiles:
            if profile['username'] == username:
                print("Current profile information:")
                print("Title:", profile['title'])
                print("Major:", profile['major'])
                print("University:", profile['university'])
                print("Info:", profile['info'])
                print("Experience:", profile['experience'])
                print("Education:", profile['education'])
                print("\n")

                # Prompt user for new information
                new_title = input("Enter new title (press enter to skip): ")
                new_major = input("Enter new major (press enter to skip): ").title()
                new_university = input("Enter new university (press enter to skip): ").title()
                new_info = input("Enter new info (press enter to skip): ")
                new_experience = self.get_experience(profile)
                new_education = input("Enter new education (press enter to skip): ")

                # Update profile with new information
                if new_title:
                    profile['title'] = new_title
                if new_major:
                    profile['major'] = new_major
                if new_university:
                    profile['university'] = new_university
                if new_info:
                    profile['info'] = new_info
                if new_experience:
                    profile['experience'] = new_experience
                if new_education:
                    profile['education'] = new_education

                # Write updated profiles to file
                with open(self.filename, 'w') as file:
                    json.dump(self.profiles, file, indent=2)

                print("Profile updated successfully!")
                return
        print("Profile not found.")
        
    def get_experience(self, profile):
        print("Experience:")
        test = input("Would you like to add/edit an Experience (Max of three), y/n? ")
        if (profile['experience'] == [] and test == 'y'):
            print("No Experiences, adding!")
            self.add_experience(profile)

        return
    
    def add_experience(self, profile):
        add = True
        while (len(profile['experience']) < 3 and add == True):
            counter = len(profile['experience'])
            profile['experience'].append(["-", "-", "-", "-", "-", "-"])
            for i in profile['experience']:
                print("Experience:")
                print("\tJob Title: ", i[0])
                print("\tEmployer: ", i[1])
                print("\tDate Started: ", i[2])
                print("\tDate Ended: ", i[3])
                print("\tLocation: ", i[4])
                print("\tDescription:\n\t\t", i[5], "\n")

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
