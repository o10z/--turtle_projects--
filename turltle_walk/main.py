from turtle import Turtle, Screen
import random
import turtle as t

t.colormode(255)
tim = Turtle()
tim.hideturtle()
tim.shape("classic")
tim.width(15)
tim.speed("fastest")


colors = ["SkyBlue", "Blue", "Red", "purple", "yellow", "magenta", "green", "Brown", "black"]
num = []

def random_colour():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_colour = (r, g, b)
    return random_colour

def randomwalk():
    for _ in range(200):
        tim.color(random_colour())
        tim.right(random.choice([0, 90, 180, 270]))
        tim.forward(30)

randomwalk()
screen = Screen()
screen.exitonclick()
