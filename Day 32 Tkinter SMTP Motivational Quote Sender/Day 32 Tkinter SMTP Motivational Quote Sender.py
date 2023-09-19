import smtplib
import random
import tkinter

my_email = "8888888889asdf@gmail.com"
password = "glwm iacp kcnz isio"

def send_quote():
    with open("quotes.txt") as quotes:
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs=email_input.get(),
                            msg=f"Subject:Here's Your Motivational Quote!\n\n{random.choice(quotes.readlines())}")
        connection.close()

window = tkinter.Tk()
window.title("SMTP Motivational Quote Sender")
window.config(padx=25, pady=25)

email_input = tkinter.Entry(width= 40)
email_input.insert(0, string="max.mustermann@gmail.com")
email_input.grid(sticky="nswe", column=0, row=0, columnspan=2)

send_button = tkinter.Button(text="Send Quote", command=send_quote)
send_button.grid(column=2, row=0)

window.mainloop()
