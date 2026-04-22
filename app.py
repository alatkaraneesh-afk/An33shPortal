import streamlit as st
import os
import base64

# 1. Page Config
st.set_page_config(page_title="AN33SHPORTAL: GAME HUB", page_icon="🤫", layout="wide")

# 2. Header & Your Description
st.title("GAME HUB 🕹️")
st.markdown("### Your boy noticed iboss is getting a little crazy. Here, take these games, more will come!")
st.write("---")

game_dir = "static/slope"

if os.path.exists(game_dir):
    all_files = sorted([f for f in os.listdir(game_dir) if f.endswith(".html") and f != "placeholder.txt"])
    
    if all_files:
        query = st.text_input("🔍 Search for a game:", key="main_search").lower()
        st.write("---")
        
        cols = st.columns(3)
        count = 0
        for i, file_name in enumerate(all_files):
            display_name = file_name.replace(".html", "").replace("_", " ").replace("-", " ").title()
            
            if query in display_name.lower():
                with cols[count % 3]:
                    st.subheader(display_name)
                    
                    file_path = os.path.join(game_dir, file_name)
                    with open(file_path, "rb") as f:
                        file_bytes = f.read()
                    
                    # --- AUTO LAUNCHER (ABOUT:BLANK STEALTH) ---
                    # We escape the code properly so it doesn't break the JS injection
                    b64_content = base64.b64encode(file_bytes).decode()
                    func_id = f"launch_{i}"
                    js_code = f"""
                    <script>
                    function {func_id}() {{
                        var win = window.open("about:blank", "_blank");
                        if (win) {{
                            const b64 = "{b64_content}";
                            const html = atob(b64);
                            win.document.write(html);
                            win.document.close();
                        }} else {{
                            alert("Pop-up blocked! Please allow pop-ups for this site.");
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

st.caption("Pro-tip: Auto-Launch opens in 'about:blank' for extra stealth. If it still blocks, just Download.")
