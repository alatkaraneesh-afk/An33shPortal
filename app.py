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

# --- 1. SESSION STATE INITIALIZATION ---
if 'stealth_mode' not in st.session_state:
    st.session_state.stealth_mode = True
if 'show_notif' not in st.session_state:
    st.session_state.show_notif = False
if 'user_id' not in st.session_state:
    st.session_state.user_id = str(random.randint(10000, 99999))

# --- 2. MUST BE FIRST STREAMLIT COMMAND ---
if st.session_state.stealth_mode:
    st.set_page_config(page_title="Advanced Calculus - Module 4", page_icon="📝", layout="wide")
else:
    st.set_page_config(page_title="AN33SH PORTAL", page_icon="🔥", layout="wide")

# --- 3. USER TRACKING ---
def get_active_users():
    session_dir = Path(".sessions")
    session_dir.mkdir(exist_ok=True)
    Path(session_dir / f"{st.session_state.user_id}.lock").touch()
    current_time = time.time()
    for f in session_dir.glob("*.lock"):
        if current_time - f.stat().st_mtime > 15:
            try:
                f.unlink()
            except:
                pass
    return len(list(session_dir.glob("*.lock")))

active_now = get_active_users()

if active_now > MAX_USERS or SYSTEM_LOCKED:
    st.markdown('<meta http-equiv="refresh" content="0; URL=https://google.com">', unsafe_allow_html=True)
    st.stop()

# --- 4. CACHED UTILITIES ---
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

