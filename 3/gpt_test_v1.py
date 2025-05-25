import requests
import json

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

if __name__ == "__main__":
    access_token = 'YOUR_ACCESS_TOKEN'  # Replace with your actual access token
    track_id = '3n3Ppam7vgaVa1iaRUc9Lp'  # Replace with the track ID you are interested in
    
    audio_features = get_audio_features(track_id, access_token)
    audio_analysis = get_audio_analysis(track_id, access_token)
    
    if audio_features:
        print("Audio Features:")
        print(json.dumps(audio_features, indent=4))
        
    if audio_analysis:
        print("Audio Analysis:")
        print(json.dumps(audio_analysis, indent=4))
