import random

stages = ['''
  +---+
  |   |
      |
      |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''']

word_list = [
    {"word": "python", "hint": "A popular programming language"},
    {"word": "javascript", "hint": "Another widely used programming language"},
    {"word": "programming", "hint": "The act of writing code"},
    {"word": "hangman", "hint": "The name of this game"},
    {"word": "computer", "hint": "An electronic device for processing data"},
    {"word": "keyboard", "hint": "Input device for computers"},
    {"word": "developer", "hint": "Someone who writes software"}
]

def choose_word():
    return random.choice(word_list)

def play_hangman(word, hint):
    word = word.lower()
    guessed_letters = set()
    attempts = 5

    print("Welcome to Hangman!")
    print("Hint: " + hint)
    print("Try to guess the word. You have 5 attempts.")

    while attempts > 0:
        display_word = "".join([letter if letter in guessed_letters else "_" for letter in word])

        print(stages[5 - attempts])
        print("Word: " + display_word)
        print("Guessed letters: " + ", ".join(guessed_letters))
        print(f"Attempts left: {attempts}")

        if set(word) == guessed_letters:
            print(f"Congratulations! You guessed the word: {word}")
            break

        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You've already guessed that letter.")
        else:
            guessed_letters.add(guess)
            if guess not in word:
                attempts -= 1

    if attempts == 0 and set(word) != guessed_letters:
        print(f"Out of attempts! The word was '{word}'.")
        print(stages[5]) 
if __name__ == "__main__":
    chosen_word = choose_word()
    play_hangman(chosen_word["word"], chosen_word["hint"])
