""" SMS Weather Alert Project """
import requests
import os
import smtplib

MY_EMAIL = "ryanzmudka@gmail.com"
PASS = os.environ.get("EMAIL_PASSWORD")
HOST = "smtp.gmail.com"

account_sid: str | None = os.environ.get("TWILIO_SID")
auth_token: str | None = os.environ.get("TWILIO_AUTH_TOKEN")
ow_api_key: str | None = os.environ.get("OWM_API_KEY")

parameters = {
    "lon": -85.668083,
    "lat": 42.963360,
    "appid": ow_api_key,
    "units": "imperial",
    "cnt": 3,
}

request = requests.get(
    url="http://api.openweathermap.org/data/2.5/forecast",
    params=parameters
)
request.raise_for_status()
weather_data = request.json()
# print(weather_data)

# Check if rain in the next 12 hours, id of <700 means rain/precipitation
forecast_data_list = weather_data["list"]

will_rain = False
rain_alert_condition: str

for weather_forecast in forecast_data_list:
    upcoming_weather_code = weather_forecast["weather"][0]["id"]
    upcoming_weather_description = weather_forecast["weather"][0]["description"]
    print(upcoming_weather_description)

    if int(upcoming_weather_code) < 700:
        will_rain = True
        rain_alert_condition = upcoming_weather_description

if will_rain:
    connection = smtplib.SMTP(host=HOST)
    connection.starttls()
    connection.login(MY_EMAIL, PASS)
    connection.sendmail(
        from_addr=MY_EMAIL,
        to_addrs=MY_EMAIL,
        msg="Subject: Weather Update\n\n Rain is coming today! Bring an umbrella!"
    )
