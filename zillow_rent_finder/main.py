"""
Zillow Price Finder

- Use Zillow clone website to practice scraping with Beautiful Soup and entering data into a form with Selenium
- Open Zillow and find the rent for San Fran that is <$3000 a month - Scrape with Beautiful Soup
- Create a Google Sheet and Form for this project
- Use Selenium to fill out the Google Form with the date for each listing
- Form should populate the Sheet with entered data
- Open Zillow Clone website, live website has many bot checks :(

"""
import selenium.common.exceptions
from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
from bs4 import BeautifulSoup

# Constants
ZILLOW_URL = "https://appbrewery.github.io/Zillow-Clone/"
FORM_URL = "https://forms.gle/WR9UTvvj926Euy1R9"

# Scrape with beautiful soup and grab all listings
zillow_response = requests.get(url=ZILLOW_URL)
zillow_data = zillow_response.text
soup = BeautifulSoup(zillow_data, "html.parser")

# Find address, price and link for each listing
addresses = [address.getText().replace("\n", "").replace("|", "").strip() for address in soup.findAll(name="address")]
prices = [price.getText().replace("/mo", "").replace("+", "").replace(" 1bd", "").replace("1 bd", "")
          for price in soup.findAll("span", class_="PropertyCardWrapper__StyledPriceLine")]
links = [link["href"] for link in soup.findAll("a", class_="property-card-link")]

# Open Google form
driver = webdriver.Firefox()
driver.get(FORM_URL)


def submit_data(listing_data):
    # Find form fields
    fields = driver.find_elements(By.CLASS_NAME, value="whsOnd.zHQkBf")
    address_field = fields[0]
    price_field = fields[1]
    link_field = fields[2]

    # Input data - list indexes match
    listing_index = addresses.index(listing_data)

    address_field.send_keys(listing_data)
    price_field.send_keys(prices[listing_index])
    link_field.send_keys(links[listing_index])

    submit_button = driver.find_element(By.CLASS_NAME, value="NPEfkd.RveJvd.snByac")
    submit_button.click()
    print(f"Data entered for {listing_data}")


for listing in addresses:
    try:
        submit_data(listing_data=listing)
    except selenium.common.exceptions.ElementNotInteractableException:  # Prevents invalid elements
        print("Element skipped")
    else:
        # If data entry successful, resubmit and enter next set of data
        resubmit_button = driver.find_element(By.TAG_NAME, "a")
        resubmit_button.click()
