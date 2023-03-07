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
            "major": major.capitalize(),
            "university": university.capitalize(),
            "info": info,
            "experience": experience,
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
            new_major = input("Enter new major (press enter to skip): ").capitalize()
            new_university = input("Enter new university (press enter to skip): ").capitalize()
            new_info = input("Enter new info (press enter to skip): ")
            new_experience = input("Enter new experience (press enter to skip): ")
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