import requests
from datetime import datetime
import tkinter
import smtplib

my_email = "8888888889asdf@gmail.com"
password = "glwm iacp kcnz isio"

iss_response = requests.get(url="http://api.open-notify.org/iss-now.json")
iss_response.raise_for_status()
json_data = iss_response.json()
iss_latitude = float(json_data["iss_position"]["latitude"])
iss_longitude = float(json_data["iss_position"]["longitude"])

# __________function checking every 60 seconds if it is night yet and if ISS is overhead__________#


def is_iss_overhead_tonight():
    monitor_iss.config(text="MONITORING")

    MY_LAT = float(lat_input.get())
    MY_LNG = float(lng_input.get())

    parameters = {
        "lat": MY_LAT,
        "lng": MY_LNG,
        "formatted": 0
    }

    # ______adjust the time zone from UTC to CET or CEST______#
    if datetime.today().month > 3 and datetime.today().month < 10:
        offset = 2
    else:
        offset = 1

    sun_response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
    sun_response.raise_for_status()
    sunset_hour = int(sun_response.json()["results"]["sunset"].split("T")[1].split("+")[0].split(":")[0]) + offset
    sunrise_hour = int(sun_response.json()["results"]["sunrise"].split("T")[1].split("+")[0].split(":")[0]) + offset
    current_hour = datetime.now().time().hour

    if (current_hour >= sunset_hour or current_hour <= sunrise_hour) and MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LNG-5 <= iss_longitude <= MY_LNG+5:
        app_title_label.config(text="Look up! The ISS is flying above you right now!", font=("bold"))
        window.lift()
        window.attributes('-topmost', True)
        window.after_idle(window.attributes, '-topmost', False)
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs=email_input.get(), msg=f"Subject:ISS Overhead Monitor: Look up! :)\n\nLook up! The ISS is flying above you right now!\n\nYour latitude: {MY_LAT}\nYour longitude: {MY_LNG}\nISS latitude: {iss_latitude}\nISS longitude: {iss_longitude}")
        connection.close()
        window.after_cancel(is_iss_overhead_tonight)
    window.after(60000, is_iss_overhead_tonight)



# __________GUI setup__________#

window = tkinter.Tk()
window.title("ISS Overhead Monitor")
window.configure(padx=25, pady=10)

app_title_label = tkinter.Label(
    text="This app monitors if ISS is visible on the night sky above you.\nIf so, this window will come to the front and inform you about it.\nPlus: it will send you an email notification to the email specified below.")
app_title_label.grid(column=0, row=0, columnspan=2, pady=10)

lat_label = tkinter.Label(text="Your latitude:")
lat_label.grid(column=0, row=1, pady=5)

lat_input = tkinter.Entry()
lat_input.insert(0, string=51.110550)
lat_input.grid(sticky="nswe", column=1, row=1, pady=5)

lng_label = tkinter.Label(text="Your longitude:")
lng_label.grid(column=0, row=2, pady=5)

lng_input = tkinter.Entry()
lng_input.insert(0, string=17.025560)
lng_input.grid(sticky="nswe", column=1, row=2, pady=5)

email_label = tkinter.Label(text="Your email:")
email_label.grid(column=0, row=3, pady=5)

email_input = tkinter.Entry()
email_input.insert(0, string="max.mustermann@gmail.com")
email_input.grid(sticky="nswe", column=1, row=3, pady=5)

monitor_iss = tkinter.Button(text="Start monitoring", command=is_iss_overhead_tonight)
monitor_iss.grid(column=0, row=4, columnspan=2, pady=10)

window.mainloop()
