import streamlit as st
import os

st.set_page_config(page_title="An33shPortal", page_icon="🎮", layout="wide")

st.title("An33shPortal 🕹️")

# 1. Search and Game Selection
game_dir = "static/slope"
all_files = [f for f in os.listdir(game_dir) if f.endswith(".html") and f not in ["404.html", "index.html"]]
search_query = st.text_input("🔍 Search games...", "").lower()
filtered_games = sorted([f for f in all_files if search_query in f.lower()])

# 2. Pick a Game
selected_game_file = st.selectbox("Select a game to load:", filtered_games, format_func=lambda x: x.replace(".html", "").replace("-", " ").title())

# 3. THE STEALTH LOAD
if st.button("🚀 LAUNCH GAME"):
    # This path pulls the file directly from YOUR server
    game_path = f"app/static/slope/{selected_game_file}"
    
    st.markdown(f"**Now Playing:** {selected_game_file.replace('.html', '').title()}")
    
    # Using an iframe to keep the game 'trapped' inside your Streamlit domain
    # This prevents iBoss from seeing it as a separate game site
    st.components.v1.iframe(game_path, height=700, scrolling=True)

st.write("---")
st.caption("If 'Refused to Connect' appears, try a different game. Some games contain 'trackers' that iBoss hates.")
