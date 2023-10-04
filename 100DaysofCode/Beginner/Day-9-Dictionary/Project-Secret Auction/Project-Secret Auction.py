from art import logo
import os

print(logo)
bidder = []
end_auction = False

"""
new bidders are saved inside a list
"""
def new_bidder(bidder_name,bid_amount):
    new_person = {}
    new_person["Name"] = bidder_name
    new_person["Bid"] = bid_amount
    bidder.append(new_person)

def highest_bidder():
    highest_bid = 0
    for bid in bidder:
        if bid['Bid'] > highest_bid:
            winner = bid['Name']
            highest_bid = bid['Bid']
            
    print(f"The winner is {winner} with a bid of ${highest_bid}")

while not end_auction:
    name = input("What is your name ? ")
    bid = float(input("What is your bid ? "))
    new_bidder(name, bid)
    
    should_continue=input("Are there any other bidders ? yes or no ")
    
    if should_continue == 'no':
        end_auction = True
        highest_bidder()
        print(bidder)
    elif should_continue == 'yes':
        os.system('cls')