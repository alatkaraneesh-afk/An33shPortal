import streamlit as st
import os
import base64
import random

# 1. SETUP SESSION STATE
if 'stealth_mode' not in st.session_state:
    st.session_state.stealth_mode = True

# 2. DYNAMIC PAGE CONFIG (TAB MASKING)
if st.session_state.stealth_mode:
    st.set_page_config(
        page_title="World History - Project Draft", 
        page_icon="https://gstatic.com", 
        layout="wide"
    )
else:
    st.set_page_config(page_title="AN33SH PORTAL", page_icon="🐦‍🔥", layout="wide")

# --- UI STYLE UPGRADE ---
st.markdown("""
    <style>
    @import url('https://googleapis.com');
    html, body, [data-testid="stAppViewContainer"] { background-color: #050505; font-family: 'Inter', sans-serif; }
    #MainMenu {visibility: hidden;} footer {visibility: hidden;}
    
    /* SIDEBAR COLOR */
    [data-testid="stSidebar"] { 
        background-color: #000000 !important; 
        border-right: 1px solid #111;
    }

    /* THE GHOST TRIGGER: PITCH BLACK */
    div.stButton > button[key="ghost_btn"] {
        background-color: #000000 !important;
        color: #000000 !important;
        border: none !important;
        height: 100px !important;
        width: 100% !important;
        box-shadow: none !important;
        cursor: default !important;
        outline: none !important;
    }
    div.stButton > button[key="ghost_btn"]:hover, 
    div.stButton > button[key="ghost_btn"]:active, 
    div.stButton > button[key="ghost_btn"]:focus {
        background-color: #000000 !important;
        color: #000000 !important;
        border: none !important;
        box-shadow: none !important;
    }

    /* Game UI Styles */
    .stButton>button {
        width: 100%; border-radius: 12px; height: 3.5em;
        background: linear-gradient(135deg, #ff4b4b 0%, #a10000 100%);
        color: white; border: none; font-weight: 900;
    }
    [data-testid="stVerticalBlockBorderWrapper"] {
        background: #0f0f0f; border-radius: 16px; border: 1px solid #222; padding: 20px;
    }
    h1, h2, h3, p, span, label { color: #ffffff !important; }
    </style>

    <script>
    // PANIC KEY: Press Escape to instantly jump to Google Classroom
    document.addEventListener('keydown', function(e) {
        if (e.key === 'Escape') {
            window.location.replace("https://google.com");
        }
    });
    </script>
""", unsafe_allow_html=True)

# LAUNCHER HELPER
def launch_game(file_path):
    with open(file_path, "rb") as f:
        b64 = base64.b64encode(f.read()).decode()
    js_code = f"""<script>var t=window.parent||window;var w=t.open("about:blank","_blank");w.document.write(atob("{b64}"));w.document.close();</script>"""
    st.components.v1.html(js_code, height=0)

# --- SIDEBAR (The Ghost Zone) ---
with st.sidebar:
    st.markdown("### Resources")
    st.caption("• Primary Sources")
    st.caption("• Citation Guide")
    st.caption("• Timeline PDF")
    
    # These only appear when the portal is UNLOCKED
    if not st.session_state.stealth_mode:
        st.write("---")
        if st.button("🎲 FEELING LUCKY?"):
            game_dir = "static/slope"
            if os.path.exists(game_dir):
                files = [f for f in os.listdir(game_dir) if f.endswith(".html")]
                if files: launch_game(os.path.join(game_dir, random.choice(files)))
        
        st.write("---")
        st.markdown('<a href="https://google.com" target="_self"><button style="width:100%; background:red; color:white; border-radius:10px; border:none; padding:12px; font-weight:bold; cursor:pointer;">⚠️ EMERGENCY EXIT</button></a>', unsafe_allow_html=True)

    # Push the ghost button to the very bottom
    for _ in range(25): st.write("")
    
    # THE VOID BUTTON: Totally black, matches sidebar background
    if st.button(" ", key="ghost_btn"):
        st.session_state.stealth_mode = not st.session_state.stealth_mode
        st.rerun()

# 3. UI LOGIC
if st.session_state.stealth_mode:
    # --- STEALTH LANDER ---
    st.title("Unit 4: Global Conflict and Resolution")
    st.info("Draft Status: In Progress | Saved to Cloud")
    st.markdown("### Overview\nAnalysing the socio-political shifts of the late 19th century.")
    st.text_area("Research Field", "The industrial shift led to a massive migration toward urban centers...", height=400)
else:
    # --- GAME HUB ---
    st.components.v1.html("<script>window.history.replaceState({}, '', 'https://google.com');</script>", height=0)
    col1, col2 = st.columns([1, 5])
    with col1:
        if os.path.exists("static/slope/an33shlogo.jpg"): st.image("static/slope/an33shlogo.jpg", width=100)
    with col2:
        st.title("AN33SH PORTAL 🐦‍🔥")
        st.caption("Your boy noticed IBoss is blocking everything. Hit ESC for Panic.")

    game_dir = "static/slope"
    @st.fragment
    def game_hub():
        if os.path.exists(game_dir): 
            all_files = sorted([f for f in os.listdir(game_dir) if f.endswith(".html")])
            search_col, page_col = st.columns([3, 1])
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
