from turtle import Turtle, Screen
import random

myColorList = ["red","green","black","purple","blue","goldenrod", "dodger blue"]

t = Turtle()
t.hideturtle()
t.penup()
t.speed(0)
t.left(90)
t.forward(250)
t.left(90)
t.forward(60)
t.right(180)
t.pendown()

x = 3

while True:
    t.pencolor(random.choice(myColorList))
    for z in range(x):
        t.forward(100)
        t.right(360/x)
    x += 1



screen = Screen()
screen.exitonclick()