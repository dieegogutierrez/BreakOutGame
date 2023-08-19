import constants
from turtle import Turtle

try:
    with open('highscore.txt', 'r') as file:
        highscore = int(file.read())
except FileNotFoundError:
    with open('highscore.txt', 'w') as file:
        file.write(str(0))
    highscore = 0


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.score = 0
        self.highscore = highscore
        self.lives = 3
        self.hideturtle()
        self.setheading(90)
        self.pensize(width=5)
        self.color("white")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        self.clear()
        self.goto(constants.LEFT_BORDER, constants.TOP_BORDER_BRICKS + constants.PADDING)
        self.pendown()
        self.setheading(0)
        self.forward(constants.RIGHT_BORDER - constants.LEFT_BORDER)
        self.penup()
        self.goto(constants.LEFT_BORDER + constants.PADDING, constants.TOP_BORDER - constants.PADDING)
        self.write(f'Score: {self.score}', font=constants.FONT_STYLE, align='left')
        self.goto(0, constants.TOP_BORDER - constants.PADDING)
        self.write(f'Highest Score: {self.highscore}', font=constants.FONT_STYLE, align='center')
        self.goto(constants.RIGHT_BORDER - constants.PADDING, constants.TOP_BORDER - constants.PADDING)
        self.write("❤️" * self.lives, font=constants.FONT_STYLE, align='right')

    def update_score(self):
        self.score += 20
        if self.score > self.highscore:
            self.highscore = self.score
            with open('highscore.txt', 'w') as file:
                file.write(str(self.highscore))
        self.refresh()

    def reset(self):
        self.score = 0
        self.lives = 3
        self.refresh()