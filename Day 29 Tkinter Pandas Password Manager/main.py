import tkinter
import random
import pandas as pd

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '-', '+', '=', '{', '[', '}', ']', '|', ':', ';', '<',
           ',', '>', '.', '?', '/']
upper_alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                  'U', 'V', 'W', 'X', 'Y', 'Z']
lower_alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                  'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']


def pass_gen():
    password_list = []
    for x in range(5):
        password_list.append(random.choice(symbols))
        password_list.append(random.choice(upper_alphabet))
        password_list.append(random.choice(lower_alphabet))
        password_list.append(random.choice(numbers))
    randomized_password_list = "".join(random.sample(password_list, len(password_list)))
    password_entry.delete(0, tkinter.END)
    password_entry.insert(0, string=randomized_password_list)

# ---------------------------- SAVE CREDENTIALS ------------------------------- #


def save_credentials():
    credentials_dict = {
        "website": [website_entry.get()],
        "username": [username_entry.get()],
        "password": [password_entry.get()]
    }
    credentials_df = pd.DataFrame(credentials_dict)
    credentials_df.to_csv("password_manager.csv", mode="a", header=False, index=False)
    website_entry.delete(0, tkinter.END)
    username_entry.delete(0, tkinter.END)
    password_entry.delete(0, tkinter.END)


# -------------------------- SEARCH CREDENTIALS ----------------------------- #


def seach_credentials():
    searched_df = pd.read_csv("password_manager.csv")
    username_entry.delete(0, tkinter.END)
    username_entry.insert(0, string=searched_df[searched_df.website == website_entry.get()].username.iloc[0])
    password_entry.delete(0, tkinter.END)
    password_entry.insert(0, string=searched_df[searched_df.website == website_entry.get()].password.iloc[0])


# ---------------------------- UI SETUP ------------------------------- #

window = tkinter.Tk()
window.title("Tkinter Password Manager")
window.configure(background="white")
window.config(padx=40, pady=40)

canvas = tkinter.Canvas(window, width=200, height=189, bg="white", highlightthickness=0)
canvas.grid(column=1, row=0)

padlock_img = tkinter.PhotoImage(file="logo.png")
canvas.create_image(100, 95, image=padlock_img)

website_label = tkinter.Label(text="Website:", bg="white")
website_label.grid(column=0, row=1)

website_entry = tkinter.Entry()
website_entry.grid(sticky="nswe", column=1, row=1)

search_button = tkinter.Button(text="Search", command=seach_credentials)
search_button.grid(sticky="nswe", column=2, row=1)

username_label = tkinter.Label(text="Username:", bg="white")
username_label.grid(column=0, row=2)

username_entry = tkinter.Entry()
username_entry.insert(0, string="max.mustermann@gmail.com")
username_entry.grid(sticky="nswe", column=1, row=2, columnspan=2)

password_label = tkinter.Label(text="Password:", bg="white")
password_label.grid(column=0, row=3)

password_entry = tkinter.Entry()
password_entry.grid(sticky="we", column=1, row=3)

generate_button = tkinter.Button(text="Generate Button", command=pass_gen)
generate_button.grid(sticky="nswe", column=2, row=3)

add_button = tkinter.Button(text="Add", command=save_credentials)
add_button.grid(sticky="nswe", column=1, row=4, columnspan=2)

window.mainloop()
