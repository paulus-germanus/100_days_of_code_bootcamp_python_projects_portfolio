from turtle import Turtle, Screen
import random
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(800, 600)
screen.tracer(0)


def l_up():
    l_ycor = 280
    l_seg = 0
    for l in left_player_racquet:
        if left_player_racquet[l_seg].ycor() <= l_ycor:
            l_ycor -= 10
            l_seg += 1
            l.forward(20)


def l_down():
    l_ycor = -180
    l_seg = 0
    for l in left_player_racquet:
        if left_player_racquet[l_seg].ycor() >= l_ycor:
            l_ycor -= 10
            l_seg += 1
            l.backward(20)


def r_up():
    r_ycor = 280
    r_seg = 0
    for r in right_player_racquet:
        if right_player_racquet[r_seg].ycor() <= r_ycor:
            r_ycor -= 10
            r_seg += 1
            r.forward(20)


def r_down():
    r_ycor = -180
    r_seg = 0
    for r in right_player_racquet:
        if right_player_racquet[r_seg].ycor() >= r_ycor:
            r_ycor -= 10
            r_seg += 1
            r.backward(20)


mid_line_t = Turtle()
mid_line_t.speed(0)
mid_line_t.color("white")
mid_line_t.pencolor("white")
mid_line_t.penup()
mid_line_t.hideturtle()
mid_line_t.goto(0, 295)
mid_line_t.setheading(270)
for x in range(14):
    mid_line_t.penup()
    mid_line_t.forward(20)
    mid_line_t.pendown()
    mid_line_t.forward(20)

left_player_score = 0
right_player_score = 0

left_player_score_t = Turtle()
left_player_score_t.speed(0)
left_player_score_t.color("white")
left_player_score_t.penup()
left_player_score_t.hideturtle()
left_player_score_t.goto(-55, 230)
left_player_score_t.write(arg=left_player_score, align="center", font=("Calibri", 30, "bold"))

right_player_score_t = Turtle()
right_player_score_t.speed(0)
right_player_score_t.color("white")
right_player_score_t.penup()
right_player_score_t.hideturtle()
right_player_score_t.goto(55, 230)
right_player_score_t.write(arg=right_player_score, align="center", font=("Calibri", 30, "bold"))

left_racquet_start_posit = [(-335, 40), (-335, 30), (-335, 20), (-335, 10), (-335, 0), (-335, -10), (-335, -20),
                            (-335, -30), (-335, -40), (-335, -50)]
left_player_racquet = []
for l in left_racquet_start_posit:
    l_seg = Turtle()
    l_seg.speed(0)
    l_seg.left(90)
    l_seg.shape("square")
    l_seg.color("white")
    l_seg.penup()
    l_seg.goto(l)
    l_seg.shapesize(0.5, 0.5, 0)
    left_player_racquet.append(l_seg)

right_racquet_start_posit = [(330, 40), (330, 30), (330, 20), (330, 10), (330, 0), (330, -10), (330, -20), (330, -30),
                             (330, -40), (330, -50)]
right_player_racquet = []
for r in right_racquet_start_posit:
    r_seg = Turtle()
    r_seg.speed(0)
    r_seg.left(90)
    r_seg.shape("square")
    r_seg.color("white")
    r_seg.penup()
    r_seg.goto(r)
    r_seg.shapesize(0.5, 0.5, 0)
    right_player_racquet.append(r_seg)

shuttlecock = Turtle()
shuttlecock.speed(0)
shuttlecock.color("white")
shuttlecock.penup()
shuttlecock.shape("circle")
shuttlecock.shapesize(1.2, 1.2, 0)
shuttlecock.setheading(random.choice(
    [random.randint(315, 360), random.randint(0, 45), random.randint(135, 180), random.randint(181, 225)]))

screen.listen()
screen.onkey(fun=l_up, key="w")
screen.onkey(fun=l_down, key="s")
screen.onkey(fun=r_up, key="Up")
screen.onkey(fun=r_down, key="Down")

game_on = True

while game_on:
    screen.update()
    time.sleep(0.08)
    shuttlecock.forward(10)

    for l in left_player_racquet:
        if shuttlecock.distance(l) <= 20 and shuttlecock.xcor() > -340:
            shuttlecock.setheading(180 - shuttlecock.heading())

    for r in right_player_racquet:
        if shuttlecock.distance(r) <= 20 and shuttlecock.xcor() <= 335:
            shuttlecock.setheading(180 - shuttlecock.heading())

    if shuttlecock.xcor() > 380:
        shuttlecock.goto(0, 0)
        shuttlecock.setheading(
            random.choice(
                [random.randint(315, 360), random.randint(0, 45), random.randint(135, 180), random.randint(181, 225)]))
        left_player_score_t.clear()
        left_player_score += 1
        left_player_score_t.write(arg=left_player_score, align="center", font=("Calibri", 30, "bold"))
    elif shuttlecock.xcor() < -380:
        shuttlecock.goto(0, 0)
        shuttlecock.setheading(
            random.choice(
                [random.randint(315, 360), random.randint(0, 45), random.randint(135, 180), random.randint(181, 225)]))
        right_player_score_t.clear()
        right_player_score += 1
        right_player_score_t.write(arg=right_player_score, align="center", font=("Calibri", 30, "bold"))
    elif shuttlecock.ycor() > 290 or shuttlecock.ycor() < -290:
        shuttlecock.setheading(-shuttlecock.heading())