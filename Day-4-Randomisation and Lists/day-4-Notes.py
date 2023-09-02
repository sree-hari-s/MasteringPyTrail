import random
a=random.randint(1,2)
print(a)

b=random.random()
print(b)

alphabets = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 
                'M', 'N','O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W','X', 'Y', 'Z']

#list elements can be accessed by positive indexing and negative indexing also
print(alphabets[0])

print(alphabets[-1])

#add values to a list

alphabets.append("AA")

alphabets.extend(["AB","AC","AD","AE","AF"])

print(alphabets)

fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

dirty_dozen = [fruits, vegetables]

print(dirty_dozen[1][1])
print(dirty_dozen[0])
print(dirty_dozen[1])
