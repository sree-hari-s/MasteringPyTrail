from bs4 import BeautifulSoup
import requests
from requests import HTTPError
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os
from spotipy import SpotifyException
from dotenv import load_dotenv

load_dotenv()

# Load Spotify API credentials from environment variables
CLIENT_ID = os.environ["SPOTIPY_CLIENT_ID"]
CLIENT_SECRET = os.environ["SPOTIPY_CLIENT_SECRET"]
REDIRECT_URL = os.environ["SPOTIPY_REDIRECT_URI"]


def get_date():
    """
    Prompt user to input a date in the format YYYY-MM-DD.
    """
    input_date = input("Which date to use? Please enter a date in the format YYYY-MM-DD: ")
    return input_date


def get_top_100_at_date(input_date: str) -> list:
    """
    Get the top 100 songs at a given date from the Billboard website.
    """
    try:
        response = requests.get(url=f"https://www.billboard.com/charts/hot-100/{input_date}")
        response.raise_for_status()
        print(f"Response code is: {response.status_code}")
        soup = BeautifulSoup(response.text, "html.parser")

        # Extract song names from the HTML
        song_tags = soup.find_all(name="div", class_="o-chart-results-list-row-container")
        song_names = [
            song.find_all(name="li")[3].find(name="h3").getText().strip()
            for song in song_tags
        ]
        print(f"{len(song_names)} in songs_list")
        return song_names

    except (AttributeError, HTTPError):
        print("Please enter another date")
        input_date = get_date()
        # Recursively call get_top_100_at_date with the new date
        return get_top_100_at_date(input_date)


def get_user_id(my_spotipy):
    """
    Get the user ID from the authenticated Spotify instance.
    """
    user_id = my_spotipy.current_user()["id"]
    return user_id


def create_playlist(my_spotipy, user_id, name="100 Days of Code", description="From Day 46 in 100 Days of Code"):
    """
    Create a new private playlist.
    """
    my_spotipy.user_playlist_create(
        user=user_id, name=name, public=False, description=description
    )


def get_most_recent_playlist(my_spotipy):
    """
    Get the ID of the most recently created playlist.
    """
    date_playlist = my_spotipy.current_user_playlists()["items"][0]["id"]
    return date_playlist


def get_track_ids(my_spotipy, songs: list) -> list:
    """
    Convert each song from its name to its Spotify ID value.
    """
    song_ids = []
    count = 0
    for song in songs:
        try:
            # Search for the song on Spotify and get its track ID
            track_id = my_spotipy.search(q=song, type="track")["tracks"]["items"][0]["id"]
            print(f"{count}) {track_id}")
            song_ids.append(track_id)
            count += 1
        except SpotifyException:
            print(f"No name found")
            pass
    return song_ids


def add_songs(my_spotipy, user_id, playlist_id, songs: list):
    """
    Add a list of songs to a Spotify playlist.
    """
    my_spotipy.user_playlist_add_tracks(
        user=user_id, playlist_id=playlist_id, tracks=songs
    )


def main():
    # Get user input for the date
    input_date = get_date()
    # Get the top 100 songs at the given date
    songs_list = get_top_100_at_date(input_date=input_date)
    print(songs_list)

    # Set up Spotify API authentication
    scope = "playlist-modify-private playlist-read-private"
    sp = spotipy.Spotify(
        auth_manager=SpotifyOAuth(
            scope=scope,
            redirect_uri=REDIRECT_URL,
            client_id=CLIENT_ID,
            client_secret=CLIENT_SECRET,
            show_dialog=True,
            cache_path="token.txt",
        )
    )

    # Get the user ID from Spotify
    user_id = get_user_id(sp)
    # Create a new private playlist
    create_playlist(
        sp, user_id=user_id, name=f"Top 100 song in the week of {input_date}"
    )

    # Get the ID of the most recently created playlist
    top_100_at_date_playlist = get_most_recent_playlist(sp)
    # Get the Spotify track IDs for the top 100 songs
    top_100_tracks_ids = get_track_ids(sp, songs_list)
    # Add the top 100 songs to the playlist
    add_songs(
        my_spotipy=sp,
        user_id=user_id,
        playlist_id=top_100_at_date_playlist,
        songs=top_100_tracks_ids,
    )


if __name__ == "__main__":
    main()
