"""
Spotify Music Time Machine

- Take user input as a date (yyyy-mm-dd)
- Scrape Billboard.com for the top 100 songs on that day
- Use Spotify API to create a playlist based on the top songs of that day

For year search https://www.billboard.com/charts/hot-100/2024-08-14

Follow OOP for this project
(Stretch) Make a UI for this project
"""
from dotenv import load_dotenv
from modules.song_data import SongData
from modules.playlist import MakePlaylist

# Load environment vars
load_dotenv()

# Get data for date requested
song_data = SongData()

# Make Playlist
MakePlaylist(song_data=song_data.song_and_artist, date=song_data.date).create_playlist()
