# Music Time Machine

## What It Does
- Creates a Spotify Playlist for the Billboard Top 100 songs for a given date

## How It Works
- Web scrapes the Billboard website using the BeautifulSoup library.
- Finds the song names and artist names from the returned data
- Sends the data to Spotify Web API
- Spotify API creates a new playlist and populates it with the top 100 songs - sometimes it can't find a song and will skip

## How To Use It
- Create a developer account on Spotify
- Create an Application in Spotify API Dashboard
- Obtain your Client Secret and Client ID
- Create a .env file and populate with your SPOTIFY_CLIENT_ID and SPOTIFY_CLIENT_SECRET 
  - Example: SPOTIFY_CLIENT_ID = <your_ID>
- Can set REDIRECT_URL to http://localhost/ but use whatever you used when creating the Application in Spotify
- Run main.py - python ./music_time_machine/main.py
- Enter date and watch the playlist be created
  - Redirect link will open in your browser, accept the dialog and paste the url into the terminal to continue
