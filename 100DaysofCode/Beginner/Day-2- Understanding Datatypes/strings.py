message = "geeksforgeeks"

print(message[2:5])
print(message[-10:-2])
print(message[:5])
print(message[2:])

"""
Deletion of a character from a string is not allowed
as python string are immutable 
"""
message[-1] ="D"
print(message)