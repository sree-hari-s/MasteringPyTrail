#Datatypes

#string
print("hello"[0]) #returns a first character
"""
pulling out a character from a string is called subscripting
number in between square brackets determines which character you pull out
"""
print("hello"[-1]) #returns the last character

print("123"+"345") #concatenates to 123345

#Integer

print(123+345) #returns the sum 

#float 
"""
refers to floating point numbers, to represent pi 
"""

pi = 3.14

#boolean
True , False

print(True+False)
print(False+False)


#Type Error

num_char = len(input("What is your name? "))
"""
Type Error- cannot concatenate integer into a string
"""
#print("Your name is " + num_char+ "characters long")

new_num_char = str(num_char)
print("Your name is " + new_num_char+ " characters long")

print(type(num_char))
print(type(new_num_char))

a=123
print(type(a))

print(10 +float("100.0")) #110.0 output
print(str(10)+ str(100)) #10100 output

