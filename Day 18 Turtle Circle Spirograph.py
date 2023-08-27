from turtle import Turtle, Screen
import turtle
import random

turtle.colormode(255)
t = Turtle()
t.hideturtle()
t.speed(0)
screen = Screen()
screen.delay(0)


def random_color():
    return random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)


for x in range(360):
    t.circle(130)
    t.color(random_color())
    t.right(1)

screen.exitonclick()