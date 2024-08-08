import smtplib
import datetime as dt
from random import choice, randint

# Set email and password
my_email = "ryanzmudka@gmail.com"
with open(file="./automated_bday_emails/.env", mode="r") as env_file:
    password = env_file.read()

# Send email on a monday
monday = 0 # value for monday in datetime

current_datetime = dt.datetime.now()
current_day = current_datetime.weekday()

if current_day == monday:
    print(current_day)
    print("It is Monday!")

    # Pick random quote from file
    with open(file="./automated_bday_emails/data/quotes.txt") as quotes:
        # Read quotes and pick a random one
        quotes = quotes.readlines()
        todays_quote = choice(quotes)
        print(todays_quote)

    with smtplib.SMTP(host="smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="lonewolf111113456@gmail.com",
            msg=f"Subject:Monday Motivational\n\n{todays_quote}"
        )