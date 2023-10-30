import requests
from bs4 import BeautifulSoup
import smtplib

my_email = "8888888889asdf@gmail.com"
password = "glwm iacp kcnz isio"
users_email = input("Plz enter your email to receive the price alert.\n")

tracked_website = "https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1"

header = {
    "User-Agent": "Chrome/118.0.0.0",
    "Accept-Language": "en-GB,en;q=0.9"
}

response = requests.get(tracked_website, headers=header)
soup = BeautifulSoup(response.text, parser="lxml", features="lxml")

item_name = soup.find(id="productTitle").getText().strip().encode('utf-8')
item_price = float(soup.find(class_="a-offscreen").getText().strip("$"))

if item_price <= 100:
    connection = smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email, to_addrs=users_email, msg=f"Subject:Amazon Price Tracker Alert!\n\nItem name:\n{item_name}\nItem price at the moment:\n${item_price}\nAmazon link:\n{tracked_website}")
    connection.close()
