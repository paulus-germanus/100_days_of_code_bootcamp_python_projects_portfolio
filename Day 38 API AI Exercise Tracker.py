import requests
import datetime
import tkinter
import webbrowser

nutritionix_api_id = "56ed2258"
nutritionix_api_key = "de5b423f4c66166f8babb16e4d4a0def"

nutri_header = {
    "x-app-id": nutritionix_api_id,
    "x-app-key": nutritionix_api_key,
}

sheety_header = {
    "Authorization": "Bearer G/d]OILJY;KC6ufOpmWzV}j>UH=u5U4?LoADi;>>[Q*5H5"
}


def analise_data_with_nutritionix_and_post_activity_with_sheety():
    nutri_params = {
        "query": query_entry.get(),
        "gender": gender_var.get(),
        "weight_kg": float(weight_entry.get()),
        "height_cm": float(height_entry.get()),
        "age": int(age_entry.get()),
    }

    nutri_response = requests.post(url="https://trackapi.nutritionix.com/v2/natural/exercise", headers=nutri_header,
                                   json=nutri_params)
    date = datetime.date.today().strftime('%d.%m.%Y')
    time = datetime.datetime.now().strftime("%H:%M:%S")
    for x in nutri_response.json()["exercises"]:
        exercise = x["name"]
        duration = x["duration_min"]
        calories = x["nf_calories"]

        sheety_json_payload = {
            "workout": {
                "date": date,
                "time": time,
                "exercise": exercise,
                "duration": duration,
                "calories": calories,
            }
        }

        sheety_response = requests.post(
            url="https://api.sheety.co/05ef102e7c623678e6a4442243e7f7ef/myWorkouts/workouts",
            headers=sheety_header, json=sheety_json_payload)
        print(sheety_response.text)


window = tkinter.Tk()
window.title("API AI Exercise Tracker")
window.configure(bg="white")
window.config(padx=20, pady=10)

gender_label = tkinter.Label(text="Gender:", bg="white")
gender_label.grid(column=0, row=0, pady=5)

gender_var = tkinter.StringVar(window)
gender_var.set("male")

gender_menu = tkinter.OptionMenu(window, gender_var, "male", "female")
gender_menu.config(bg="white", highlightthickness=0)
gender_menu["menu"].config(bg="white")
gender_menu.grid(sticky="nswe", column=1, row=0, pady=5)

age_label = tkinter.Label(text="Age:", bg="white")
age_label.grid(column=2, row=0, pady=5)

age_entry = tkinter.Entry()
age_entry.insert(0, string=35)
age_entry.grid(sticky="nswe", column=3, row=0, pady=5)

height_label = tkinter.Label(text="Height (in cm):", bg="white")
height_label.grid(column=0, row=1, pady=5)

height_entry = tkinter.Entry()
height_entry.insert(0, string=172)
height_entry.grid(sticky="nswe", column=1, row=1, pady=5)

weight_label = tkinter.Label(text="Weight (in kg):", bg="white")
weight_label.grid(column=2, row=1, pady=5)

weight_entry = tkinter.Entry()
weight_entry.insert(0, string=76)
weight_entry.grid(sticky="nswe", column=3, row=1, pady=5)

query_label = tkinter.Label(text="Describe your activity:", bg="white")
query_label.grid(column=0, row=2, pady=5)

query_entry = tkinter.Entry()
query_entry.insert(0, string="e.g. I cycled 1h and ran 10km")
query_entry.grid(sticky="nswe", column=1, row=2, columnspan=3, pady=5)

button_upload_activity = tkinter.Button(text="Upload Activity", bg="white",
                                        command=analise_data_with_nutritionix_and_post_activity_with_sheety)
button_upload_activity.grid(sticky="nswe", column=1, row=3, columnspan=2)

button_open_log_in_browser = tkinter.Button(text="Open Log in Browser", bg="white", command=lambda: webbrowser.open(
    "https://docs.google.com/spreadsheets/d/1P4XoN_ud_aIfFnJdrUTQlgaFfOgm9v3_EBwfRtxZiDU"))
button_open_log_in_browser.grid(sticky="nswe", column=1, row=4, columnspan=2)

window.mainloop()
