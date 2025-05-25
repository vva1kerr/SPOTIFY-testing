"""
Spotify dev website
    https://developer.spotify.com/
Spotipy github
    https://github.com/plamere/spotipy



"""
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy.oauth2 import SpotifyOAuth
print("\nstarting...\n")

cid = "e4e9a2c7695142c9aa70de6731523f5e" # your client id
secret = "ddadeffabd4a44448e78ec0afad0e06c" # your secret id

# without userser auth
artist = input("artist username: ").lower()
WorWO = input("user auth w/wo: ").lower()

if WorWO == "wo":
    sp = spotipy.Spotify(
        auth_manager=SpotifyClientCredentials(
            client_id="e4e9a2c7695142c9aa70de6731523f5e",
            client_secret="ddadeffabd4a44448e78ec0afad0e06c"))

    results = sp.search(q=artist, limit=10)
    for idx, track in enumerate(results['tracks']['items']):
        print(idx, track['name'])

elif WorWO == "w":
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="e4e9a2c7695142c9aa70de6731523f5e",
                                               client_secret="ddadeffabd4a44448e78ec0afad0e06c",
                                               redirect_uri="testingwalker-rh://callback",
                                               scope="user-read-recently-played"))

    results = sp.current_user_recently_played()
    for idx, item in enumerate(results['items']):
        track = item['track']
        print(idx, track['artists'][0]['name'], " - ", track['name'])