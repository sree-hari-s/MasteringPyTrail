"""
# Virtual Coin Toss Program

In this program, you will create a virtual coin toss simulation that randomly outputs either "Heads" or "Tails." The program will follow these guidelines:

- The first letter should be capitalized and spelled exactly like in the example, i.e., "Heads" and "Tails."

To achieve this, you'll use a random number generation technique:

1. Generate a random number, which can be either 0 or 1.
   - 1 represents "Heads."
   - 0 represents "Tails."

Based on the generated number, the program will print either "Heads" or "Tails."

Example Output:
- If the random number is 1, the program will print "Heads."
- If the random number is 0, the program will print "Tails."

This program provides a fun way to simulate a coin toss virtually. Enjoy your virtual coin flipping!

"""

import random
toss = random.randint(0,1)
print("Heads") if toss==0 else print("Tails")