import random
import turtle
from turtle import Turtle, Screen

turtle.colormode(255)
t = Turtle()
t.speed(0)
t.hideturtle()
angle = [90, 180, 270]
t.pensize(5)
screen = Screen()
screen.delay(0)


def random_color():
    return random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)


while True:
    t.forward(35)
    t.color(random_color())
    t.right(random.choice(angle))
    if t.xcor() < -250 or t.xcor() > 250 or t.ycor() < -200 or t.ycor() > 200:
        t.penup()
        t.home()
        t.pendown()