import streamlit as st
import os

# 1. Update browser tab title and icon
st.set_page_config(page_title="GAME HUB", page_icon="🎮", layout="wide")

# 2. Main titles and your custom description
st.title("GAME HUB 🕹️")
st.markdown("### Your boy noticed iboss is getting a little crazy. Here, take these games, more will come!")
st.write("---")

# 3. Path to your game folder
game_dir = "static/slope"

if os.path.exists(game_dir):
    # Find all .html games (filtering out placeholder)
    all_files = sorted([f for f in os.listdir(game_dir) if f.endswith(".html") and f != "placeholder.txt"])
    
    if not all_files:
        st.warning("No games found. Add some .html files to the folder!")
    else:
        # Search bar for the boys
        query = st.text_input("🔍 Search for a game:", "")
        
        # Display in a clean list
        for file_name in all_files:
            if query.lower() in file_name.lower():
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
                            key=file_name
                        )
                st.write("---")
else:
    st.error("Error: 'static/slope' directory not found.")

st.caption("Instructions: Download and open the file from your computer. Turn off Wi-Fi if iBoss tries to block the local screen.")
