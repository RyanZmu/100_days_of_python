"""
Movie Rankings:

- Use Empire's Top 100 Movies of All Time list
- Scape the list and place it into a text file
 - Number and Title listed
"""
import requests
from bs4 import BeautifulSoup

response = requests.get(url="https://www.empireonline.com/movies/features/best-movies-2/")

soup = BeautifulSoup(response.text, "html.parser")
print(soup.prettify())

get_titles = soup.findAll(name="h3")
titles_list = [title.string for title in get_titles]


# Create text file
with open(file="./movie_ranking_beautiful_soup/movies.txt", mode="w") as movie_file:
    # [::-1] will reverse a list
    for title in titles_list[::-1]:
        movie_file.write(f"{title}\n")

