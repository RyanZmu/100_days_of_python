"""
Pixela API Habit Tracker
- Use Pixela to track habits using API calls
- Use Put/Post/Delete to edit pixels for a given day
"""
import requests
import os
from datetime import datetime

pixela_endpoint = "https://pixe.la/v1/users"
USERNAME = os.environ.get("USERNAME")
TOKEN = os.environ.get("TOKEN")
CODING_GRAPH_ID = "graph1"

headers = {
    "X-USER-TOKEN": TOKEN
}

# ======= Create new user account =======
# user_params = {
#     "username": USERNAME,
#     "agreeTermsOfService": "yes",
#     "notMinor": "yes",
# }

# Use json instead of params
# user_response = requests.post(url=pixela_endpoint, json=user_params)
# print(user_response.text)


# ======= Create a new graph ======
# graph_params = {
#     "id": "graph1",
#     "name": "Coding Graph",
#     "unit": "hour",
#     "type": "float",
#     "color": "sora"
# }

# graph_request = requests.post(url=f"{pixela_endpoint}/{USERNAME}/graphs", json=graph_params, headers=headers)
# print(graph_request.text)


# ======= Post to the Coding habit graph =======
today = datetime.now().strftime("%Y%m%d")
print(today)

graph_post_params = {
    "date": today,
    "quantity": input("How many hours have you studied code today?"),
}

graph_post_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{CODING_GRAPH_ID}"

pixela_post_request = requests.post(
    url=graph_post_endpoint,
    json=graph_post_params,
    headers=headers
)
print(pixela_post_request.text)


# ======= Use Put to change existing data =======
# graph_put_params = {
#     "quantity": "6",
# }
#
# graph_put_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{CODING_GRAPH_ID}/{today}"

# graph_put_request = requests.put(
#     url=graph_put_endpoint,
#     json=graph_put_params,
#     headers=headers
# )
# print(graph_put_request.text)


# ======= Use Delete to remove a pixel =======
# graph_delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{CODING_GRAPH_ID}/{today}"

# graph_delete_request = requests.delete(
#     url=graph_delete_endpoint,
#     headers=headers
# )
# print(graph_delete_request.text)


