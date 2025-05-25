import requests
import base64
import json

# Your Client ID and Client Secret
CLIENT_ID = "e4e9a2c7695142c9aa70de6731523f5e"
CLIENT_SECRET = "ddadeffabd4a44448e78ec0afad0e06c"

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
    
    if access_token:
        print("Access Token:", access_token)
        
        track_id = '3n3Ppam7vgaVa1iaRUc9Lp'  # Replace with the track ID you are interested in

        audio_features = get_audio_features(track_id, access_token)
        audio_analysis = get_audio_analysis(track_id, access_token)

        if audio_features:
            print("Audio Features:")
            print(json.dumps(audio_features, indent=4))

        if audio_analysis:
            print("Audio Analysis:")
            print(json.dumps(audio_analysis, indent=4))
