import streamlit as st
import os
import base64

# 1. Page Config
st.set_page_config(page_title="GAME HUB", page_icon="🐦‍🔥", layout="wide")

# 2. Header & Your Description
st.title("AN33SHPORTAL: GAME HUB 🐦‍🔥")
st.markdown("### Your boy noticed iboss is getting a little crazy. Here, take these 300+ games, more will come! (KEEP THE URL BOX EMPTY, IBOSS IS SNEAKY!")
st.write("---")

# 3. CACHING (This keeps the site fast by remembering game data)
@st.cache_data
def get_game_data(file_path):
    with open(file_path, "rb") as f:
        data = f.read()
    # Scramble to Base64 once and save in memory
    b64 = base64.b64encode(data).decode()
    return data, b64

game_dir = "static/slope"

if os.path.exists(game_dir):
    # Automatically find all your .html games
    all_files = sorted([f for f in os.listdir(game_dir) if f.endswith(".html") and f != "placeholder.txt"])
    
    if all_files:
        # Search bar
        query = st.text_input("🔍 Search for a game:", key="main_search").lower()
        st.write("---")
        
        # Grid layout: 3 games per row
        cols = st.columns(3)
        count = 0
        
        for i, file_name in enumerate(all_files):
            display_name = file_name.replace(".html", "").replace("_", " ").replace("-", " ").title()
            
            if query in display_name.lower():
                with cols[count % 3]:
                    st.subheader(display_name)
                    
                    # Use the fast cached data
                    binary_data, b64_content = get_game_data(os.path.join(game_dir, file_name))
                    
                    # --- AUTO LAUNCHER (ABOUT:BLANK STEALTH) ---
                    func_id = f"launch_{i}"
                    js_code = f"""
                    <script>
                    function {func_id}() {{
                        var win = window.open("about:blank", "_blank");
                        if (win) {{
                            const html = atob("{b64_content}");
                            win.document.write(html);
                            win.document.close();
                        }} else {{
                            alert("Pop-up blocked! Allow pop-ups to launch.");
                        }}
                    }}
                    </script>
                    <button onclick="{func_id}()" style="width:100%; height:40px; background-color:#1a73e8; color:white; border:none; border-radius:8px; cursor:pointer; font-weight:bold; margin-bottom:5px;">
                        🚀 AUTO-LAUNCH
                    </button>
                    """
                    st.components.v1.html(js_code, height=50)

                    # --- SECURE DOWNLOAD ---
                    st.download_button(
                        label="📥 DOWNLOAD",
                        data=binary_data,
                        file_name=file_name,
                        mime="text/html",
                        key=f"dl_{i}"
                    )
                    st.write("---")
                    count += 1
    else:
        st.warning("No games found in static/slope/")
else:
    st.error("Error: Folder 'static/slope' not found.")

st.caption("Pro-tip: Auto-Launch uses 'about:blank' for stealth. Use Download if the launcher fails.")
