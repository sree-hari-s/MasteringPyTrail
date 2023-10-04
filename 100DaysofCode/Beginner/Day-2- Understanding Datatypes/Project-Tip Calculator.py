"""
## Tip Calculator

# Instructions

If the bill was $150.00, split between 5 people, with 12% tip. 

Each person should pay (150.00 / 5) * 1.12 = 33.6

Format the result to 2 decimal places = 33.60

Thus everyone's share of the total bill is $30.00 plus a $3.60 tip.

# Example Input


Welcome to the tip calculator!
What was the total bill? $124.56
How much tip would you like to give? 10, 12, or 15? 12
How many people to split the bill? 7


# Example Output


Each person should pay: $19.93

"""
def game():
    print("Welcome to the Tip Calculator!")
    total_bill = float(input("What was the total bill? $"))
    tip_amount = int(input("How much tip would you like to give? 10, 12, or 15? "))
    number_of_people = int(input("How many people to split the bill? "))

    amount_per_person = round((total_bill/number_of_people)*(1+(tip_amount/100)),2)
    amount_per_person = "{:.2f}".format(amount_per_person)
    print(f"Each person should pay: ${amount_per_person}")

from os import system
    
while input("Do you want to Calculate Tip? (y/n): ") == "y":
    system('cls')
    game()