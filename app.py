import streamlit as st
import os

st.set_page_config(page_title="An33shPortal", page_icon="🎮", layout="wide")

st.title("An33shPortal 🕹️")

game_dir = "static/slope"
all_files = [f for f in os.listdir(game_dir) if f.endswith(".html")]
selected_game = st.selectbox("Select Game", sorted(all_files))

if st.button("🚀 GO"):
    file_path = os.path.join(game_dir, selected_game)
    
    # READ the file locally so it's not a 'request' iBoss can see
    with open(file_path, 'r', encoding='utf-8') as f:
        game_html = f.read()
    
    # Use components.html to inject the raw code directly
    # This avoids using a 'src' URL that filters hate
    st.components.v1.html(game_html, height=800, scrolling=True)

st.caption("Tip: If a game fails, try a simple one like 'snake.html' to see if it's a code block.")
