import urllib.parse
import requests
import base64
import json
import configparser
import os

def load_config():
    """Load Spotify API credentials from config file."""
    config = configparser.ConfigParser()
    current_dir = os.path.dirname(os.path.abspath(__file__))
    config_path = os.path.join(current_dir, "base", "config.ini")
    config.read(config_path)
    auth_url = config['CLIENT_CREDENTIALS']['AUTH_URL']
    base_url = config['CLIENT_CREDENTIALS']['BASE_URL']
    return (
        config['CLIENT_CREDENTIALS']['CLIENT_ID'],
        config['CLIENT_CREDENTIALS']['CLIENT_SECRET'],
        auth_url,
        base_url
    )

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

def get_access_token(client_id, client_secret, auth_url):
    """Get Spotify API access token using client credentials."""
    header = {
        'Authorization': f"Basic {base64.b64encode(f'{client_id}:{client_secret}'.encode()).decode()}",
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    payload = {'grant_type': 'client_credentials'}
    
    print(f"Making auth request to: {auth_url}")  # Debug
    print(f"Using client_id: {client_id[:5]}...")  # Debug
    
    response = requests.post(auth_url, headers=header, data=payload)
    print(f"Auth response: {response.status_code}")  # Debug
    
    if response.status_code == 200:
        token = response.json()['access_token']
        print(f"Got token: {token[:10]}...")  # Debug
        return token
    print(f"Auth Error: {response.status_code} - {response.text}")
    return None

def get_audio_features(track_id, access_token, base_url):
    """Get audio features for a track using Spotify API."""
    url = "https://api.spotify.com/v1/audio-features/" + track_id
    headers = {
        'Authorization': f'Bearer {access_token}'
    }
    
    print(f"Making features request to: {url}")  # Debug
    print(f"With headers: {headers}")  # Debug
    
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    print(f"Features Error: {response.status_code} - {response.text}")
    return None

def get_audio_analysis(track_id, access_token):
    """Fetch audio analysis for a track from Spotify API."""
    url = f"https://api.spotify.com/v1/audio-analysis/{track_id}"
    headers = {
        'Authorization': f'Bearer {access_token}',
        # 'Content-Type': 'application/json',
        # 'Accept': 'application/json'
    }
    
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to get audio analysis: {response.content}")
        return None

def get_track_data(spotify_url):
    """Get audio features for a Spotify track URL."""
    try:
        client_id, client_secret, auth_url, base_url = load_config()
        access_token = get_access_token(client_id, client_secret, auth_url)
        
        if not access_token:
            print("No access token received")
            return None, None
            
        track_id = spotify_url.split('/')[-1].split('?')[0]
        print(f"Track ID: {track_id}")  # Debug line
        
        features = get_audio_features(track_id, access_token, base_url)
        audio_analysis = get_audio_analysis(track_id, access_token)
        
        return features, audio_analysis
    except Exception as e:
        print(f"Error in get_track_data: {str(e)}")
        return None, None

if __name__ == "__main__":
    # Example usage
    spotify_url = "https://open.spotify.com/track/4YQgOgIElFtEvwJQ9ArWL7?si=37e91e4ee1444477"
    features, analysis = get_track_data(spotify_url)
    
    if features:
        print("\nAudio Features:")
        print(json.dumps(features, indent=4))
    
    if analysis:
        print("\nAudio Analysis:")
        print(json.dumps(analysis, indent=4)) 