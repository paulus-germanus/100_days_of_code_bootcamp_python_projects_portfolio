import requests
import datetime
import tkinter
import webbrowser

PIXELA_ENDPOINT = "https://pixe.la//v1/users"
PIXELA_USERNAME = "jonirenicus"
PIXELA_TOKEN = "DryONDP201w20cuA9dD5}JohAxXH@1<?7cjZ=5H2m9hx5%n"
PIXELA_GRAPH_ID = "graph01"
TODAY_DATE = datetime.date.today().strftime('%Y%m%d')

pixela_header = {
    "X-USER-TOKEN": PIXELA_TOKEN
}


def post_to_pixela():
    pixel_parameters = {
        "date": TODAY_DATE,
        "quantity": str(var.get()),
    }
    post_graph_pixela = requests.put(url=f"{PIXELA_ENDPOINT}/{PIXELA_USERNAME}/graphs/{PIXELA_GRAPH_ID}/{TODAY_DATE}", json=pixel_parameters, headers=pixela_header)
    print(post_graph_pixela.text)


def delete_pixel():
    pixel_parameters = {
        "date": TODAY_DATE,
    }
    delete_pixela_pixel = requests.delete(url=f"{PIXELA_ENDPOINT}/{PIXELA_USERNAME}/graphs/{PIXELA_GRAPH_ID}/{TODAY_DATE}", json=pixel_parameters, headers=pixela_header)
    print(delete_pixela_pixel.text)


window = tkinter.Tk()
window.title("Pixela Coding Daily Habit Tracker")
window.configure(background="white")
window.config(padx=25, pady=10)

pixela_logo = tkinter.Canvas(window, width=88, height=88, bg="white", highlightthickness=0)
pixela_logo.grid(column=0, row=0, pady=10)

pixela_logo_img = tkinter.PhotoImage(file="pixela_logo.png")
pixela_logo.create_image(44, 44, image=pixela_logo_img)

var = tkinter.IntVar()
coded_checkbox = tkinter.Checkbutton(window, text="Coded today!",variable=var, onvalue=1, offvalue=0, bg="white")
coded_checkbox.grid(column=0, row=1)

post_button = tkinter.Button(text="Post to Pixela", command=post_to_pixela, bg="white")
post_button.grid(sticky="nswe", column=0, row=2)

delete_pixel_button = tkinter.Button(text="Delete today's pixel", command=delete_pixel, bg="white")
delete_pixel_button.grid(sticky="nswe", column=0, row=3)

open_graph_in_browser_button = tkinter.Button(text="Open graph in browser", command=lambda: webbrowser.open("https://pixe.la/v1/users/jonirenicus/graphs/graph01.html"), bg="white")
open_graph_in_browser_button.grid(column=0, row=4)

window.mainloop()