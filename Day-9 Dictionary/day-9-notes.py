#simple dictionary
programming_dictionary={
    "bug":"An error in a program",
    "function": "A piece of code that you can call easily over and over again"
}

programming_dictionary["loop"] ="The action of doing something over and over again"

print(programming_dictionary)


for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])
    
#Nested dictionary

"""
Lists inside a dictionary
"""

travel_log = {
    "India" : {"Cities_Visited": ["Kerala","Tamil Nadu","Delhi"], "total_visits":12},
    "Germany" : [ "Berlin","Hamburg","Stuttgart",]
}

#Nesting dictionary in lists

travel_log = [
{
  "country": "France", 
  "cities_visited": ["Paris", "Lille", "Dijon"], 
  "total_visits": 12,
},
{
  "country": "Germany",
  "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
  "total_visits": 5,
},
]



starting_dictionary = {
    "a": 9,
    "b": 8,
}


final_dictionary = {
    "a": 9,
    "b": 8,
    "c": 7,
}

starting_dictionary['c'] = 7
final_dictionary= starting_dictionary
print(final_dictionary)

print(final_dictionary[1])

order = {
    "starter": {1: "Salad", 2: "Soup"},
    "main": {1: ["Burger", "Fries"], 2: ["Steak"]},
    "dessert": {1: ["Ice Cream"], 2: []},
}

print(order["main"][2][0])