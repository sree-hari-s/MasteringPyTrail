import os
import requests
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()

MY_LATITUDE = 8.528861
MY_LONGITUDE = 76.913048

parameters ={
"lat": MY_LATITUDE,
"lon": MY_LONGITUDE,
"appid": os.environ['api_key'],
"exclude":"current,minutely,daily,alerts"
}
OWM_endpoint = "https://api.openweathermap.org/data/2.8/onecall"
response = requests.get(OWM_endpoint,params=parameters)
response.raise_for_status()
weather_data = response.json()

weather_12hr = weather_data['hourly'][:12] # Slice through the dictionary to get required data to a list
will_rain = False
for hour_data in weather_12hr:
    weather_code = hour_data['weather'][0]['id']
    if int(weather_code)<700:
        will_rain=True

if will_rain:
    msg = "Bring an Umbrella"

    client = Client(os.environ["account_sid"], os.environ["auth_token"])

    message = client.messages \
        .create(
            from_= os.environ['from_phone'],
            body=msg,
            to=os.environ['to_phone']
        )

    print(message.status)