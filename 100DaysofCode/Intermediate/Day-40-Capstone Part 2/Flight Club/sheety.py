import os
import requests
from dotenv import load_dotenv

load_dotenv()

BEARER = os.environ['BEARER_TOKEN']

PROJECT = "flightDeals"
SHEET = "users"

base_url = "https://api.sheety.co/2c8f8a6fe47964efb55f3d3f55787223"

def post_new_row(first_name, last_name,email):
    endpoint_url = f'{base_url}/{PROJECT}/{SHEET}'
    
    headers = {
        "Authorization" : f"Bearer {BEARER}"
    }
    
    body = {
        "user":{
            "firstName":first_name,
            "lastName":last_name,
            "email":email
        }
    }
    
    response = requests.post(url = endpoint_url,json=body,headers=headers)
    response.raise_for_status()
    print(response.text)