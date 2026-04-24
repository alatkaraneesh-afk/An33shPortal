import streamlit as st
import os
import base64
import random

# --- 0. DEVELOPER NOTIFICATION ---
LATEST_UPDATE = "Making the app faster, hang on. -An33sh"

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

# --- CYBER-STYLISH UI ---
st.markdown("""
    <style>
    @import url('https://googleapis.com');
    
    html, body, [data-testid="stAppViewContainer"] { 
        background: radial-gradient(circle at top right, #0a0a0c, #050505);
        font-family: 'Inter', sans-serif;
        color: #e0e0e0;
    }
    
    #MainMenu {visibility: hidden;} footer {visibility: hidden;}
    
    [data-testid="stVerticalBlockBorderWrapper"] {
        background: rgba(20, 20, 25, 0.7) !important;
        backdrop-filter: blur(10px);
        border-radius: 20px !important;
        border: 1px solid rgba(255, 255, 255, 0.05) !important;
        transition: transform 0.3s ease, border 0.3s ease;
    }

    [data-testid="stVerticalBlockBorderWrapper"]:hover {
        border: 1px solid rgba(255, 75, 75, 0.4) !important;
        transform: translateY(-5px);
    }

    [data-testid="stSidebar"] { 
        background-color: rgba(0, 0, 0, 0.95) !important; 
        border-right: 1px solid #222;
    }

    .stButton>button {
        width: 100%; border-radius: 12px; height: 3.5em;
        background: linear-gradient(135deg, #ff4b4b 0%, #7d0000 100%);
        color: white; border: none; font-weight: 800;
        text-transform: uppercase; letter-spacing: 1px;
        box-shadow: 0 4px 15px rgba(255, 75, 75, 0.2);
    }
    
    .stButton>button:hover {
        box-shadow: 0 0 20px rgba(255, 75, 75, 0.4);
        transform: scale(1.02);
    }

    div.stButton > button[key="ghost_btn"] {
        background: transparent !important;
        color: transparent !important;
        border: none !important;
        height: 10px !important;
        cursor: default !important;
    }

    .spy-warning {
        color: #ff4b4b; font-weight: 900; font-size: 14px; text-align: center;
        border: 2px solid #ff4b4b; padding: 10px; border-radius: 10px; margin-bottom: 20px; text-transform: uppercase;
    }

    h1, h2, h3 { 
        font-family: 'JetBrains Mono', monospace !important;
        font-weight: 800 !important;
        background: linear-gradient(90deg, #fff, #888);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }

    .stTextInput input {
        background-color: #111 !important;
        border: 1px solid #333 !important;
        color: white !important;
        border-radius: 10px !important;
    }
    </style>

    <script>
    document.addEventListener('keydown', function(e) {
        if (e.key === 'Escape') { window.location.replace("https://google.com"); }
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
        st.title("📚 Course Materials")
        st.markdown("---")
        st.caption("• Primary Sources")
        st.caption("• Citation Guide")
        st.caption("• Timeline PDF")
    else:
        if st.button("🔔 DEVELOPER NOTIFICATIONS"):
            st.session_state.show_notif = not st.session_state.show_notif
            st.rerun()
            
        if st.session_state.show_notif:
            st.info(f"📢 MESSAGE FROM AN33SH:\n\n{LATEST_UPDATE}")

        st.write("---")
        # Restored Sidebar Alert
        st.markdown('<div class="spy-warning">IF YOU SUSPECT A TEACHER IS SPYING ON YOU, PRESS ALT+F4 OR PRESS THE BUTTON ON THE BOTTOM.</div>', unsafe_allow_html=True)
        
        st.title("🛡️ Admin Controls")
        if st.button("🎲 FEELING LUCKY?"):
            game_dir = "static/slope"
            if os.path.exists(game_dir):
                files = [f for f in os.listdir(game_dir) if f.endswith(".html")]
                if files: launch_game(os.path.join(game_dir, random.choice(files)))
        
        st.write("---")
        st.markdown('<a href="https://google.com" target="_self"><button style="width:100%; background:red; color:white; border-radius:10px; border:none; padding:12px; font-weight:bold; cursor:pointer;">⚠️ EMERGENCY EXIT</button></a>', unsafe_allow_html=True)

    for _ in range(20): st.write("")
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
    if os.path.exists("static/slope/an33shlogo.jpg"):
        st.image("static/slope/an33shlogo.jpg", width=150)
    st.title("AN33SH PORTAL 🐦‍🔥")
    st.caption("Your boy noticed IBoss is blocking everything lately. Dont worry, take these 300+ games. KEEP THE URL BOX BLANK AND NEVER LET A TEACHER SEE THIS SITE.")
    # Restored Suggestions Caption
    st.caption("SUGGESTIONS: https://forms.gle/32uS6xmQuGyHP6Hi8")
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
            
            st.write("---")
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
