def some_function(name):
    print(f"hello {name}")

name = input("Please enter your name? ")
some_function(name)


def greet_with(name,location):
    print(f"Hello {name}\nWhat is it like in {location}")

name,location = input("Please enter your name and location ").split(" ")
greet_with(name=name,location=location)