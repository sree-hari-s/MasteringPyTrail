from turtle import Turtle
FONT = ("Courier", 24, "normal")
ALIGNMENT="center"

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('black')
        self.penup()
        self.hideturtle()
        self.goto(-280,260)
        self.level = 1
        self.current_level()
        
    def increase_level(self):
        self.clear()
        self.level += 1
        self.current_level()
        
    def current_level(self):
        self.write(f'Level {self.level}',font=FONT)
        
    def game_over(self):
        self.goto(0,0)
        self.write("Game Over",align=ALIGNMENT,font=FONT)