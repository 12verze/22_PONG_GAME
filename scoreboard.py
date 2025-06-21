from turtle import *

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("red")
        self.score1 = 0
        self.score2 = 0

    def updatescore(self):
        self.clear()
        self.goto(180, 200)
        self.write(self.score1, align="center", font=("Courier", 30, "normal"))
        self.goto(-180, 200)
        self.write(self.score2, align="center", font=("Courier", 30, "normal"))

    def point1(self):
        self.score1 += 1
        self.updatescore()

    def point2(self):
        self.score2 += 1
        self.updatescore()