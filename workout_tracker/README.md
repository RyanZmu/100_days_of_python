# Workout Tracker

## What It Does
- Uses Google Sheets, Sheety API and Nutritionix API
- Updates Google Sheet using Natural Language queries
- Connects to Google Sheet using Sheety API calls

## How To Use It
- Create your own Google Sheet named Workout Trainer
- Create a Sheety account and link your Sheet
- Set Basic Authentication up with your Sheety project
- Get an API Key and APP ID from Nutritionix API
- Create Environment Variables for each api key and account
  - NUTRI_API_KEY = os.environ.get("NUTRI_API_KEY")
  - NUTRI_APP_ID = os.environ.get("NUTRI_APP_ID")
  - SHEETY_TOKEN = os.environ.get("SHEETY_TOKEN")
  - SHEETY_USERNAME = os.environ.get("SHEETY_USERNAME")
  - SHEETY_PASSWORD = os.environ.get("SHEETY_PASSWORD")
- Run main.py in the console and say what workout you did
- Open Google Sheet and look at updated data