# --- 5. ENHANCED UI STYLE ---
st.markdown("""
<style>
@import url('https://googleapis.com');

/* Base Styles */
html, body, [data-testid="stAppViewContainer"] {
    background: radial-gradient(circle at 90% 10%, #0c0d14, #050508) !important;
    font-family: 'Inter', sans-serif;
    color: #e2e8f0;
}

/* Header UI Elements */
header, [data-testid="stHeader"] {
    background: transparent !important;
}
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}

/* Card Container Premium Glassmorphism */
[data-testid="stVerticalBlockBorderWrapper"] {
    background: rgba(15, 17, 26, 0.6) !important;
    backdrop-filter: blur(16px) saturate(120%);
    -webkit-backdrop-filter: blur(16px) saturate(120%);
    border-radius: 16px !important;
    border: 1px solid rgba(255, 255, 255, 0.04) !important;
    box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.3) !important;
    transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
    padding: 10px !important;
}
[data-testid="stVerticalBlockBorderWrapper"]:hover {
    border: 1px solid rgba(255, 75, 75, 0.25) !important;
    transform: translateY(-4px);
    box-shadow: 0 12px 40px 0 rgba(255, 75, 75, 0.08) !important;
}

/* Button Customizations */
.stButton>button {
    width: 100%;
    border-radius: 10px;
    height: 3.2em;
    background: linear-gradient(135deg, #ef4444 0%, #991b1b 100%) !important;
    color: #ffffff !important;
    font-weight: 700;
    letter-spacing: 0.05em;
    text-transform: uppercase;
    border: none !important;
    box-shadow: 0 4px 12px rgba(239, 68, 68, 0.2);
    transition: all 0.2s ease;
}
.stButton>button:hover {
    transform: translateY(-1px);
    box-shadow: 0 6px 20px rgba(239, 68, 68, 0.35);
    background: linear-gradient(135deg, #f87171 0%, #b91c1c 100%) !important;
}

/* Tab Premium Styling */
button[data-baseweb="tab"] {
    font-family: 'JetBrains Mono', monospace !important;
    font-weight: 700 !important;
    color: #94a3b8 !important;
    border-bottom: 2px solid transparent !important;
}
button[aria-selected="true"] {
    color: #ef4444 !important;
    border-bottom: 2px solid #ef4444 !important;
}

/* Absolutely Secret Button - Looks like empty dead space */
div.stButton > button[key="ghost_btn"] {
    background: transparent !important;
    color: transparent !important;
    border: none !important;
    height: 40px !important;
    box-shadow: none !important;
    min-height: 40px !important;
    padding: 0 !important;
    cursor: default !important;
}
div.stButton > button[key="ghost_btn"]:hover, 
div.stButton > button[key="ghost_btn"]:active, 
div.stButton > button[key="ghost_btn"]:focus {
    background: transparent !important;
    color: transparent !important;
    border: none !important;
    box-shadow: none !important;
}

/* Warnings and Badges */
.spy-warning {
    color: #f87171;
    font-weight: 700;
    font-size: 13px;
    text-align: center;
    border: 1px solid rgba(239, 68, 68, 0.3);
    background: rgba(239, 68, 68, 0.06);
    padding: 12px;
    border-radius: 10px;
    margin-bottom: 20px;
    letter-spacing: 0.02em;
}
h1, h2, h3 {
    font-family: 'JetBrains Mono', monospace !important;
    font-weight: 800 !important;
    letter-spacing: -0.02em;
    background: linear-gradient(135deg, #ffffff 30%, #94a3b8 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}
.user-badge {
    background: rgba(34, 197, 94, 0.08);
    color: #4ade80;
    padding: 6px 16px;
    border-radius: 50px;
    font-size: 11px;
    font-weight: 700;
    font-family: 'JetBrains Mono', monospace;
    border: 1px solid rgba(34, 197, 94, 0.2);
    text-align: center;
    display: block;
    margin-bottom: 20px;
    letter-spacing: 0.05em;
}

/* Clean Form Elements */
textarea {
    background-color: rgba(10, 11, 18, 0.5) !important;
    border: 1px solid rgba(255, 255, 255, 0.08) !important;
    color: #cbd5e1 !important;
    border-radius: 10px !important;
}
input {
    background-color: rgba(10, 11, 18, 0.5) !important;
    border: 1px solid rgba(255, 255, 255, 0.08) !important;
    color: #cbd5e1 !important;
    border-radius: 8px !important;
}

/* Sidebar scroll fix layout */
[data-testid="stSidebarUserContent"] {
    padding-top: 2rem !important;
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
        st.caption("• Primary Sources\n• Citation Guide\n• Module 4 PDF\n• Assignment Syllabus")
        st.caption("• Course Lecture Notes (Oct)")
        st.caption("• Formula Reference Sheets")
        
        # Security Feature: Generates massive vertical blank space pushing the button out of sight
        for _ in range(18):
            st.write("")
            
        st.caption("© 2024 University Academic Portal System")
        
        # Secret activation button (Looks perfectly like empty white space at the bottom)
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
        st.markdown('<div class="spy-warning">IF YOU SUSPECT A TEACHER IS SPYING, PRESS ESCAPE OR THE EMERGENCY EXIT IMMEDIATELY.</div>', unsafe_allow_html=True)
        st.title("🛡️ Admin Controls")
        if st.button("🎲 FEELING LUCKY?"):
            if os.path.exists(GAME_DIR):
                files = [f for f in os.listdir(GAME_DIR) if f.endswith(".html")]
                if files:
                    launch_game(random.choice(files))
        st.write("---")
        st.markdown('<a href="https://google.com" target="_self"><button style="width:100%; background:#dc2626; color:white; border-radius:10px; border:none; padding:12px; font-weight:bold; cursor:pointer;">⚠️ EMERGENCY EXIT</button></a>', unsafe_allow_html=True)
        
        # Quick toggle to turn stealth mode back on
        if st.button("🔒 LOCK BACK TO STUDY MODE"):
            st.session_state.stealth_mode = True
            st.rerun()

# --- 7. MAIN CONTENT ---
if st.session_state.stealth_mode:
    st.title("Module 4: Differential Equations")
    st.info("Current Topic: Linear Second-Order Equations with Constant Coefficients")
    st.text_area("Personal Research Notes & Formulas", "Enter research data here...", height=450)
else:
    st_autorefresh(interval=5000, key="frequent_refresh")
    st.markdown('<div style="text-align: center;">', unsafe_allow_html=True)
    if os.path.exists(LOGO_PATH):
        st.image(LOGO_PATH, width=130)
    st.title("AN33SH PORTAL 🔥")
    
    @st.fragment(run_every=15)
    def timed_caption():
        caps = ["Stay quiet, stay undetected.", "Your work is safe here.", "The only portal you'll ever need."]
        st.subheader(random.choice(caps))
    timed_caption()
    
    st.caption("SUGGESTIONS: forms.gle | EMERGENCY SITES: google.com")
    st.markdown('</div>', unsafe_allow_html=True)
    
    tab1, tab2, tab3 = st.tabs(["🎮 GAMES", "🌐 PROXY", "🔊 SOUNDBOARD"])
    
    with tab1:
        if os.path.exists(GAME_DIR):
            all_games = sorted([f for f in os.listdir(GAME_DIR) if f.endswith(".html")])
            c1, c2 = st.columns([3, 1])
            with c1:
                query = st.text_input("🔍 Search Game Catalog...", placeholder="Type to filter...").lower()
            
            filtered = [f for f in all_games if query in f.lower()] if query else all_games
            pages = max(1, (len(filtered) // 12) + 1)
            
            with c2:
                page = st.number_input("Page", min_value=1, max_value=pages, step=1)
            
            st.write("---")
            display_games = filtered[(page-1)*12 : page*12]
            
            cols = st.columns(3)
            for i, file_name in enumerate(display_games):
                with cols[i % 3]:
                    with st.container(border=True):
                        game_title = file_name.replace(".html", "").replace("_", " ").title()
                        st.markdown(f"<h3 style='font-size:16px; margin-bottom:10px;'>{game_title}</h3>", unsafe_allow_html=True)
                        if st.button("LAUNCH 🚀", key=f"p_{file_name}"):
                            launch_game(file_name)
        else:
            st.error("Game directory not found.")
            
    with tab2:
        st.markdown("<p style='text-align:center; color:#94a3b8;'>Proxy components bypass unblocked. Configuration offline.</p>", unsafe_allow_html=True)
        
    with tab3:
        st.markdown("<p style='text-align:center; color:#94a3b8;'>Soundboard configurations offline.</p>", unsafe_allow_html=True)
