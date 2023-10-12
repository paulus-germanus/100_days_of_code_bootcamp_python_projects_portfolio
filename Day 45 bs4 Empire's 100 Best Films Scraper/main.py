from bs4 import BeautifulSoup
import requests

response = requests.get("https://www.empireonline.com/movies/features/best-movies-2/")

soup = BeautifulSoup(response.text, "html.parser")

empire_films = [x.getText() for x in soup.find_all(name="h3", class_="listicleItem_listicle-item__title__hW_Kn")][::-1]

with open("100_best_films.txt", mode="a") as file:
    for x in empire_films:
        file.write(f"{x}\n")