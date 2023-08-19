import time
import constants
from turtle import Screen
from ui import Ui
from ball import Ball
from paddle import Paddle
from scoreboard import Scoreboard
from bricks import Bricks


screen = Screen()
screen.setup(constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT)
screen.title("Break Out Game")
screen.bgcolor('black')
screen.tracer(0)
screen.listen()

ui = Ui()

while not ui.game_is_on:
    screen.update()
    screen.onkeypress(ui.start_game, 'Return')

ball = Ball()
wall = Bricks()
paddle = Paddle()
scoreboard = Scoreboard()

screen.onkeypress(ui.toggle_pause, 'p')
screen.onkeypress(paddle.move_left, 'Left')
screen.onkeypress(paddle.move_right, 'Right')

while ui.game_is_on:
    screen.update()
    if not ui.paused:
        time.sleep(ball.move_speed)
        ball.move()
        ball.check_collision(paddle, wall, scoreboard)

        if ball.ycor() < paddle.ycor() - constants.PADDING:
            scoreboard.lives -= 1
            scoreboard.refresh()
            if scoreboard.lives > 0:
                ball.reset_position()
                paddle.reset_position()

    if not wall.bricks or scoreboard.lives == 0:
        ui.game_over()
        wait_time = time.time() + 5

        while time.time() < wait_time:
            screen.update()
            screen.onkeypress(lambda: ui.restart_game(ball, paddle, scoreboard, wall), 'space')
        if not ui.game_is_on:
            screen.clear()


screen.exitonclick()
