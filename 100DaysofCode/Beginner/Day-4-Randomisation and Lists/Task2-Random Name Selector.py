"""
# Random Name Selector Program

In this program, you will create a random name selector that chooses a person from a list of names. The selected person will be responsible for paying for everybody's food bill. It's worth noting that you are not allowed to use the `choice()` function for this task.

To achieve this, you'll follow these steps:

1. Create a list called `names` to store the names of the people. You will input these names as a string in the following format:
   - Enter all the names as "name, name, name," separated by commas and spaces. For example: "Alice, Bob, Carol."

2. Split the `names_string` into individual names and store them in the `names` list.

3. Use a random number generation technique to select a random name from the `names` list. You will not use the `choice()` function for this.

The selected person will be tasked with paying for everyone's food bill, making it a fun way to decide who covers the expenses.

Enjoy using this program to randomly select the lucky participant for treating everyone to a meal!

"""


# Import the random module here

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
import random
len_names =len(names)
choice =random.randint(0, len_names-1)
print(f"{names[choice]} is going to buy the meal today!")

#Alterative method
"""
using choice() method 
"""
print(f"{random.choice(names)} is going to buy the meal today")