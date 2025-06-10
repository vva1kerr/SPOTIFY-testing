import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

import streamlit as st
from spotify.albums import Albums

st.set_page_config(page_title="Albums", page_icon="💿")

st.title("💿 Album Explorer")

col1, col2 = st.columns([2,1])

with col1:
    album_id = st.text_input(
        "Enter Album ID",
        placeholder="e.g., 4aawyAB9vmqN3uQ7FjRGTy",
        help="You can find an album's ID in its Spotify URL"
    )

    if st.button("Get Album Info") and album_id:
        try:
            album_info = Albums().get_album(album_id)
            
            if isinstance(album_info, dict):
                if album_info.get('images'):
                    st.image(album_info['images'][0]['url'], width=300)
                
                st.subheader(album_info.get('name', 'Unknown Album'))
                st.write(f"**Artist:** {album_info.get('artists', [{}])[0].get('name', 'Unknown Artist')}")
                st.write(f"**Release Date:** {album_info.get('release_date', 'N/A')}")
                st.write(f"**Total Tracks:** {album_info.get('total_tracks', 0)}")
                
                # Display tracks
                st.subheader("Tracks")
                for idx, track in enumerate(album_info.get('tracks', {}).get('items', []), 1):
                    duration_ms = track.get('duration_ms', 0)
                    duration_min = duration_ms // 60000
                    duration_sec = (duration_ms % 60000) // 1000
                    st.write(f"{idx}. {track['name']} ({duration_min}:{duration_sec:02d})")
                
                # Add collapsible JSON section
                with st.expander("View Raw Album Data"):
                    st.json(album_info)

        except Exception as e:
            st.error(f"Error fetching album data: {str(e)}")

with col2:
    st.info("""
    **How to find an Album ID:**
    1. Go to the album's Spotify page
    2. Click 'Share'
    3. Copy Spotify URI
    4. The ID is the string after 'album:'
    """)
