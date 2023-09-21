import turtle as t
import random

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

def movement():
    length = int(t.numinput("Random Walk", "Enter a number:"))
    directions = [0,90,180,270]
    tim = t.Turtle()
    for _ in range(length):
        tim.pensize(10)
        tim.speed('fastest')
        tim.color(random.choice(colours))
        tim.forward(30) 
        tim.setheading(random.choice(directions))

movement()
screen = t.Screen()
screen.exitonclick()