import streamlit as st
import os
import base64
import random
import time
from pathlib import Path
from streamlit_autorefresh import st_autorefresh 

# --- 0. DEVELOPER NOTIFICATION ---
LATEST_UPDATE = "WORKING ON IT-An33sh"

# --- SAFETY FEATURE: THRESHOLD LOCK ---
MAX_USERS = 15 
KILL_SWITCH = False 

# --- REAL USER COUNT LOGIC ---
def get_active_users():
    session_dir = Path(".sessions")
    session_dir.mkdir(exist_ok=True)
    if 'user_id' not in st.session_state:
        st.session_state.user_id = str(random.randint(10000, 99999))
    session_file = session_dir / f"{st.session_state.user_id}.lock"
    session_file.touch()
    current_time = time.time()
    for f in session_dir.glob("*.lock"):
        if current_time - f.stat().st_mtime > 10: 
            try: f.unlink()
            except: pass
    return len(list(session_dir.glob("*.lock")))

active_now = get_active_users()

# --- KILL SWITCH CHECK ---
if active_now > MAX_USERS or KILL_SWITCH:
    st.markdown('<meta http-equiv="refresh" content="0; URL=https://google.com">', unsafe_allow_html=True)
    st.stop()

# 1. SETUP SESSION STATE
if 'stealth_mode' not in st.session_state:
    st.session_state.stealth_mode = True
if 'show_notif' not in st.session_state:
    st.session_state.show_notif = False

# 2. DYNAMIC PAGE CONFIG
if st.session_state.stealth_mode:
    st.set_page_config(page_title="Advanced Calculus - Module 4", page_icon="📝", layout="wide")
else:
    st.set_page_config(page_title="AN33SH PORTAL", page_icon="🐦‍🔥", layout="wide")

# --- UI STYLE ---
st.markdown("""
    <style>
    @import url('https://googleapis.com');
    html, body, [data-testid="stAppViewContainer"] { background: radial-gradient(circle at top right, #0a0a0c, #050505); font-family: 'Inter', sans-serif; color: #e0e0e0; }
    #MainMenu {visibility: hidden;} footer {visibility: hidden;}
    [data-testid="stVerticalBlockBorderWrapper"] { background: rgba(20, 20, 25, 0.7) !important; backdrop-filter: blur(10px); border-radius: 20px !important; border: 1px solid rgba(255, 255, 255, 0.05) !important; transition: transform 0.3s ease; }
    [data-testid="stVerticalBlockBorderWrapper"]:hover { border: 1px solid rgba(255, 75, 75, 0.4) !important; transform: translateY(-5px); }
    .stButton>button { width: 100%; border-radius: 12px; height: 3.5em; background: linear-gradient(135deg, #ff4b4b 0%, #7d0000 100%); color: white; border: none; font-weight: 800; text-transform: uppercase; letter-spacing: 1px; box-shadow: 0 4px 15px rgba(255, 75, 75, 0.2); }
    div.stButton > button[key="ghost_btn"] { background: transparent !important; color: transparent !important; border: none !important; height: 10px !important; box-shadow: none !important; min-height: 10px !important; padding: 0 !important; }
    .spy-warning { color: #ff4b4b; font-weight: 900; font-size: 14px; text-align: center; border: 2px solid #ff4b4b; padding: 10px; border-radius: 10px; margin-bottom: 20px; text-transform: uppercase; }
    h1, h2, h3 { font-family: 'JetBrains Mono', monospace !important; font-weight: 800 !important; background: linear-gradient(90deg, #fff, #888); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }
    .coming-soon { border: 1px dashed #444; padding: 50px; text-align: center; border-radius: 20px; background: rgba(255,255,255,0.02); margin-top: 20px; }
    .user-badge { background:rgba(0,255,0,0.1); color:#00ff00; padding:5px 15px; border-radius:50px; font-size:12px; font-weight:bold; border:1px solid rgba(0,255,0,0.3); text-align:center; display:block; margin-bottom:20px; }
    </style>
    <script>
    window.parent.document.title = "Advanced Calculus - Module 4";
    document.addEventListener('keydown', function(e) { if (e.key === 'Escape') { window.location.replace("https://google.com"); } });
    </script>
""", unsafe_allow_html=True)

# --- OPTIMIZED GAME LAUNCHER ---
@st.cache_data
def get_base64_game(file_path):
    """Encodes the game once and keeps it in memory for instant access."""
    with open(file_path, "rb") as f:
        return base64.b64encode(f.read()).decode()

