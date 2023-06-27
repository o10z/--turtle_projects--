import time
import turtle
from turtle import Turtle, Screen
from player_char import Character
from ball import Ball
from scoreboard import Scoreboard

# Screen layout and colour
screen = Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("PONG")

# ball
ball = Ball()
# player 1
left_player = Character()
left_player.goto(-350, 0)

# player 2
right_player = Character()
right_player.goto(350, 0)

# scoreboard
scoreboard = Scoreboard()
scoreboard.update()

# players movement
move = 20
def left_up():
    left_player.fd(move)


def left_down():
    left_player.bk(move)


def right_up():
    right_player.fd(move)


def right_down():
    right_player.bk(move)



screen.onkey(left_up, key="w")
screen.onkey(left_down, key="s")
screen.onkey(right_up, key="Up")
screen.onkey(right_down, key="Down")
screen.listen()



game_is_on = True
while game_is_on:
    time.sleep(0.04)
    screen.update()
    ball.move()
    # Detect coalition with wall

    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.wall_bounce()

    if ball.distance(right_player) < 50 and ball.xcor() > 330 or ball.distance(left_player) < 50 and ball.xcor() < -330:
        ball.paddle_bounce()

    if ball.xcor() > 380:
        ball.reset()
        scoreboard.l_point()

    if ball.xcor() < -380:
        ball.reset()
        scoreboard.r_point()



screen.exitonclick()


