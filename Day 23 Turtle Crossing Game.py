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
screen.setup(600, 600)
screen.tracer(0)

kerb = Turtle()
kerb.hideturtle()
kerb.penup()
kerb.goto(320, 260)
kerb.pendown()
kerb.goto(-320, 260)
kerb.penup()
kerb.goto(320, -260)
kerb.pendown()
kerb.goto(-320, -260)

cars = []

for car in range(30):
    new_car = Turtle()
    new_car.penup()
    new_car.setheading(180)
    new_car.shape("square")
    new_car.shapesize(1, 2, 0)
    new_car.color(random.choice(rgb_colors))
    new_car.goto(random.randint(320, 920), random.randint(-248, 248))
    cars.append(new_car)

level = 1
score_t = Turtle()
score_t.hideturtle()
score_t.penup()
score_t.goto(-240, 261)
score_t.write(arg=f"Level: {level}", align="center", font=("Calibri", 23, "bold"))

turtle = Turtle()
turtle.shape("turtle")
turtle.penup()
turtle.left(90)
turtle.goto(0, -280)


def turtle_move():
    turtle.forward(15)


screen.listen()
screen.onkey(fun=turtle_move, key="space")

game_on = True
car_forward_1 = 3
car_forward_2 = 10
god_mode = 66

while game_on:
    screen.update()
    time.sleep(0.1)
    for c in cars:
        c.forward(random.randint(car_forward_1, car_forward_2))
        if c.xcor() < -330:
            c.goto(random.randint(320, 920), random.randint(-248, 248))
        elif god_mode == 66:
            turtle.color("gold")
            score_t.goto(207, 261)
            score_t.write(arg="GOD MODE", align="center", font=("Calibri", 23, "bold"))
        elif turtle.distance(c) < 20 and god_mode != 66:
            game_on = False
            score_t.goto(0, 0)
            score_t.write(arg="GAME OVER", align="center", font=("Calibri", 40, "bold"))

    if turtle.ycor() >= 270:
        turtle.color("black")
        god_mode = random.randint(0, 100)
        level += 1
        score_t.clear()
        score_t.goto(-240, 261)
        score_t.write(arg=f"Level: {level}", align="center", font=("Calibri", 23, "bold"))
        turtle.goto(0, -280)
        car_forward_1 += 1
        car_forward_2 += 1

screen.exitonclick()
