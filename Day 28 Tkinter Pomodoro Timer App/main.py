from tkinter import *
import time

# ---------------------------- CONSTANTS ------------------------------- #
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20


# ---------------------------- TIMER RESET ------------------------------- #

def reset():
    timer_label.config(text="Timer")
    check_mark_label.config(text="")
    canvas.itemconfigure(canvas_text, text="00:00")


# ---------------------------- TIMER MECHANISM ------------------------------- #

def timer(given_time):
    minutes = given_time
    for y in range(given_time):
        if minutes >= 10:
            canvas.itemconfigure(canvas_text, text=f"{minutes}:00")
        else:
            canvas.itemconfigure(canvas_text, text=f"0{minutes}:00")
        minutes -= 1
        seconds = 60
        for x in range(60):
            time.sleep(1)
            window.update()
            seconds -= 1
            if minutes >= 10:
                if seconds >= 10:
                    canvas.itemconfigure(canvas_text, text=f"{minutes}:{seconds}")
                else:
                    canvas.itemconfigure(canvas_text, text=f"{minutes}:0{seconds}")
            else:
                if seconds >= 10:
                    canvas.itemconfigure(canvas_text, text=f"0{minutes}:{seconds}")
                else:
                    canvas.itemconfigure(canvas_text, text=f"0{minutes}:0{seconds}")


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def countdown():
    countdown_on = True
    while countdown_on:
        check_marks = ""
        for n in range(8):
            if n == 7:
                timer_label.config(text="Long Break")
                window.lift()
                window.attributes('-topmost', True)
                window.after_idle(window.attributes, '-topmost', False)
                check_marks += "✓"
                check_mark_label.config(text=check_marks)
                timer(LONG_BREAK_MIN)
                countdown_on = False
            elif n % 2 == 0:
                timer_label.config(text="Work")
                timer(WORK_MIN)
            elif n % 2 != 0:
                timer_label.config(text="Break")
                window.lift()
                window.attributes('-topmost', True)
                window.after_idle(window.attributes, '-topmost', False)
                check_marks += "✓"
                check_mark_label.config(text=check_marks)
                timer(SHORT_BREAK_MIN)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Tkinter Pomodoro Timer")
window.configure(background=YELLOW)
window.config(padx=40, pady=40)

timer_label = Label(text="Timer", font=(FONT_NAME, 26, "bold"), fg=GREEN, bg=YELLOW)
timer_label.grid(column=1, row=0)

canvas = Canvas(window, width=200, height=223, bg=YELLOW, bd=0, highlightthickness=0)
canvas.grid(column=1, row=1)

tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(0, 0, anchor=NW, image=tomato_img)
canvas_text = canvas.create_text(100, 128, text="00:00", font=(FONT_NAME, 26, "bold"), fill=YELLOW)

start_button = Button(text="Start", command=countdown)
start_button.grid(column=0, row=2)

check_mark_label = Label(text="", font=(FONT_NAME, 20, "bold"), fg=GREEN, bg=YELLOW)
check_mark_label.grid(column=1, row=2)

reset_button = Button(text="Reset", command=reset)
reset_button.grid(column=2, row=2)

window.mainloop()
