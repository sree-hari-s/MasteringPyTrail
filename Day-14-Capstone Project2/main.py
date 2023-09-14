from art import logo,vs
from game_data import data
import random

# for i in data:
#     print(i['name'])

def generate_random_data():
    return random.choice(data)

def compare(A_followers,B_followers,guess):
    if A_followers>B_followers:
        return guess == 'a'
    else:
        return guess == 'b'
    
from os import system

def formatted_data(data):
    return f"{data['name']}, {data['description']}, from {data['country']}"

def game():
    print(logo)
    final_score = 0
    A = generate_random_data()
    B = generate_random_data()
    end_of_game = False
    while not end_of_game:
        A = B
        B = generate_random_data()
        while A == B:
            B = generate_random_data()
        print("Compare:")
        print(formatted_data(A))
        print(vs)
        print("Against B:")
        print(formatted_data(B))
        choice = input("Who has more followers? Type 'A' or 'B': ").lower()
        result = compare(A['follower_count'], B['follower_count'],choice)
        if result:
            final_score+=1
            system('cls')
            print(f"You're Right, Current score : {final_score}")
        else:
            end_of_game = True
            print(f"Sorry, that's wrong. Final score is {final_score}\nGAME OVER")

while input("\nDo you want to play a Higher Lower Game? (y/n):").lower()=='y':
    system('cls')
    game()