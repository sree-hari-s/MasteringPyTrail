from turtle import Screen
import time
from paddle import Paddle

def Screen_setup():
    screen.bgcolor('black')
    screen.setup(width=800,height=600)

def game():
    Screen_setup()
    screen.tracer(0)
    
    r_paddle = Paddle(-350,0)
    l_paddle = Paddle(350,0)
    
    screen.listen()
    screen.onkey(r_paddle.go_up,'w')
    screen.onkey(r_paddle.go_down,'s')
    screen.onkey(l_paddle.go_up,'Up')
    screen.onkey(l_paddle.go_down,'Down')
    
    game_is_on = True
    while game_is_on:
        screen.update()

screen = Screen()
Screen_setup()

while screen.textinput("Ping-Pong Game", "Do you want to play Pong Game? y/n:").lower() == "y":
    game()
    time.sleep(2)
    screen.clearscreen()
    Screen_setup()


screen.exitonclick()