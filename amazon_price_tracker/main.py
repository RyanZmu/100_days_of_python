"""
Amazon Price Tracker

- Check amazon to find prices for a product on Amazon
- Send an email alert when product's price drops to or below our desired price with the URl
- Set a time to check every day for a deal
- Use web scraping to find price
"""
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import os
import smtplib
import requests

# Load environment vars
load_dotenv()
EMAIL = os.environ.get("EMAIL")
HOST = os.environ.get("HOST")
TOKEN = os.environ.get("TOKEN")

PRICE_POINT = 5.00
PRODUCT_URL = ("https://www.amazon.com/HARTZ-Just-Cats-Variety-Pack/dp/B00KFOH8PQ?_encoding=UTF8&fpw=new&fpl=fresh&ref_"
               "=eemb_p_d_2975241011_ai_2975303011_7_6_i&pd_rd_w=8Qo0U&content-id=amzn1.sym.dc5af51f-3de0-461a-83cd"
               "-87d91e3fbd18&pf_rd_p=dc5af51f-3de0-461a-83cd-87d91e3fbd18&pf_rd_r=QADNB4QNNCYBD69HBXFS&pd_rd_wg=froDt"
               "&pd_rd_r=1dcd9ed5-f1e1-4d84-b241-53031b221e0c&pd_rd_i=B00KFOH8PQ")


product = requests.get(url=PRODUCT_URL).text

soup = BeautifulSoup(product, "html.parser")
print(soup.prettify())

product_name = soup.find(name="span", class_="a-size-large").getText().strip()
current_price_dollars = soup.find(name="span", class_="a-price-whole").getText()
current_price_cents = soup.find(name="span", class_="a-price-fraction").getText()

current_price = f"{current_price_dollars}{current_price_cents}"
print(product_name)
print(current_price)

if float(current_price) < PRICE_POINT:
    connection = smtplib.SMTP(host=HOST)
    connection.starttls()
    connection.login(EMAIL, TOKEN)
    connection.sendmail(
        from_addr=EMAIL,
        to_addrs=EMAIL,
        msg=f"Subject:{product_name} Price Drop!\n\nThe price of {product_name} is now ${current_price} - Buy Now!"
            f"\n {PRODUCT_URL}"
    )
