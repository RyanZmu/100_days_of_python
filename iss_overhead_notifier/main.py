# ISS Overhead Notifier
# If the ISS is close to my current position AND it is nighttime
# Send an email to tell me to look up
# BONUS: Check every 60 seconds
import requests
from datetime import datetime
import smtplib
import time
from geopy.geocoders import Nominatim


MY_LAT =  42.963795
MY_LONG = -85.670006
HOST = "smtp.gmail.com"
MY_EMAIL = "ryanzmudka@gmail.com"

with open(file="./iss_overhead_notifier/.env") as password_file:
    PASSWORD = password_file.read()

#======== API Calls ========
def is_iss_over_head():
    global MY_LAT, MY_LONG
    # ISS API
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    # Raise exceptions for a non 200 status code
    response.raise_for_status()

    data = response.json()
    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    iss_position = (iss_latitude, iss_longitude)
    print({"iss_pos":iss_position})
    # Output where the ISS is currently
    geolocator = Nominatim(user_agent="iss_overhead_notifier")
    location = geolocator.reverse(query=iss_position, language="en")
    if location is not None:
        print(f"The ISS is currently over {location}")

    # Current POS can be +5 or -5 degrees of ISS position
    if MY_LONG - 5 <= iss_position[0] <= MY_LONG + 5 and MY_LAT - 5 <= iss_position[1] <= MY_LAT + 5 :
        return True
    else:
        return False

def is_night():
    global MY_LAT, MY_LONG
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "time_format": 24,
    }

    # Sunset/Sunrise API
    response = requests.get(url=f"https://api.sunrisesunset.io/json", params=parameters)
    response.raise_for_status()
    data = response.json()

    sunset = int(data["results"]["sunset"][0:2])

    time_now = datetime.now().hour
    print(time_now)

    if time_now >= sunset:
        return True
    else:
        return False

# Continiously Check every 60 seconds
while True:
    time.sleep(60)
    print(f"ISS Notifier is running at {datetime.now()}!")
    if is_iss_over_head() and is_night():
        print("Hey the ISS is overhead and it's nighttime! - Sending Email")
        connection = smtplib.SMTP(host=HOST)
        connection.starttls()
        connection.login(MY_EMAIL, PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"Subject:ISS Notifier\n\nThe ISS is overhead your current location - go look!!"
        )
    else:
        print("The ISS is either not overhead or it is not nighttime :(")


