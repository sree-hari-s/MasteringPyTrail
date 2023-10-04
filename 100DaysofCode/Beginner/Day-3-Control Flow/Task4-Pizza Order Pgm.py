"""
# Automatic Pizza Order Program

Welcome to Python Pizza, where we've built an automatic pizza order program to calculate your final bill based on your order preferences.

## Pizza Sizes and Prices

- Small Pizza: $15
- Medium Pizza: $20
- Large Pizza: $25

## Additional Toppings

- Pepperoni for Small Pizza: +$2
- Pepperoni for Medium or Large Pizza: +$3
- Extra Cheese for Any Size Pizza: +$1

Simply input your order details, and our program will calculate the total cost for you. Enjoy your delicious pizza!

"""

# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

#Initial idea for this solution 
if size == 'S':
    total_cost = 15
    if add_pepperoni == "Y":
        total_cost += 2
    if extra_cheese == "Y":
        total_cost += 1
elif size == 'M':
    total_cost = 20
    if add_pepperoni == "Y":
        total_cost += 3
    if extra_cheese == "Y":
        total_cost += 1
elif size == 'L':
    total_cost = 25
    if add_pepperoni == "Y":
        total_cost += 3
    if extra_cheese == "Y":
        total_cost += 1
else:
    print("Invalid Size! Please provide a valid size.")
print(f"Your final bill is: ${total_cost}")


"""
Alternate solution

if size == 'S':
    total_cost = 15
elif size == 'M':
    total_cost = 20
elif size == 'L':
    total_cost = 25
else:
    print("Invalid Size! Please provide a valid size.")
if add_pepperoni == "Y":
    if size == 'S':
        total_cost += 2
    else:
        total_cost += 3
if extra_cheese == "Y":
    total_cost +=1
print(f"Your final bill is: ${total_cost}")
"""