from turtle import Turtle, Screen
import random

tim = Turtle()
tim.shape("turtle")
colors = ["SkyBlue", "Blue", "Red", "purple", "yellow", "magenta", "green", "Brown", "black"]


def star():
    tim.color()
    for _ in range(5):
        tim.fd(100)
        tim.rt(216)


def make_shapes(number_of_side):
    angle = 360 / number_of_side
    for _ in range(number_of_side):
        tim.fd(100)
        tim.rt(angle)


for _ in range(3, 11):
    tim.color(random.choice(colors))
    make_shapes(_)

star()

screen = Screen()
screen.exitonclick()
