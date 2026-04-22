import streamlit as st
import os

# Boring title to avoid teacher attention
st.set_page_config(page_title="Academic Resource Portal", page_icon="📝")

st.title("Resource Dashboard: Section 4")

game_dir = "static/slope"
if os.path.exists(game_dir):
    all_files = sorted([f for f in os.listdir(game_dir) if f.endswith(".html")])
    selected = st.selectbox("Select Module to Review:", all_files)

    file_path = os.path.join(game_dir, selected)
    with open(file_path, "r", encoding="utf-8") as f:
        # We escape the code so it doesn't break the JavaScript
        html_content = f.read().replace('`', '\\`').replace('$', '\\$')

    # This script 'smuggles' the game as a Blob
    js_code = f"""
    <script>
    function launchStealth() {{
        const code = `{html_content}`;
        const blob = new Blob([code], {{ type: 'text/html' }});
        const url = URL.createObjectURL(blob);
        const win = window.open(url, '_blank');
        if (!win) {{
            alert("Please allow pop-ups for this site to launch the module!");
        }}
    }}
    </script>
    <button onclick="launchStealth()" style="
        width: 100%; 
        height: 60px; 
        background-color: #2e7d32; 
        color: white; 
        border: none; 
        border-radius: 12px; 
        font-size: 18px; 
        font-weight: bold; 
        cursor: pointer;
        box-shadow: 0px 4px 15px rgba(0,0,0,0.2);">
        🚀 AUTHORIZE & OPEN MODULE
    </button>
    """
    st.components.v1.html(js_code, height=100)
    st.caption("Tip: If nothing happens, check the address bar for a 'Pop-up Blocked' icon and click 'Always Allow'.")
else:
    st.error("Technical Error: Directory not found.")
