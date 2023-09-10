from turtle import Turtle, Screen

import pandas
import pandas as pd

screen = Screen()
screen.setup(725, 490)
screen.bgpic("blank_states_img.gif")
screen.tracer(0)
screen.title("State the States")

t = Turtle()
t.hideturtle()
t.penup()

game_on = True
states_stated = 0
states = pd.read_csv("50_states.csv")
state_list = states.state.to_list()

try:
    while game_on:
        screen.update()
        answer = screen.textinput(title=f"{states_stated}/50 States Stated", prompt="State another state's name!").title()
        if answer == "dunno":
            game_on = False
        elif answer in state_list:
            states_stated += 1
            t.goto(int(states[states.state == answer].x.iloc[0]), int(states[states.state == answer].y.iloc[0]))
            t.write(arg=answer, align="center", font=("monaco", 10, "bold"))
            state_list.remove(answer)

    pandas.DataFrame(state_list).to_csv("not_stated_states_to_learn.csv")

except AttributeError:
    pandas.DataFrame(state_list).to_csv("not_stated_states_to_learn.csv")