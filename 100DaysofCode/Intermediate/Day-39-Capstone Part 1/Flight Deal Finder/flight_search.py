import os
import requests
from dotenv import load_dotenv

load_dotenv()

TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"


class FlightSearch:

    def get_destination_code(self, city_name):
        location_endpoint = f"{TEQUILA_ENDPOINT}/locations/query"
        headers = {"apikey": os.environ['TEQUILA_API_KEY']}
        query = {"term": city_name, "location_types": "city"}
        response = requests.get(url=location_endpoint, headers=headers, params=query)
        results = response.json()["locations"]
        code = results[0]["code"]
        return code
