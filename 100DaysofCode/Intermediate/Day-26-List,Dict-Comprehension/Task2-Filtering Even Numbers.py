"""
Instructions
In this list comprehension exercise you will practice using list comprehension to filter out the even numbers from a series of numbers.

First, use list comprehension to convert the list_of_strings to a list of integers.

Then use list comprehension again to create a new list called result. This new list should only contain the even numbers from the list numbers.

Again, try to use Python's List Comprehension instead of a Loop.
"""
list_of_strings = input().split(',')
# 🚨 Do  not change the code above

# TODO: Use list comprehension to convert the strings to integers 👇:
integer_list = [int(n) for n in list_of_strings]

# TODO: Use list comprehension to filter out the odd numbers
# and store the even numbers in a list called "result"
result = [even for even in integer_list if even%2 == 0]

# Write your code 👆 above:
print(result)