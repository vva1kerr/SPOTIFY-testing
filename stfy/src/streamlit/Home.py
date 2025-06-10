import streamlit as st

st.set_page_config(
    page_title="Spotify Explorer",
    page_icon="🎵",
    layout="wide"
)

st.title("🎵 Spotify Data Explorer")
st.markdown("""
Welcome to the Spotify Data Explorer! This application allows you to explore:
- 🎤 Artists: Look up artist information, popularity, and top tracks
- 💿 Albums: Explore album details and track listings
- 🎼 Tracks: Get detailed information about specific songs
- 🔍 Search: Find artists, albums, and tracks across Spotify
- 🎸 Genres: Browse Spotify's available music genres

Select a page from the sidebar to get started!

### How to Use IDs
Most pages require Spotify IDs. You can find these by:
1. Going to the item's page in Spotify
2. Clicking 'Share'
3. Copying the Spotify URI
4. The ID is the string after 'artist:', 'album:', or 'track:'
""")

st.sidebar.success("Select a page above.")
