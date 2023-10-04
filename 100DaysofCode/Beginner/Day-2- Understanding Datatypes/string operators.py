message1= "Hello World!"
message2= "Welcome to GFG"

print(message1 + message2)
print(message1*3)
print(message1[6])
print(message2[0:7])

str1 ="Hello"

if str1 in message1:
    print("It is present in message1")
if str1 not in message2:
    print("It is not present in message2")