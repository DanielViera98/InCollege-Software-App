### Handles checking if registered password is secure ###

def verify_login_info(data, username, password):
  if username in data:
    return data[username]['password'] == password

  else:
    return False

def has_capital_letter(password):
  for char in password:
    if char.isupper(): return True
  return False

def has_min_char(password):
  return len(password) >= 8

def has_max_char(password):
  return len(password) <= 12

def has_digit(password):
  for char in password:
    if char.isdigit(): return True
  return False

def has_special_char(password):
  for char in password:
    if not char.isalnum(): return True
  return False

def is_secure_password(password):
  return has_capital_letter(password) and\
    has_min_char(password) and\
    has_max_char(password) and\
    has_max_char(password) and\
    has_digit(password) and\
    has_special_char(password)