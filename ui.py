from turtle import Turtle
import constants


class Ui(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 50)
        self.paused = False
        self.game_is_on = False
        self.write("BREAKOUT GAME!", align="center", font=(constants.FONT_STYLE[0], 50, constants.FONT_STYLE[2]))
        self.goto(0, 0)
        self.write("Press 'Return' to start.", align="center", font=constants.FONT_STYLE)

    def pause(self):
        self.clear()
        self.goto(0, -10)
        self.write("PAUSE", align="center", font=(constants.FONT_STYLE[0], 50, constants.FONT_STYLE[2]))
        self.goto(0, -60)
        self.write("Press 'p' to resume.", align="center", font=constants.FONT_STYLE)

    def game_over(self):
        self.clear()
        self.goto(0, -10)
        self.write("GAME OVER", align="center", font=(constants.FONT_STYLE[0], 50, constants.FONT_STYLE[2]))
        self.goto(0, -60)
        self.write("Press 'Space' to restart or", align="center", font=constants.FONT_STYLE)
        self.goto(0, -80)
        self.write("wait 5 seconds and click to exit.", align="center", font=constants.FONT_STYLE)
        self.game_is_on = False

    def toggle_pause(self):
        self.paused = not self.paused
        if self.paused:
            self.pause()
        else:
            self.clear()

    def start_game(self):
        self.clear()
        self.game_is_on = True

    def restart_game(self, ball, paddle, scoreboard, wall):
        self.clear()
        self.game_is_on = True
        ball.reset_position()
        paddle.reset_position()
        scoreboard.reset()
        wall.reset()