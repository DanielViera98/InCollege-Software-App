import json
from io import StringIO
from Profiles import Profile_manager
from Tests.helpers import MockUser1, MockUser2, empty_all

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
    assert updated_profile['education'] == []
    
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
    
def test_view_friends_profile(monkeypatch):
    
    user1 = MockUser1()
    input = StringIO('n\nn\n')
    monkeypatch.setattr('sys.stdin', input)
    user1.system.add_account(user1.username, user1.password, user1.first_name[0], user1.last_name[0], user1.email[0], user1.SMS[0], user1.targeted_advertising[0], user1.friends_list[0], user1.requests, [], [])
    
    user2 = MockUser2()
    user2.system.add_account(user2.username, user2.password, user2.first_name[0], user2.last_name[0], user2.email[0], user2.SMS[0], user2.targeted_advertising[0], user2.friends_list[0], user2.requests, [], [])
    
    input = StringIO('Nobody2\nHere2\n\n')
    monkeypatch.setattr('sys.stdin', input)
    user1.college.send_request()
    print(dir(user1))
    
    input = StringIO('1\n1\n\n\n\n')
    monkeypatch.setattr('sys.stdin', input)
    user2.college.pending_requests()
    print(dir(user2))
    
    ############################################
    
    try:
        input = StringIO('2\n1\n\n\n3\n')
        monkeypatch.setattr('sys.stdin', input)
        user1.college.manage_friends()
    except:
        user1.college.manage_friends().assertFalse(True, 'Exception raised')


