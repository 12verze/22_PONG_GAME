from turtle import *
from ball import Ball
from paddle import *
import time
from scoreboard import *

screen = Screen()
screen.bgcolor("black")
screen.setup(800,600)
screen.title("pong game")
screen.tracer(0)
screen.listen()

paddle1 = Paddle(350, 0)
paddle2 = Paddle(-350, 0)

ball = Ball()

score = Score()
score.updatescore()

screen.onkey(paddle1.up,"Up")
screen.onkey(paddle1.down,"Down")
screen.onkey(paddle2.up,"w")
screen.onkey(paddle2.down,"s")


game_on = True
a = 1
b = 1
score1 = 0
score2 = 0


while game_on:
    time.sleep(ball.speedy)
    screen.update()
    ball.move(a,b)

    if int(ball.ycor()) >= 290:
        b = -1
    if int(ball.ycor()) <= -290:
        b = 1


    if ball.distance(paddle1) <50 and ball.xcor() > 320 or ball.distance(paddle2) <50 and ball.xcor() < -320:
        ball.speedy *= 0.7
        if int(ball.xcor()) > 320:
            a = -1
        if int(ball.xcor()) < -320:
            a = 1

    if ball.xcor() >370:
        score.point2()
        ball.goto(0,0)
        a *= -1
        ball.speedy = 0.1
    if ball.xcor() < -370:
        score.point1()
        ball.goto(0,0)
        a *= -1
        ball.speedy = 0.1







screen.exitonclick()