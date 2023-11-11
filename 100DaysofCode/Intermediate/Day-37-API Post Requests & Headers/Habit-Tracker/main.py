import datetime as dt
import requests

pixels_endpoint = "https://pixe.la/v1/users"

TOKEN = "fasjkhfalksjhffas"
USERNAME = "sreeharis"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService" : "yes",
    "notMinor" : "yes",
}

response = requests.post(url = pixels_endpoint,json=user_params)
print(response.text)

graph_endpoint = f"{pixels_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id":"graph1",
    "name":"Step Counter Graph",
    "unit" : "Km",
    "type" : "float",
    "color" : "shibafu"
}

headers = {
    "X-USER-TOKEN": TOKEN,
}

response = requests.post(url=graph_endpoint,json=graph_config,headers=headers)
print(response.text)

