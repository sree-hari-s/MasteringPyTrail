list_of_strings = input().split(',')
# 🚨 Do  not change the code above

# TODO: Use list comprehension to convert the strings to integers 👇:
integer_list = [int(n) for n in list_of_strings]

# TODO: Use list comprehension to filter out the odd numbers
# and store the even numbers in a list called "result"
result = [even for even in integer_list if even%2 == 0]

# Write your code 👆 above:
print(result)