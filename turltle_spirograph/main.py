from turtle import Turtle, Screen
import random
import turtle as t
tim = Turtle()
tim.speed("fastest")
t.colormode(255)
r = 100


def random_colour():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    colour = (r, g, b)
    return colour


for _ in range(180):
    tim.circle(r)
    tim.color(random_colour())
    current_heading = tim.heading()
    tim.setheading(current_heading + 2)

tim.shape("classic")

screen = Screen()
screen.exitonclick()
