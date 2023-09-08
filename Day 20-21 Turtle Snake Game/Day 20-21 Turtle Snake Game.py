from turtle import Turtle, Screen
import turtle
import random
import time

turtle.colormode(255)

rgb_colors = [(226, 231, 235), (54, 108, 149), (225, 201, 108), (134, 85, 58), (229, 235, 234), (224, 141, 62),
              (197, 144, 171), (143, 180, 206), (137, 82, 106), (210, 90, 68), (232, 226, 194), (69, 101, 86),
              (132, 183, 132), (65, 156, 86), (137, 132, 74), (232, 221, 225), (58, 47, 41), (106, 46, 54),
              (12, 104, 95), (118, 125, 145), (215, 176, 187), (223, 178, 168)]

screen = Screen()
screen.setup(660, 660)
screen.delay(0)
screen.bgcolor("black")
screen.tracer(0)

bug_t = Turtle()
bug_t.speed(0)
bug_t.hideturtle()
bug_t.penup()


def spawn_new_bug_t():
    bug_t.clear()
    global bug_t_cord_x
    global bug_t_cord_y
    bug_t_cord_x = random.randint(-300, 300)
    bug_t_cord_y = random.randint(-300, 300)
    bug_t.goto(bug_t_cord_x, bug_t_cord_y)
    bug_t.dot(23, random.choice(rgb_colors))


def north():
    if segments[0].heading() != 270:
        segments[0].setheading(90)


def south():
    if segments[0].heading() != 90:
        segments[0].setheading(270)


def east():
    if segments[0].heading() != 180:
        segments[0].setheading(0)


def west():
    if segments[0].heading() != 0:
        segments[0].setheading(180)

with open("high_score.txt") as file:
    high_score = file.read()
score = 0

score_t = Turtle()
score_t.speed(0)
score_t.hideturtle()
score_t.color("white")
score_t.penup()
score_t.goto(0, 290)
score_t.write(arg=f"Score: {score} | High score: {high_score}", align="center", font=("Calibri", 23, "bold"))

starting_position = [(0, 0), (20, 0), (40, 0)]
segments = []

for position in starting_position:
    snake_t = Turtle()
    snake_t.penup()
    snake_t.color("white")
    snake_t.shape("square")
    snake_t.goto(position)
    segments.append(snake_t)

screen.listen()
screen.onkey(fun=north, key="Up")
screen.onkey(fun=south, key="Down")
screen.onkey(fun=east, key="Right")
screen.onkey(fun=west, key="Left")

spawn_new_bug_t()
game_on = True

while game_on:
    screen.update()
    time.sleep(0.2)
    for segment_number in range(len(segments)-1, 0, -1):
        new_x = segments[segment_number - 1].xcor()
        new_y = segments[segment_number - 1].ycor()
        segments[segment_number].goto(new_x, new_y)
    segments[0].forward(20)
    for x in range(1, len(segments)-1):
        if segments[0].distance(segments[x]) < 10:
            score_t.goto(0, 0)
            score_t.write(arg="GAME OVER", align="center", font=("Calibri", 40, "bold"))
            game_on = False
    if segments[0].xcor() >= 330 or segments[0].xcor() <= -330 or segments[0].ycor() >= 330 or segments[0].ycor() <= -330:
        score_t.goto(0, 0)
        score_t.write(arg="GAME OVER", align="center", font=("Calibri", 40, "bold"))
        game_on = False
    elif bug_t_cord_x-14 <= segments[0].xcor() <= bug_t_cord_x+14 and bug_t_cord_y-14 <= segments[0].ycor() <= bug_t_cord_y+14:
        score += 1
        if high_score < score:
            high_score += 1
        spawn_new_bug_t()
        score_t.clear()
        score_t.write(arg=f"Score: {score} | High score: {high_score}", align="center", font=("Calibri", 23, "bold"))
        snake_t = Turtle()
        snake_t.penup()
        snake_t.color("white")
        snake_t.shape("square")
        segments[-1].position()
        segments.append(snake_t)
        with open("high_score.txt", mode="w") as high_s:
            high_s.write(f"{high_score}")