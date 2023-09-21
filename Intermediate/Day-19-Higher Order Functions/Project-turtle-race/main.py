from turtle import Turtle, Screen
screen = Screen()

screen.setup(width=500, height=400)
user_bet = screen.textinput("Make Your Bet","Which turtle will win the race: ? Enter a color? ").lower()

colors =['violet','indigo','blue','green','yellow','orange','red']
y_start = [100,60,20,-20,-60,-100,-140,-180]
for i in range(len(colors)-1):
    tim = Turtle(shape='turtle')
    tim.color(colors[i])
    tim.penup()
    tim.goto(x=-220,y=y_start[i])

screen.exitonclick()