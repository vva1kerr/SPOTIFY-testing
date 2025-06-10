import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

import streamlit as st
from spotify.search import Search

st.set_page_config(page_title="Search", page_icon="🔍")

st.title("🔍 Search Spotify")

query = st.text_input("Enter search term")
search_type = st.selectbox(
    "Search type",
    ["track", "artist", "album"]
)

if st.button("Search") and query:
    try:
        results = Search().search(query, type=search_type)
        
        if isinstance(results, dict):
            items = results.get(f"{search_type}s", {}).get("items", [])
            
            for item in items:
                st.write("---")
                st.write(f"**Name:** {item.get('name')}")
                st.write(f"**ID:** {item.get('id')}")
                
                if search_type in ["album", "artist"]:
                    images = item.get('images', [])
                    if images:
                        st.image(images[0].get('url'), width=200)
                
                if search_type == "track":
                    st.write(f"**Artist:** {item.get('artists', [{}])[0].get('name')}")
                    st.write(f"**Album:** {item.get('album', {}).get('name')}")
                elif search_type == "artist":
                    st.write(f"**Followers:** {item.get('followers', {}).get('total'):,}")
                    st.write(f"**Genres:** {', '.join(item.get('genres', ['N/A']))}")
                elif search_type == "album":
                    st.write(f"**Artist:** {item.get('artists', [{}])[0].get('name')}")
                    st.write(f"**Release Date:** {item.get('release_date')}")
            
            # Add collapsible JSON section
            with st.expander("View Raw Search Results"):
                st.json(results)
            
    except Exception as e:
        st.error(f"Error performing search: {str(e)}")
