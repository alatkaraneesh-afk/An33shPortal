import streamlit as st
import os

st.title("Project Research Hub")

# We use an Iframe with the 'Sandbox' attribute.
# This prevents the game from 'talking' to the internet.
# If it can't talk to the internet, iBoss can't see what it's doing.

game_file = "static/slope/slope3.html" # Change this to your main game

if st.button("🚀 Launch Stealth Module"):
    with open(game_file, 'r', encoding='utf-8') as f:
        code = f.read()
    
    # The 'sandbox' attribute is the key. 
    # 'allow-scripts' lets the game run.
    # We DO NOT add 'allow-same-origin', which stops it from talking to the web.
    st.components.v1.html(code, height=700, scrolling=True)

st.info("This version runs the game in a 'Sandbox' so it can't call home to game servers.")
