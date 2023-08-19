import constants
from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape('circle')
        self.color('white')
        self.goto(0, -100)
        self.x_move = 4
        self.y_move = 4
        self.move_speed = constants.BALL_SPEED

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1
        self.move_speed *= 0.9

    def bounce_x(self):
        self.x_move *= -1

    def reset_position(self):
        self.home()
        self.move_speed = constants.BALL_SPEED

    def check_collision(self, paddle, wall, scoreboard):
        top_border_ball = int(self.ycor() + constants.BALL_HEIGHT / 2)
        bottom_border_ball = int(self.ycor() - constants.BALL_HEIGHT / 2)
        left_border_ball = int(self.xcor() - constants.BALL_WIDTH / 2)
        right_border_ball = int(self.xcor() + constants.BALL_WIDTH / 2)
        top_border_paddle = int(paddle.ycor() + constants.PADDLE_HEIGHT / 2)

        # Check collision with bricks
        for brick in wall.bricks:
            top_border_brick = int(brick.ycor() + constants.BRICK_HEIGHT / 2)
            bottom_border_brick = int(brick.ycor() - constants.BRICK_HEIGHT / 2)
            left_border_brick = int(brick.xcor() - constants.BRICK_WIDTH / 2)
            right_border_brick = int(brick.xcor() + constants.BRICK_WIDTH / 2)

            if (left_border_ball <= right_border_brick and
                    right_border_ball >= left_border_brick and
                    top_border_ball >= bottom_border_brick and
                    bottom_border_ball <= top_border_brick):

                wall.delete(brick)
                scoreboard.update_score()

                if left_border_ball <= left_border_brick or right_border_ball >= right_border_brick:
                    self.bounce_x()
                else:
                    self.bounce_y()

        # Check collision with paddle
        if self.distance(paddle) < constants.PADDLE_WIDTH and bottom_border_ball == top_border_paddle:
            if paddle.xcor() > 0:
                if self.xcor() > paddle.xcor():
                    self.bounce_x()
                    self.bounce_y()
                else:
                    self.bounce_y()
            elif paddle.xcor() < 0:
                if self.xcor() < paddle.xcor():
                    self.bounce_x()
                    self.bounce_y()
                else:
                    self.bounce_y()
            else:
                self.bounce_x()
                self.bounce_y()

        # Check collision with walls
        if left_border_ball <= constants.LEFT_BORDER or right_border_ball >= constants.RIGHT_BORDER:
            self.bounce_x()

        # Check collision with scoreboard
        if top_border_ball >= constants.TOP_BORDER_BRICKS + constants.PADDING:
            self.bounce_y()