from turtle import Turtle, Screen
import random
pointer = Turtle()
screen = Screen()

side = 3
colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
while side <= 10:
    for _ in range(side):
        pointer.pencolor(random.choice(colors))
        pointer.pensize(2)
        pointer.forward(50)
        pointer.left(360/side)
    side+=1



screen.exitonclick()