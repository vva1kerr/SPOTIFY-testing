import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

import streamlit as st
from spotify.tracks import Tracks

st.set_page_config(page_title="Tracks", page_icon="🎼")

st.title("🎼 Track Explorer")

col1, col2 = st.columns([2,1])

with col1:
    track_id = st.text_input(
        "Enter Track ID",
        placeholder="e.g., 5QO79kh1waicV47BqGRL3g",
        help="You can find a track's ID in its Spotify URL"
    )

    if st.button("Get Track Info") and track_id:
        try:
            track_info = Tracks().get_track(track_id)
            
            if isinstance(track_info, dict):
                st.subheader(track_info.get('name', 'Unknown Track'))
                st.write(f"**Artist:** {track_info.get('artists', [{}])[0].get('name', 'Unknown Artist')}")
                st.write(f"**Album:** {track_info.get('album', {}).get('name', 'Unknown Album')}")
                
                duration_ms = track_info.get('duration_ms', 0)
                duration_min = duration_ms // 60000
                duration_sec = (duration_ms % 60000) // 1000
                st.write(f"**Duration:** {duration_min}:{duration_sec:02d}")
                
                st.write(f"**Popularity:** {track_info.get('popularity', 'N/A')}/100")
                
                if track_info.get('album', {}).get('images'):
                    st.image(track_info['album']['images'][0]['url'], width=300)
                
                # Add collapsible JSON section
                with st.expander("View Raw Track Data"):
                    st.json(track_info)

        except Exception as e:
            st.error(f"Error fetching track data: {str(e)}")

with col2:
    st.info("""
    **How to find a Track ID:**
    1. Go to the track's Spotify page
    2. Click 'Share'
    3. Copy Spotify URI
    4. The ID is the string after 'track:'
    """)
