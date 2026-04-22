import streamlit as st
import os
import base64

# 1. SETUP SESSION STATE
if 'stealth_mode' not in st.session_state:
    st.session_state.stealth_mode = True

# 2. DYNAMIC PAGE CONFIG
if st.session_state.stealth_mode:
    st.set_page_config(page_title="Advanced Calculus - Module 4", page_icon="📝", layout="wide")
else:
    st.set_page_config(page_title="AN33SH PORTAL", page_icon="🐦‍🔥", layout="wide")

# CUSTOM CSS FOR PRO UI
st.markdown("""
    <style>
    /* Hide Only the Menu and Footer, NOT the header/sidebar button */
    #MainMenu {visibility: hidden;} 
    footer {visibility: hidden;}
    ...

    
    /* Modern Button Styling */
    .stButton>button {
        width: 100%;
        border-radius: 12px;
        height: 3.5em;
        background-color: #ff4b4b;
        color: white;
        border: none;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background-color: #ff2b2b;
        transform: scale(1.02);
    }
    
    /* Glassmorphism Card Style */
    [data-testid="stVerticalBlockBorderWrapper"] {
        background: rgba(255, 255, 255, 0.05);
        border-radius: 15px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        padding: 20px;
        transition: 0.3s;
    }
    </style>
""", unsafe_allow_html=True)

# --- SIDEBAR ---
with st.sidebar:
    st.title("🛡️ Admin Controls")
    if st.checkbox("Enable Educational View", value=st.session_state.stealth_mode):
        st.session_state.stealth_mode = True
    else:
        st.session_state.stealth_mode = False
    
    st.write("---")
    st.markdown('<a href="https://google.com" target="_self"><button style="width:100%; background:red; color:white; border-radius:10px; border:none; padding:12px; font-weight:bold; cursor:pointer;">⚠️ EMERGENCY EXIT</button></a>', unsafe_allow_html=True)

# 3. UI LOGIC
if st.session_state.stealth_mode:
    st.title("Module 4: Differential Equations")
    st.info("Current Topic: Linear Second-Order Equations with Constant Coefficients")
    st.markdown("""
    ### Overview
    In this section, we explore methodology for solving differential equations of the form:
    $$ay'' + by' + cy = 0$$
    Using the characteristic equation $ar^2 + br + c = 0$.
    """)
    st.image("https://wikimedia.org", caption="Fig 1.2: Sinusoidal Variance")

else:
    col1, col2 = st.columns([1, 5])
    with col1:
        if os.path.exists("static/slope/an33shlogo.jpg"):
            st.image("static/slope/an33shlogo.jpg", width=100)
    with col2:
        st.title("AN33SHPORTAL 🐦‍🔥")
        st.caption("300+ Games | Stealth Mode | By: An33sh")

    game_dir = "static/slope"
    
    # FRAGMENT FOR HIGH SPEED SEARCH/PAGINATION
    @st.fragment
    def game_hub():
        if os.path.exists(game_dir): 
            all_files = sorted([f for f in os.listdir(game_dir) if f.endswith(".html")])
            
            search_col, page_col = st.columns([3, 1])
            with search_col:
                query = st.text_input("🔍 Search games...", placeholder="FNAF, Slope, Soccer...").lower()
            
            filtered_games = [f for f in all_files if query in f.lower()]
            
            games_per_page = 12
            n_pages = max(1, (len(filtered_games) // games_per_page) + 1)
            with page_col:
                page = st.number_input("Page", min_value=1, max_value=n_pages, step=1)
            
            start_idx = (page - 1) * games_per_page
            display_list = filtered_games[start_idx : start_idx + games_per_page]

            st.write("---")
            cols = st.columns(3)
            
            for i, file_name in enumerate(display_list):
                display_name = file_name.replace(".html", "").replace("_", " ").replace("-", " ").title()
                with cols[i % 3]:
                    with st.container(border=True):
                        st.subheader(display_name)
                        
                        file_path = os.path.join(game_dir, file_name)
                        
                        # Use unique keys for every game interaction
                        if st.button(f"🎮 PLAY {display_name}", key=f"play_{file_name}"):
                            with open(file_path, "rb") as f:
                                b64 = base64.b64encode(f.read()).decode()
                            
                            # LAUNCHER SCRIPT (Direct injection to escape sandboxing)
                            js_code = f"""
                            <script>
                            var target = window.parent || window;
                            var win = target.open("about:blank", "_blank");
                            win.document.write(atob("{b64}"));
                            win.document.close();
                            </script>
                            """
                            st.components.v1.html(js_code, height=0)

                        with open(file_path, "rb") as f:
                            st.download_button("📥 DOWNLOAD", f.read(), file_name=file_name, key=f"dl_{file_name}")

            st.caption(f"Showing {len(display_list)} of {len(filtered_games)} games")
        else:
            st.error("Game folder not found!")

    game_hub()
