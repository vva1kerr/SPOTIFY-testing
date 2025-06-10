import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

import streamlit as st
from spotify.genres import Genres

st.set_page_config(page_title="Genres", page_icon="🎸")

st.title("🎸 Available Genres")

if st.button("Get Genres"):
    try:
        genres = Genres().get_available_genre_seeds()
        
        if isinstance(genres, dict) and 'genres' in genres:
            genre_list = genres.get('genres', [])
            
            # Create columns for better visual organization
            cols = st.columns(3)
            for i, genre in enumerate(sorted(genre_list)):
                cols[i % 3].write(f"- {genre}")
            
            # Add a count at the bottom
            st.info(f"Total number of genres: {len(genre_list)}")
            
            # Add collapsible JSON section
            with st.expander("View Raw Genre Data"):
                st.json(genres)
        else:
            st.error(f"Unexpected response format: {genres}")
            
    except Exception as e:
        st.error(f"Error fetching genres: {str(e)}")
        st.error("Please check your Spotify API credentials in config.ini")

st.info("""
These are Spotify's available genre seeds that can be used for recommendations. 
Each genre represents a specific style or category of music in Spotify's classification system.

If you're seeing an error, please make sure your Spotify API credentials are properly configured in the config.ini file.
""")
