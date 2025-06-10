import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import configparser

def get_features():
    """Get audio features using Spotipy."""
    # Load credentials from config
    config = configparser.ConfigParser()
    config.read(r"C:\Users\foo\Desktop\stfy\src\spotify\base\config.ini")
    
    client_id = config['CLIENT_CREDENTIALS']['CLIENT_ID']
    client_secret = config['CLIENT_CREDENTIALS']['CLIENT_SECRET']
    
    # Initialize Spotipy client
    client_credentials_manager = SpotifyClientCredentials(
        client_id=client_id,
        client_secret=client_secret
    )
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
    
    # Test track ID
    track_id = "4ZtFanR9U6ndgddUvNcjcG"
    
    print("Requesting features...")
    features = sp.audio_features(track_id)
    print(f"Features received: {features}")
    
    return features

if __name__ == "__main__":
    features = get_features()
    if features:
        print("\nFeatures:", features[0]) 