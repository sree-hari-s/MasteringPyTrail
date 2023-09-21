import turtle as t
from random_colors import *


def small_circle():
    """
    Draw a small circle
    """
    t.hideturtle()
    t.colormode(255)
    t.color(random_color())
    t.filling()
    t.begin_fill()
    t.circle(10)
    t.end_fill()
    
t.penup()
# t.hideturtle()
t.setheading(225)
t.forward(300)
t.setheading(0)
number_of_dots = 100

for dot_count in range(1,number_of_dots+1):
    t.colormode(255)
    t.dot(20,random_color())
    t.forward(50)
    if dot_count % 10 == 0:
        t.setheading(90)
        t.forward(50)
        t.setheading(180)
        t.forward(500)
        t.setheading(0)
        
screen = t.Screen()
screen.exitonclick()