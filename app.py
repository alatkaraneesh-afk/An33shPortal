import streamlit as st
import os
import base64

# Use an academic title to avoid manual teacher inspection
st.set_page_config(page_title="Data Visualization Portal", page_icon="📊")

st.title("Project Analysis Dashboard")

# 1. Path to your 'shelf'
game_dir = "static/slope"

if os.path.exists(game_dir):
    # Find all .html files
    all_files = sorted([f for f in os.listdir(game_dir) if f.endswith(".html")])
    selected = st.selectbox("Select Research Module:", all_files)

    if st.button("🚀 UNBLOCK & LAUNCH"):
        file_path = os.path.join(game_dir, selected)
        
        # Read the file on the SERVER (hidden from iBoss)
        with open(file_path, "r", encoding="utf-8") as f:
            html_content = f.read()

        # Convert to Base64 (Scrambles the game code into random letters)
        b64 = base64.b64encode(html_content.encode()).decode()

        # This JS trick creates a 'Blob' URL in memory
        # iBoss cannot block this in advance because the URL is unique to you
        js_code = f"""
        <script>
        function launch() {{
            const code = atob("{b64}");
            const blob = new Blob([code], {{ type: 'text/html' }});
            const url = URL.createObjectURL(blob);
            window.open(url, '_blank');
        }}
        </script>
        <button onclick="launch()" style="
            width: 100%; height: 60px; background-color: #1a73e8; 
            color: white; border: none; border-radius: 10px; 
            font-size: 18px; font-weight: bold; cursor: pointer;">
            👉 CLICK TO VIEW AUTHORIZED MODULE
        </button>
        """
        st.components.v1.html(js_code, height=100)
else:
    st.error("Technical Error: Storage directory not found.")
