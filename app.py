import streamlit as st
import os
import base64
import random
import time
from pathlib import Path
from streamlit_autorefresh import st_autorefresh

# --- 0. SECURITY CONFIG (KILL SWITCH FEATURES) ---
MAX_USERS = 15 
LATEST_UPDATE = "-An33sh"
GAME_DIR = "static/slope"
# The "bricked" state is handled by this variable. 
# Change to False and re-push to GitHub to manually reset.
SYSTEM_LOCKED = False 

# --- 1. USER TRACKING & AUTO-KILL ---
def get_active_users():
    session_dir = Path(".sessions")
    session_dir.mkdir(exist_ok=True)
    if 'user_id' not in st.session_state:
        st.session_state.user_id = str(random.randint(10000, 99999))
    Path(session_dir / f"{st.session_state.user_id}.lock").touch()
    current_time = time.time()
    for f in session_dir.glob("*.lock"):
        if current_time - f.stat().st_mtime > 15:
            try: f.unlink()
            except: pass
    return len(list(session_dir.glob("*.lock")))

active_now = get_active_users()

# THRESHOLD TRIGGER: Auto-locks if the portal gets too crowded/noisy
if active_now > MAX_USERS:
    SYSTEM_LOCKED = True

# THE REDIRECT: If locked, no code below this line ever runs.
if SYSTEM_LOCKED:
    st.markdown('<meta http-equiv="refresh" content="0; URL=https://google.com">', unsafe_allow_html=True)
    st.stop()

# --- 2. CACHED UTILITIES ---
@st.cache_data
def get_base64_game(file_path):
    with open(file_path, "rb") as f:
        return base64.b64encode(f.read()).decode()

def launch_game(file_name):
    path = os.path.join(GAME_DIR, file_name)
    b64 = get_base64_game(path)
    js_code = f"""<script>
    var w = window.parent.open('about:blank', '_blank');
    if(w) {{
        w.document.title = "Google Docs";
        w.document.write(atob("{b64}"));
        w.document.close();
    }}</script>"""
    st.components.v1.html(js_code, height=0)

# --- 3. SESSION & PAGE CONFIG ---
if 'stealth_mode' not in st.session_state: st.session_state.stealth_mode = True

if st.session_state.stealth_mode:
    st.set_page_config(page_title="Advanced Calculus - Module 4", page_icon="📝", layout="wide")
else:
    st.set_page_config(page_title="AN33SH PORTAL", page_icon="🐦‍🔥", layout="wide")

# --- 4. UI STYLE (STRICT STEALTH) ---
st.markdown("""
    <style>
    @import url('https://googleapis.com');
    html, body, [data-testid="stAppViewContainer"] { background: radial-gradient(circle at top right, #0a0a0c, #050505); font-family: 'Inter', sans-serif; color: #e0e0e0; }
    #MainMenu {visibility: hidden;} footer {visibility: hidden;}
    .stButton>button { width: 100%; border-radius: 12px; height: 3.5em; background: linear-gradient(135deg, #ff4b4b 0%, #7d0000 100%); color: white; font-weight: 800; text-transform: uppercase; }
    .spy-warning { color: #ff4b4b; font-weight: 900; font-size: 14px; text-align: center; border: 2px solid #ff4b4b; padding: 10px; border-radius: 10px; margin-bottom: 20px; }
    .user-badge { background:rgba(0,255,0,0.1); color:#00ff00; padding:5px 15px; border-radius:50px; font-size:12px; font-weight:bold; border:1px solid rgba(0,255,0,0.3); text-align:center; display:block; margin-bottom:20px; }
    </style>
    <script>
    /* EMERGENCY KEY BINDS */
    window.parent.document.title = "Advanced Calculus - Module 4";
    document.addEventListener('keydown', function(e) { 
        if (e.key === 'Escape') { window.location.replace("https://google.com"); }
    });
    </script>
""", unsafe_allow_html=True)

# --- 5. SIDEBAR (ADMIN & STEALTH) ---
with st.sidebar:
    if st.session_state.stealth_mode:
        st.title("📚 Course Materials")
        st.markdown("---")
        st.caption("• Primary Sources\n• Citation Guide\n• Module 4 PDF")
    else:
        st.markdown(f'<div class="user-badge">● {active_now} USERS ONLINE</div>', unsafe_allow_html=True)
        if st.button("🔔 DEVELOPER NOTIFICATIONS"):
            st.info(f"📢 MESSAGE FROM AN33SH:\n\n{LATEST_UPDATE}")
        st.write("---")
        st.markdown('<div class="spy-warning">IF YOU SUSPECT A TEACHER IS SPYING, PRESS THE BUTTON ON THE BOTTOM OR PRESS ALT+TAB.</div>', unsafe_allow_html=True)
        st.title("🛡️ Admin Controls")
        if st.button("🎲 FEELING LUCKY?"):
            if os.path.exists(GAME_DIR):
                files = [f for f in os.listdir(GAME_DIR) if f.endswith(".html")]
                if files: launch_game(random.choice(files))
        st.write("---")
        st.markdown('<a href="https://google.com" target="_self"><button style="width:100%; background:red; color:white; border-radius:10px; border:none; padding:12px; font-weight:bold;">⚠️ EMERGENCY EXIT</button></a>', unsafe_allow_html=True)
    
    # THE SECRET GHOST TOGGLE
    for _ in range(25): st.write("")
    if st.button(" ", key="ghost_btn"):
        st.session_state.stealth_mode = not st.session_state.stealth_mode
        st.rerun()

# --- 6. MAIN PORTAL ---
if st.session_state.stealth_mode:
    st.title("Module 4: Differential Equations")
    st.text_area("Notes", "Enter research data here...", height=400)
else:
    st_autorefresh(interval=5000, key="frequent_refresh")
    st.title("AN33SH PORTAL 🐦‍🔥")
    
    @st.fragment(run_every=15)
    def timed_caption():
        caps = ["Stay quiet, stay undetected.", "Your work is safe here.", "The only portal you'll ever need."]
        st.subheader(random.choice(caps))
    timed_caption()
    
    st.caption("SUGGESTIONS: https://forms.gle")

    tab1, tab2 = st.tabs(["🎮 GAMES", "🌐 PROXY"])
    with tab1:
        if os.path.exists(GAME_DIR):
            all_games = sorted([f for f in os.listdir(GAME_DIR) if f.endswith(".html")])
            query = st.text_input("🔍 Search...", placeholder="Type to filter...").lower()
            filtered = [f for f in all_games if query in f.lower()] if query else all_games
            
            display = filtered[:12] # Simplified for performance
            cols = st.columns(3)
            for i, file_name in enumerate(display):
                with cols[i % 3]:
                    with st.container(border=True):
                        st.subheader(file_name.replace(".html", "").replace("_", " ").title())
                        if st.button("PLAY", key=f"p_{file_name}"): launch_game(file_name)
    with tab2:
        st.markdown("### 🛰️ PROXY COMING SOON")
