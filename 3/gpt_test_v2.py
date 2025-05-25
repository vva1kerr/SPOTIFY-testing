import requests
import json

# Your Spotify API token goes here. You can get this token from Spotify Developer Dashboard
API_TOKEN = "YOUR_API_TOKEN_HERE"

# Base URL for all Spotify API endpoints
BASE_URL = "https://api.spotify.com/v1/"

# Spotify Track ID
TRACK_ID = "YOUR_TRACK_ID_HERE"

# Get Audio Features for a Track
def get_audio_features(track_id, api_token):
    url = f"{BASE_URL}audio-features/{track_id}"
    headers = {"Authorization": f"Bearer {api_token}"}
    
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return json.loads(response.text)
    else:
        return None

# Get Audio Analysis for a Track
def get_audio_analysis(track_id, api_token):
    url = f"{BASE_URL}audio-analysis/{track_id}"
    headers = {"Authorization": f"Bearer {api_token}"}
    
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return json.loads(response.text)
    else:
        return None

# Fetching data
audio_features = get_audio_features(TRACK_ID, API_TOKEN)
audio_analysis = get_audio_analysis(TRACK_ID, API_TOKEN)

# Printing the results
if audio_features:
    print("Audio Features:")
    print(json.dumps(audio_features, indent=4))
else:
    print("Couldn't fetch Audio Features")

if audio_analysis:
    print("Audio Analysis:")
    print(json.dumps(audio_analysis, indent=4))
else:
    print("Couldn't fetch Audio Analysis")
