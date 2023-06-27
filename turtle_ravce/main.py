from turtle import Turtle, Screen
import random
screen = Screen()
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make a bet", prompt="Which turtle will win the race? Enter a color:")
position = [-70,-40, -10, 20, 50, 80]
all_turtles = []
is_race_on = False


for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.pu()
    new_turtle.goto(x=-240, y=position[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() >= 225:
            is_race_on = False
            print(f"Winner:{turtle.pencolor()}")
            winner = turtle.pencolor()
            if winner == user_bet:
                print("You won the bet")
            else:
                print("Sorry you lost...GGs")
        else:
            rand_distance = random.randint(1,10)
            turtle.fd(rand_distance)
