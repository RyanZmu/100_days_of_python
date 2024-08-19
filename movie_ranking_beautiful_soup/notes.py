from bs4 import BeautifulSoup

with open(file="./movie_ranking_beautiful_soup/website.html") as website:
    contents = website.read()

soup = BeautifulSoup(contents, features="html.parser")

print(soup.prettify())
# print(soup.title)
# print(soup.title.name)
# print(soup.title.string)

all_anchors = soup.findAll(name="a")

for tag in all_anchors:
    print(tag.getText())



