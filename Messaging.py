import json
from AccountSystem import AccountSystem

class Messaging():

    def __init__(self, sender, recipient):
        self.sender = sender
        self.recipient = recipient
        self.system = AccountSystem()
    
    def send_message(self, message):
        data = self.system.load_accounts()
        data[self.recipient]['message_inbox'].append([self.sender, message])
            
        # Open the JSON file again in 'write' mode
        with open('students.json', 'w') as f:
            # Write the updated Python object back to the JSON file
            json.dump(data, f, indent=2)
        input("Message sent! ")
        return True
    
    