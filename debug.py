from replit import db


# Writes list of accounts created to file
def export_db():
	f = open("credentials.txt", "w")
	f.write(f"# of Accounts: {len(db)}\n\n")

	for k, v in db.items():
		f.write(f"Username: {k}\n\tPassword: {v}")
		f.write("\n\n")

	f.close()

# Clear the database
def reset_db():
	for key in db.keys():
		del db[key]
