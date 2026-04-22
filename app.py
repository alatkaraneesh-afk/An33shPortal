import streamlit as st
import os
import base64

st.set_page_config(page_title="Math Study Hub", page_icon="📈")
st.title("Resource Dashboard")

game_dir = "static/slope"
if os.path.exists(game_dir):
    all_files = sorted([f for f in os.listdir(game_dir) if f.endswith(".html")])
    selected = st.selectbox("Select Module:", all_files)

    file_path = os.path.join(game_dir, selected)
    with open(file_path, "r", encoding="utf-8") as f:
        # Encode to Base64 so the game code doesn't "leak" or break the JS
        game_b64 = base64.b64encode(f.read().encode()).decode()

    # This script decodes the Base64 and builds the game in a new tab
    js_code = f"""
    <div id="btn-container">
        <button onclick="launch()" style="
            width: 100%; height: 60px; background-color: #1a73e8; 
            color: white; border: none; border-radius: 10px; 
            font-size: 18px; font-weight: bold; cursor: pointer;">
            🚀 AUTHORIZE & OPEN MODULE
        </button>
    </div>

    <script>
    function launch() {{
        const b64 = "{game_b64}";
        const byteCharacters = atob(b64);
        const byteNumbers = new Array(byteCharacters.length);
        for (let i = 0; i < byteCharacters.length; i++) {{
            byteNumbers[i] = byteCharacters.charCodeAt(i);
        }}
        const byteArray = new Uint8Array(byteNumbers);
        const blob = new Blob([byteArray], {{type: 'text/html'}});
        const url = URL.createObjectURL(blob);
        
        const win = window.open();
        if (win) {{
            win.location.href = url;
        }} else {{
            alert("Please allow pop-ups for this site!");
        }}
    }}
    </script>
    """
    st.components.v1.html(js_code, height=100)
else:
    st.error("Directory not found.")
