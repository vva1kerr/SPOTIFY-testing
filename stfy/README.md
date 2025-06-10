# STFY - Spotify Explorer

A Streamlit application for exploring Spotify data using the Spotify Web API.

## Setup
1. Create virtual environment:
```bash
python -m venv myenv
source myenv/bin/activate  # On Windows: myenv\Scripts\activate
```

2. Install requirements:
```bash
pip install -r requirements.txt
```

3. Configure Spotify credentials in `src/spotify/base/config.ini`

4. Run the application:
```bash
# Terminal 1 - OAuth server
cd src/spotify/web
uvicorn main:app --reload

# Terminal 2 - Streamlit app
cd src/streamlit
streamlit run streamlit_app.py
```








sequenceDiagram
    participant User
    participant Streamlit
    participant FastAPI
    participant Spotify
    
    User->>Streamlit: Requests protected data
    Streamlit->>Spotify: Redirects to Spotify login
    Spotify->>FastAPI: Sends auth code to callback URL
    FastAPI->>Spotify: Exchanges code for token
    FastAPI->>Streamlit: Provides access token
    Streamlit->>Spotify: Makes API calls with token



If you're only building pages that show general Spotify data (artists, albums, tracks), you don't need to run the FastAPI server yet. 



# Spotify Rate Limits
https://developer.spotify.com/documentation/web-api/concepts/rate-limits

https://spotipy.readthedocs.io/en/2.11.1/

https://community.spotify.com/t5/Spotify-for-Developers/Changes-to-Web-API/td-p/6540414