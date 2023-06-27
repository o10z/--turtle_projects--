from turtle import Turtle, Screen
tim = Turtle()
screen = Screen()


def move_forwards():
    tim.fd(10)


def move_back():
    tim.bk(10)


def head_left():
    current_heading = tim.heading()
    tim.setheading(current_heading + 10)


def head_right():
    current_heading = tim.heading() + 10
    tim.setheading(current_heading - 10)


def clear():
    tim.reset()


screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_back)
screen.onkey(key="a", fun=head_left)
screen.onkey(key="d", fun=head_right)
screen.onkey(key="c", fun=clear)
screen.exitonclick()