def launch_game(file_path):
    # Retrieve the pre-encoded string (Instant)
    b64 = get_base64_game(file_path)
    # Using a slightly faster JS injection method
    js_code = f"""
    <script>
    var w = window.open('about:blank', '_blank');
    if(w) {{
        w.document.title = "Google Docs"; 
        w.document.body.style.margin = "0";
        var ifr = w.document.createElement('iframe');
        ifr.src = "data:text/html;base64,{b64}";
        ifr.style.width = "100vw";
        ifr.style.height = "100vh";
        ifr.style.border = "none";
        w.document.body.appendChild(ifr);
    }}
    </script>
    """
    st.components.v1.html(js_code, height=0)


# --- SIDEBAR ---
with st.sidebar:
    if st.session_state.stealth_mode:
        st.title("📚 Course Materials")
        st.markdown("---")
        st.caption("• Primary Sources\n• Citation Guide\n• Timeline PDF")
    else:
        # Move User Counter Here
        st.markdown(f'<div class="user-badge">● {active_now} USERS ONLINE</div>', unsafe_allow_html=True)
        
        if st.button("🔔 DEVELOPER NOTIFICATIONS"):
            st.session_state.show_notif = not st.session_state.show_notif
            st.rerun()
        if st.session_state.show_notif: st.info(f"📢 MESSAGE FROM AN33SH:\n\n{LATEST_UPDATE}")
        
        st.write("---")
        st.markdown('<div class="spy-warning">IF YOU SUSPECT A TEACHER IS SPYING, PRESS THE BUTTON ON THE BOTTOM OR PRESS ALT+TAB.</div>', unsafe_allow_html=True)
        
        st.title("🛡️ Admin Controls")
        if st.button("🎲 FEELING LUCKY?"):
            game_dir = "static/slope"
            files = get_game_files(game_dir)
            if files: launch_game(os.path.join(game_dir, random.choice(files)))
            
        st.write("---")
        st.markdown('<a href="https://google.com" target="_self"><button style="width:100%; background:red; color:white; border-radius:10px; border:none; padding:12px; font-weight:bold; cursor:pointer;">⚠️ EMERGENCY EXIT</button></a>', unsafe_allow_html=True)
    
    for _ in range(25): st.write("")
    if st.button(" ", key="ghost_btn"):
        st.session_state.stealth_mode = not st.session_state.stealth_mode
        st.rerun()

# --- MAIN CONTENT ---
if st.session_state.stealth_mode:
    st.title("Module 4: Differential Equations")
    st.info("Current Topic: Linear Second-Order Equations with Constant Coefficients")
    st.text_area("Research Field", "Analysing socio-political shifts in late 20th century...", height=400)
else:
    st_autorefresh(interval=2000, key="frequent_refresh")
    st.markdown('<div style="text-align: center;">', unsafe_allow_html=True)
    if os.path.exists("static/slope/an33shlogo.jpg"): st.image("static/slope/an33shlogo.jpg", width=150)
    st.title("AN33SH PORTAL 🐦‍🔥")
    
    # OG CAPTIONS + SUGGESTIONS
    captions = ["Stay quiet, stay undetected.", "Your work is safe here.", "The only portal you'll ever need."]
    st.subheader(random.choice(captions))
    st.caption("SUGGESTIONS: https://forms.gle/ryUj2FLXiQKG6wc99")
    st.markdown('</div>', unsafe_allow_html=True)

    tab1, tab2 = st.tabs(["🎮 GAMES", "🌐 PROXY"])
    
    with tab1:
        game_dir = "static/slope"
        all_files = get_game_files(game_dir)
        c1, c2 = st.columns(2)
        with c1: query = st.text_input("🔍 Search...", placeholder="Slope...").lower()
        filtered = [f for f in all_files if query in f.lower()]
        pages = max(1, (len(filtered) // 12) + 1)
        with c2: page = st.number_input("Page", min_value=1, max_value=pages, step=1)
        
        st.write("---")
        display = filtered[(page-1)*12 : page*12]
        cols = st.columns(3)
        for i, file_name in enumerate(display):
            with cols[i % 3]:
                with st.container(border=True):
                    st.subheader(file_name.replace(".html", "").replace("_", " ").title())
                    if st.button("PLAY", key=f"p_{file_name}"): 
                        launch_game(os.path.join(game_dir, file_name))
    
    with tab2:
        st.markdown('<div class="coming-soon"><h2 style="color:#ff4b4b;">🛰️ STEALTH PROXY</h2><p>COMING SOON</p></div>', unsafe_allow_html=True)
