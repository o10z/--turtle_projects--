import random
import turtle as t
from turtle import Turtle, Screen

rgb_list = [(120, 94, 77), (34, 35, 56), (75, 79, 115), (105, 79, 105), (52, 38, 48), (173, 155, 122), (190, 130, 187),
            (53, 54, 94), (52, 37, 30), (144, 132, 100)]
t.colormode(255)

tim = Turtle()
tim.hideturtle()
tim.speed("fastest")


def random_colour():
    colour = random.choice(rgb_list)
    r = colour[0]
    g = colour[1]
    b = colour[2]
    return r, g, b


def dot_line(spacing):
    for _ in range(10):
        tim.dot(15, (random_colour()))
        tim.up()
        tim.fd(spacing)


def left(nu):
    tim.lt(90)
    tim.fd(nu)
    tim.lt(90)
    tim.fd(nu)


def right(n):
    tim.rt(90)
    tim.fd(n)
    tim.rt(90)
    tim.fd(n)


num = 20
for _ in range(10):
    dot_line(num)
    if _ % 2 == 0:
        left(num)
    else:
        right(num)

screen = Screen()
screen.exitonclick()
