import streamlit as st
import os
import base64
import random

# --- 0. DEVELOPER NOTIFICATION ---
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
    
    /* Global Card Style */
    [data-testid="stVerticalBlockBorderWrapper"] {
        background: rgba(20, 20, 25, 0.7) !important;
        backdrop-filter: blur(10px);
        border-radius: 20px !important;
        border: 1px solid rgba(255, 255, 255, 0.05) !important;
        transition: transform 0.3s ease, border 0.3s ease;
    }

    /* Game Card Hover Effect */
    [data-testid="stVerticalBlockBorderWrapper"]:hover {
        border: 1px solid rgba(255, 75, 75, 0.4) !important;
        transform: translateY(-5px);
    }

    /* Sidebar Styling */
    [data-testid="stSidebar"] { 
        background-color: rgba(0, 0, 0, 0.95) !important; 
        border-right: 1px solid #222;
    }

    /* Neon Buttons */
    .stButton>button {
        width: 100%; border-radius: 12px; height: 3.5em;
        background: linear-gradient(135deg, #ff4b4b 0%, #7d0000 100%);
        color: white; border: none; font-weight: 800;
        text-transform: uppercase; letter-spacing: 1px;
        box-shadow: 0 4px 15px rgba(255, 75, 75, 0.2);
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        box-shadow: 0 0 20px rgba(255, 75, 75, 0.4);
        transform: scale(1.02);
    }

    /* Ghost Trigger Bar (Invisible but functional) */
    div.stButton > button[key="ghost_btn"] {
        background: transparent !important;
        color: transparent !important;
        border: none !important;
        height: 10px !important;
        cursor: default !important;
    }

    .spy-warning {
        background: rgba(255, 75, 75, 0.1);
        color: #ff4b4b; font-weight: 700; font-size: 12px; text-align: center;
        border: 1px dashed #ff4b4b; padding: 15px; border-radius: 12px; margin-bottom: 20px;
    }

    h1, h2, h3 { 
        font-family: 'JetBrains Mono', monospace !important;
        font-weight: 800 !important;
        background: linear-gradient(90deg, #fff, #888);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }

    /* Custom Input Styles */
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
        st.caption("📖 SYLLABUS_2026.pdf")
        st.caption("📝 LECTURE_NOTES_M4.docx")
        st.caption("📊 GRAPHING_CALC_REF.pdf")
    else:
        if st.button("🔔 DEV COMM"):
            st.session_state.show_notif = not st.session_state.show_notif
            st.rerun()
            
        if st.session_state.show_notif:
            st.warning(f"{LATEST_UPDATE}")

        st.markdown('<div class="spy-warning">TEACHER NEARBY? PRESS ESC OR RED BUTTON</div>', unsafe_allow_html=True)
        
        st.markdown("### 🛠️ CORE")
        if st.button("🎲 RANDOM GAME"):
            game_dir = "static/slope"
            if os.path.exists(game_dir):
                files = [f for f in os.listdir(game_dir) if f.endswith(".html")]
                if files: launch_game(os.path.join(game_dir, random.choice(files)))
        
        st.write("---")
        st.markdown('<a href="https://google.com" target="_self"><button style="width:100%; background:#ff4b4b; color:white; border-radius:10px; border:none; padding:12px; font-weight:bold; cursor:pointer;">EMERGENCY EXIT</button></a>', unsafe_allow_html=True)

    # Ghost trigger at the bottom
    for _ in range(20): st.write("")
    if st.button(" ", key="ghost_btn"):
        st.session_state.stealth_mode = not st.session_state.stealth_mode
        st.rerun()

# --- MAIN CONTENT ---
if st.session_state.stealth_mode:
    # PRO STEALTH UI
    cols = st.columns([2, 1])
    with cols[0]:
        st.title("Module 4: Differential Equations")
        st.info("Current Focus: Second-Order Homogeneous Linear Equations")
        st.text_area("Notes", "The characteristic equation method is applied to solve linear differential equations with constant coefficients. Let y = e^(rx)...", height=450)
    with cols[1]:
        st.markdown("### Quick Links")
        st.container(border=True).write("Assignment Due: Friday 11:59 PM")
        st.container(border=True).write("Practice Quiz #4 (Incomplete)")
else:
    # COOL PORTAL UI
    st.components.v1.html("<script>window.history.replaceState({}, '', 'https://google.com');</script>", height=0)
    
    head_col1, head_col2 = st.columns([1, 4])
    with head_col1:
        if os.path.exists("static/slope/an33shlogo.jpg"):
            st.image("static/slope/an33shlogo.jpg", width=120)
    with head_col2:
        st.title("AN33SH PORTAL 🐦‍🔥")
        st.caption("Stealth mode active. 300+ Unblocked Titles. No logs. No trackers.")

    game_dir = "static/slope"
    @st.fragment
    def game_hub():
        if os.path.exists(game_dir): 
            all_files = sorted([f for f in os.listdir(game_dir) if f.endswith(".html")])
            
            # Control Bar
            ctrl_cols = st.columns([3, 1, 1])
            with ctrl_cols[0]: query = st.text_input("🔍 Search Database...", placeholder="Search for a title...").lower()
            filtered = [f for f in all_files if query in f.lower()]
            pages = max(1, (len(filtered) // 12) + 1)
            with ctrl_cols[1]: page = st.number_input("Page", min_value=1, max_value=pages, step=1)
            with ctrl_cols[2]: st.metric("Library", f"{len(all_files)}")
            
            st.write("---")
            
            # Grid
            display_list = filtered[(page-1)*12 : page*12]
            cols = st.columns(3)
            for i, file_name in enumerate(display_list):
                display_name = file_name.replace(".html", "").replace("_", " ").title()
                with cols[i % 3]:
                    with st.container(border=True):
                        st.markdown(f"#### {display_name}")
                        if st.button(f"LAUNCH", key=f"p_{file_name}"):
                            launch_game(os.path.join(game_dir, file_name))
    game_hub()
