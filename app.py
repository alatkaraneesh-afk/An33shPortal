import streamlit as st
import os
import base64

# 1. Page Config
st.set_page_config(page_title="GAME HUB", page_icon="🫡", layout="wide")

# 2. Header & Your Description
st.title("AN33SHPOTAL: GAME HUB 🕹️")
st.markdown("### Your boy noticed iboss is getting a little crazy. Here, take these games, more will come!")
st.write("---")

game_dir = "static/slope"

if os.path.exists(game_dir):
    # Get all .html games
    all_files = sorted([f for f in os.listdir(game_dir) if f.endswith(".html") and f != "placeholder.txt"])
    
    if all_files:
        # Unique key for search bar
        query = st.text_input("🔍 Search for a game:", key="main_search_input").lower()
        st.write("---")
        
        # Counter to ensure every button has a unique ID
        for i, file_name in enumerate(all_files):
            display_name = file_name.replace(".html", "").replace("_", " ").replace("-", " ").title()
            
            # Filter logic
            if query in display_name.lower():
                col1, col2, col3 = st.columns([2, 1, 1])
                
                with col1:
                    st.subheader(display_name)
                
                # Load file data
                file_path = os.path.join(game_dir, file_name)
                with open(file_path, "rb") as f:
                    file_bytes = f.read()
                
                with col2:
                    # --- AUTO LAUNCHER ---
                    b64_content = base64.b64encode(file_bytes).decode()
                    # Creating a unique function name for every game to prevent JS conflicts
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
                    <button onclick="{func_id}()" style="width:100%; height:45px; background-color:#1a73e8; color:white; border:none; border-radius:8px; cursor:pointer; font-weight:bold;">
                        🚀 AUTO-LAUNCH
                    </button>
                    """
                    st.components.v1.html(js_code, height=60)

                with col3:
                    # --- SECURE DOWNLOAD ---
                    # Using the index 'i' to ensure the key is always unique
                    st.download_button(
                        label="📥 DOWNLOAD",
                        data=file_bytes,
                        file_name=file_name,
                        mime="text/html",
                        key=f"btn_dl_{i}"
                    )
                st.write("---")
    else:
        st.warning("Upload some .html files to static/slope/ on GitHub to see them here!")
else:
    st.error("Error: 'static/slope' directory not found.")

st.caption("Pro-tip: Use Auto-Launch first. If iBoss blocks the new tab, use Download and open it from your computer!")
