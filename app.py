import streamlit as st
import os
import base64
import random

# --- 0. DEVELOPER NOTIFICATION (CHANGE TEXT HERE) ---
LATEST_UPDATE = "Hey guys! I added some games that you'll love. Stay stealthy. - An33sh"

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
    html, body, [data-testid="stAppViewContainer"] { background-color: #050505; font-family: 'Inter', sans-serif; }
    #MainMenu {visibility: hidden;} footer {visibility: hidden;}
    
    [data-testid="stSidebar"] { 
        background-color: #000000 !important; 
        border-right: 1px solid #111;
    }

    /* THE GHOST TRIGGER BAR */
    div.stButton > button[key="ghost_btn"] {
        background-color: #111111 !important;
        color: #111111 !important;
        border: none !important;
        height: 4px !important;
        width: 100% !important;
        padding: 0px !important;
        box-shadow: none !important;
        cursor: default !important;
        outline: none !important;
        min-height: 4px !important;
    }
    div.stButton > button[key="ghost_btn"]:hover { background-color: #1a1a1a !important; }

    .stButton>button {
        width: 100%; border-radius: 12px; height: 3.5em;
        background: linear-gradient(135deg, #ff4b4b 0%, #a10000 100%);
        color: white; border: none; font-weight: 900;
    }
    
    .spy-warning {
        color: #ff4b4b; font-weight: 900; font-size: 14px; text-align: center;
        border: 2px solid #ff4b4b; padding: 10px; border-radius: 10px; margin-bottom: 20px; text-transform: uppercase;
    }

    [data-testid="stVerticalBlockBorderWrapper"] {
        background: #0f0f0f; border-radius: 16px; border: 1px solid #222; padding: 20px;
    }
    h1, h2, h3, p, span, label { color: #ffffff !important; }

    /* Centering the main header */
    .centered-header {
        text-align: center;
        width: 100%;
    }
    </style>

    <script>
    document.addEventListener('keydown', function(e) {
        if (e.key === 'Escape') {
            window.location.replace("https://google.com");
        }
    });
    </script>
""", unsafe_allow_html=True)

def launch_game(file_path):
    with open(file_path, "rb") as f:
        b64 = base64.b64encode(f.read()).decode()
    js_code = f"""<script>var t=window.parent||window;var w=t.open("about:blank","_blank");w.document.write(atob("{b64}"));w.document.close();</script>"""
    st.components.v1.html(js_code, height=0)

# --- SIDEBAR ---
with st.sidebar:
    if st.session_state.stealth_mode:
        st.markdown("### Resources")
        st.caption("• Primary Sources")
        st.caption("• Citation Guide")
        st.caption("• Timeline PDF")
    else:
        # Toggle Notification Logic
        if st.button("🔔 DEVELOPER NOTIFICATIONS"):
            st.session_state.show_notif = not st.session_state.show_notif
            st.rerun()
            
        if st.session_state.show_notif:
            st.info(f"📢 MESSAGE FROM AN33SH:\n\n{LATEST_UPDATE}")

        st.write("---")
        st.markdown('<div class="spy-warning">IF YOU SUSPECT A TEACHER IS SPYING ON YOU, PRESS ALT+F4 OR PRESS THE BUTTON ON THE BOTTOM.</div>', unsafe_allow_html=True)
        
        st.title("🛡️ Admin Controls")
        if st.button("🎲 FEELING LUCKY?"):
            game_dir = "static/slope"
            if os.path.exists(game_dir):
                files = [f for f in os.listdir(game_dir) if f.endswith(".html")]
                if files: launch_game(os.path.join(game_dir, random.choice(files)))
        
        st.write("---")
        st.markdown('<a href="https://google.com" target="_self"><button style="width:100%; background:red; color:white; border-radius:10px; border:none; padding:12px; font-weight:bold; cursor:pointer;">⚠️ EMERGENCY EXIT</button></a>', unsafe_allow_html=True)

    for _ in range(25): st.write("")
    
    if st.button(" ", key="ghost_btn"):
        st.session_state.stealth_mode = not st.session_state.stealth_mode
        st.rerun()

# 3. UI LOGIC
if st.session_state.stealth_mode:
    st.title("Module 4: Differential Equations")
    st.info("Current Topic: Linear Second-Order Equations with Constant Coefficients")
    st.markdown("### Overview\nAnalysing the socio-political shifts of the late 19th century.")
    st.text_area("Research Field", "The industrial shift led to a massive migration toward urban centers...", height=400)
else:
    st.components.v1.html("<script>window.history.replaceState({}, '', 'https://google.com');</script>", height=0)
    
    # CENTERED LOGO AND HEADER
    st.markdown('<div class="centered-header">', unsafe_allow_html=True)
    if os.path.exists("static/slope/an33shlogo.jpg"):
        st.image("static/slope/an33shlogo.jpg", width=150)
    st.title("AN33SH PORTAL 🐦‍🔥")
    st.caption("Your boy noticed IBoss is blocking everything lately. Dont worry, take these 300+ games. KEEP THE URL BOX BLANK AND NEVER LET A TEACHER SEE THIS SITE.")
    st.caption("SUGGESTIONS: https://docs.google.com/forms/d/e/1FAIpQLSeMT7Ty9wa4yjAFIDdilg6tlS0a93tY8trDL-KcDYhfcFHkYw/viewform?usp=publish-editor")
    st.markdown('</div>', unsafe_allow_html=True)

    game_dir = "static/slope"
    @st.fragment
    def game_hub():
        if os.path.exists(game_dir): 
            all_files = sorted([f for f in os.listdir(game_dir) if f.endswith(".html")])
            search_col, page_col = st.columns(2)
            with search_col: query = st.text_input("🔍 Search games...", placeholder="Slope...").lower()
            filtered = [f for f in all_files if query in f.lower()]
            pages = max(1, (len(filtered) // 12) + 1)
            with page_col: page = st.number_input("Page", min_value=1, max_value=pages, step=1)
            
            display_list = filtered[(page-1)*12 : page*12]
            cols = st.columns(3)
            for i, file_name in enumerate(display_list):
                display_name = file_name.replace(".html", "").replace("_", " ").title()
                with cols[i % 3]:
                    with st.container(border=True):
                        st.subheader(display_name)
                        if st.button(f"PLAY", key=f"p_{file_name}"):
                            launch_game(os.path.join(game_dir, file_name))
    game_hub()
