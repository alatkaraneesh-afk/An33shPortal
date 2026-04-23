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
    [data-testid="stSidebar"] { background-color: #0a0a0a; border-right: 1px solid #ff4b4b33; }

    /* The Secret Ghost Button Style */
    .ghost-trigger>div>button {
        background: #0a0a0a !important;
        border: 1px solid #0a0a0a !important;
        color: #0a0a0a !important;
        height: 50px !important;
        width: 50px !important;
        margin-top: 100px !important;
        cursor: default !important;
    }
    .ghost-trigger>div>button:active, .ghost-trigger>div>button:focus {
        box-shadow: none !important;
        outline: none !important;
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
    st.caption("• Primary Sources\n• Citation Guide\n• Timeline PDF")
    
    # Large gap to push the trigger to the bottom
    for _ in range(15): st.write("")
    
    # THE SECRET BLACK IMAGE TRIGGER
    st.markdown('<div class="ghost-trigger">', unsafe_allow_html=True)
    if st.button("⬛", key="ghost_btn"):
        # This toggles mode. To the user, it just looks like clicking a dead square.
        st.session_state.stealth_mode = not st.session_state.stealth_mode
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

# 3. UI LOGIC
if st.session_state.stealth_mode:
    # --- STEALTH LANDER ---
    st.title("Unit 4: Global Conflict and Resolution")
    st.info("Draft Status: In Progress | Saved to Cloud")
    st.markdown("### Overview\nAnalysing the socio-political shifts of the late 19th century.")
    st.text_area("Research Field", "Enter observations here...", height=400)
else:
    # --- GAME HUB ---
    st.components.v1.html("<script>window.history.replaceState({}, '', 'https://google.com');</script>", height=0)
    col1, col2 = st.columns([1, 5])
    with col1:
        if os.path.exists("static/slope/an33shlogo.jpg"): st.image("static/slope/an33shlogo.jpg", width=100)
    with col2:
        st.title("AN33SH PORTAL 🐦‍🔥")
        st.caption("Status: Stealth Mode Active. Hit ESC for Panic.")

    game_dir = "static/slope"
    @st.fragment
    def game_hub():
        if os.path.exists(game_dir): 
            all_files = sorted([f for f in os.listdir(game_dir) if f.endswith(".html")])
            search_col, page_col = st.columns([3,1])
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
