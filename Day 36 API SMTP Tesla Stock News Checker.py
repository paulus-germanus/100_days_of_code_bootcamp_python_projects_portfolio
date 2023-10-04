import requests
import html
import smtplib

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

alpha_vantage_api_key = "WLUZCSL3FR5PTDFN"
news_api_key = "dec7dfc2a15f4fd0a6e06c8a7dfd6d77"

my_email = "8888888889asdf@gmail.com"
password = "glwm iacp kcnz isio"
recipient_email = input("Please enter your email address: ")

alpha_vantage_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": alpha_vantage_api_key,
    "outputsize": "compact",
    "datatype": "json",
}

alpha_vantage_response = requests.get(url="https://www.alphavantage.co/query", params=alpha_vantage_params)
alpha_vantage_response.raise_for_status()
a_v_daily_close_yesterday = float(alpha_vantage_response.json()["Time Series (Daily)"][
                                      list(alpha_vantage_response.json()["Time Series (Daily)"].keys())[0]]["4. close"])
a_v_daily_close_day_before_yesterday = float(alpha_vantage_response.json()["Time Series (Daily)"][
                                                 list(alpha_vantage_response.json()["Time Series (Daily)"].keys())[1]][
                                                 "4. close"])

news_api_params = {
    "q": COMPANY_NAME,
    "from": list(alpha_vantage_response.json()["Time Series (Daily)"].keys())[0],
    "language": "en",
    "apiKey": news_api_key,
}

news_api_response = requests.get(url="https://newsapi.org/v2/everything", params=news_api_params)
news_api_response.raise_for_status()
tsla_news = f'Brief: {html.unescape(news_api_response.json()["articles"][0]["description"])}\nLink: {news_api_response.json()["articles"][0]["url"]};\n\nBrief: {html.unescape(news_api_response.json()["articles"][1]["description"])}\nLink: {news_api_response.json()["articles"][1]["url"]}\n\nBrief: {html.unescape(news_api_response.json()["articles"][2]["description"])}\nLink: {news_api_response.json()["articles"][2]["url"]}'

if a_v_daily_close_yesterday <= a_v_daily_close_day_before_yesterday * 0.99:
    difference = round((a_v_daily_close_yesterday - a_v_daily_close_day_before_yesterday) / a_v_daily_close_yesterday * 100)
    connection = smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email, to_addrs=recipient_email,
                        msg=f"Subject:TSLA: DOWN {difference}%\n\n{tsla_news}")
    connection.close()
elif a_v_daily_close_yesterday >= a_v_daily_close_day_before_yesterday * 1.01:
    difference = round((a_v_daily_close_yesterday - a_v_daily_close_day_before_yesterday) / a_v_daily_close_yesterday * 100)
    connection = smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email, to_addrs=recipient_email,
                        msg=f"Subject:TSLA: UP {difference}%\n\n{tsla_news}")
    connection.close()
