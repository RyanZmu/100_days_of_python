import requests
# HTTP Refresher
# 1xx - Hold on
# 2xx - Getting expected data
# 3xx - Rejected
# 4xx - User Error
# 5xx - Server Error

response = requests.get(url="http://api.open-notify.org/iss-now.json")

# Raise exceptions for a non 200 status code
response.raise_for_status()

data = response.json()
latitude = data["iss_position"]["latitude"]
longitude = data["iss_position"]["longitude"]

iss_position = (longitude, latitude)

print(iss_position)
