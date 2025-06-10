import streamlit as st
import matplotlib.pyplot as plt
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from spotify.spotify_web_api_track_data import get_track_data
from spotify.visualize_song_data_features import create_feature_plot

st.title("Feature Visualization")

spotify_url = st.text_input("Enter Spotify Track URL:")

if spotify_url:
    features, _ = get_track_data(spotify_url)
    
    if features:
        st.subheader("Audio Features Visualization")
        fig = plt.figure(figsize=(10, 6))
        create_feature_plot(features)
        st.pyplot(fig)