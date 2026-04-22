# Check if a secret "key" is in the URL (e.g., an33sh.streamlit.app/?access=true)
query_params = st.query_params
if "access" not in query_params:
    # If the secret key isn't there, immediately kick them to Google Classroom
    st.markdown('<meta http-equiv="refresh" content="0; URL=https://google.com">', unsafe_allow_html=True)
    st.stop()

import streamlit as st
import os
import base64

# 1. SETUP SESSION STATE FOR STEALTH (Default to Study Mode for safety)
if 'stealth_mode' not in st.session_state:
    st.session_state.stealth_mode = True

# 2. DYNAMIC PAGE CONFIG (Masks the Browser Tab)
if st.session_state.stealth_mode:
    st.set_page_config(page_title="Advanced Calculus - Module 4", page_icon="📝", layout="wide")
else:
    st.set_page_config(page_title="AN33SH PORTAL", page_icon="🐦‍🔥", layout="wide")

# Custom CSS
st.markdown("""
    <style>
    .stButton>button { width: 100%; border-radius: 10px; height: 3em; font-weight: bold; }
    .game-card { background-color: #262730; padding: 20px; border-radius: 15px; border: 1px solid #444; }
    div[data-testid="stExpander"] { border: none !important; box-shadow: none !important; }
    #MainMenu {visibility: hidden;} footer {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# --- SIDEBAR STEALTH CONTROLS ---
with st.sidebar:
    st.title("Admin Controls")
    # THE ANTI-DETECTION TOGGLE
    if st.checkbox("Enable Educational View", value=st.session_state.stealth_mode):
        st.session_state.stealth_mode = True
    else:
        st.session_state.stealth_mode = False
    
    st.write("---")
    # PANIC BUTTON
    st.markdown('<a href="https://google.com" target="_self"><button style="width:100%; background:red; color:white; border-radius:5px; border:none; padding:10px; cursor:pointer;">⚠️ EMERGENCY EXIT</button></a>', unsafe_allow_html=True)

# 3. UI LOGIC
if st.session_state.stealth_mode:
    # --- THE "FAKE" EDUCATIONAL SITE ---
    st.title("Module 4: Differential Equations")
    st.info("Current Topic: Linear Second-Order Equations with Constant Coefficients")
    st.markdown("""
    ### Overview
    In this section, we explore the methodology for solving differential equations of the form:
    $$ay'' + by' + cy = 0$$
    Using the characteristic equation $ar^2 + br + c = 0$, we can determine the fundamental solution set based on the discriminant.
    
    *   **Resource 1:** [Derivation of the Quadratic Formula](https://wikipedia.org)
    *   **Resource 2:** [Applications in Physics](https://wikipedia.org)
    """)
    st.image("https://wikimedia.org", caption="Fig 1.2: Sinusoidal Variance")

else:
    # --- THE ACTUAL GAME HUB ---
    col1, col2 = st.columns([1, 5])
    with col1:
        if os.path.exists("static/slope/an33shlogo.jpg"):
            st.image("static/slope/an33shlogo.jpg", width=100)
    with col2:
        st.title("AN33SHPORTAL 🐦‍🔥")
        st.caption("Your boy noticed IBoss is blocking everything lately. Dont worry, take these 300+ games. Remember to turn on educational view when a teacher is spying!")
        st.caption("Email me suggestions at alatkaraneesh@gmail.com")

    game_dir = "static/slope"
    if os.path.exists(game_dir): 
        all_files = sorted([f for f in os.listdir(game_dir) if f.endswith(".html")])
        
        search_col, page_col = st.columns([3, 1])
        with search_col:
            query = st.text_input("🔍 Search games...", placeholder="FNAF, Slope, Soccer...").lower()
        
        filtered_games = [f for f in all_files if query in f.lower()]
        
        games_per_page = 12
        n_pages = (len(filtered_games) // games_per_page) + 1
        with page_col:
            page = st.number_input("Page", min_value=1, max_value=max(1, n_pages), step=1)
        
        start_idx = (page - 1) * games_per_page
        end_idx = start_idx + games_per_page
        display_list = filtered_games[start_idx:end_idx]

        cols = st.columns(3)
        for i, file_name in enumerate(display_list):
            display_name = file_name.replace(".html", "").replace("_", " ").title()
            with cols[i % 3]:
                with st.container(border=True):
                    st.subheader(display_name)
                    with st.expander("🎮 Play / Download"):
                        file_path = os.path.join(game_dir, file_name)
                        with open(file_path, "rb") as f:
                            binary_data = f.read()
                            b64_content = base64.b64encode(binary_data).decode()

                        js_code = f"""
                        <script>
                        function launch_{i}() {{
                            var win = window.open("about:blank", "_blank");
                            win.document.write(atob("{b64_content}"));
                            win.document.close();
                        }}
                        </script>
                        <button onclick="launch_{i}()" style="width:100%; height:40px; background:#ff4b4b; color:white; border:none; border-radius:8px; cursor:pointer;">🚀 LAUNCH STEALTH</button>
                        """
                        st.components.v1.html(js_code, height=50)
                        st.download_button("📥 Download HTML", binary_data, file_name=file_name, key=f"dl_{file_name}")

        st.write(f"Showing {start_idx+1}-{min(end_idx, len(filtered_games))} of {len(filtered_games)} games")
    else:
        st.error("Game folder not found!")
