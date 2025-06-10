import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

import streamlit as st
from spotify.artists import Artists

st.set_page_config(page_title="Artists", page_icon="🎤")

st.title("🎤 Artist Explorer")

col1, col2 = st.columns([2,1])

with col1:
    artist_id = st.text_input(
        "Enter Artist ID",
        placeholder="e.g., 1ukmGETCwXTbgrTrkRDnmn",
        help="You can find an artist's ID in their Spotify URL"
    )

    if st.button("Get Artist Info") and artist_id:
        try:
            artist_info = Artists().get_artist(artist_id)
            
            if isinstance(artist_info, dict):
                if artist_info.get('images'):
                    st.image(artist_info['images'][0]['url'], width=300)
                
                st.subheader(artist_info.get('name', 'Unknown Artist'))
                st.write(f"**Genres:** {', '.join(artist_info.get('genres', ['N/A']))}")
                st.write(f"**Followers:** {artist_info.get('followers', {}).get('total', 0):,}")
                st.write(f"**Popularity:** {artist_info.get('popularity', 'N/A')}/100")
                
                # Get top tracks
                top_tracks = Artists().get_artist_top_tracks(artist_id)
                if isinstance(top_tracks, dict) and 'tracks' in top_tracks:
                    st.subheader("Top Tracks")
                    for idx, track in enumerate(top_tracks['tracks'], 1):
                        st.write(f"{idx}. {track['name']} - {track.get('album', {}).get('name', 'Unknown Album')}")
                
                # Add collapsible JSON sections
                with st.expander("View Raw Artist Data"):
                    st.json(artist_info)
                
                if isinstance(top_tracks, dict):
                    with st.expander("View Raw Top Tracks Data"):
                        st.json(top_tracks)
        
        except Exception as e:
            st.error(f"Error fetching artist data: {str(e)}")

with col2:
    st.info("""
    **How to find an Artist ID:**
    1. Go to the artist's Spotify page
    2. Click 'Share'
    3. Copy Spotify URI
    4. The ID is the string after 'artist:'
    """)
