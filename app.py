import streamlit as st
import os

# Set the page title and icon
st.set_page_config(page_title="An33shPortal:Game downloader", page_icon="😈", layout="wide")

st.title("An33shPortal:Game downloader")
st.write("---")

# Path to your game shelf
game_dir = "static/slope"

if os.path.exists(game_dir):
    # Find all .html files and ignore the placeholder
    all_files = sorted([f for f in os.listdir(game_dir) if f.endswith(".html")])
    
    if not all_files:
        st.warning("No games found in the directory.")
    else:
        # Search bar for quick navigation
        query = st.text_input("🔍 Search for a game:", "")
        
        # Filter games based on search
        filtered_files = [f for f in all_files if query.lower() in f.lower()]
        
        st.write(f"Showing {len(filtered_files)} games")
        st.write("---")

        # Display games in a clean list with download buttons
        for file_name in filtered_files:
            # Clean up the name for display (e.g. 'mini_car_game.html' -> 'Mini Car Game')
            display_name = file_name.replace(".html", "").replace("_", " ").replace("-", " ").title()
            
            col1, col2 = st.columns([3, 1])
            
            with col1:
                st.subheader(display_name)
            
            with col2:
                file_path = os.path.join(game_dir, file_name)
                with open(file_path, "rb") as f:
                    st.download_button(
                        label="📥 DOWNLOAD",
                        data=f,
                        file_name=file_name,
                        mime="text/html",
                        key=file_name  # Unique key for Streamlit
                    )
            st.write("---")
else:
    st.error("Error: 'static/slope' directory not found.")
    st.info("Ensure your files are uploaded to the correct folder on GitHub.")

st.caption("Instructions: Download the file and open it locally. Turn off Wi-Fi if the screen is intercepted.")
