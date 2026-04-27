import streamlit as st
import os
import base64
import random
import time
from pathlib import Path

# --- 0. DEVELOPER NOTIFICATION ---
LATEST_UPDATE = "SUCK MY BALLS IAN-An33sh"

# --- SAFETY FEATURE: EMERGENCY KILL SWITCH ---
KILL_SWITCH = False 

if KILL_SWITCH:
    st.markdown('<meta http-equiv="refresh" content="0; URL=https://google.com">', unsafe_allow_html=True)
    st.stop()

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
        if current_time - f.stat().st_mtime > 30:
            try: f.unlink()
            except: pass
    return len(list(session_dir.glob("*.lock")))

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
    [data-testid="stVerticalBlockBorderWrapper"] { background: rgba(20, 20, 25, 0.7) !important; backdrop-filter: blur(10px); border-radius: 20px !important; border: 1px solid rgba(255, 255, 255, 0.05) !important; transition: transform 0.3s ease, border 0.3s ease; }
    [data-testid="stSidebar"] { background-color: rgba(0, 0, 0, 0.95) !important; border-right: 1px solid #222; }
    .stButton>button { width: 100%; border-radius: 12px; height: 3.5em; background: linear-gradient(135deg, #ff4b4b 0%, #7d0000 100%); color: white; border: none; font-weight: 800; text-transform: uppercase; letter-spacing: 1px; box-shadow: 0 4px 15px rgba(255, 75, 75, 0.2); }
    
    /* GHOST BUTTON: Styled to be hidden way down */
    div.stButton > button[key="ghost_btn"] { 
        background: transparent !important; 
        color: transparent !important; 
        border: none !important; 
        height: 10px !important; 
        box-shadow: none !important;
        min-height: 10px !important;
        padding: 0 !important;
    }

    .spy-warning { color: #ff4b4b; font-weight: 900; font-size: 14px; text-align: center; border: 2px solid #ff4b4b; padding: 10px; border-radius: 10px; margin-bottom: 20px; text-transform: uppercase; }
    h1, h2, h3 { font-family: 'JetBrains Mono', monospace !important; font-weight: 800 !important; background: linear-gradient(90deg, #fff, #888); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }
    .stTextInput input { background-color: #111 !important; border: 1px solid #333 !important; color: white !important; border-radius: 10px !important; }
    #popup-alert { display: none; position: fixed; top: 100px; left: 50%; transform: translateX(-50%); z-index: 1000000 !important; background: linear-gradient(90deg, #ff4b4b, #a10000); color: white; padding: 18px 30px; border-radius: 15px; font-weight: 900; box-shadow: 0 10px 30px rgba(255, 75, 75, 0.8); border: 2px solid white; text-align: center; min-width: 320px; text-transform: uppercase; }
    </style>

    <div id="popup-alert">⚠️ POPUP BLOCKED! Enable popups in your browser address bar to play.</div>

    <script>
    window.parent.document.title = "Advanced Calculus - Module 4";
    var link = window.parent.document.querySelector("link[rel*='icon']") || window.parent.document.createElement('link');
    link.type = 'image/x-icon';
    link.rel = 'shortcut icon';
    link.href = 'https://gstatic.com';
    window.parent.document.getElementsByTagName('head').appendChild(link);
    document.addEventListener('keydown', function(e) { if (e.key === 'Escape') { window.location.replace("https://google.com"); } });
    </script>
""", unsafe_allow_html=True)

def launch_game(file_path):
    with open(file_path, "rb") as f:
        b64 = base64.b64encode(f.read()).decode()
    js_code = f"""<script>var t=window.parent||window;var w=t.open("about:blank","_blank");if(!w){{t.document.getElementById('popup-alert').style.display='block';}}else{{w.document.title="Google Docs";w.document.write(atob("{b64}"));w.document.close();}}</script>"""
    st.components.v1.html(js_code, height=0)

# --- SIDEBAR ---
with st.sidebar:
    if st.session_state.stealth_mode:
        st.title("📚 Course Materials")
        st.markdown("---")
        st.caption("• Primary Sources")
        st.caption("• Citation Guide")
        st.caption("• Timeline PDF")
    else:
        if st.button("🔔 DEVELOPER NOTIFICATIONS"):
            st.session_state.show_notif = not st.session_state.show_notif
            st.rerun()
        if st.session_state.show_notif: st.info(f"📢 MESSAGE FROM AN33SH:\n\n{LATEST_UPDATE}")
        st.write("---")
        st.markdown('<div class="spy-warning">IF YOU SUSPECT A TEACHER IS SPYING ON YOU, PRESS ALT+TAB OR PRESS THE BUTTON ON THE BOTTOM.</div>', unsafe_allow_html=True)
        st.title("🛡️ Admin Controls")
        if st.button("🎲 FEELING LUCKY?"):
            game_dir = "static/slope"
            if os.path.exists(game_dir):
                files = [f for f in os.listdir(game_dir) if f.endswith(".html")]
                if files: launch_game(os.path.join(game_dir, random.choice(files)))
        st.write("---")
        st.markdown('<a href="https://google.com" target="_self"><button style="width:100%; background:red; color:white; border-radius:10px; border:none; padding:12px; font-weight:bold; cursor:pointer;">⚠️ EMERGENCY EXIT</button></a>', unsafe_allow_html=True)
    
    # THE SCROLL GAP: Hidden spacer so you have to scroll down to find the ghost button
    for _ in range(25): st.write("")
    
    if st.button(" ", key="ghost_btn"):
        st.session_state.stealth_mode = not st.session_state.stealth_mode
        st.rerun()

# --- MAIN CONTENT ---
if st.session_state.stealth_mode:
    st.title("Module 4: Differential Equations")
    st.info("Current Topic: Linear Second-Order Equations with Constant Coefficients")
    st.markdown("### Overview\nAnalysing the socio-political shifts of the late 19th century.")
    st.text_area("Research Field", "The industrial shift led to a massive migration toward urban centers...", height=400)
else:
    st.components.v1.html("<script>window.history.replaceState({}, '', 'https://google.com');</script>", height=0)
    st.markdown('<div style="text-align: center;">', unsafe_allow_html=True)
    if os.path.exists("static/slope/an33shlogo.jpg"): st.image("static/slope/an33shlogo.jpg", width=150)
    st.title("AN33SH PORTAL 🐦‍🔥")
    
    # REAL ONLINE USERS
    count = get_active_users()
    st.markdown(f'<div style="text-align:center;margin-top:-15px;margin-bottom:20px;"><span style="background:rgba(0,255,0,0.1);color:#00ff00;padding:5px 15px;border-radius:50px;font-size:12px;font-weight:bold;border:1px solid rgba(0,255,0,0.3);">● {count} USERS ONLINE</span></div>', unsafe_allow_html=True)
    
    st.caption("Your boy noticed IBoss is blocking everything lately. Dont worry, take these 300+ games.")
    st.caption("SUGGESTIONS: https://forms.gle")
    st.markdown('</div>', unsafe_allow_html=True)

    tab1, tab2 = st.tabs(["🎮 GAMES", "🌐 PROXY (BETA)"])
    with tab1:
        game_dir = "static/slope"
        if os.path.exists(game_dir): 
            all_files = sorted([f for f in os.listdir(game_dir) if f.endswith(".html")])
            search_col, page_col = st.columns(2)
            with search_col: query = st.text_input("🔍 Search games...", placeholder="Slope...").lower()
            filtered = [f for f in all_files if query in f.lower()]
            pages = max(1, (len(filtered) // 12) + 1)
            with page_col: page = st.number_input("Page", min_value=1, max_value=pages, step=1)
            st.write("---")
            display_list = filtered[(page-1)*12 : page*12]
            cols = st.columns(3)
            for i, file_name in enumerate(display_list):
                with cols[i % 3]:
                    with st.container(border=True):
                        st.subheader(file_name.replace(".html", "").replace("_", " ").title())
                        if st.button("PLAY", key=f"p_{file_name}"): launch_game(os.path.join(game_dir, file_name))
    with tab2:
        st.markdown('<div class="coming-soon-box"><div class="coming-soon-text">⚡ ULTRA-STEALTH PROXY ⚡</div><h3 style="color: white; margin-top: 30px;">STATUS: <span style="color: #ff4b4b;">COMING SOON</span></h3></div>', unsafe_allow_html=True)
