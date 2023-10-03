from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial",20,"normal")
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color('white')
        self.hideturtle()
        self.goto(0,270)
        self.score = 0
        with open('data.txt',mode='r') as file:
            self.high_score = int(file.read())
        self.current_score()
        
    def increase_score(self):
        self.score += 1
        self.current_score()

    def current_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}",align=ALIGNMENT,font=FONT)
    
    def game_over(self):
        self.goto(0,0)
        self.write("Game Over",align=ALIGNMENT,font=FONT)
    
    def reset(self):
        if self.score > self.high_score:
            with open('data.txt',mode='w') as file:
                self.high_score = file.write(str(self.score))
        self.score = 0
        self.current_score()