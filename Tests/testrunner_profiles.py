import json
from Profiles import Profile_manager

def test_add_profile():
    # Initialize the profile manager and load existing profiles
    pm = Profile_manager()
    initial_num_profiles = pm.num_profiles
    with open('example_profiles.json') as f:
        expected_profiles = json.load(f)

    # Add a new profile
    new_profile = {
        "username": "jsmith",
        "title": "Software Engineer",
        "major": "Computer Science",
        "university": "Stanford",
        "info": "Passionate about coding",
        "experience": [],
        "education": "Bachelor's degree"
    }
    pm.update_profiles(**new_profile)

    # Check if the number of profiles has increased
    assert pm.num_profiles == initial_num_profiles + 1

    # Check if the new profile has been saved correctly
    expected_profiles.append(new_profile)
    with open(pm.filename) as f:
        saved_profiles = json.load(f)
    assert saved_profiles == expected_profiles

def test_edit_profile():
    # Initialize the profile manager and load existing profiles
    pm = Profile_manager()
    with open('example_profiles.json') as f:
        initial_profiles = json.load(f)

    # Edit an existing profile
    username = "tan123"
    new_title = "Software Developer"
    pm.edit_profile(username, new_title=new_title)

    # Check if the profile has been edited correctly
    for profile in pm.profiles:
        if profile["username"] == username:
            assert profile["title"] == new_title

    # Check if the edited profile has been saved correctly
    with open(pm.filename) as f:
        saved_profiles = json.load(f)
    assert saved_profiles == pm.profiles
