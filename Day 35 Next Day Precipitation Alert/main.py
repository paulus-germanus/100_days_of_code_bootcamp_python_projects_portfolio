import requests
import tkinter
import datetime
import smtplib

MY_LAT = 51.16369624501019
MY_LNG = 17.10779428482056

my_email = "8888888889asdf@gmail.com"
password = "glwm iacp kcnz isio"


def send_email():
    connection = smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email, to_addrs=email_input.get(),
                        msg=f"Subject:There is probability for precipitation tomorrow.\n\nPrecipitation tomorrow at:\n{precipitation_time_mm}")
    connection.close()


def check_and_display_weather():
    global precipitation_time_mm
    MY_LAT = float(lat_input.get())
    MY_LNG = float(lng_input.get())

    # since Open Weather's free APIs weren't available anymore I went with Open Meteo's API

    open_meteo_parameters = {
        "latitude": MY_LAT,
        "longitude": MY_LNG,
        "hourly": "precipitation",
        "timezone": "auto",
        "start_date": datetime.date.today() + datetime.timedelta(days=1),
        "end_date": datetime.date.today() + datetime.timedelta(days=1)
    }

    open_meteo_response = requests.get("https://api.open-meteo.com/v1/forecast", params=open_meteo_parameters)
    open_meteo_response.raise_for_status()
    hourly_precipitation = open_meteo_response.json()["hourly"]["precipitation"]
    precipitation_time_mm = ', '.join(str(x) for x in
                                      [(f"h/{x}:00", f"{hourly_precipitation[x]}mm") for x in range(24) if
                                       hourly_precipitation[x] > 0])

    o_m_logo_canvas.delete("all")
    o_m_logo_canvas.create_text(191, 75, text=f"Precipitation tomorrow at:\n{precipitation_time_mm}", width=360,
                                font=("helvetica", 9, "bold"))
    check_weather_button.destroy()
    send_text_button = tkinter.Button(text="Send email", bg="white", command=send_email)
    send_text_button.grid(column=0, row=6, columnspan=2, pady=10)


# __________GUI setup__________#

window = tkinter.Tk()
window.title("Rain Alert")
window.configure(background="white")
window.config(padx=25, pady=10)

o_m_logo_canvas = tkinter.Canvas(window, width=382, height=150, bg="white", highlightthickness=0)
o_m_logo_canvas.grid(column=0, row=0, columnspan=2)

o_m_logo = tkinter.PhotoImage(file="open_meteo_logo.png")
o_m_logo_canvas.create_image(191, 75, image=o_m_logo)

lat_lng = tkinter.Label(
    text="Specify the latitude and longitude to be checked for precipitation.", bg="white")
lat_lng.grid(column=0, row=1, columnspan=2, pady=10)

lat_label = tkinter.Label(text="Your latitude:", bg="white")
lat_label.grid(column=0, row=2, pady=5)

lat_input = tkinter.Entry()
lat_input.insert(0, string=51.16369624501019)
lat_input.grid(sticky="nswe", column=1, row=2, pady=5)

lng_label = tkinter.Label(text="Your longitude:", bg="white")
lng_label.grid(column=0, row=3, pady=5)

lng_input = tkinter.Entry()
lng_input.insert(0, string=17.10779428482056)
lng_input.grid(sticky="nswe", column=1, row=3, pady=5)

lat_lng = tkinter.Label(
    text="Specify the email address to send the forecast to.", bg="white")
lat_lng.grid(column=0, row=4, columnspan=2, pady=10)

phone_number_label = tkinter.Label(text="Your email address:", bg="white")
phone_number_label.grid(column=0, row=5, pady=5)

email_input = tkinter.Entry()
email_input.insert(0, string="max.mustermann@gmail.com")
email_input.grid(sticky="nswe", column=1, row=5, pady=5)

check_weather_button = tkinter.Button(text="Check weather for the given lat and lng", bg="white", command=check_and_display_weather)
check_weather_button.grid(column=0, row=6, columnspan=2, pady=10)

window.mainloop()
