import turtle as t
import random

t.colormode(255)
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

def draw_circle():
    t.speed('fastest')  
    t.pencolor(random_color())
    t.circle(100)

def draw_spirograph(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        draw_circle()
        t.setheading(t.heading()+size_of_gap)

size = int(t.numinput("Gap","Enter the gap between the circle: "))
draw_spirograph(size)

    
draw_circle()

screen = t.Screen()
screen.exitonclick()