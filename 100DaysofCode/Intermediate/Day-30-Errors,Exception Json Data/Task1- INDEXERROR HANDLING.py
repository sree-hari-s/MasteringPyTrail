"""
Use Exception handling to prevent the program from crashing. 
If the user enters something that is out of range just print a default output of "Fruit pie".

fruits = eval(input())
# 🚨 Do not change the code above

# TODO: Catch the exception and make sure the code runs without crashing.
def make_pie(index):
    fruit = fruits[index]
    print(fruit + " pie")


# 🚨 Do not change the code below
make_pie(4)
"""

fruits = eval(input())
# 🚨 Do not change the code above

# TODO: Catch the exception and make sure the code runs without crashing.
def make_pie(index):
    try:
        fruit = fruits[index]
        print(fruit + " pie")
    except IndexError:
        print("Fruit pie")

# 🚨 Do not change the code below
make_pie(4)
