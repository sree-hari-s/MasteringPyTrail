import requests
import datetime as dt
import time 

MY_LATITUDE = 8.528861
MY_LONGITUDE = 76.913048

def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    data = response.json()

    iss_longitude = float(data['iss_position']['longitude'])
    iss_latitude = float(data['iss_position']['latitude'])
    iss_position = (iss_latitude, iss_longitude)
    print(f"ISS Location:{iss_position}")
    if MY_LATITUDE-5<= iss_latitude <=MY_LATITUDE+5 and MY_LONGITUDE-5<= iss_longitude <=MY_LONGITUDE+5:
        return True    

def is_night():
    parameters = {
        "lat" : MY_LATITUDE,
        "lng" : MY_LONGITUDE,
        "formatted": 0
    }

    response = requests.get(url="https://api.sunrise-sunset.org/json",params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data['results']['sunrise'].split('T')[-1].split(":")[0])
    sunset = int(data['results']['sunset'].split('T')[-1].split(":")[0])
    time_now = dt.datetime.now().hour
    print(f"Sunrise: {sunrise}\nSunset: {sunset}\nTime now: {time_now}")
    my_position = (MY_LATITUDE,MY_LONGITUDE)
    print(f"My Position: {my_position}")
    if time_now >= sunset or time_now <= sunrise:
        return True

while True:
    if is_night() and is_iss_overhead():
        print("Please look at the sky")
    else:
        print("ISS not nearby")
    time.sleep(60)