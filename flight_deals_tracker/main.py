"""
Flight Deal Tracker
- Use a Google Sheet to track places I want to travel
- Have a defined price for what I want to pay for the flight
- Feed Locations to a Flight Search API for the next 6 months starting at tomorrow's date
- If the price is lower than the price I am looking for - send an email with the details
- Using Flight Search API to get IATA codes (city code)
"""
from datetime import datetime, timedelta

from data_manager import DataManager
from flight_deals_tracker.flight_data import FlightData
from flight_deals_tracker.flight_search import FlightSearch
from notification_manager import NotificationManager

ORIGIN_CITY_CODE = "GRR"

# Classes
data_manager = DataManager()
flight_search = FlightSearch()
flight_data = FlightData()

# Get data from sheet
sheet_data = data_manager.sheet_data

# Check for missing iata codes
for row in sheet_data:
    if row["iataCode"] == "":
        print(f"Adding missing city code for {row["city"]}")
        code = flight_search.get_city_codes(row)
        print(row["city"])
        print(row["id"])
        data_manager.update_city_codes(city=row["city"], code=code, id=row["id"])

        # Update sheet data
        sheet_data = data_manager.sheet_data

# Search for flights starting 5 days out and over a 6-month span
from_time = datetime.now() + timedelta(days=5)
to_time = datetime.now() + timedelta(days=6 * 30)

for city in sheet_data:
    # Get data for each city
    flight_search_data = flight_search.find_flight_data(
        data=city,
        to_time=to_time,
        from_time=from_time,
        origin_city=ORIGIN_CITY_CODE
    )

    # Send search data to FLight Data to parse and find the cheapest flight
    print(flight_search_data)
    flight_data_check = flight_data.find_lowest_price(
        flight_data=flight_search_data["data"],
        lowest_price=city["lowestPrice"],
        city_name=city["city"]
    )

# Send the cheapest flight to Notification
if flight_data.low_price_found:
    print("Cheap Price Notification")
    NotificationManager(flight_data.cheapest_flight).send_email_alert()
