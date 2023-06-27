from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.level = 1

    def update(self):
        self.clear()
        self.goto(-200, 250)
        self.write(f"Level:{self.level}", align="center", font=FONT)

    def point(self):
        self.level += 1
        self.update()

    def game_over(self):
        self.goto(0,0)
        self.write(f"Game Over...", align="center", font=FONT)

