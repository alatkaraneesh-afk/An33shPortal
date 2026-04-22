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
