from turtle import Turtle

class Paddle(Turtle):
    def __init__(self,pos_x,pos_y):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.shapesize(stretch_wid=5,stretch_len=1)
        self.penup()
        self.goto(x=pos_x,y=pos_y)
    
    def go_up(self):
        new_y = self.ycor()+20
        self.goto(self.xcor(),new_y)
        
    def go_down(self):
        new_y = self.ycor()-20
        self.goto(self.xcor(),new_y)