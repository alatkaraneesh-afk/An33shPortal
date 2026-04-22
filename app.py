import streamlit as st

st.set_page_config(page_title="An33shPortal", page_icon="🎮")

st.title("An33shPortal 🕹️")

# We are hard-coding 1v1.lol to see if we can get it to work first
st.subheader("Featured Game: 1v1.LOL")

# This link points directly to your static file on the Streamlit server
# It opens in a new tab to bypass the "Refused to Connect" iframe error
st.markdown("""
    <a href="app/static/slope/1v1-lol.html" target="_blank">
        <button style="
            width:100%; 
            height:60px; 
            background-color:#00ff00; 
            color:black; 
            border:none; 
            border-radius:15px; 
            cursor:pointer; 
            font-weight:bold;
            font-size:20px;">
            🚀 PLAY 1V1.LOL (DIRECT)
        </button>
    </a>
""", unsafe_allow_html=True)

st.write("---")
st.write("### All Other Games")
# Simple dropdown for everything else
game_choice = st.selectbox("Select another game:", ["slope3.html", "subway-surfers.html", "retro-bowl.html"])
st.link_button(f"Launch {game_choice}", f"app/static/slope/{game_choice}")
import streamlit as st
import os

st.set_page_config(page_title="An33shPortal", page_icon="🎮")
st.title("An33shPortal 🕹️")

game_dir = "static/slope"
if os.path.exists(game_dir):
    all_files = sorted([f for f in os.listdir(game_dir) if f.endswith(".html")])
    selected_game = st.selectbox("Choose your game:", all_files)

    if st.button("🚀 UNBLOCK & PLAY"):
        file_path = os.path.join(game_dir, selected_game)
        
        with open(file_path, "r", encoding="utf-8") as f:
            html_content = f.read()

        # This JS trick creates a "Blob" in memory.
        # It's much harder for iBoss to track because it has no fixed URL.
        js_code = f"""
            <script>
            function launchGame() {{
                const gameCode = `{html_content.replace('`', '\\`').replace('$', '\\$')}`;
                const blob = new Blob([gameCode], {{ type: 'text/html' }});
                const url = URL.createObjectURL(blob);
                window.open(url, '_blank');
            }}
            </script>
            <button onclick="launchGame()" style="
                width:100%; 
                height:50px; 
                background-color:#ff4b4b; 
                color:white; 
                border:none; 
                border-radius:10px; 
                cursor:pointer; 
                font-weight:bold;
                font-size:16px;">
                👉 CLICK TO LAUNCH (BLOB MODE)
            </button>
        """
        st.components.v1.html(js_code, height=60)
        st.info("If the tab still closes, it means your school has 'Strict Mode' on. Try a simpler game like 'Snake' first.")
else:
    st.error("Folder 'static/slope' not found!")
