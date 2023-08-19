from turtle import Turtle
import constants


class Brick(Turtle):
    def __init__(self, x_cor, y_cor, color_num):
        super().__init__()
        self.penup()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=4)
        self.color(constants.COLORS[color_num])
        self.goto(x=x_cor, y=y_cor)


class Bricks:
    def __init__(self):
        self.bricks = []
        self.create_wall()

    def create_wall(self):
        y = constants.TOP_BORDER_BRICKS + constants.BRICK_HEIGHT
        for row_num in range(8):
            y -= constants.BRICK_HEIGHT + 5
            for x in range(constants.LEFT_BORDER_BRICKS, constants.RIGHT_BORDER_BRICKS, constants.BRICK_WIDTH + 5):
                brick = Brick(x, y, row_num)
                self.bricks.append(brick)

    def delete(self, brick):
        brick.goto(3000, 3000)
        self.bricks.remove(brick)

    def reset(self):
        for brick in self.bricks:
            self.delete(brick)
        self.create_wall()
