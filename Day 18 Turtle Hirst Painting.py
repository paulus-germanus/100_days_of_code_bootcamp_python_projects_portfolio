from turtle import Turtle, Screen
import turtle
import random

turtle.colormode(255)

t = Turtle()
t.hideturtle()
t.speed(0)
t.penup()
t.setx(-265)
t.sety(-215)
screen = Screen()
screen.delay(0)

rgb_colors = [(226, 231, 235), (54, 108, 149), (225, 201, 108), (134, 85, 58), (229, 235, 234), (224, 141, 62),
              (197, 144, 171), (143, 180, 206), (137, 82, 106), (210, 90, 68), (232, 226, 194), (188, 78, 122),
              (69, 101, 86), (132, 183, 132), (65, 156, 86), (137, 132, 74), (48, 155, 195), (183, 191, 202),
              (232, 221, 225), (58, 47, 41), (47, 59, 96), (38, 44, 64), (106, 46, 54), (41, 55, 48), (12, 104, 95),
              (118, 125, 145), (182, 194, 199), (215, 176, 187), (223, 178, 168), (54, 45, 52)]

for y in range(15):
    for x in range(35):
        t.dot(10, random.choice(rgb_colors))
        t.forward(15)
        t.dot(10, random.choice(rgb_colors))
    t.left(90)
    t.forward(15)
    t.left(90)

    for x in range(35):
        t.dot(10, random.choice(rgb_colors))
        t.forward(15)
        t.dot(10, random.choice(rgb_colors))
    t.right(90)
    t.forward(15)
    t.right(90)

screen.exitonclick()