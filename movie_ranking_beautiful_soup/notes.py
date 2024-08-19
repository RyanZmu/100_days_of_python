from bs4 import BeautifulSoup
import requests

response = requests.get(url="https://news.ycombinator.com/news")
# print(response.text

# Get titles and links for each article
soup = BeautifulSoup(response.text, features="html.parser")
# print(soup.prettify())

article_tag = soup.select(selector=".titleline a")
article_text = [article.getText() for article in article_tag]
article_links = [article.get("href") for article in article_tag]

# Output all articles and links
# print(article_text)
# print(article_links)

# Output all up votes - runs getText on each item
article_upvote = [int(score.getText().split()[0]) for score in soup.findAll(name="span", class_="score")]
# print(article_upvote)

# Find highest upvoted article
highest_value: int = max(article_upvote)
highest_value_index: int = article_upvote.index(highest_value)

highest_upvoted_article = article_text[highest_value_index]
highest_upvoted_link = article_links[highest_value_index]

print(highest_upvoted_article)
print(highest_upvoted_link)


# Messing with Beautiful Soup locally
# with open(file="./movie_ranking_beautiful_soup/website.html") as website:
#     contents = website.read()
#
#
# # Print different tags and output nicely
# print(soup.prettify())
# # print(soup.title)
# # print(soup.title.name)
# # print(soup.title.string)
#
# # Get all Anchor links
# all_anchors = soup.findAll(name="a")
# for tag in all_anchors:
#     print(tag.get("href"))
#
# # Get specific heading with id=random
# heading = soup.find(name="h1", id="random")
# print(heading)
#
# # When looking for class attribute, add an _
# paragraph = soup.find(name="p", class_="random")
# print(paragraph)
# print(paragraph.get("class"))
#
# # Getting nested elements
# # Can use CSS selectors to get elements with soup
# company_url = soup.select_one(selector="p em a")
# print(company_url)
#
# all_headings = soup.select(".random")
# print(all_headings)
