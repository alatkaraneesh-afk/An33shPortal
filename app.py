import streamlit as st
import os

# 1. Boring academic title to hide from manual inspection
st.set_page_config(page_title="Assignment Research Portal", page_icon="📖", layout="wide")

# Hide Streamlit UI elements that scream "This is an app!"
st.markdown("<style>#MainMenu {visibility: hidden;} footer {visibility: hidden;} .stDeployButton {display:none;}</style>", unsafe_allow_html=True)

if 'active_module' not in st.session_state:
    st.session_state.active_module = None

# --- PORTAL VIEW ---
if st.session_state.active_module is None:
    st.title("Resource Dashboard")
    st.info("Select a resource module below to begin your analysis.")
    
    game_dir = "static/slope"
    if os.path.exists(game_dir):
        # Scan for all games automatically
        files = sorted([f for f in os.listdir(game_dir) if f.endswith(".html")])
        
        # Grid layout for a professional look
        cols = st.columns(3)
        for i, file_name in enumerate(files):
            clean_name = file_name.replace(".html", "").replace("-", " ").title()
            with cols[i % 3]:
                if st.button(f"📄 Open {clean_name}", key=file_name):
                    st.session_state.active_module = file_name
                    st.rerun()
    else:
        st.error("Directory not found. Please ensure files are in 'static/slope/'")

# --- INJECTION VIEW (The "Unblockable" Part) ---
else:
    if st.button("⬅ Back to Dashboard"):
        st.session_state.active_module = None
        st.rerun()

    file_path = f"static/slope/{st.session_state.active_module}"
    
    # We read the file on the SERVER, not the browser.
    # iBoss cannot see this request because it's happening inside the Streamlit cloud.
    with open(file_path, 'r', encoding='utf-8') as f:
        raw_html = f.read()
    
    # Inject raw code directly into the page. 
    # No iframes = No "Refused to Connect" error.
    st.components.v1.html(raw_html, height=900, scrolling=True)
