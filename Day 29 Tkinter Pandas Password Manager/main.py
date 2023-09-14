import tkinter
from tkinter import messagebox
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

    website_list = pd.read_csv("password_manager.csv").website.to_list()

    if len(website_entry.get()) == 0 or len(username_entry.get()) == 0 or len(password_entry.get()) == 0:
        messagebox.showinfo(title="Hmm...",
                            message="Please populate all the entry fields to proceed.")
    elif website_entry.get() in website_list:
        add_another_creds = messagebox.askokcancel(title="Ups, duplicate!",
                                                   message=f"The credentials for {website_entry.get()} already exist in the database. Would you like to overwrite the credentials for {website_entry.get()}?")
        if add_another_creds:
            load_existing_data = pd.read_csv("password_manager.csv")
            existing_data_dict = load_existing_data.to_dict()
            # key_list = list(existing_data_dict["website"].keys())
            value_list = list(existing_data_dict["website"].values())
            position = value_list.index(website_entry.get())
            existing_data_dict["username"][position] = username_entry.get()
            existing_data_dict["password"][position] = password_entry.get()
            updated_credentials_df = pd.DataFrame(existing_data_dict)
            updated_credentials_df.to_csv("password_manager.csv", index=False)
            website_entry.delete(0, tkinter.END)
            username_entry.delete(0, tkinter.END)
            password_entry.delete(0, tkinter.END)
            messagebox.showinfo(title="Great success!",
                                message=f"You have successfully updated the credentials for {website_entry.get()} in the database.")
    else:
        add_credentials = messagebox.askokcancel(title="U sure?",
                                                 message=f"Are you sure you want to add the following details to the database?\nWebsite: {website_entry.get()}\nUsername: {username_entry.get()}\nPassword: {password_entry.get()}")
        if add_credentials:
            credentials_df = pd.DataFrame(credentials_dict)
            credentials_df.to_csv("password_manager.csv", mode="a", header=False, index=False)
            website_entry.delete(0, tkinter.END)
            username_entry.delete(0, tkinter.END)
            password_entry.delete(0, tkinter.END)
            messagebox.showinfo(title="Great success!",
                                message="You have successfully added the entered credentials to the database.")


# -------------------------- SEARCH CREDENTIALS ----------------------------- #


def seach_credentials():
    try:
        searched_df = pd.read_csv("password_manager.csv")
        username_entry.delete(0, tkinter.END)
        username_entry.insert(0, string=searched_df[searched_df.website == website_entry.get()].username.iloc[0])
        password_entry.delete(0, tkinter.END)
        password_entry.insert(0, string=searched_df[searched_df.website == website_entry.get()].password.iloc[0])
    except IndexError:
        messagebox.showinfo(title="Great failure!",
                            message="The website you are looking for seems not to be saved in the database.")


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
