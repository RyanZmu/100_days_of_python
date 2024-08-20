import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os

class MakePlaylist:
    def __init__(self, song_data, date):
        self.CLIENT_ID = os.environ.get("SPOTIFY_CLIENT_ID")
        self.CLIENT_SECRET = os.environ.get("SPOTIFY_SECRET")
        self.REDIRECT_URI = os.environ.get("REDIRECT_URI")
        self.ENDPOINT = "https://api.spotify.com/v1/"
        self.date = date
        self.song_data = song_data
        self.song_uris = []
        self.playlist_id = 0

    def create_playlist(self):
        # Authenticate with Spotify
        sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=self.CLIENT_ID,
                                                       client_secret=self.CLIENT_SECRET,
                                                       redirect_uri=self.REDIRECT_URI,
                                                       scope="playlist-modify-private"))

        current_user = sp.current_user()["id"]

        # Create new playlist
        playlists = sp.user_playlist_create(
            user=current_user,
            name=f"{self.date} Billboard Top 100",
            description=f"Check out the Billboard Top 100 songs from {self.date} This was generated with Python :-)",
            public=False
        )

        self.playlist_id = playlists["id"]
        print(f"Created playlist {self.date} Billboard Top 100")

        # Populate playlist
        self.add_songs_to_playlist()

    def add_songs_to_playlist(self):
        # Authenticate with Spotify
        sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=self.CLIENT_ID,
                                                       client_secret=self.CLIENT_SECRET,
                                                       redirect_uri="http://localhost/",
                                                       scope="playlist-modify-private"
                                                       )
                             )
        # Get song URIs
        for track in self.song_data:
            try:
                song_data = sp.search(q=f"{track}")
                song_uri = (song_data["tracks"]["items"][0]["uri"])
                self.song_uris.append(song_uri)
            except KeyError:
                print(f"{track} not found")
            else:
                print(f"Added {track}")

        # Add songs to playlist
        add_songs = sp.playlist_add_items(
            playlist_id=self.playlist_id,
            items=self.song_uris
        )

        print(add_songs)



