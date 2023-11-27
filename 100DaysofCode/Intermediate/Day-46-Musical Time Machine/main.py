import os
import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv

load_dotenv()

URL = "https://www.billboard.com/charts/hot-100"

desired_date = input("Enter a date you would like to go back to: ? (format is YYYY-MM-DD) ")
endpoint =f"{URL}/{desired_date}/"
print(endpoint)
response = requests.get(url=endpoint)
soup = BeautifulSoup(response.text,'html.parser')

# with open('index.html','w') as f:
#     f.write(soup.prettify())

"""
title = soup.find('h3')
print(title.getText().split())
"""
top_100_song_title_tag = soup.select(selector="li h3")
song_title = [title.get_text().strip() for title in top_100_song_title_tag[:100]]

for songs in song_title:
    print(songs)
    
spotify = spotipy.Spotify(
    client_credentials_manager=SpotifyClientCredentials(
        client_id=os.environ['SPOTIPY_CLIENT_ID'],
        client_secret=os.environ['SPOTIPY_CLIENT_SECRET'],
        )
    )
