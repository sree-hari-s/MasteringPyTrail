from turtle import Turtle, Screen

dash = Turtle()
screen = Screen()

for _ in range(10):
    dash.forward(10)
    dash.penup()
    dash.forward(10)
    dash.pendown()

screen.exitonclick()