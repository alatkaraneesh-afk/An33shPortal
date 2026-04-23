import streamlit as st
import os
import base64
import random

# 1. SETUP SESSION STATE
if 'stealth_mode' not in st.session_state:
    st.session_state.stealth_mode = True

# 2. DYNAMIC PAGE CONFIG (TAB MASKING)
if st.session_state.stealth_mode:
    # Makes the tab look exactly like a Google Doc
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

    /* Modern Button Styling */
    .stButton>button {
        width: 100%; border-radius: 12px; height: 3.5em;
        background: linear-gradient(135deg, #ff4b4b 0%, #a10000 100%);
        color: white; border: none; font-weight: 900; letter-spacing: 1px;
        text-transform: uppercase; box-shadow: 0 4px 15px rgba(255, 75, 75, 0.2);
        transition: all 0.3s ease;
    }
    .stButton>button:hover { transform: translateY(-2px); box-shadow: 0 0 20px rgba(255, 75, 75, 0.6); color: white; }

    /* Cyberpunk Game Card Style */
    [data-testid="stVerticalBlockBorderWrapper"] {
        background: #0f0f0f; border-radius: 16px; border: 1px solid #222;
        padding: 20px; transition: all 0.4s ease;
    }
    [data-testid="stVerticalBlockBorderWrapper"]:hover { border-color: #ff4b4b; background: #141414; box-shadow: 0 0 25px rgba(255, 75, 75, 0.1); }

    h1, h2, h3, p, span, label { color: #ffffff !important; }
    .stCaption { color: #888 !important; }
    .stTextInput>div>div>input { background-color: #111; color: white; border: 1px solid #333; border-radius: 8px; }
    
    /* Invisible Secret Button */
    .secret-btn>div>button {
        background: transparent !important;
        border: none !important;
        color: transparent !important;
        height: 10px !important;
        margin-top: -20px !important;
    }
    </style>

    <script>
    // PANIC KEY: Press Escape to instantly jump to Google Classroom
    document.addEventListener('keydown', function(e) {
        if (e.key === 'Escape') {
            window.location.replace("https://classroom.google.com");
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

# --- SIDEBAR ---
with st.sidebar:
    st.title("🛡️ Admin Controls")
    
    # Hidden way to relock for the owner
    if not st.session_state.stealth_mode:
        if st.button("🔒 LOCK PORTAL"):
            st.session_state.stealth_mode = True
            st.rerun()
    else:
        st.write("Educational Mode Active")

    st.write("---")
    st.markdown('<a href="https://classroom.google.com" target="_self"><button style="width:100%; background:red; color:white; border-radius:10px; border:none; padding:12px; font-weight:bold; cursor:pointer;">⚠️ EMERGENCY EXIT (ESC)</button></a>', unsafe_allow_html=True)

# 3. UI LOGIC
if st.session_state.stealth_mode:
    # --- STEALTH LANDER ---
    st.title("Module 4: Differential Equations")
    st.info("Draft Status: In Progress | Shared with Class")
    st.markdown("### Overview\nSolving equations of the form: $$ay'' + by' + cy = 0$$")
    
    # THE SECRET TRICK
    # Tell the bros: "Click twice quickly on the image to enter."
    col_img, col_txt = st.columns([1, 1])
    with col_img:
        st.image("https://wikimedia.org", caption="Fig 1.2: Sinusoidal Variance")
        st.markdown('<div class="secret-btn">', unsafe_allow_html=True)
        if st.button("⠀", key="secret_trick"): # Invisible button
            st.session_state.stealth_mode = False
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)
    with col_txt:
        st.text_area("Research Notes:", "The characteristic equation determines the fundamental solution set...", height=250)

else:
    # --- GAME HUB ---
    st.components.v1.html("""
        <script>
        window.history.replaceState({}, '', 'https://google.com');
        </script>
    """, height=0)

    col1, col2 = st.columns([1, 5])
    with col1:
        if os.path.exists("static/slope/an33shlogo.jpg"): st.image("static/slope/an33shlogo.jpg", width=100)
    with col2:
        st.title("AN33SH PORTAL 🐦‍🔥")
        st.caption("Your boy noticed IBoss is blocking everything lately. Dont worry, take these 300+ games. Remember to use the 'ESC' key if a teacher walks by!")
        st.caption("Email me suggestions at alatkaraneesh@gmail.com")

    game_dir = "static/slope"
    
    @st.fragment
    def game_hub():
        if os.path.exists(game_dir): 
            all_files = sorted([f for f in os.listdir(game_dir) if f.endswith(".html")])
            st.subheader("🔥 TRENDING NOW")
            f_cols = st.columns(3)
            featured = ["slopeoffline.html", "fnaf.html", "tinyfishing.html"] 
            for i, f_game in enumerate([g for g in featured if g in all_files]):
                with f_cols[i]:
                    if st.button(f"⭐ {f_game.replace('.html','').replace('_', ' ').title()}", key=f"feat_{i}"):
                        launch_game(os.path.join(game_dir, f_game))

            st.write("---")
            search_col, page_col = st.columns([3, 1])
            with search_col: query = st.text_input("🔍 Search games...", placeholder="FNAF, Slope...").lower()
            
            filtered = [f for f in all_files if query in f.lower()]
            pages = max(1, (len(filtered) // 12) + 1)
            with page_col: page = st.number_input("Page", min_value=1, max_value=pages, step=1)
            
            display_list = filtered[(page-1)*12 : page*12]
            cols = st.columns(3)
            
            for i, file_name in enumerate(display_list):
                display_name = file_name.replace(".html", "").replace("_", " ").title()
                with cols[i % 3]:
                    with st.container(border=True):
                        img_path = os.path.join(game_dir, file_name.replace(".html", ".jpg"))
                        if os.path.exists(img_path): st.image(img_path, use_container_width=True)
                        else: st.markdown("<h1 style='text-align: center;'>🎮</h1>", unsafe_allow_html=True) 
                        
                        st.subheader(display_name)
                        if st.button(f"PLAY", key=f"p_{file_name}"):
                            launch_game(os.path.join(game_dir, file_name))
                        
                        with open(os.path.join(game_dir, file_name), "rb") as f:
                            st.download_button("📥 DOWNLOAD", f.read(), file_name=file_name, key=f"dl_{file_name}")

            st.caption(f"Showing {len(display_list)} of {len(filtered)} games")
        else: st.error("Folder 'static/slope' missing!")
    game_hub()
