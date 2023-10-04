# #For loop
# alphabets = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", 
#              "m", "n", "o", "p","q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

# for alphabet in alphabets:
#     print(alphabet)
    
# total =0
# for i in range(1, 101):
#     total += i
# print(total)

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
not_randomized_password = ""
for _ in range(nr_letters):
    not_randomized_password+=random.choice(letters)
for _ in range(nr_symbols):
    not_randomized_password+=random.choice(symbols)
for _ in range(nr_numbers):
    not_randomized_password+=random.choice(numbers)

print(not_randomized_password)
