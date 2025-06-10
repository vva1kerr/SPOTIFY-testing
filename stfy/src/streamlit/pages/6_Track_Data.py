import streamlit as st
import sys
import os

# Add the src directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from spotify.spotify_web_api_track_data import get_track_data

st.title("Spotify Track Data")

spotify_url = st.text_input("Enter Spotify Track URL:", 
                           "https://open.spotify.com/track/6YvvTg8WaWMdCaBBBwd8e5")

if st.button("Analyze Track"):
    if spotify_url:
        features, analysis = get_track_data(spotify_url)
        
        if features:
            st.subheader("Audio Features")
            st.json(features)
        
        if analysis:
            st.subheader("Audio Analysis")
            st.json(analysis)