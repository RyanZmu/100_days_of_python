import smtplib
import os

HOST = "smtp.gmail.com"
MY_EMAIL = "ryanzmudka@gmail.com"
PASS = os.environ.get("EMAIL_PASSWORD")

class NotificationManager:
    def __init__(self, data):
        self.cheap_flight = data

    def send_email_alert(self):
        number_of_stops = len(self.cheap_flight["itineraries"][0]["segments"])
        price = self.cheap_flight["price"]["total"]
        seats_left = self.cheap_flight["numberOfBookableSeats"]
        departure_date = self.cheap_flight["lastTicketingDateTime"]
        departure_airport = self.cheap_flight["itineraries"][0]["segments"][0]["departure"]["iataCode"]
        arrival_airport = self.cheap_flight["itineraries"][0]["segments"][number_of_stops - 1]["arrival"]["iataCode"]

        email_message = (f"Found cheap flight to {arrival_airport} from {departure_airport} on {departure_date}\n\n"
                         f"There are {seats_left} seats left, at a price of {price} for each ticket")

        connection = smtplib.SMTP(host=HOST)
        connection.starttls()
        connection.login(MY_EMAIL, PASS)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=email_message
        )


