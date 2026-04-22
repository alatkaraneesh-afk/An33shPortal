import streamlit as st
import os
import base64

# Set the page title and icon
st.set_page_config(page_title="An33shPortal:Game downloader", page_icon="🎮", layout="wide")

st.title("An33shPortal: Game Hub")
st.write("---")

game_dir = "static/slope"

if os.path.exists(game_dir):
    all_files = sorted([f for f in os.listdir(game_dir) if f.endswith(".html")])
    
    query = st.text_input("🔍 Search for a game:", "")
    filtered_files = [f for f in all_files if query.lower() in f.lower()]
    
    for file_name in filtered_files:
        display_name = file_name.replace(".html", "").replace("_", " ").replace("-", " ").title()
        
        # Read the file data
        file_path = os.path.join(game_dir, file_name)
        with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
            html_content = f.read()
        
        with open(file_path, "rb") as f:
            binary_data = f.read()

        col1, col2, col3 = st.columns([2, 1, 1])
        
        with col1:
            st.subheader(display_name)
            
        with col2:
            # OPTION 1: AUTO-OPEN (The "Stealth Blob" method)
            b64 = base64.b64encode(html_content.encode()).decode()
            js_code = f"""
            <script>
            function launch() {{
                const code = atob("{b64}");
                const blob = new Blob([code], {{ type: 'text/html' }});
                const url = URL.createObjectURL(blob);
                window.open(url, '_blank');
            }}
            </script>
            <button onclick="launch()" style="width:100%; height:45px; background-color:#1a73e8; color:white; border:none; border-radius:8px; cursor:pointer; font-weight:bold;">
                🚀 AUTO-LAUNCH
            </button>
            """
            st.components.v1.html(js_code, height=60)
            
        with col3:
            # OPTION 2: THE UNBLOCKABLE DOWNLOAD (Backup)
            st.download_button(
                label="📥 DOWNLOAD",
                data=binary_data,
                file_name=file_name,
                mime="text/html",
                key=f"dl_{file_name}"
            )
        st.write("---")
else:
    st.error("Error: 'static/slope' directory not found.")

st.caption("If 'Auto-Launch' is blocked by iBoss, use the 'Download' button and open the file from your computer.")
