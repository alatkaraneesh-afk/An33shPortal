import streamlit as st
import os
import base64
import random
import time
from pathlib import Path
from streamlit_autorefresh import st_autorefresh

# --- 0. SECURITY CONFIG ---
MAX_USERS = 15
LATEST_UPDATE = "Hey guys, Im working on making the site faster. In the meantime, you can play games like BitLife, Paperio2, and 2048. Stay stealthy! -An33sh"
GAME_DIR = "static/slope"
SOUND_DIR = "static/sounds"
LOGO_PATH = "static/slope/an33shlogo.jpg"
SYSTEM_LOCKED = False

# --- 1. USER TRACKING ---
def get_active_users():
    session_dir = Path(".sessions")
    session_dir.mkdir(exist_ok=True)
    if 'user_id' not in st.session_state:
        st.session_state.user_id = str(random.randint(10000, 99999))
    
    # Update timestamp file for this user
    user_file = session_dir / f"{st.session_state.user_id}.lock"
    user_file.touch()
    
    # Prune files older than 10 seconds for real-time accuracy
    current_time = time.time()
    for f in session_dir.glob("*.lock"):
        if current_time - f.stat().st_mtime > 10:
            try:
                f.unlink()
            except:
                pass
                
    # Return actual unique active files remaining
    return max(1, len(list(session_dir.glob("*.lock"))))

active_now = get_active_users()

# THRESHOLD KILL SWITCH
if active_now > MAX_USERS or SYSTEM_LOCKED:
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

def play_sound(file_name):
    path = os.path.join(SOUND_DIR, file_name)
    with open(path, "rb") as f:
        data = f.read()
        b64 = base64.b64encode(data).decode()
        audio_html = f"""
            <audio autoplay style="display:none;">
                <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
            </audio>
        """
        st.components.v1.html(audio_html, height=0)

# --- 3. SESSION STATE ---
if 'stealth_mode' not in st.session_state:
    st.session_state.stealth_mode = True
if 'show_notif' not in st.session_state:
    st.session_state.show_notif = False

# --- 4. PAGE CONFIG ---
if st.session_state.stealth_mode:
    st.set_page_config(page_title="Advanced Calculus - Module 4", page_icon="📝", layout="wide")
else:
    st.set_page_config(page_title="AN33SH PORTAL", page_icon="🐦‍🔥", layout="wide")

# --- 5. UI STYLE ---
st.markdown("""
<style>
@import url('https://googleapis.com');
html, body, [data-testid="stAppViewContainer"] {
    background: radial-gradient(circle at top right, #0a0a0c, #050505);
    font-family: 'Inter', sans-serif;
    color: #e0e0e0;
}
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
[data-testid="stVerticalBlockBorderWrapper"] {
    background: rgba(20, 20, 25, 0.7) !important;
    backdrop-filter: blur(10px);
    border-radius: 20px !important;
    border: 1px solid rgba(255, 255, 255, 0.05) !important;
    transition: transform 0.3s ease;
}
[data-testid="stVerticalBlockBorderWrapper"]:hover {
    border: 1px solid rgba(255, 75, 75, 0.4) !important;
    transform: translateY(-5px);
}
.stButton>button {
    width: 100%;
    border-radius: 12px;
    height: 3.5em;
    background: linear-gradient(135deg, #ff4b4b 0%, #7d0000 100%);
    color: white;
    font-weight: 800;
    text-transform: uppercase;
}
div.stButton > button[key="ghost_btn"] {
    background: transparent !important;
    color: transparent !important;
    border: none !important;
    height: 10px !important;
    box-shadow: none !important;
    min-height: 10px !important;
    padding: 0 !important;
}
.spy-warning {
    color: #ff4b4b;
    font-weight: 900;
    font-size: 14px;
    text-align: center;
    border: 2px solid #ff4b4b;
    padding: 10px;
    border-radius: 10px;
    margin-bottom: 20px;
}
h1, h2, h3 {
    font-family: 'JetBrains Mono', monospace !important;
    font-weight: 800 !important;
    background: linear-gradient(90deg, #fff, #888);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}
.user-badge {
    background:rgba(0,255,0,0.1);
    color:#00ff00;
    padding:5px 15px;
    border-radius:50px;
    font-size:12px;
    font-weight:bold;
    border:1px solid rgba(0,255,0,0.3);
    text-align:center;
    display:block;
    margin-bottom:20px;
}
.proxy-container {
    background: rgba(255, 75, 75, 0.05);
    border: 1px dashed rgba(255, 75, 75, 0.3);
    border-radius: 15px;
    padding: 40px;
    text-align: center;
    margin: 20px 0;
}
.proxy-text {
    font-family: 'JetBrains Mono', monospace;
    font-size: 22px;
    font-weight: 800;
    letter-spacing: 2px;
    background: linear-gradient(90deg, #ff4b4b, #7d0000);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    text-transform: uppercase;
}
</style>
<script>
window.parent.document.title = "Advanced Calculus - Module 4";
document.addEventListener('keydown', function(e) {
    if (e.key === 'Escape') {
        window.location.replace("https://google.com");
    }
});
</script>
""", unsafe_allow_html=True)

