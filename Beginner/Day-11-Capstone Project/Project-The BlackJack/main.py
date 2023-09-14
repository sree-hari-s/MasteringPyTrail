"""
############## Blackjack Project #####################

Difficulty Normal 😎: Use all Hints below to complete the project.
Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############## Our Blackjack House Rules #####################

# The deck is unlimited in size. 
# There are no jokers. 
# The Jack/Queen/King all count as 10.
# The the Ace can count as 11 or 1.
# Use the following list as the deck of cards:
# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# The cards in the list have equal probability of being drawn.
# Cards are not removed from the deck as they are drawn.
# The computer_cards is the dealer.
"""
import random
from art import logo


def deal_card():
  """
  Returns a random card from the deck.
  """
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card

def calculate_score(cards):
  """
  Returns the score and check for a blackjack (a hand with only 2 cards: ace + 10) and 
  return 0 instead of the actual score. 
  0 will represent a blackjack in our game.
  check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1.
  """
  if len(cards) == 2 and sum(cards) ==21:
    return 0
  elif sum(cards) > 21 and 11 in cards:
    cards.remove(11)
    cards.append(1)
  return sum(cards)

def compare(user_score, computer_score):
  """
  Compares the score of user against computer score and returns the result using return statement
  """
  if user_score > 21 and computer_score > 21:
    return "You went over. You lose "
  
  if user_score == computer_score:
    return "Draw "
  elif computer_score == 0:
    return "Lose, opponent has Blackjack "
  elif user_score == 0:
    return "Win with a Blackjack "
  elif user_score > 21:
    return "You went over. You lose "
  elif computer_score > 21:
    return "Opponent went over. You win "
  elif user_score > computer_score:
    return "You win "
  else:
    return "You lose "


def game():
  print(logo)
  user_cards = []
  computer_cards = []

  for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

  is_game_over = False

  while not is_game_over:
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)

    print(f"Your cards:{user_cards}, Current score:{sum(user_cards)}")
    print(f"Computer's first card:{computer_cards[0]}")
    if user_score == 0 or computer_score == 0 or user_score > 21:
      is_game_over = True
    else:
      user_should_deal = input("\nType 'y' to get another card, type 'n' to pass:")
      if user_should_deal == "y":
        user_cards.append(deal_card())
      else:
        is_game_over = True

  while computer_score !=0 and computer_score<17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)

  print(f"\nYour final Hand is {user_cards} and your final score is {user_score}.")
  print(f"Computer's final hand is {computer_cards} and final score is {computer_score}")
  print(compare(user_score,computer_score))

import os
while input("\nDo you want to play a game of BlackJack? (y/n):")=='y':
  os.system('cls')
  game()




