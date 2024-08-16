"""
Workout Tracker
- Use Natural Language to add exercises to a Google spreadsheet
"""
import os
import requests
from requests.auth import HTTPBasicAuth
from datetime import datetime

# Constants
NUTRI_API_KEY = os.environ.get("NUTRI_API_KEY")
NUTRI_APP_ID = os.environ.get("NUTRI_APP_ID")

# Endpoints
nutri_api_endpoint = "https://trackapi.nutritionix.com"
nutri_api_exercise_endpoint = f"{nutri_api_endpoint}/v2/natural/exercise"
sheety_api_endpoint = "https://api.sheety.co/40c569d88fe8435409662e9a2ac66abe/workoutTracker/sheet1"

# Nutri request
nutri_headers = {
    "x-app-id": NUTRI_APP_ID,
    "x-app-key": NUTRI_API_KEY
}

nutri_parameters = {
    "query": input("What exercise did you perform today and for how long?")
}

nutri_exercise_request = requests.post(url=nutri_api_exercise_endpoint, json=nutri_parameters, headers=nutri_headers)
nutri_exercise_data = nutri_exercise_request.json()
print(nutri_exercise_data)

# Get relevant parts of Nutri output
exercise_info = nutri_exercise_data["exercises"][0]
exercise_name = exercise_info["name"]
exercise_duration = exercise_info["duration_min"]
exercise_calories = exercise_info["nf_calories"]

# Add a row to workout tracker using Sheety
SHEETY_TOKEN = os.environ.get("SHEETY_TOKEN")
SHEETY_USERNAME = os.environ.get("SHEETY_USERNAME")
SHEETY_PASSWORD = os.environ.get("SHEETY_PASSWORD")

# Sheety request
sheety_headers = {
    "Authorization": SHEETY_TOKEN
}

sheety_params = {
    "sheet1": {
        "date": datetime.now().strftime("%m/%d/%Y"),
        "time": datetime.now().strftime("%I:%M:%S"),
        "exercise": exercise_name,
        "duration": exercise_duration,
        "calories": exercise_calories
    }
}

# Use Basic authentication
auth = HTTPBasicAuth(username=SHEETY_USERNAME, password=SHEETY_PASSWORD)
sheety_request = requests.post(
    url=sheety_api_endpoint,
    json=sheety_params,
    headers=sheety_headers,
    auth=auth
)

print(sheety_request.text)
