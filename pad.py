from turtle import Turtle

STARTING_POSITION = (0, -320)


class Pad(Turtle):
    def __init__(self):
        super().__init__(shape='square')
        self.shapesize(stretch_wid=1, stretch_len=4.5)
        self.color('cyan')
        self.penup()
        self.goto(STARTING_POSITION)

    def go_right(self):
        if self.xcor() <= 340:
            self.goto(self.xcor() + 20, self.ycor())

    def go_left(self):
        if self.xcor() >= -340:
            self.goto(self.xcor() - 20, self.ycor())

    def restart(self):
        self.goto(STARTING_POSITION)

