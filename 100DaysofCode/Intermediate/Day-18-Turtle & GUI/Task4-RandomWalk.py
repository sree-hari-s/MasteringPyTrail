import turtle as t
import random

t.colormode(255)
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)


def movement():
    length = int(t.numinput("Random Walk", "Enter a number:"))
    directions = [0,90,180,270]
    tim = t.Turtle()
    for _ in range(length):
        tim.pensize(10)
        tim.speed('fastest')
        tim.color(random_color())
        tim.forward(30) 
        tim.setheading(random.choice(directions))

movement()
screen = t.Screen()
screen.exitonclick()