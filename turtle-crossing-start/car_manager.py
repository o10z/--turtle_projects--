import random
from random import Random
from turtle import Turtle
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.speed = 5


    def create_car(self):
        if random.randint(0,3) == 3:
            new_car = Turtle("square")
            new_car.shapesize(stretch_len=2, stretch_wid=1)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            random_y = random.randint(-230, 230)
            new_car.goto(300, random_y)
            new_car.rt(180)
            self.all_cars.append(new_car)

    def move_car(self):
        for car in self.all_cars:
            car.fd(self.speed)

    def upgrade(self):
        self.speed += MOVE_INCREMENT


