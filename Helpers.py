# Helper method to print options
def print_options(options, label="Back"):
    
  for i, option in enumerate(options):
    print(f"{i+1}. {option}")
    
  print(f"{len(options)+1}. {label}")