"""
# https://developer.spotify.com/documentation/web-api/reference/get-audio-features

danceability: Danceability describes how suitable a track is for dancing 
    based on a combination of musical elements including tempo, rhythm stability, beat strength, and overall regularity. A value of 0.0 is least danceable and 1.0 is most danceable.
energy: Energy is a measure from 0.0 to 1.0 and represents a perceptual 
    measure of intensity and activity. Typically, energetic tracks feel fast, loud, and noisy. For example, death metal has high energy, while a Bach prelude scores low on the scale. Perceptual features contributing to this attribute include dynamic range, perceived loudness, timbre, onset rate, and general entropy.
key: 
loudness: 
mode: 
speechiness: 
acousticness: A confidence measure from 0.0 to 1.0 of whether the track 
    is acoustic. 1.0 represents high confidence the track is acoustic.
instrumentalness: 
liveness: 
valence: 
tempo: 
type: 
id: 
uri: 
track_href: 
analysis_url: A URL to access the full audio analysis of this track. An 
    access token is required to access this data.
duration_ms: The duration of the track in milliseconds.
time_signature: 
"""

import requests
import base64
import json

# Your Client ID and Client Secret
CLIENT_ID = "e4e9a2c7695142c9aa70de6731523f5e"
CLIENT_SECRET = "ddadeffabd4a44448e78ec0afad0e06c"
spotify_url = "https://open.spotify.com/track/4YQgOgIElFtEvwJQ9ArWL7?si=37e91e4ee1444477"



import urllib.parse

def extract_track_id_from_url(spotify_url):
    # Parse the URL to get its components
    parsed_url = urllib.parse.urlparse(spotify_url)
    
    # Check if the URL is a valid Spotify track URL
    if "open.spotify.com" in parsed_url.netloc and "/track/" in parsed_url.path:
        # Extract the track ID from the path
        path_segments = parsed_url.path.split("/")
        if len(path_segments) > 2 and path_segments[1] == 'track':
            track_id = path_segments[2]
            return track_id
    return None


def get_audio_features(track_id, access_token):
    url = f"https://api.spotify.com/v1/audio-features/{track_id}"
    headers = {
        'Authorization': f'Bearer {access_token}',
    }
    
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to get audio features: {response.content}")
        return None

def get_audio_analysis(track_id, access_token):
    url = f"https://api.spotify.com/v1/audio-analysis/{track_id}"
    headers = {
        'Authorization': f'Bearer {access_token}',
    }
    
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to get audio analysis: {response.content}")
        return None
        
def get_access_token(client_id, client_secret):
    TOKEN_URL = "https://accounts.spotify.com/api/token"

    # Prepare the header
    header = {}
    encoded = base64.b64encode(f"{client_id}:{client_secret}".encode('utf-8')).decode('ascii')
    header["Authorization"] = f"Basic {encoded}"

    # Prepare the payload
    payload = {"grant_type": "client_credentials"}

    # Make the POST request
    response = requests.post(TOKEN_URL, headers=header, data=payload)

    print(response.status_code)
    if response.status_code == 200:
        token_info = json.loads(response.text)
        return token_info['access_token']
    else:
        print("Couldn't fetch Access Token")
        return None

# The rest of your functions remain the same.

if __name__ == "__main__":
    access_token = get_access_token(CLIENT_ID, CLIENT_SECRET)
    
    # if access_token:
    #     print("Access Token:", access_token)

        # track_id = extract_track_id_from_url(spotify_url)
    #     if track_id:
    #         print(f"Extracted Track ID: {track_id}")
    #     else:
    #         print("Invalid Spotify URL")
        
    #     # track_id = '3n3Ppam7vgaVa1iaRUc9Lp'  # Replace with the track ID you are interested in

    #     audio_features = get_audio_features(track_id, access_token)
    #     audio_analysis = get_audio_analysis(track_id, access_token)

    #     if audio_features:
    #         print("Audio Features:")
    #         print(json.dumps(audio_features, indent=4))

    #     if audio_analysis:
    #         print("Audio Analysis:")
    #         print(json.dumps(audio_analysis, indent=4))



    if access_token: 
        track_id = extract_track_id_from_url(spotify_url)
        audio_features = get_audio_features(track_id, access_token)
        audio_analysis = get_audio_analysis(track_id, access_token)

        # Save audio features to JSON
        if audio_features:
            with open("SONG_DATA/audio_features.json", "w") as f:
                json.dump(audio_features, f, indent=4)

        # Save audio analysis to JSON
        if audio_analysis:
            with open("SONG_DATA/audio_analysis.json", "w") as f:
                json.dump(audio_analysis, f, indent=4)
 