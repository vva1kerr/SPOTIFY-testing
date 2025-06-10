import streamlit as st
import pandas as pd
import numpy as np
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from spotify.spotify_web_api_track_data import get_track_data

def calculate_statistics(data):
    """Calculate statistics for a single track's features."""
    features = [
        'danceability', 'energy', 'key', 'loudness', 'mode',
        'speechiness', 'acousticness', 'instrumentalness',
        'liveness', 'valence', 'tempo'
    ]
    
    stats = {}
    for feature in features:
        value = data.get(feature)
        if value is not None:
            stats[feature] = value
    
    return pd.DataFrame([stats])

st.title("Track Statistics")

spotify_url = st.text_input("Enter Spotify Track URL:")

if spotify_url:
    features, analysis = get_track_data(spotify_url)
    
    if features:
        st.subheader("Audio Features Statistics")
        stats_df = calculate_statistics(features)
        st.dataframe(stats_df)
        
    if analysis and 'track' in analysis:
        st.subheader("Track Analysis Statistics")
        track_stats = analysis['track']
        track_df = pd.DataFrame([track_stats])
        st.dataframe(track_df)