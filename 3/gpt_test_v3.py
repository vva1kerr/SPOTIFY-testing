import requests
import base64
import json

# Your Client ID and Client Secret
CLIENT_ID = "e4e9a2c7695142c9aa70de6731523f5e"
CLIENT_SECRET = "ddadeffabd4a44448e78ec0afad0e06c"

# Base URL for Spotify API
TOKEN_URL = "https://accounts.spotify.com/api/token"

# Prepare the header
header = {}
encoded = base64.b64encode(f"{CLIENT_ID}:{CLIENT_SECRET}".encode('utf-8')).decode('ascii')
header["Authorization"] = f"Basic {encoded}"

# Prepare the payload
payload = {}
payload["grant_type"] = "client_credentials"

# Make the POST request
response = requests.post(TOKEN_URL, headers=header, data=payload)

# Extract Access Token from response
if response.status_code == 200:
    token_info = json.loads(response.text)
    access_token = token_info['access_token']
    print("Access Token:", access_token) # BQDfucJt52AW6YuPAVxqcepBd8q_puFPyQTh6XLsLQvSk0NiIzCbmYjYy9Gt6_fnkEOS0I7szgohkmryBxS75AS6IfGKeMYCtsCxtaP6PAw7LcBWyMQ
else:
    print("Couldn't fetch Access Token")
