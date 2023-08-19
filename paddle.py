import constants
from turtle import Turtle


class Paddle(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.color("white")
        self.goto(0, constants.BOTTOM_BORDER + constants.PADDING)

    def move_right(self):
        if self.xcor() < constants.DIST_PADDLE_BORDER:
            new_x = self.xcor() + constants.PADDLE_SPEED
            self.goto(new_x, self.ycor())

    def move_left(self):
        if self.xcor() > -constants.DIST_PADDLE_BORDER:
            new_x = self.xcor() - constants.PADDLE_SPEED
            self.goto(new_x, self.ycor())

    def reset_position(self):
        self.goto(0, constants.BOTTOM_BORDER + constants.PADDING)
