from turtle import Turtle


STARTING_POSITION = (0, -298)
MOVE_DISTANCE_X = 10
MOVE_DISTANCE_Y = 10


class Ball(Turtle):
    def __init__(self):
        super().__init__(shape='circle')
        self.color('white')
        self.penup()
        self.goto(STARTING_POSITION)
        self.move_x = MOVE_DISTANCE_X
        self.move_y = MOVE_DISTANCE_Y

    def move_forward(self):
        self.goto(self.xcor() + self.move_x, self.ycor() + self.move_y)

    def bounce_sideways(self):
        self.move_x *= -1

    def bounce_upwall(self):
        self.move_y *= -1

    def bounce_on_stick(self, detect_left_right, deflection):
        if deflection == 16:
            move = 10           # total 4 halfs of paddle deflection at 16 right and left part
        else:
            move = 12           # total 4 halfs of paddle deflection at 32 right and left part
        if detect_left_right:
            self.move_x = -move
        elif not detect_left_right:
            self.move_x = move
        self.move_y *= -1

    def restart(self):
        self.goto(STARTING_POSITION)
