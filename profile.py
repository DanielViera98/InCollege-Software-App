import json
import os

class ProfileManager:
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

    def update_profiles(self,username, title, major, university, info, experience, education):
        new_profile = {}
        new_profile[username] = {
            "title": title,
            "major": major,
            "university": university,
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
