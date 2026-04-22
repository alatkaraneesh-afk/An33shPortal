import streamlit as st
import os
import base64

# Academic title to hide from manual inspection
st.set_page_config(page_title="Math Study Portal", page_icon="📚")

st.title("Resource Dashboard: Section 4")
st.write("---")

# The path to your NEW pure file
game_path = "static/slope/slopeoffline.html"

if os.path.exists(game_path):
    with open(game_path, "r", encoding="utf-8") as f:
        # This scrambles the game code into random letters (Base64)
        # This is the "Cloak" that hides it from iBoss
        b64_data = base64.b64encode(f.read().encode()).decode()
    
    # This button launches the game in your RAM (no external connection)
    st.markdown(f"""
        <a href="data:text/html;base64,{b64_data}" target="_blank" style="text-decoration:none;">
            <div style="
                padding:20px;
                background-color:#1a73e8;
                color:white;
                text-align:center;
                border-radius:12px;
                font-weight:bold;
                cursor:pointer;
                box-shadow: 0px 4px 10px rgba(0,0,0,0.3);">
                ✅ ACCESS AUTHORIZED MODULE
            </div>
        </a>
    """, unsafe_allow_html=True)
    
    st.caption("Note: If the tab opens but is blank, check the address bar for 'Pop-up Blocked'.")

else:
    st.error(f"Technical Error: {game_path} not found.")
    st.info("Check your GitHub folder names. It must be 'static/slope/slopeoffline.html'")
