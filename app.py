import streamlit as st
import os
import base64

st.set_page_config(page_title="An33shPortal", page_icon="🎮")

st.title("An33shPortal 🕹️")

# 1. Get the list of games
game_dir = "static/slope"
if os.path.exists(game_dir):
    all_files = sorted([f for f in os.listdir(game_dir) if f.endswith(".html")])
    selected_game = st.selectbox("Choose your game:", all_files)

    if st.button("🚀 UNBLOCK & PLAY"):
        file_path = os.path.join(game_dir, selected_game)
        
        # Read the local game file
        with open(file_path, "r", encoding="utf-8") as f:
            html_content = f.read()
        
        # Encode the HTML into Base64 (this hides the code from iBoss)
        b64 = base64.b64encode(html_content.encode()).decode()
        
        # Create a "Data URL"
        # This tells the browser: "Open this raw code as a webpage"
        href = f"data:text/html;base64,{b64}"
        
        st.success(f"Game '{selected_game}' is ready!")
        st.markdown(f'<a href="{href}" target="_blank" style="text-decoration:none;"><button style="width:100%; height:50px; background-color:#ff4b4b; color:white; border:none; border-radius:10px; cursor:pointer; font-weight:bold;">👉 CLICK HERE TO LAUNCH UNBLOCKED</button></a>', unsafe_allow_html=True)
        
        st.info("Note: This opens the game in a new tab using 'Data Encoding' to bypass the iBoss filter.")
else:
    st.error("Folder 'static/slope' not found!")
