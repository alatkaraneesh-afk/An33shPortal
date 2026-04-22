import streamlit as st
import os
import base64

# 1. Page Config
st.set_page_config(page_title="GAME HUB", page_icon="🎮", layout="wide")

# 2. Header & Your Description
st.title("AN33SHPORTAL: GAME HUB")
st.markdown("### Your boy noticed iboss is getting a little crazy. Here, take these 300+ games, more will come! (REMEMBER TO KEEP THE URL BOX BLANK IF YOU WANT THIS SITE TO STAY UP!)")
st.write("---")

game_dir = "static/slope"

if os.path.exists(game_dir):
    # This automatically finds ALL your new games (fnaf, tinyfishing, chess, etc.)
    all_files = sorted([f for f in os.listdir(game_dir) if f.endswith(".html") and f != "placeholder.txt"])
    
    if all_files:
        # Search bar for the boys to find specific games
        query = st.text_input("🔍 Search for a game:", key="main_search").lower()
        st.write("---")
        
        # Grid layout: 3 games per row
        cols = st.columns(3)
        
        count = 0
        for i, file_name in enumerate(all_files):
            # Clean up the name for display (e.g. 'tinyfishing.html' -> 'Tinyfishing')
            display_name = file_name.replace(".html", "").replace("_", " ").replace("-", " ").title()
            
            # Filter based on search query
            if query in display_name.lower():
                with cols[count % 3]:
                    st.subheader(display_name)
                    
                    # Load file data
                    file_path = os.path.join(game_dir, file_name)
                    with open(file_path, "rb") as f:
                        file_bytes = f.read()
                    
                    # --- AUTO LAUNCHER (BLOB) ---
                    b64_content = base64.b64encode(file_bytes).decode()
                    func_id = f"launch_{i}"
                    js_code = f"""
                    <script>
                    function {func_id}() {{
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
                    <button onclick="{func_id}()" style="width:100%; height:40px; background-color:#1a73e8; color:white; border:none; border-radius:8px; cursor:pointer; font-weight:bold; margin-bottom:5px;">
                        🚀 AUTO-LAUNCH
                    </button>
                    """
                    st.components.v1.html(js_code, height=50)

                    # --- SECURE DOWNLOAD ---
                    st.download_button(
                        label="📥 DOWNLOAD",
                        data=file_bytes,
                        file_name=file_name,
                        mime="text/html",
                        key=f"dl_{i}"
                    )
                    st.write("---")
                    count += 1
    else:
        st.warning("No games found. Make sure they are in static/slope/")
else:
    st.error("Error: Folder 'static/slope' not found.")

st.caption("Pro-tip: Use Auto-Launch first. If iBoss blocks the new tab, use Download and open it from your computer!")
