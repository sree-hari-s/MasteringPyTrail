import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

def Screen_setup():
    screen = Screen()
    screen.title('Turtle Crossing Game')
    screen.setup(width=600, height=600)
    screen.tracer(0)

def game():
    Screen_setup()
    score = Scoreboard()
    car_manager = CarManager()
    player = Player()
    screen.listen()
    screen.onkey(player.move_up,'Up')

    game_is_on = True
    while game_is_on:
        time.sleep(0.1)
        screen.update()
        
        car_manager.create_car()
        car_manager.move_cars()

        # Detect collisions with car
        for car in car_manager.all_cars:
            if car.distance(player) < 20:
                score.game_over()
                #game_is_on = False
                
        # Detect successful crossing 
        if player.is_at_finish_line():
            player.go_to_start()
            score.increase_level()
            car_manager.increase_speed()
        
screen = Screen()
Screen_setup()

while screen.textinput("Turtle Crossing Game", "Do you want to play Turtle Crossing? y/n:").lower() == "y":
    game()
    time.sleep(3)
    screen.clearscreen()
    Screen_setup()