from turtle import Turtle, Screen, clearscreen


t = Turtle()
screen = Screen()


def move_forward():
    t.forward(10)


def clear_drawing():
    t.clear()
    t.penup()
    t.home()
    t.pendown()


def move_backward():
    t.backward(10)


def turn_left():
    #t.left(90)
    new_heading = t.heading() +10
    t.setheading(new_heading)


def turn_right():
    #t.right(90)
    new_heading = t.heading()-10
    t.setheading(new_heading)


screen.listen()
screen.onkey(key='w', fun=move_forward)
screen.onkey(key='s', fun=move_backward)
screen.onkey(key='c', fun=clear_drawing)
screen.onkey(key='a', fun=turn_left)
screen.onkey(key='d', fun=turn_right)

screen.exitonclick()
