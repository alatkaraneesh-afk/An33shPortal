import streamlit as st
import os
import base64

# 1. Page Config
st.set_page_config(page_title="GAME HUB", page_icon="🎮", layout="wide")

# 2. Header & Your Description
st.title("AN33SHPORTAL: GAME HUB 🕹️")
st.markdown("### Your boy noticed iboss is getting a little crazy. Here, take these games, more will come!")
st.write("---")

game_dir = "static/slope"

if os.path.exists(game_dir):
    all_files = sorted([f for f in os.listdir(game_dir) if f.endswith(".html") and f != "placeholder.txt"])
    
    query = st.text_input("🔍 Search for a game:", "")
    
    for file_name in all_files:
        if query.lower() in file_name.lower():
            display_name = file_name.replace(".html", "").replace("_", " ").replace("-", " ").title()
            
            # Read the file for both methods
            file_path = os.path.join(game_dir, file_name)
            
            # Binary for download
            with open(file_path, "rb") as f:
                binary_data = f.read()
            
            # Text for Auto-Launcher (Encoding it to hide from iBoss)
            try:
                b64_content = base64.b64encode(binary_data).decode()
            except:
                continue

            col1, col2, col3 = st.columns([2, 1, 1])
            
            with col1:
                st.subheader(display_name)
                
            with col2:
                # --- THE AUTO LAUNCHER (BLOB METHOD) ---
                js_code = f"""
                <script>
                function launch() {{
                    const b64 = "{b64_content}";
                    const byteCharacters = atob(b64);
                    const byteNumbers = new Array(byteCharacters.length);
                    for (let i = 0; i < byteCharacters.length; i++) {{
                        byteNumbers[i] = byteCharacters.charCodeAt(i);
                    }}
                    const byteArray = new Uint8Array(byteNumbers);
                    const blob = new Blob([byteArray], {{type: 'text/html'}});
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
                # --- THE SECURE DOWNLOAD ---
                st.download_button(
                    label="📥 DOWNLOAD",
                    data=binary_data,
                    file_name=file_name,
                    mime="text/html",
                    key=f"dl_{file_name}"
                )
            st.write("---")
else:
    st.error("Error: Folder 'static/slope' not found.")

st.caption("Pro-tip: Use Auto-Launch first. If iBoss blocks the new tab, use Download and open it from your computer!")
import streamlit as st
import os

# 1. Update browser tab title and icon
st.set_page_config(page_title="GAME HUB", page_icon="🎮", layout="wide")

# 2. Main titles and your custom description
st.title("GAME HUB 🕹️")
st.markdown("### Your boy noticed iboss is getting a little crazy. Here, take these games, more will come!")
st.write("---")

# 3. Path to your game folder
game_dir = "static/slope"

if os.path.exists(game_dir):
    # Find all .html games (filtering out placeholder)
    all_files = sorted([f for f in os.listdir(game_dir) if f.endswith(".html") and f != "placeholder.txt"])
    
    if not all_files:
        st.warning("No games found. Add some .html files to the folder!")
    else:
        # Search bar for the boys
        query = st.text_input("🔍 Search for a game:", "")
        
        # Display in a clean list
        for file_name in all_files:
            if query.lower() in file_name.lower():
                display_name = file_name.replace(".html", "").replace("_", " ").replace("-", " ").title()
                
                col1, col2 = st.columns([3, 1])
                
                with col1:
                    st.subheader(display_name)
                
                with col2:
                    file_path = os.path.join(game_dir, file_name)
                    with open(file_path, "rb") as f:
                        st.download_button(
                            label="📥 DOWNLOAD",
                            data=f,
                            file_name=file_name,
                            mime="text/html",
                            key=file_name
                        )
                st.write("---")
else:
    st.error("Error: 'static/slope' directory not found.")

st.caption("Instructions: Download and open the file from your computer. Turn off Wi-Fi if iBoss tries to block the local screen.")
