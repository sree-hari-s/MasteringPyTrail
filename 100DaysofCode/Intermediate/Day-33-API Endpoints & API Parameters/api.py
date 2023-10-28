import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")
print(response.status_code)
data = response.json()

longitude = data['iss_position']['longitude']
latitude = data['iss_position']['latitude']

iss_postion = (longitude,latitude)
print(iss_postion)