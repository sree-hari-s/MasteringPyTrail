import random

word_list = [
    {"word": "python", "hint": "A popular programming language"},
    {"word": "java", "hint": "Another widely used programming language"},
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
    attempts = 6

    print("Welcome to Hangman!")
    print(f"Hint: {hint}")
    print("Try to guess the word. You have 6 attempts.")

    while attempts > 0:
        display_word = ""
        for letter in word:
            if letter in guessed_letters:
                display_word += letter
            else:
                display_word += "_"

        print("Word: " + display_word)
        print("Guessed letters: " + ", ".join(guessed_letters))
        print(f"Attempts left: {attempts}")

        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You've already guessed that letter.")
        elif guess in word:
            guessed_letters.add(guess)
        else:
            guessed_letters.add(guess)
            attempts -= 1

        if set(word) == guessed_letters:
            print("Congratulations! You guessed the word: " + word)
            break

    if attempts == 0:
        print(f"Out of attempts! The word was '{word}'.")

if __name__ == "__main__":
    chosen_word = choose_word()
    play_hangman(chosen_word["word"], chosen_word["hint"])
