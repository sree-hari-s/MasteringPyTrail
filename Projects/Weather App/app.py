import tkinter as tk
from tkinter import messagebox
import requests

# Replace this with your WeatherAPI.com RapidAPI key
RAPIDAPI_KEY = "YOUR_RAPIDAPI_KEY"

def get_weather(city):
    url = "https://weatherapi-com.p.rapidapi.com/current.json"
    querystring = {"q": city}
    headers = {
        # Add your own API Key from this given link : https://rapidapi.com/weatherapi/api/weatherapi-com
        "X-RapidAPI-Key":"",
        "X-RapidAPI-Host":"weatherapi-com.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    if response.status_code == 200:
        data = response.json()
        location = data['location']['name']
        temperature = data['current']['temp_c']
        weather_description = data['current']['condition']['text']

        result_label.config(text=f'Weather in {location}:\nTemperature: {temperature}°C\nDescription: {weather_description}')
    else:
        messagebox.showerror('Error', 'City not found.')

def display_weather():
    city = city_entry.get()
    if not city:
        messagebox.showerror('Error', 'Please enter a city name.')
        return

    get_weather(city)

# Create the main window
window = tk.Tk()
window.title('Weather App')

# Create and arrange widgets
city_label = tk.Label(window, text='Enter City:')
city_label.pack()

city_entry = tk.Entry(window)
city_entry.pack()

get_weather_button = tk.Button(window, text='Get Weather', command=display_weather)
get_weather_button.pack()

result_label = tk.Label(window, text='', wraplength=300)
result_label.pack()

# Start the GUI main loop
window.mainloop()
