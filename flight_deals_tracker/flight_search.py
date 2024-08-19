import os
import requests

# Flight API endpoints
flight_api_endpoint = "https://test.api.amadeus.com/v2"
flight_api_city_search_endpoint = "https://test.api.amadeus.com/v1/reference-data/locations"
flight_deals_api_endpoint = f"{flight_api_endpoint}/shopping/flight-offers"
token_auth_endpoint = "https://test.api.amadeus.com/v1/security/oauth2/token"

class FlightSearch:
    def __init__(self):
        self.flight_search_data: list = []
        self.api_key = os.environ.get("FLIGHT_API_KEY")
        self.api_secret = os.environ.get("FLIGHT_SECRET")
        self.flight_token = self.get_new_flight_token()

    def find_flight_data(self, data, from_time, to_time, origin_city):
        # Get city codes from sheety
        city_data = data
        flight_headers = {
            "Authorization": f"Bearer {self.flight_token}"
        }

        # Use flight search with city code
        flight_search_parameters = {
            "originLocationCode": origin_city,
            "destinationLocationCode": city_data["iataCode"],
            "departureDate": from_time.strftime("%Y-%m-%d"),
            "returnDate": to_time.strftime("%Y-%m-%d"),
            "adults": 1,
            "currencyCode": "USD",
        }

        flight_deals_request = requests.get(
            url=flight_deals_api_endpoint,
            params=flight_search_parameters,
            headers=flight_headers
        )
        flight_deals_request_data = flight_deals_request.json()
        self.flight_search_data.append(flight_deals_request_data)
        return flight_deals_request_data

    def get_new_flight_token(self):
        flight_headers = {
            "Content-Type": "application/x-www-form-urlencoded"
        }

        auth_parameters = {
            "grant_type": "client_credentials",
            "client_id": self.api_key,
            "client_secret": self.api_secret
        }

        api_token_request = requests.post(
            url=token_auth_endpoint,
            data=auth_parameters,
            headers=flight_headers
        )

        api_token_request.raise_for_status()
        # print(api_token_request.json())
        return api_token_request.json()["access_token"]

    def get_city_codes(self, data):
        parameters = {
            "keyword": data["city"],
            "subType": "CITY"
        }

        headers = {
            "Authorization": f"Bearer {self.flight_token}"
        }

        city_codes_request = requests.get(url=flight_api_city_search_endpoint, headers=headers, params=parameters)
        print(city_codes_request.json())
        return city_codes_request.json()["data"][0]["iataCode"]

