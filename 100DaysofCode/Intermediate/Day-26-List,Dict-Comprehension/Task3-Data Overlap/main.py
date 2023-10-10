# TODO
"""
Take a look inside file1.txt and file2.txt. They each contain a bunch of numbers, each number on a new line.
You are going to create a list called result which contains the numbers that are common in both files.
"""

with open('file1.txt', 'r') as file1:
    list1 = file1.readlines()

with open('file2.txt', 'r') as file2:
    list2 = file2.readlines()
    
result = [int(num) for num in list1 if num in list2 ]

print(result)