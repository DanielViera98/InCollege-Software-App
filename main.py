from debug import export_db, reset_db
from App import InCollege
from replit import db

def main():
	app = InCollege()
	app.run()


if __name__ == "__main__":
	main()

	# Uncomment below to clear the database
	# reset_db()

	export_db()
