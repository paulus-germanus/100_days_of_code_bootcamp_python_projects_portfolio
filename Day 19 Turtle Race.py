from scipy.spatial import KDTree
from webcolors import (
    CSS3_HEX_TO_NAMES,
    hex_to_rgb, )
from turtle import Turtle, Screen
import turtle
import random

turtle.colormode(255)
rgb_colors = [(226, 231, 235), (54, 108, 149), (225, 201, 108), (134, 85, 58), (229, 235, 234), (224, 141, 62),
              (197, 144, 171), (143, 180, 206), (137, 82, 106), (210, 90, 68), (232, 226, 194), (69, 101, 86),
              (132, 183, 132), (65, 156, 86), (137, 132, 74), (232, 221, 225), (58, 47, 41), (106, 46, 54),
              (12, 104, 95), (118, 125, 145), (215, 176, 187), (223, 178, 168)]

screen = Screen()
screen.setup(width=500, height=400)
screen.delay(0)


def convert_rgb_to_names(rgb_tuple):
    # a dictionary of all the hex and their respective names in css3
    css3_db = CSS3_HEX_TO_NAMES
    names = []
    rgb_values = []
    for color_hex, color_name in css3_db.items():
        names.append(color_name)
        rgb_values.append(hex_to_rgb(color_hex))

    kdt_db = KDTree(rgb_values)
    distance, index = kdt_db.query(rgb_tuple)
    return names[index]


finish_line_t = Turtle()
finish_line_t.penup()
finish_line_t.hideturtle()
finish_line_t.goto(210, 170)
finish_line_t.pendown()
finish_line_t.goto(210, -170)

t_list = [Turtle() for t in range(8)]
t_color_names = []
t_start_x = -230
t_start_y = 157.5

for t in t_list:
    t.penup()
    t.shape("turtle")
    t.setx(t_start_x)
    t.sety(t_start_y)
    t_color = random.choice(rgb_colors)
    t.color(t_color)
    t_color_names.append(convert_rgb_to_names(t_color))
    rgb_colors.remove(t_color)
    t_start_y -= 45

user_colour_choice = turtle.textinput(title="Make your bet.",
                                      prompt=f"Which turtle will win the race? Choose a color ({t_color_names[0]}, {t_color_names[1]}, {t_color_names[2]}, {t_color_names[3]}, {t_color_names[4]}, {t_color_names[5]}, {t_color_names[6]}, {t_color_names[7]}): ")

screen.delay(10)
game_on = True

while game_on:
    for t in t_list:
        t.forward(random.randint(1, 10))
        if t.xcor() >= 200:
            game_on = False
            color_tuple = ()
            if convert_rgb_to_names(t.color()[0]) == user_colour_choice:
                print(f"Congrats! You've won! The {convert_rgb_to_names(t.color()[0])} turtle has won the race!")
            else:
                print(f"Sorry... you've lost. You chose {user_colour_choice} and the winning turtle was {convert_rgb_to_names(t.color()[0])}.")

screen.exitonclick()
