from turtle import Screen
import time
from pad import Pad
from ball import Ball
from score import Scoreboard
from blocks import Blocks

screen = Screen()
screen.setup(800, 700)
screen.bgcolor('black')
screen.title('Atari Breakout Game')
screen.colormode(255)
screen.tracer(0)
level = screen.numinput(title="Block Types", prompt='Please select the type you want. \nPress 1 for type1\n'
                                                    'Press 2 for type2\n Press 3 for type 3', minval=1, maxval=3)

if not level:
    screen.bye()
else:
    stick = Pad()
    ball = Ball()
    stats = Scoreboard()
    bricks = Blocks(level)

    screen.listen()
    screen.onkeypress(stick.go_right, 'Right')
    screen.onkeypress(stick.go_left, 'Left')

    game_on = True
    speed_time = 0.1
    speed_counter = 1


    def block_delete():
        global speed_counter
        speed_counter += 1
        brick.goto(0, 400)
        index = bricks.blocks_holder.index(brick)
        del bricks.blocks_holder[index]
        stats.score += 1
        stats.show_score_and_lives_remaining()


    while game_on:
        screen.update()
        ball.move_forward()
        if not bricks.blocks_holder:
            stats.game_won()
            game_on = False

        for brick in bricks.blocks_holder:
            # 35 and 38 are calculated using Pythagoras theorem in which the max distance between the ball center and pad center is calculated
            #the abs(abs(brick.ycor()) - abs(ball.ycor())) detects the range of brick height and distance method the ball's xcordinate from the center of brick
            if ball.distance(brick) <= 38 and abs(abs(brick.ycor()) - abs(ball.ycor())) < 15:
                ball.bounce_sideways()
                block_delete()
            elif ball.distance(brick) <= 35:
                ball.bounce_upwall()
                block_delete()

        if ball.xcor() >= 375 or ball.xcor() <= -375:
            ball.bounce_sideways()
        if ball.ycor() >= 280:
            ball.bounce_upwall()
        if ball.ycor() == -308 and ball.distance(stick) <= 50:
            deflection = round(ball.distance(stick))
            if ball.xcor() <= stick.xcor():
                ball.bounce_on_stick(True, deflection)
            else:
                ball.bounce_on_stick(False, deflection)
        if ball.ycor() <= -360:
            ball.restart()
            stick.restart()
            ball.bounce_upwall()
            speed_time = 0.1
            speed_counter = 1
            stats.lives -= 1
            stats.show_score_and_lives_remaining()
        if stats.lives == 0:
            stats.game_over()
            game_on = False
        if speed_counter == 5:
            speed_counter = 1    # this is done so that the speed is not inceased if block is not hit for continuous while loop as speedcounter will remain 5
            speed_time *= 0.9

        time.sleep(speed_time)

    screen.mainloop()