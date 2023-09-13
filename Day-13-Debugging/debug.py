############ DEBUGGING#####################

# TODO # Describe Problem
"""
def my_function():
  for i in range(1, 20):
    if i == 20:
      print("You got it")
my_function()

20 is not included in the range need to change to 21 to get the result to be printed out.
"""

# NOTE Updated Code
# def my_function():
#   for i in range(1, 21):
#     if i == 20:
#       print("You got it")
# my_function()


# TODO # Reproduce the Bug
"""
from random import randint
dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
dice_num = randint(1, 6)
print(dice_imgs[dice_num])

Error occurred is IndexError that occurs when index value is 6
"""
# NOTE Updated Code
# from random import randint
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(0, 5)
# print(dice_imgs[dice_num])

# TODO # Play Computer
"""
year = int(input("What's your year of birth?"))
if year > 1980 and year < 1994:
  print("You are a millennial.")
elif year > 1994:
  print("You are a Gen Z.")
  
No out put if year less than 1980 and the year 1994
"""

# NOTE Updated Code
# year = int(input("What's your year of birth?"))
# if year > 1980 and year < 1994:
#   print("You are a millennial.")
# elif year >= 1994:
#   print("You are a Gen Z.")


# TODO # Fix the Errors
"""
age = input("How old are you?")
if age > 18:
print("You can drive at age {age}.")

Type casting not done
wrong indentation 
f string not setup
"""
# NOTE Updated Code
# age = int(input("How old are you?"))
# if age > 18:
#     print(f"You can drive at age {age}.")

# TODO #Print is Your Friend
"""
pages = 0
word_per_page = 0
pages = int(input("Number of pages: "))
word_per_page == int(input("Number of words per page: "))
total_words = pages * word_per_page
print(total_words)

'==' instead of '=' to get the value of the word_per_page
"""

# NOTE Updated Code
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page = int(input("Number of words per page: "))
# print(f"Total pages :{pages}, Words per page: {word_per_page}")
# total_words = pages * word_per_page
# print(total_words)


# TODO #Use a Debugger
"""
def mutate(a_list):
  b_list = []
  for item in a_list:
    new_item = item * 2
  b_list.append(new_item)
  print(b_list)

mutate([1,2,3,5,8,13])

indentation not proper in the function mutate,
b_list.append(new_item) should be in the same indentation
"""


# NOTE Updated Code
# def mutate(a_list):
#   b_list = []
#   for item in a_list:
#     new_item = item * 2
#     b_list.append(new_item)
#   print(b_list)

# mutate([1,2,3,5,8,13])
