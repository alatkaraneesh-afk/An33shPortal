import streamlit as st
import os
import base64
import random

# --- 1. FULL SITE CLOAKING LOGIC ---
query_params = st.query_params
is_cloaked = query_params.get("is_cloaked") == "true"

def launch_full_cloak():
    # Update this with your actual deployed URL
    portal_url = "https://streamlit.app"
    
    js = f"""
    <script>
    var target = window.parent || window;
    var win = target.open("about:blank", "_blank");
    if (win) {{
        win.document.title = "Advanced Calculus - Module 4";
        var doc = win.document.body;
        doc.style.margin = "0"; 
        doc.style.height = "100vh";
        doc.style.overflow = "hidden";
        
        var iframe = win.document.createElement("iframe");
        iframe.src = "{portal_url}";
        iframe.style.width = "100%"; 
        iframe.style.height = "100%"; 
        iframe.style.border = "none";
        doc.appendChild(iframe);
        
        // Redirect original tab to hide the evidence
        target.location.replace("https://classroom.google.com");
    }} else {{
        alert("❌ POP-UP BLOCKED! Click the icon in your address bar and select 'Always Allow'.");
    }}
    </script>
    """
    st.components.v1.html(js, height=0)

# --- 2. SETUP SESSION STATE ---
if 'stealth_mode' not in st.session_state:
    st.session_state.stealth_mode = True

# --- 3. DYNAMIC PAGE CONFIG ---
if st.session_state.stealth_mode:
    st.set_page_config(page_title="Advanced Calculus - Module 4", page_icon="📝", layout="wide")
else:
    st.set_page_config(page_title="AN33SH PORTAL", page_icon="🐦‍🔥", layout="wide")

# UI STYLE
st.markdown("""
    <style>
    @import url('https://googleapis.com');
    html, body, [data-testid="stAppViewContainer"] { background-color: #050505; font-family: 'Inter', sans-serif; }
    #MainMenu {visibility: hidden;} footer {visibility: hidden;}
    [data-testid="stSidebar"] { background-color: #0a0a0a; border-right: 1px solid #ff4b4b33; }
    .stButton>button {
        width: 100%; border-radius: 12px; height: 3.5em;
        background: linear-gradient(135deg, #ff4b4b 0%, #a10000 100%);
        color: white; border: none; font-weight: 900; letter-spacing: 1px;
        text-transform: uppercase; box-shadow: 0 4px 15px rgba(255, 75, 75, 0.2);
        transition: all 0.3s ease;
    }
    .stButton>button:hover { transform: translateY(-2px); box-shadow: 0 0 20px rgba(255, 75, 75, 0.6); color: white; }
    [data-testid="stVerticalBlockBorderWrapper"] {
        background: #0f0f0f; border-radius: 16px; border: 1px solid #222;
        padding: 20px; transition: all 0.4s ease;
    }
    h1, h2, h3, p, span, label { color: #ffffff !important; }
    .stCaption { color: #888 !important; }
    .stTextInput>div>div>input { background-color: #111; color: white; border: 1px solid #333; border-radius: 8px; }
    </style>
""", unsafe_allow_html=True)

# LAUNCHER HELPER (For individual games inside the cloak)
def launch_game(file_path):
    with open(file_path, "rb") as f:
        b64 = base64.b64encode(f.read()).decode()
    js_code = f"""<script>var t=window.parent||window;var w=t.open("about:blank","_blank");w.document.write(atob("{b64}"));w.document.close();</script>"""
    st.components.v1.html(js_code, height=0)

# --- 4. THE LANDER (URL MASKER) ---
if not is_cloaked:
    st.title("Student Resource Portal")
    st.info("Authenticated Session Required")
    st.write("Click below to launch your educational modules in a secure stealth window.")
    placeholder = st.empty()
    if st.button("🚀 LAUNCH SECURE MODULES", type="primary"):
        with placeholder:
            launch_full_cloak()
    st.stop()

# --- 5. THE ACTUAL APP (Only runs inside about:blank) ---
with st.sidebar:
    st.title("🛡️ Admin Controls")
    st.session_state.stealth_mode = st.checkbox("Enable Educational View", value=st.session_state.stealth_mode)
    
    if not st.session_state.stealth_mode:
        st.write("---")
        if st.button("🎲 FEELING LUCKY?"):
            game_dir = "static/slope"
            if os.path.exists(game_dir):
                files = [f for f in os.listdir(game_dir) if f.endswith(".html")]
                if files: launch_game(os.path.join(game_dir, random.choice(files)))
    
    st.write("---")
    st.markdown('<a href="https://google.com" target="_self"><button style="width:100%; background:red; color:white; border-radius:10px; border:none; padding:12px; font-weight:bold; cursor:pointer;">⚠️ EMERGENCY EXIT</button></a>', unsafe_allow_html=True)

if st.session_state.stealth_mode:
    st.title("Module 4: Differential Equations")
    st.info("Current Topic: Linear Second-Order Equations with Constant Coefficients")
    st.markdown("### Overview\nSolving equations of the form: $$ay'' + by' + cy = 0$$")
    st.image("https://wikimedia.org", caption="Fig 1.2: Sinusoidal Variance")
else:
    col1, col2 = st.columns([1, 5])
    with col1:
        if os.path.exists("static/slope/an33shlogo.jpg"): st.image("static/slope/an33shlogo.jpg", width=100)
    with col2:
        st.title("AN33SH PORTAL 🐦‍🔥")
        st.caption("Your boy noticed IBoss is blocking everything lately. Dont worry, take these 300+ games. Remember to turn on educational view when a teacher is spying!")
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
