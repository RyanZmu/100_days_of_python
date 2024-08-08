# import smtplib

# my_email = "ryanzmudka@gmail.com"

# with open(file="./automated_bday_emails/.env", mode="r") as env_file:
#     password = env_file.read()

# with smtplib.SMTP(host="smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs="lonewolf111113456@gmail.com",
#         msg="HELLO FROM PYTHON"
#     )

import datetime as dt

now = dt.datetime.now()
year = now.year
if year == 2024:
    print("It's 2024!")
month = now.month
day_of_week = now.weekday() #counts from 0 = Monday
print(day_of_week)

# Set a birthday
date_of_birth = dt.datetime(year=1994, month=2, day=17)
print(date_of_birth)

