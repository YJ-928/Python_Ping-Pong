from turtle import Turtle

# Constants
# to create long paddle using a single stretched turtle
PADDLE_STRETCH_LEN = 1
PADDLE_STRETCH_WID = 5
PADDLE_SHAPE = "square"
PADDLE_COLOR_RHS = "red"
PADDLE_COLOR_LHS = "blue"
PADDLE_SPEED = "fastest"
LHS_PADDLE_POSITION = (-350, 0)
RHS_PADDLE_POSITION = (350, 0)


class Paddle:

    def __init__(self):
        self.paddle_list = []
        self.create_paddle()
        self.lhs_paddle = self.paddle_list[0]
        self.rhs_paddle = self.paddle_list[1]

    def create_paddle(self):
        """Creates long singular paddle's using
        stretch len and stretch width method"""
        # creating LHS paddle
        paddle_LHS = Turtle(shape=PADDLE_SHAPE)
        paddle_LHS.shapesize(stretch_len=PADDLE_STRETCH_LEN,
                             stretch_wid=PADDLE_STRETCH_WID)
        paddle_LHS.color(PADDLE_COLOR_LHS)
        paddle_LHS.speed(PADDLE_SPEED)
        paddle_LHS.penup()
        paddle_LHS.goto(LHS_PADDLE_POSITION)
        self.paddle_list.append(paddle_LHS)
        # creating RHS paddle
        paddle_RHS = Turtle(shape=PADDLE_SHAPE)
        paddle_RHS.shapesize(stretch_len=PADDLE_STRETCH_LEN,
                             stretch_wid=PADDLE_STRETCH_WID)
        paddle_RHS.color(PADDLE_COLOR_RHS)
        paddle_RHS.speed(PADDLE_SPEED)
        paddle_RHS.penup()
        paddle_RHS.goto(RHS_PADDLE_POSITION)
        self.paddle_list.append(paddle_RHS)

    def lhs_move_up(self):
        """Moves LHS paddle up"""
        new_y = self.lhs_paddle.ycor() + 20
        self.lhs_paddle.goto(self.lhs_paddle.xcor(), new_y)

    def lhs_move_down(self):
        """Moves LHS paddle down"""
        new_y = self.lhs_paddle.ycor() - 20
        self.lhs_paddle.goto(self.lhs_paddle.xcor(), new_y)

    def rhs_move_up(self):
        """Moves RHS paddle up"""
        new_y = self.rhs_paddle.ycor() + 20
        self.rhs_paddle.goto(self.rhs_paddle.xcor(), new_y)

    def rhs_move_down(self):
        """Moves RHS paddle down"""
        new_y = self.rhs_paddle.ycor() - 20
        self.rhs_paddle.goto(self.rhs_paddle.xcor(), new_y)
