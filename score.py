from turtle import Turtle

LIVES = 3


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.lives = LIVES
        self.score = 0
        self.color('white')
        self.hideturtle()
        self.penup()
        self.show_score_and_lives_remaining()

    def show_score_and_lives_remaining(self):
        self.clear()
        self.uper_wall()
        self.goto(-350, 300)
        self.write(f'Score:{self.score}', align='left', font=('arial', 20, 'bold'))
        self.goto(350, 300)
        self.write(f'Lives Remaining:{self.lives}', align='right', font=('arial', 20, 'bold'))

    def uper_wall(self):
        self.goto(-410, 295)
        self.pensize(5)
        self.pendown()
        self.forward(800)
        self.penup()

    def game_over(self):
        self.show_score_and_lives_remaining()
        self.goto(0, 0)
        self.write('Game Over........', align='center', font=('arial', 30, 'bold'))

    def game_won(self):
        self.show_score_and_lives_remaining()
        self.goto(0, 0)
        self.write('Congratulations you won!!!!', align='center', font=('arial', 30, 'bold'))