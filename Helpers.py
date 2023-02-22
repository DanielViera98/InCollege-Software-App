# Helper method to print options
def print_options(options, label="Back", toggle=""):
    
  for i, option in enumerate(options):
    print(f"{i+1}. {option} ")
    
  print(f"{len(options)+1}. {label} ")
  
def print_toggle_options(options):
  
  i = 1
  for option, value in options:
    print(f"{i}. {option} : {value}")
    i += 1
    
  print(f"{i}. Back ")