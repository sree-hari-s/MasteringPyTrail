print("Play Rock Paper Scissors\n")
    #Draw 
    #0 0
    #1 1
    #2 2     
    
    # Lose
    # 0 1 
    # 1 2
    # 2 0 
    
    # Win 
    # 0 2 
    # 1 0 
    # 2 1
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random
your_choice = int(input("What do you choose? Type 0 for Rock,1 for Paper and 2 for Scissors.\n"))
computer_choice = random.randint(0,2)
# if your_choice == 0:
#     print(rock)
# elif your_choice == 1:
#     print(paper)
# elif your_choice == 2:
#     print(scissors)
# else:
#     print("Invalid choice!")
#     exit()
# print("Computer chose:")   
# if computer_choice == 0:
#     print(rock)
# elif computer_choice == 1:
#     print(paper)
# elif computer_choice == 2:
#     print(scissors)

# if your_choice == computer_choice:
#     print("Draw!")
# elif (your_choice == 0 and computer_choice == 1) or (your_choice == 1 and computer_choice == 2) or (your_choice ==2 and computer_choice == 0) :
#     print("You Lose")
# elif (your_choice == 0 and computer_choice == 2) or (your_choice == 1 and computer_choice == 0) or (your_choice == 2 and computer_choice ==1):
#     print("You Win")


#Alternate code
# Define the win and lose conditions
if your_choice >2:
    print("Invalid Choice! You lose")
    exit()
else:
    game_images = [rock,paper,scissors]
    print("Your Choice",game_images[your_choice])
    print("Computer Choice",game_images[computer_choice])
    lose_conditions = [(0, 1), (1, 2), (2, 0)]
    win_conditions = [(0, 2), (1, 0), (2, 1)]

    if (your_choice,computer_choice) in lose_conditions:
        print("You Lose")
    elif (your_choice,computer_choice) in win_conditions:
        print("You Win")
