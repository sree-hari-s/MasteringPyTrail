import sheety

print("Welcome to Flights Club")

firstname = input("What is your first name? ").title()
lastname = input("What is your last name? ").title()

email1 = "email1"
email2 = "email2"

while email1 != email2:
    email1 = input("Enter your email address? ")
    if email1.lower() == "quit" or email1.lower() == "exit":
        exit()
    email2 = input("Confirm your email address ")
    if email2.lower() == "quit" or email2.lower() == "exit":
        exit()

print("Welcome to Flights Club")

sheety.post_new_row(firstname, lastname, email1)