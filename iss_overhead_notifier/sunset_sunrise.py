import requests
from datetime import datetime

parameters = {
    "lat": 42.965462,
    "lng": -85.670174,
}


response = requests.get(url=f"https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
# print(data)

sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]

print(f"Today's sunrise is at {sunrise} and sunset is at {sunset}")

time_now = datetime.now()
# print(time_now)
