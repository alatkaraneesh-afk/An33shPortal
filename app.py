import streamlit as st

st.set_page_config(page_title="Educational Research Portal", page_icon="📚")

st.title("Resource Gateway")
st.write("If local modules are intercepted, use the encrypted cloud gateways below.")

# These are "Proxies" or "Embedders" that often bypass iboss 
# because they tunnel the traffic through a different domain.

col1, col2 = st.columns(2)

with col1:
    st.subheader("Gateway A (Recommended)")
    # Using Google Translate as a Proxy - it's hard for schools to block
    target_url = "https://github.io"
    proxy_url = f"https://google.com{target_url}"
    st.link_button("🌐 Open via Google Cloud", proxy_url)

with col2:
    st.subheader("Gateway B (Stealth)")
    # Using a known "unblockable" GitHub mirror
    st.link_button("🚀 Open via Mirror", "https://miroware.io")

st.info("""
**The Strategy:** 
We aren't running the code on your PC anymore. We are asking **Google Translate** to fetch the game for us. 
1. Click 'Gateway A'.
2. If it asks to translate, just click 'Original'.
3. iboss will only see 'google.com' traffic, not 'game' traffic.
""")
import streamlit as st
import os

st.set_page_config(page_title="Project Archive", page_icon="📁")

st.title("Project File Downloader")
st.write("If the preview is blocked, download the source file to run it locally.")

game_dir = "static/slope"
if os.path.exists(game_dir):
    all_files = sorted([f for f in os.listdir(game_dir) if f.endswith(".html")])
    selected = st.selectbox("Select Project File:", all_files)

    file_path = os.path.join(game_dir, selected)
    
    with open(file_path, "rb") as f:
        file_data = f.read()
    
    # This button forces the browser to download the file instead of opening it
    st.download_button(
        label=f"📥 DOWNLOAD {selected.upper()}",
        data=file_data,
        file_name=f"Project_{selected}",
        mime="text/html"
    )

    st.info("""
    **HOW TO RUN:**
    1. Click the **Download** button above.
    2. Go to your computer's **Downloads** folder.
    3. Right-click the file and 'Open with' Chrome or Firefox.
    4. Since the file is on your PC, iBoss cannot block the connection!
    """)
else:
    st.error("Technical Error: Storage directory not found.")
import streamlit as st
import os
import base64

# Use a totally boring name to stay under the radar
st.set_page_config(page_title="Data Research Tool v4", page_icon="📊")

st.title("Project Analysis Dashboard")

game_dir = "static/slope"
if os.path.exists(game_dir):
    files = sorted([f for f in os.listdir(game_dir) if f.endswith(".html")])
    selected = st.selectbox("Select Data Module:", files)

    # Load the game code
    file_path = os.path.join(game_dir, selected)
    with open(file_path, "r", encoding="utf-8") as f:
        # Step 1: Encode the game into Base64 (Scrambles the code)
        scrambled_data = base64.b64encode(f.read().encode()).decode()

    # Step 2: The JS 'Unscrambler'
    # This runs inside the browser, so iBoss can't see what's happening
    js_code = f"""
    <div style="text-align: center;">
        <button id="launchBtn" onclick="unscrambleAndLaunch()" style="
            width: 100%; height: 60px; background-color: #34a853; 
            color: white; border: none; border-radius: 12px; 
            font-size: 18px; font-weight: bold; cursor: pointer;">
            ✅ DECODE & OPEN MODULE
        </button>
    </div>

    <script>
    function unscrambleAndLaunch() {{
        const secretData = "{scrambled_data}";
        
        // Convert scrambled string back into a real file in RAM
        const decoded = atob(secretData);
        const blob = new Blob([decoded], {{type: 'text/html'}});
        const blobUrl = URL.createObjectURL(blob);
        
        // Open the new tab
        const newTab = window.open();
        if (newTab) {{
            newTab.location.href = blobUrl;
        }} else {{
            alert("Pop-up blocked! Click the icon in your address bar to 'Always Allow'.");
        }}
    }}
    </script>
    """
    st.components.v1.html(js_code, height=120)
else:
    st.error("Error: Resource path not found.")
