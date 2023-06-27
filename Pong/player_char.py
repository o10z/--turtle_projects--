from turtle import Turtle


class Character(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.turtlesize(stretch_wid=1, stretch_len=5)
        self.rt(-90)
        self.penup()
        self.speed('fastest')
