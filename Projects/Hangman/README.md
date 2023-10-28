# Hangman Game

The Hangman Game is a Python-based command-line word-guessing game. You will be presented with a word to guess, and you have a limited number of attempts to guess the word by suggesting letters. If you guess all the letters correctly before running out of attempts, you win the game.

## Usage

1. Run the Hangman game script:

```bash
python hangman.py
```

2. You'll be presented with a word to guess, along with a hint.

3. You have 6 attempts to guess the word.

4. To guess a letter, simply type a letter and press Enter.

5. If you guess a correct letter, it will be revealed in the word. If you guess an incorrect letter, it will be added to your list of guessed letters, and you will lose an attempt.

6. Keep guessing letters until you've either guessed the entire word or run out of attempts.

7. If you guess the entire word, you win the game.

8. If you run out of attempts, the game will reveal the correct word, and you lose.

## Word List

The game comes with a predefined list of words and hints. You can customize this list by modifying the `word_list` in the script. Simply add more word and hint pairs to expand the variety of words to guess.