from turtle import Turtle
import turtle
import random

turtle.colormode(255)
t = Turtle()
t.hideturtle()
t.speed(0)
t.penup()
t.setx(-55)
t.sety(270)
t.pendown()


def random_color():
    return random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)


x = 3

while True:
    t.pencolor(random_color())
    for z in range(x):
        t.forward(100)
        t.right(360/x)
    x += 1
