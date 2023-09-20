import random
import smtplib
import pandas as pd
import tkinter
import datetime as dt

# __________auto generate current date in the csv for the program to work__________#
# __________ENTER YOUR NAME AND EMAIL FOR THE FOR TESTING PURPOSES__________#
data = pd.read_csv("birthdays.csv").to_dict()
data["name"] = input("For testing purposes please enter your NAME for the program to be able to send you personalised birthday wishes: ")
data["email"] = input("For testing purposes please enter your EMAIL for the program to be able to send you birthday wishes: ")
data["month"] = {0: dt.datetime.today().date().month}
data["day"] = {0: dt.datetime.today().date().day}
pd.DataFrame(data).to_csv("birthdays.csv", index=False)

birthday_data = pd.read_csv("birthdays.csv")
try:
    birthday_name = birthday_data[birthday_data.day == dt.datetime.today().date().day].name.iloc()[0]
    birthday_age = dt.datetime.today().date().year - \
                   birthday_data[birthday_data.day == dt.datetime.today().date().day].year.iloc()[0]
except IndexError:
    birthday_name = ""
    birthday_age = ""
my_email = "8888888889asdf@gmail.com"
password = "glwm iacp kcnz isio"
with open(random.choice([r"letter_templates\letter_1.txt", r"letter_templates\letter_2.txt",
                         r"letter_templates\letter_3.txt"])) as letter:
    named_letter = "".join([x.replace("[NAME]", birthday_name.split(' ', 1)[0]) for x in letter.readlines()])

# __________check for birthdays in the csv file__________#
for x in birthday_data.month:
    if x == dt.datetime.today().date().month:
        for y in birthday_data.day:
            if y == dt.datetime.today().date().day:
                if int(str(birthday_age)[-1]) == 1:
                    ordinal_num_suffix = "st"
                elif int(str(birthday_age)[-1]) == 2:
                    ordinal_num_suffix = "nd"
                elif int(str(birthday_age)[-1]) == 3:
                    ordinal_num_suffix = "rd"
                else:
                    ordinal_num_suffix = "th"


# __________SMTP function to send wishes__________#
def send_wishes():
    connection = smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email,
                        to_addrs=birthday_data[birthday_data.day == dt.datetime.today().date().day].email.iloc()[0],
                        msg=f"Subject:All the best for your {birthday_age}{ordinal_num_suffix} birthday, {birthday_name.split(' ', 1)[0]}!\n\n{named_letter}")
    connection.close()


# __________display the birthday person function__________#
def birthdays_today():
    try:
        birthday_label.config(
            text=f"Today is {birthday_name}'s {birthday_age}{ordinal_num_suffix} birthday!\nWould you like to wish {birthday_name.split(' ', 1)[0]} happy birthday with an email?\n")
        check_button.config(text=f"Wish {birthday_name.split(' ', 1)[0]} happy birthday!", command=send_wishes)
        check_button.grid(column=1, row=1)
    except NameError:
        birthday_label.config(text="No birthdays today")
        check_button.config(text="Press again tomorrow")
        check_button.grid(column=1, row=1)


# __________GUI setup__________#
window = tkinter.Tk()
window.title("SMTP Birthday Wisher")
window.config(padx=25, pady=25)

birthday_label = tkinter.Label()
birthday_label.grid(sticky="nswe", column=0, row=0, columnspan=3)

check_button = tkinter.Button(text="Check for birthdays today", command=birthdays_today)
check_button.grid(column=0, row=0)

window.mainloop()
