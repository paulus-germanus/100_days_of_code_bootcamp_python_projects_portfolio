from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")

soup = BeautifulSoup(response.text, "html.parser")

point_list = [int(x.getText().split(" ")[0]) for x in soup.find_all(class_="score")]
highest_point_index = point_list.index(max(point_list))

print("The article with the biggest number of upvotes on https://news.ycombinator.com/ currently is:")
print(f'Title: {soup.find_all(class_="titleline")[highest_point_index].getText()}')
print(f'Link: {soup.find_all(class_="titleline")[highest_point_index].a.get("href")}')
print(f'{max(point_list)} points')
