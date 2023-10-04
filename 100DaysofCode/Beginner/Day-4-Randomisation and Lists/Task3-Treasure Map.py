"""
# X Marks the Spot Program

In this program, you will write code to mark a spot on a grid with an "X." The grid is represented as a nested list, and it contains 3x3 squares. The initial grid is formatted like this:

```
[['⬜️', '⬜️', '⬜️'],
 ['⬜️', '⬜️', '⬜️'],
 ['⬜️', '⬜️', '⬜️']]
```

To make the grid easier to visualize, the code provided uses the `print(f"{row1}\n{row2}\n{row3}")` format to display it as:

```
['⬜️', '⬜️', '⬜️']
['⬜️', '⬜️', '⬜️']
['⬜️', '⬜️', '⬜️']
```

Now, your task is to create a program that allows users to mark a square on the grid using a two-digit input system:

- The first digit specifies the column (position on the horizontal axis).
- The second digit specifies the row number (position on the vertical axis).

For example, if the user inputs "23," the program should place an "X" at the position shown below:

```
['⬜️', '⬜️', '⬜️']
['⬜️', '⬜️', 'X']
['⬜️', '⬜️', '⬜️']
```

Here are the key steps your program should follow:

1. Accept user input and convert it into a usable format (e.g., "23" should be converted to column 2 and row 3).
2. Update the nested list grid with an "X" at the specified position.

This program provides a fun way to mark a spot on the grid with an "X" and visualize the changes in the grid structure.

Enjoy using this program to explore and mark spots on the grid!
"""

# 🚨 Don't change the code below 👇
row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
horizontal = int(position[0])
vertical = int(position[1])
map[vertical-1][horizontal-1] = 'X'

#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")