# --- 6. SIDEBAR ---
with st.sidebar:
    if st.session_state.stealth_mode:
        st.title("📚 Course Materials")
        st.markdown("---")
        st.caption("• Primary Sources\n• Citation Guide\n• Module 4 PDF")
        
        # Extended vertical spacing block to drop the button deep below the fold
        for _ in range(35):
            st.write("")
            
        if st.button(" ", key="ghost_btn"):
            st.session_state.stealth_mode = not st.session_state.stealth_mode
            st.rerun()
    else:
        st.markdown(f'<div class="user-badge">● {active_now} USERS ONLINE</div>', unsafe_allow_html=True)
        if st.button("🔔 DEVELOPER NOTIFICATIONS"):
            st.session_state.show_notif = not st.session_state.show_notif
            st.rerun()
        if st.session_state.show_notif:
            st.info(f"📢 MESSAGE FROM AN33SH:\n\n{LATEST_UPDATE}")
        st.write("---")
        st.markdown('<div class="spy-warning">IF YOU SUSPECT A TEACHER IS SPYING, PRESS THE BUTTON ON THE BOTTOM OR PRESS ALT+TAB.</div>', unsafe_allow_html=True)
        st.title("🛡️ Admin Controls")
        if st.button("🎲 FEELING LUCKY?"):
            if os.path.exists(GAME_DIR):
                files = [f for f in os.listdir(GAME_DIR) if f.endswith(".html")]
                if files:
                    launch_game(random.choice(files))
        st.write("---")
        st.markdown('<a href="https://google.com" target="_self"><button style="width:100%; background:red; color:white; border-radius:10px; border:none; padding:12px; font-weight:bold;">⚠️ EMERGENCY EXIT</button></a>', unsafe_allow_html=True)
        
        if st.button(" ", key="ghost_btn"):
            st.session_state.stealth_mode = not st.session_state.stealth_mode
            st.rerun()

# --- 7. MAIN CONTENT ---
if st.session_state.stealth_mode:
    st.title("Module 4: Differential Equations")
    st.info("Current Topic: Linear Second-Order Equations with Constant Coefficients")
    st.text_area("Notes", "Enter research data here...", height=400)
else:
    st_autorefresh(interval=5000, key="frequent_refresh")
    st.markdown('<div style="text-align: center;">', unsafe_allow_html=True)
    if os.path.exists(LOGO_PATH):
        st.image(LOGO_PATH, width=150)
    st.title("AN33SH PORTAL 🐦‍🔥")
    
    @st.fragment(run_every=15)
    def timed_caption():
        caps = ["Stay quiet, stay undetected.", "Your work is safe here.", "The only portal you'll ever need."]
        st.subheader(random.choice(caps))
    timed_caption()
    
    st.caption("SUGGESTIONS: https://forms.gle/NbggSg74kXCgimkh9")
    st.caption("EMERGENCY SITES: https://docs.google.com/document/d/1xNdJqxSORoJ5iVOjP1ofgigySlX_q4jQazalNOpxwgU/edit?usp=sharing")
    st.markdown('</div>', unsafe_allow_html=True)
    
    tab1, tab2, tab3 = st.tabs(["🎮 GAMES", "🌐 PROXY", "🔊 SOUNDBOARD"])
    with tab1:
        if os.path.exists(GAME_DIR):
            all_games = sorted([f for f in os.listdir(GAME_DIR) if f.endswith(".html")])
            c1, c2 = st.columns(2)
            with c1:
                query = st.text_input("🔍 Search...", placeholder="Type to filter...").lower()
            filtered = [f for f in all_games if query in f.lower()] if query else all_games
            pages = max(1, (len(filtered) // 12) + 1)
            with c2:
                page = st.number_input("Page", min_value=1, max_value=pages, step=1)
            st.write("---")
            display = filtered[(page-1)*12 : page*12]
            cols = st.columns(3)
            for i, file_name in enumerate(display):
                with cols[i % 3]:
                    with st.container(border=True):
                        st.subheader(file_name.replace(".html", "").replace("_", " ").title())
                        if st.button("PLAY", key=f"p_{file_name}"):
                            launch_game(file_name)
                            
    with tab2:
        st.markdown("""
        <div class="proxy-container">
            <div class="proxy-text">☠️ coming soon ☠️</div>
        </div>
        """, unsafe_allow_html=True)
        
    with tab3:
        if os.path.exists(SOUND_DIR):
            sound_files = sorted([f for f in os.listdir(SOUND_DIR) if f.endswith((".mp3", ".wav"))])
            if sound_files:
                cols = st.columns(3)
                for i, sound_name in enumerate(sound_files):
                    with cols[i % 3]:
                        with st.container(border=True):
                            clean_title = sound_name.replace(".mp3", "").replace(".wav", "").replace("_", " ").title()
                            st.subheader(clean_title)
                            if st.button("PLAY", key=f"s_{sound_name}"):
                                play_sound(sound_name)
            else:
                st.write("No sound files found in directory.")
        else:
            st.write("Sound directory not found.")
