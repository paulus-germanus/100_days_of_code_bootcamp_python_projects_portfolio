import tkinter
import pandas as pd
import time
import random

BACKGROUND_COLOR = "#B1DDC6"

card_bank = pd.read_csv(r"data\french_words.csv")
to_be_learned = card_bank.to_dict(orient="records")
random_word = {}
canvas_word = ""


def right_answer():
    try:
        to_be_learned.remove(random_word)
        show_card()
    except:
        canvas.itemconfig(canvas_lang_indicator, text="Congrats!")
        canvas.itemconfig(canvas_word, text="You've learned all the words\nin the wordbank.")


def wrong_answer():
    show_card()


def show_card():
    global random_word, canvas_word, canvas_lang_indicator
    random_word = random.choice(to_be_learned)
    canvas_card_front_img = canvas.create_image(400, 263, image=card_front)
    canvas_lang_indicator = canvas.create_text(400, 130, text="French", font=("helvetica", 26, "italic"))
    canvas_word = canvas.create_text(400, 245, text=random_word["French"], font=("helvetica", 36, "bold"))
    window.update()
    time.sleep(1)
    canvas.itemconfig(canvas_card_front_img, image=card_back)
    canvas.itemconfig(canvas_lang_indicator, text="English")
    canvas.itemconfig(canvas_word, text=random_word["English"])
    window.update()


window = tkinter.Tk()
window.title("Tkinter Flashcard App")
window.configure(background=BACKGROUND_COLOR)
window.config(padx=40, pady=40)

canvas = tkinter.Canvas(window, width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)

card_front = tkinter.PhotoImage(file="images\card_front.png")
card_back = tkinter.PhotoImage(file="images\card_back.png")

right_button_img = tkinter.PhotoImage(file=r"images\right.png")
wrong_button_img = tkinter.PhotoImage(file=r"images\wrong.png")

wrong_button = tkinter.Button(window, image=wrong_button_img, highlightthickness=0,
                              command=wrong_answer)
wrong_button.grid(column=0, row=1)

right_button = tkinter.Button(window, image=right_button_img, highlightthickness=0,
                              command=right_answer)
right_button.grid(column=1, row=1)

show_card()

window.mainloop()
