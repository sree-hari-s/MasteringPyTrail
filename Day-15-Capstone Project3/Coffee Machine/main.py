from os import system
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 15,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 25,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 30,
    }
}

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def menuItems():
    print("\nCustomer Menu:")
    for idx, (item_name, item_info) in enumerate(MENU.items(), start=1):
        cost = item_info["cost"]
        print(f"{idx}.{item_name.title()}, Rs {cost}")
    print("\nFor maintainers\n4.Report\n5.Turn Off")

def is_resource_available(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item} available")
            return False
    return True

def process_Cash():
    total = int(input("Input how many Rs 100 note? "))*100
    total += int(input("Input how many Rs 50 note? "))*50
    total += int(input("Input how many Rs 20 note? "))*20
    return total


def is_transaction_complete(money_received,drink_cost):
    if money_received >= drink_cost:
        change = round(money_received - drink_cost,2)
        print(f"Here is Rs {change} in change")
        global profit
        profit+=drink_cost
        return True
    else:
        print("Sorry, That's not enough money. Money Refunded")
        return False
    
def make_drink(drink_name,order_ingredients):
    for item in order_ingredients:
        resources[item]-=order_ingredients[item]
    print(f"Here is {drink_name} Enjoy!")

def show_report():
    print("Report:")
    for item in resources:
        print(f"{item} :{resources[item]}")

is_On = True

while is_On:
    menuItems()
    choice = input("\nWhat would you like to order?(espresso/latte/cappuccino):").lower()
    if choice == 'off':
        is_On=False
    elif choice == 'report':
        show_report()
    else:
        drink = MENU[choice]
        if is_resource_available(drink["ingredients"]):
            payment = process_Cash()
            if is_transaction_complete(payment,drink["cost"]):
                make_drink(choice,drink["ingredients"])
