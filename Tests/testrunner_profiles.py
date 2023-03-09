import json
from io import StringIO
from Profiles import Profile_manager

class MockProfile():
    
    def __init__(self):
    
        self.pm = Profile_manager()
        self.username = "tan123"
        self.new_title = "New Software Developer"
        self.new_major = "New Computer Science"
        self.new_university = "New University"
        self.new_info = "New Cool Info"
        self.new_experience = []
        self.new_education = []
        

def test_edit_profile(monkeypatch):
    # Call the edit_profile method with a valid username and new information
    mp = MockProfile()
    
    mp.pm.update_profiles(mp.username, mp.new_title, mp.new_major, mp.new_university, mp.new_info, mp.new_experience, mp.new_education)
    
    input = StringIO('New Title\nNew Major\nNew University\nNew Info\nn\nn\nn\n')
    monkeypatch.setattr('sys.stdin', input)

    mp.pm.edit_profile(mp.username)
    
    updated_profile = mp.pm.profiles[0]
    assert updated_profile['title'] == 'New Title'
    assert updated_profile['major'] == 'New Major'
    assert updated_profile['university'] == 'New University'
    assert updated_profile['info'] == 'New Info'
    assert updated_profile['education'] == [['-','-','-']]
    
def test_edit_profile_max_experience(monkeypatch):
    mp = MockProfile()
    
    mp.pm.update_profiles(mp.username, mp.new_title, mp.new_major, mp.new_university, mp.new_info, mp.new_experience, mp.new_education)

    # Mock the input function to return input that tries to add more than three experience sections
    for i in range(2):
        input_string = 'Exp1\nExp2\nExp3\nExp4\nExp5\nExp6\ny\n'
        input = StringIO(input_string)
        monkeypatch.setattr('builtins.input', lambda _: input.readline().rstrip())

        mp.pm.add_experience(mp.pm.profiles[0])

    input_string = 'Exp1\nExp2\nExp3\nExp4\nExp5\nExp6\n'
    input = StringIO(input_string)
    monkeypatch.setattr('builtins.input', lambda _: input.readline().rstrip())
    mp.pm.add_experience(mp.pm.profiles[0])
    # Check that the profile was updated correctly
    
    updated_profile = mp.pm.profiles[0]
    assert len(updated_profile['experience']) == 3  # The maximum number of experience sections should be 3
