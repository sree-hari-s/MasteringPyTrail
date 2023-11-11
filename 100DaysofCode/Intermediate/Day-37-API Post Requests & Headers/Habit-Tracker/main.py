import datetime as dt
import requests

pixels_endpoint = "https://pixe.la/v1/users"

TOKEN = "fasjkhfalksjhffas"
USERNAME = "sreeharis"
GRAPH_ID ="graph1"

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
    "id":GRAPH_ID,
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

graph_data_endpoint = f"{graph_endpoint}/{GRAPH_ID}"

# today = str(dt.datetime.now().date()).replace('-','')  # using split method to get todays date
today = dt.datetime.now().strftime("%Y%m%d") # Get todays date using strftime method
# yesterday = dt.datetime(year=2023,month=11,day=10).strftime("%Y%m%d")
print(today)

graph_data = {
    "date":today,
    "quantity":"10"
}

response = requests.post(url=graph_data_endpoint,json=graph_data,headers=headers)
print(response.text)