#1. Create a greeting for your program.
#2. Ask the user for the city that they grew up in.
#3. Ask the user for the name of a pet.
#4. Combine the name of their city and pet and show them their band name.
#5. Make sure the input cursor shows on a new line:

def game():
    print("Welcome to the Band Name Generator")
    city_name=input("What's the name of the city you grew up in?\n")
    pet_name=input("What's your pet's name?\n")
    print("Your Band Name could be "+city_name+" "+pet_name)

from os import system
    
while input("Do you want to Generate a Band Name? (y/n): ") == "y":
    system('cls')
    game()