from turtle import Screen
from scoreboard import ScoreBoard
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")
screen.onkey(r_paddle.up, "t")
screen.onkey(r_paddle.down, "g")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.07)
    ball.move()

    # detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 \
       or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # when right paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    # when left paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()
