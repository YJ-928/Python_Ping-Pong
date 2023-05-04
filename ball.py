from turtle import Turtle
import random

# Constants
BALL_SHAPE = "circle"
BALL_COLOR = "white"
BALL_COLOR_AFTER_PADDLE_HIT = ["red", "blue"]
BALL_SPEED_RESET = 0.1
BALL_SPEED_INC = 0.9


class Ball(Turtle):

    def __init__(self):
        """Ball class inherits from Turtle Super class"""
        super().__init__()
        self.color(BALL_COLOR)
        self.shape(BALL_SHAPE)
        self.penup()
        self.move_x = 10
        self.move_y = 10
        self.move_speed = BALL_SPEED_RESET

    def move(self):
        """Moves the ball Continously"""
        new_x = self.xcor() + self.move_x
        new_y = self.ycor() + self.move_y
        self.goto(new_x, new_y)

    def bounce_y_axis(self):
        """Makes the ball bounce back in the 
        vertical or Y-Axis direction"""
        self.move_y *= -1  # rev the direction of the ball vertically

    def bounce_x_axis(self):
        """Makes the ball bounce back in the 
        Horizontal or X-Axis direction"""
        self.move_x *= -1  # rev the direction of the ball horizontally
        self.move_speed *= BALL_SPEED_INC
        self.color(random.choice(BALL_COLOR_AFTER_PADDLE_HIT))

    def reset(self):
        """Makes the ball reset back to centre
        and move in the direction of other player"""
        # to recenter the ball
        self.home()
        self.move_speed = BALL_SPEED_RESET
        self.color(BALL_COLOR)
        # rev both x and y to make it move towards
        # the opposite player at each reset
        self.move_x *= -1
        self.move_y *= -1
