from turtle import Turtle, Screen

# use WASD to move the turtle, C to clear the screen, ESC to exit the program

t = Turtle()
screen = Screen()


def move_forwards():
    t.forward(10)


def move_backwards():
    t.backward(10)


def turn_right():
    t.right(10)


def turn_left():
    t.left(10)


def clear():
    t.reset()


def exit():
    screen.bye()

screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="c", fun=clear)
screen.onkey(key="Escape", fun=exit)

screen.exitonclick()
