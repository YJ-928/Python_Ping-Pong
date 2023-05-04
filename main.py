import turtle
from turtle import Screen
from os import path
from time import sleep
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard


# creating game screen and initial setup
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game created by YJ-928")
screen.tracer(0)

# creating paddle obj from Paddle class
paddle = Paddle()
# creating ball obj from Ball class
ball = Ball()
# creating scoreboard obj from Scoreboard class
scoreboard = Scoreboard()

# listen to input user key_press
# onkeypress() to continously move paddle up or down
# while the key is pressed
screen.listen()
screen.onkeypress(paddle.lhs_move_up, "w")
screen.onkeypress(paddle.lhs_move_down, "s")
screen.onkeypress(paddle.rhs_move_up, "Up")
screen.onkeypress(paddle.rhs_move_down, "Down")


# loop condition
game_is_on = True

# loop to continously update/refresh the screen
while game_is_on:
    screen.update()
    sleep(ball.move_speed)
    ball.move()

    # detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y_axis()

    # detect collision with the paddles
    if ball.distance(paddle.rhs_paddle) < 50 and ball.xcor() > 320 or ball.distance(paddle.lhs_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x_axis()

    # detect when ball goes beyond RHS Paddle
    # then LHS player scores a point
    if ball.xcor() > 400:
        ball.reset()
        scoreboard.lhs_point()

    # detect when ball goes beyond LHS Paddle
    # then RHS player scores a point
    if ball.xcor() < -400:
        ball.reset()
        scoreboard.rhs_point()

# to exit only when clicked on screen
screen.exitonclick()
