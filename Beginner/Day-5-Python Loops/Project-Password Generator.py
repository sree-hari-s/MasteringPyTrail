#Password Generator Project
import random


def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    print("Welcome to the PyPassword Generator!")
    nr_letters= int(input("How many letters would you like in your password?\n")) 
    nr_symbols = int(input(f"How many symbols would you like?\n"))
    nr_numbers = int(input(f"How many numbers would you like?\n"))

    #Easy Level - Order not randomized:
    #e.g. 4 letter, 2 symbol, 2 number = JduE&!91
    """
    Random Password generator which  does not randomize the order using strings
    """
    # not_randomized_password = ""
    # for _ in range(nr_letters):
    #     not_randomized_password+=random.choice(letters)
    # for _ in range(nr_symbols):
    #     not_randomized_password+=random.choice(symbols)
    # for _ in range(nr_numbers):
    #     not_randomized_password+=random.choice(numbers)

    # print(not_randomized_password)
    """
    Random Password generator using lists
    """
    not_randomized_password = []
    for _ in range(nr_letters):
        not_randomized_password.append(random.choice(letters))
    for _ in range(nr_symbols):
        not_randomized_password.append(random.choice(symbols))
    for _ in range(nr_numbers):
        not_randomized_password.append(random.choice(numbers))
        
    print("Order of Characters not Randomized: ")
    for i in not_randomized_password:
        print(i,end="")
    #Hard Level - Order of characters randomized:
    #e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
    shuffled_password = random.sample(not_randomized_password,len(not_randomized_password))
    print("\nOrder of Characters Randomized: ")
    for i in shuffled_password:
        print(i,end="")

    #Alternative code
"""
    random.shuffle(not_randomized_password)
    password = ""
    for char in not_randomized_password:
        password += char

    print(f"\nYour password is: {password}")
"""
    
from os import system
while input("\nDo you want to Generate a new password ? (y/n): ") == "y":
    system('cls')
    password_generator()