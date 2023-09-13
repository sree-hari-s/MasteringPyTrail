"""
Number Guessing Game Objectives:

Include an ASCII art logo.
Allow the player to submit a guess for a number between 1 and 100.
Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
If they got the answer correct, show the actual answer to the player.
Track the number of turns remaining.
If they run out of turns, provide feedback to the player. 
Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
"""

import random
from art import logo

def check_guess(guess,number_guessed):
    if guess == number_guessed:
        return 0
    elif guess > number_guessed:
        return "Too high"
    elif guess < number_guessed:
        return "Too low"

def game():
    print(logo)
    print("Welcome to the Number Guessing Game")
    print("I'm thinking of a number between 1 and 100.")
    number_guessed = random.randint(1,100)

    chances = 0
    difficulty = input("Choose a difficulty, Type 'easy' or 'hard': ")
    if difficulty == 'easy':
        chances = 10
    else:
        chances =  5

    while chances !=0:
        guess = int(input("Make a guess:"))
        if check_guess(guess,number_guessed)==0:
            print(f"You got it! The answer was {guess}")
            return
        else:
            print(check_guess(guess,number_guessed))
            chances-=1
        print(f"You have {chances} attempts remaining to guess the number.")

import os
while input("\nDo you want to play a Number Guessing Game? (y/n):")=='y':
    os.system('cls')
    game()
