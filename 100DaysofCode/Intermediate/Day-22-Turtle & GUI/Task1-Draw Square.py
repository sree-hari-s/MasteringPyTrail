from turtle import Turtle, Screen, numinput, textinput, clearscreen


screen = Screen()
def square():
    pointer = Turtle()
    pointer.pensize(2)
    length = numinput("Length", "Enter the length of the square:",minval=20, maxval=300)
    for _ in range(4):
        pointer.forward(length)
        pointer.left(90)

while textinput("Draw Again", "Do you want to draw a square? y/n:").lower() == "y":
    square()
    clearscreen()

