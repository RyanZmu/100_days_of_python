"""
Stock Alert Project Outline
- Use an API to get stock prices on followed stocks - show percentage change from yesterday to current day
- Look for a big change such as a 5-10% increase in a followed stock
- Relay any breaking news related to that stock, and it's change
- Use SMS alerts to inform user that a stock they follow has gone up in value
- (Stretch) Have the app alert when a stock drops drastically, and send news as well
"""
import datetime as dt
from datetime import timedelta
import os
import requests
from twilio.rest import Client

TWILIO_AUTH_TOKEN = os.environ.get("TWILIO_AUTH_TOKEN")
TWILIO_SID = os.environ.get("TWILIO_SID")
STOCK_API_KEY = os.environ.get("STOCK_API_KEY")
NEWS_API_KEY = os.environ.get("NEWS_API_KEY")
STOCK_SYMBOL = "AAPL"
COMPANY = "Apple"

def get_stock_difference():
    yesterdays_date = str(dt.datetime.today() - timedelta(days=1))[0:10]
    prior_days_date = str(dt.datetime.today() - timedelta(days=2))[0:10]
    print(yesterdays_date)
    print(prior_days_date)

    stock_parameters = {
        "apikey": STOCK_API_KEY,
    }

    yesterdays_stock_request = requests.get(
        url=f"https://api.polygon.io/v1/open-close/{STOCK_SYMBOL}/{yesterdays_date}",
        params=stock_parameters)

    yesterdays_stock_data = yesterdays_stock_request.json()
    print(yesterdays_stock_data)

    prior_day_stock_request = requests.get(
        url=f"https://api.polygon.io/v1/open-close/{STOCK_SYMBOL}/{prior_days_date}",
        params=stock_parameters)

    prior_day_stock_data = prior_day_stock_request.json()
    print(prior_day_stock_data)

    yesterdays_closing_price = float(yesterdays_stock_data["close"])
    prior_day_closing_price = float(prior_day_stock_data["close"])
    print(yesterdays_closing_price)
    print(prior_day_closing_price)

    stock_difference = round(yesterdays_closing_price / prior_day_closing_price)
    print(stock_difference)

    if stock_difference > 0:
        print("Stock changed")
        send_sms_alert(stock_change=stock_difference)
    return stock_difference


def get_breaking_news():
    news_parameters = {
        "country": "us",
        "apikey": NEWS_API_KEY,
        "category": "business",
        "q": COMPANY
    }

    news_request = requests.get(
        url="https://newsapi.org/v2/top-headlines",
        params=news_parameters
    )

    news_data = news_request.json()
    print(news_data)

    return news_data


def send_sms_alert(stock_change):
    news_output: str
    message_to_send: str
    down_arrow = "🔽"
    up_arrow = "🔼"

    try:
        breaking_news: dict = get_breaking_news()["articles"][0]
        breaking_headline: str = breaking_news["title"]
        breaking_brief: str = breaking_news["content"]
        breaking_url: str = breaking_news["url"]
        breaking_date: str = breaking_news["publishedAt"]
    except IndexError:
        news_output = "Sorry, No news article found related to this stock change!"
    else:
        news_output = (f"Headline: {breaking_headline}\n "
                       f"Brief: {breaking_brief}\n "
                       f"Link: {breaking_url}"
                       f"Date: {breaking_date}")
    print(news_output)

    # Check if up or down arrow should be used for output
    if stock_change > 0:
        message_to_send = f"APPL: UP {up_arrow}{stock_change}%\n{news_output}"
    else:
        message_to_send = f"APPL: DOWN {down_arrow}{stock_change}%\n{news_output}"

    client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
    message = client.messages.create(
        from_="whatsapp:+14155238886",
        body=message_to_send,
        to="whatsapp:+16168265440"
    )
    print(message.sid)


# Start program
get_stock_difference()
