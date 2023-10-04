from hangman_words import word_list
from hangman_art import logo,stages
import random


def game():
    print(logo)
    chosen_word = random.choice(word_list)
    word_length = len(chosen_word)

    end_of_game = False
    lives = 6

    #Create blanks
    display = []
    for _ in range(word_length):
        display += "_"
    while not end_of_game:
        guess = input("Guess a letter: ").lower()

        #Check guessed letter
        for position in range(word_length):
            letter = chosen_word[position]
            #print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
            if letter == guess:
                display[position] = letter

        #Check if user is wrong.
        if guess not in chosen_word:
            lives -= 1
            print(f"You guessed {guess}, that's not in the word,You lose a life({lives} remaining)")
            if lives == 0:
                end_of_game = True
                print(f"You lose. The word was {chosen_word}")

        #Join all the elements in the list and turn it into a String.
        print(f"{' '.join(display)}")

        #Check if user has got all letters.
        if "_" not in display:
            end_of_game = True
            print("You win.")
            
        print(stages[lives])

from os import system

while input("Do you want to play Hangman Game? (y/n): ") == "y":
    system('cls')
    game()