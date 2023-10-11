import requests
import datetime
import smtplib

my_email = "8888888889asdf@gmail.com"
password = "glwm iacp kcnz isio"

sheety_header = {
    "Authorization": "Bearer 7ajD]OV9s[?^:J==^QEpRMk4^P2b0j.cQhP3P6SKK{EI_NE69p"
}
tequila_api_key = {
    "apikey": "sUnxAtejkO7I-FJE__BaXmETQN7RI5GW"
}
today_date = datetime.date.today().strftime('%d/%m/%Y')
today_180 = (datetime.date.today() + datetime.timedelta(days=180)).strftime('%d/%m/%Y')

sheety_response_get = requests.get("https://api.sheety.co/05ef102e7c623678e6a4442243e7f7ef/flightDeals/prices",
                                   headers=sheety_header)

email_content = ""
number_of_dealz = 0

# ----populate the Google Sheet with IATA codes for each city---- #

for x in sheety_response_get.json()["prices"]:
    if len(x["iataCode"]) == 0:
        tequila_location_params = {
            "term": x["city"],
        }
        tequila_location_response = requests.get("https://api.tequila.kiwi.com/locations/query",
                                                 headers=tequila_api_key, params=tequila_location_params)
        tequila_location_response.raise_for_status()

        city_iata_payload = {
            "price": {
                "iataCode": tequila_location_response.json()["locations"][0]["code"]
            }
        }

        sheety_response_put = requests.put(
            f"https://api.sheety.co/05ef102e7c623678e6a4442243e7f7ef/flightDeals/prices/{x['id']}",
            headers=sheety_header, json=city_iata_payload)

# ----search for flights---- #

for x in sheety_response_get.json()["prices"]:

    tequila_search_params = {
        "fly_from": "WRO",
        "fly_to": x["iataCode"],
        "date_from": today_date,
        "date_to": today_180,
        "price_to": x["lowestPrice"]
    }

    tequila_search_response = requests.get("https://api.tequila.kiwi.com/v2/search", headers=tequila_api_key,
                                           params=tequila_search_params)

    for y in tequila_search_response.json()["data"]:
        for z in sheety_response_get.json()["prices"]:
            if y["conversion"][list(y["conversion"])[0]] <= z["lowestPrice"]:
                email_content += f'From: {y["flyFrom"]}, {y["countryFrom"]["name"]}\nTo: {y["cityTo"]}, {y["countryTo"]["name"]}\nDeparture: {y["local_departure"].split("T")[0]}, {y["local_departure"].split("T")[1].split(".")[0]}\nArrival: {y["local_arrival"].split("T")[0]}, {y["local_arrival"].split("T")[1].split(".")[0]}\nPrice: {list(y["conversion"])[0]} {y["conversion"][list(y["conversion"])[0]]}\nLink: {y["deep_link"]}\n\n'
                number_of_dealz += 1

# ----send email---- #

connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(user=my_email, password=password)
connection.sendmail(from_addr=my_email, to_addrs="paulus.germanus@gmail.com",
                    msg=f"Subject: {number_of_dealz} Flight Deals Found\n\n{email_content}")
connection.close()
