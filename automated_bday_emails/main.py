# Automated Birthday Emails
# Gmail: smtp.gmail.com
# CSV to hold name,email,year,month,day
# 3 letter.txt files to randomly choose from to send
# When program finds that the day matches today's date, insert name into letter and send the person an email saying happy bday
import smtplib
import datetime as dt
import pandas
from random import choice

# Read the birthdays file
birthday_file = pandas.read_csv(filepath_or_buffer="./automated_bday_emails/data/birthdays.csv")
print(birthday_file)

# Turn into dict
birthday_dict = birthday_file.to_dict(orient="records")
print(birthday_dict)

# Check for month and day
current_date = dt.datetime.now()
today_tuple = (current_date.month, current_date.day)
current_month = current_date.month
current_day = current_date.day
print({"month": current_month}, {"day": current_day})

for person in birthday_dict:
    if person["month"] == current_month and person["day"] == current_day:
        print(f"Today is {person["name"]}'s Birthday!")

        # Pick a random letter to send
        letters_array = ["./automated_bday_emails/data/letter_1.txt", "./automated_bday_emails/data/letter_2.txt", "./automated_bday_emails/data/letter_3.txt"]
        random_letter = choice(letters_array)

        # Read contents of template
        with open(file=random_letter, mode="r") as letter:
            original_letter = letter.read()
            letter_to_send = original_letter.replace("[NAME]", person["name"])
            print(letter_to_send)

        # Set up email vars
        my_email = "ryanzmudka@gmail.com"
        host = "smtp.gmail.com"
        with open(file="./automated_bday_emails/.env", mode="r") as env_file:
            password = env_file.read()

        # Send birthday email
        with smtplib.SMTP(host=host) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=person["email"],
                msg=f"Subject:Happy Birthday!\n\n{letter_to_send}"
            )
