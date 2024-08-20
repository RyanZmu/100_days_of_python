import requests
import re
from bs4 import BeautifulSoup

class SongData:
    def __init__(self):
        self.date = input("What date do you want to search for? YYYY-MM-DD Format")
        self.song_and_artist: list = self.get_top_100()

    def get_top_100(self):
        response = requests.get(url=f"https://www.billboard.com/charts/hot-100/{self.date}")
        music_data = response.text

        soup = BeautifulSoup(music_data, features="html.parser")

        # Find the elements that contain song and artist names
        tracks = soup.select(selector="div li h3#title-of-a-story")
        artists = soup.select(selector="div.o-chart-results-list-row-container li ul li span")

        # Get text from elements and remove left over newlines
        song_list = [track.getText().replace("\n\t", "").replace("\t", "").replace("\n", "") for track in tracks]
        artist_list = [
            artist.getText().replace("\n\t", "").replace("\t", "").replace("\n", "") for artist in artists]

        # Remove all numbers from artist's array using regex
        filtered_artists = []
        for artist in artist_list:
            if re.search(string=artist, pattern="\\d") is None:
                filtered_artists.append(artist)

        # Create a dict for each song and artist
        final_track_list = []
        for song in song_list:
            try:
                index = song_list.index(song)
                track = {filtered_artists[index]: song}
            except IndexError:
                print("No artist or song found")
            else:
                final_track_list.append(track)

        return final_track_list

