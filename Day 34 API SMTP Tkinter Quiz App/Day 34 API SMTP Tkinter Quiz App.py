import tkinter
import smtplib
import requests
import html

my_email = "8888888889asdf@gmail.com"
password = "glwm iacp kcnz isio"
THEME_COLOR = "#375362"
score = 0
final_email = f''
question_number = 0

# __________request quiz questions API__________#

response = requests.get("https://opentdb.com/api.php?amount=10&difficulty=easy&type=boolean")
response.raise_for_status()
json = response.json()["results"]


# __________display next question, true and false button functions__________#


def next_question():
    global question_number, email_entry, final_email, json
    question_frame.config(bg="white")
    question_frame.itemconfig(question_text, fill=THEME_COLOR)
    if question_number < 10:
        final_email += f'Q: {html.unescape(json[question_number]["question"])}\n'
        final_email += f'A: {json[question_number]["correct_answer"]}\n'
        question_frame.itemconfig(question_text, text=html.unescape(json[question_number]["question"]))
        question_number += 1
    else:
        true_button.destroy()
        false_button.destroy()
        send_email_button = tkinter.Button(text="Send Email", command=send_email)
        send_email_button.grid(sticky="nswe", column=0, row=3, columnspan=2, pady=10)
        question_frame.itemconfig(question_text,
                                  text="There are no more questions.\n\nIf you'd like to receive your score and the question list please enter your e-below.")
        email_entry = tkinter.Entry()
        email_entry.insert(0, "max.mustermann@gmail.com")
        email_entry.grid(sticky="nswe", column=0, row=2, columnspan=2, pady=10)


def false():
    global score
    if json[question_number - 1]["correct_answer"] == "False":
        score += 1
        label_point_counter.config(text=f"Score: {score}")
        question_frame.config(bg="green")
        question_frame.itemconfig(question_text, fill="white")
    else:
        question_frame.config(bg="red")
        question_frame.itemconfig(question_text, fill="white")
    window.after(1000, next_question)


def true():
    global score
    if json[question_number - 1]["correct_answer"] == "True":
        score += 1
        label_point_counter.config(text=f"Score: {score}")
        question_frame.config(bg="green")
        question_frame.itemconfig(question_text, fill="white")
    else:
        question_frame.config(bg="red")
        question_frame.itemconfig(question_text, fill="white")
    window.after(1000, next_question)


# __________function to send an SMTP e-mail with score and question list__________#

def send_email():
    connection = smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email, to_addrs=email_entry.get(),
                        msg=f"Subject:Your score is: {score}/10.\n\n{final_email}")
    connection.close()


# __________GUI setup__________#

window = tkinter.Tk()
window.title("API SMTP Tkinter Quiz App")
window.config(padx=20, pady=20, background=THEME_COLOR)

label_point_counter = tkinter.Label(text=f"Score: {score}", bg=THEME_COLOR, font=("helvetica", 15), fg="white")
label_point_counter.grid(column=1, row=0)

question_frame = tkinter.Canvas(width=300, height=260, bg="white", highlightthickness=0)
question_frame.grid(column=0, row=1, columnspan=2, pady=20)

question_text = question_frame.create_text(150, 130, text="", width=280,
                                           font=("helvetica", 15), fill=THEME_COLOR)

false_button_img = tkinter.PhotoImage(file=r"images\false.png")
false_button = tkinter.Button(image=false_button_img, highlightthickness=0, command=false)
false_button.grid(column=0, row=2)

true_button_img = tkinter.PhotoImage(file=r"images\true.png")
true_button = tkinter.Button(image=true_button_img, highlightthickness=0, command=true)
true_button.grid(column=1, row=2)

next_question()

window.mainloop()
