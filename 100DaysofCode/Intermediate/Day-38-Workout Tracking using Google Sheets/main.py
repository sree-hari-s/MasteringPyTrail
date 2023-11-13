import os
import requests
from dotenv import load_dotenv
import datetime as dt

load_dotenv()
os.environ["API_KEY"]

HEADERS = {
    "x-app-id": os.environ["APP_ID"],
    "x-app-key": os.environ["API_KEY"],
    "x-remote-user-id": "0",
}

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

GENDER = input("Enter your gender:")
WEIGHT_KG = input("Enter your weight(in kg):")
HEIGHT_CM = input("Enter your height(in cm):")
AGE = input("Enter your age:")
exercise_text = input("Tell me which exercises you did: ")

"""
Setting a default values for testing purposes
"""
# GENDER = "male"
# WEIGHT_KG = "50"
# HEIGHT_CM = "168"
# AGE = "24"
# exercise_text = "ran for 5 kms"

input_data = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE,
}

response = requests.post(url=exercise_endpoint, json=input_data, headers=HEADERS)
print(response.status_code)
exercise_data = response.json()['exercises'][0]
print(exercise_data)
exercise = exercise_data['name'].title()
duration = exercise_data['duration_min']
calories = exercise_data['nf_calories']
today = dt.datetime.now()
date = today.strftime("%d/%m/%Y")
time = today.strftime("%X")
print(exercise)
print(duration)
print(calories)
print(today)
print(date)
print(time)

data = {
    "workout":{
        "date":date,
        "time":time,
        "exercise":exercise,
        "duration":duration,
        "calories":calories
    }
}

sheety_header = {
    "Authorization": f"Bearer {os.environ['BEARER_TOKEN']}"
}

sheety_url = "https://api.sheety.co/2c8f8a6fe47964efb55f3d3f55787223/myWorkouts/workouts"
response = requests.post(url=sheety_url, json=data,headers=sheety_header)
print(response.text)