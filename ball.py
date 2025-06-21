from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("green")
        self.speedy = 0.1

    def move(self,a ,b ):
        x = self.xcor() + a*10
        y = self.ycor() + b*10
        self.goto(x, y)

    def reset(self):
        self.goto(0, 0)