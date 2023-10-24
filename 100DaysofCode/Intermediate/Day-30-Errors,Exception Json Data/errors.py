# FileNotFoundError
"""
with open("test.txt") as file:
    file.read()
"""    

# KeyError
"""
a_dictionary ={"key": "value"}
value = a_dictionary["new_key"]
"""

# IndexError
"""
fruit_list = ["apple", "orange", "banana"]
fruit = fruit_list[4]
"""

# Type Error
"""
text = "abc"
print(text+5)
"""


"""
try:
    Something that might cause an exception
except exception1:
    Do this if there WAS an exception
except exception2:
    Multiple exceptions can be written
else:
    Do this if there was NO exception
finally:
    Do this no matter what happens
    Finally is not often used.
"""

# Example 

try:
    file = open("test.txt")
    a_dictionary = {"key": "value"}
    print(a_dictionary["testing"])
except FileNotFoundError:
    file = open("test.txt","w")
    file.write("File Created")
except KeyError as error_message:
    print(f"The key {error_message}, does not exist")
else:
    content = file.read()
    print(content)
finally:
    file.close()
    print("File Closed")

"""
Raising our own Exceptions
"""

height = float(input("height:"))
weight = int(input("weight:"))
bmi = weight/height**2
if height>3:
    raise ValueError("Human height should not be over 3 meters")
print(bmi)