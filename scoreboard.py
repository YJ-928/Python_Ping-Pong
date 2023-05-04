from turtle import Turtle

# Constants
SCORE_COLOR = "white"
SCORE_COLOR_AFTER_LHS_WINS = "blue"
SCORE_COLOR_AFTER_RHS_WINS = "red"
SCORE_SPEED = "fastest"
SCORE_ALIGN = "center"
SCORE_FONT = ("Courier", 60, "normal")
LHS_SCORE_POS = (-100, 200)
RHS_SCORE_POS = (100, 200)


class Scoreboard(Turtle):

    def __init__(self):
        """Scoreboard class inherits from Turtle super class"""
        super().__init__()
        self.color(SCORE_COLOR)
        self.hideturtle()
        self.penup()
        self.lhs_score = 0
        self.rhs_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        """Updates the Scoreboard with new scores"""
        self.clear()
        self.goto(LHS_SCORE_POS)
        self.write(self.lhs_score, align=SCORE_ALIGN, font=SCORE_FONT)
        self.goto(RHS_SCORE_POS)
        self.write(self.rhs_score, align=SCORE_ALIGN, font=SCORE_FONT)

    def lhs_point(self):
        """Updates the score for LHS Player"""
        self.lhs_score += 1
        self.color(SCORE_COLOR_AFTER_LHS_WINS)
        self.update_scoreboard()

    def rhs_point(self):
        """Updates the score for RHS Player"""
        self.rhs_score += 1
        self.color(SCORE_COLOR_AFTER_RHS_WINS)
        self.update_scoreboard()
