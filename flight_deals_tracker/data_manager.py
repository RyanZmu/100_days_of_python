import os
import requests

# Sheety API
sheety_api_endpoint = "https://api.sheety.co/40c569d88fe8435409662e9a2ac66abe/flightPrices/sheet1"
sheety_user_api_endpoint = "https://api.sheety.co/40c569d88fe8435409662e9a2ac66abe/flightPrices/users"

class DataManager:
    def __init__(self):
        self.SHEETY_TOKEN = os.environ.get("SHEETY_TOKEN")
        self.SHEETY_USERNAME = os.environ.get("SHEETY_USERNAME")
        self.SHEETY_PASSWORD = os.environ.get("SHEETY_PASSWORD")
        self.sheet_data = self.get_sheety_data()

    def get_sheety_data(self):
        sheety_headers = {
            "Authorization": self.SHEETY_TOKEN
        }

        sheety_get_request = requests.get(url=sheety_api_endpoint, headers=sheety_headers)
        sheety_data = sheety_get_request.json()

        self.sheet_data = sheety_data["sheet1"]
        return sheety_data["sheet1"]

    def update_city_codes(self, code, city, id):
        sheety_headers = {
            "Authorization": self.SHEETY_TOKEN,
            "Content-Type": "application/json"
        }

        new_data = {
            "sheet1": {
                "iataCode": code,
            }
        }

        update_sheet = requests.put(url=f"{sheety_api_endpoint}/{id}", json=new_data, headers=sheety_headers)
        print(update_sheet.text)

    def update_users(self):
        pass

