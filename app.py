import streamlit as st
import os
import base64

# --- 1. FULL SITE CLOAKING LOGIC ---
query_params = st.query_params
is_cloaked = query_params.get("is_cloaked") == "true"

def launch_full_cloak():
    # CRITICAL: Change this URL to your actual deployed app link
    portal_url = "https://streamlit.app"
    
    js = f"""
    <script>
    function tryOpen() {{
        // Escape the Streamlit iframe sandbox
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
            target.location.replace("https://google.com");
        } else {{
            alert("❌ Pop-up Blocked! Click the icon in your address bar and select 'Always Allow'.");
        }}
    }}
    tryOpen();
    </script>
    """
    st.components.v1.html(js, height=0)


# --- 2. PAGE SETUP ---
if 'stealth_mode' not in st.session_state:
    st.session_state.stealth_mode = True

if st.session_state.stealth_mode:
    st.set_page_config(page_title="Advanced Calculus - Module 4", page_icon="📝", layout="wide")
else:
    st.set_page_config(page_title="AN33SH PORTAL", page_icon="🐦‍🔥", layout="wide")

st.markdown("""
    <style>
    .stButton>button { width: 100%; border-radius: 10px; height: 3em; font-weight: bold; }
    #MainMenu {visibility: hidden;} footer {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# --- 3. THE LANDER (Only shows if NOT in about:blank) ---
if not is_cloaked:
    st.title("Student Resource Portal")
    st.info("Authenticated Session Required")
    st.write("Please click below to launch your educational modules in a secure window.")
    
    placeholder = st.empty()
    if st.button("🚀 LAUNCH SECURE MODULES", type="primary"):
        with placeholder:
            launch_full_cloak()
    st.stop() 

# --- 4. THE ACTUAL APP (Only runs inside about:blank) ---
with st.sidebar:
    st.title("Admin Controls")
    if st.checkbox("Enable Educational View", value=st.session_state.stealth_mode):
        st.session_state.stealth_mode = True
    else:
        st.session_state.stealth_mode = False
    st.write("---")
    st.markdown('<a href="https://google.com" target="_self"><button style="width:100%; background:red; color:white; border-radius:5px; border:none; padding:10px; cursor:pointer;">⚠️ EMERGENCY EXIT</button></a>', unsafe_allow_html=True)

if st.session_state.stealth_mode:
    st.title("Module 4: Differential Equations")
    st.info("Current Topic: Linear Second-Order Equations with Constant Coefficients")
    st.markdown("### Overview\nIn this section, we explore methodology for solving differential equations...")
    st.image("https://wikimedia.org", caption="Fig 1.2: Sinusoidal Variance")
else:
    col1, col2 = st.columns([1, 5])
    with col1:
        if os.path.exists("static/slope/an33shlogo.jpg"):
            st.image("static/slope/an33shlogo.jpg", width=100)
    with col2:
        st.title("AN33SHPORTAL 🐦‍🔥")
        st.caption("URL: about:blank | STATUS: CLOAKED")

    game_dir = "static/slope"
    if os.path.exists(game_dir): 
        all_files = sorted([f for f in os.listdir(game_dir) if f.endswith(".html")])
        search_col, page_col = st.columns([3, 1])
        with search_col:
            query = st.text_input("🔍 Search games...", placeholder="FNAF, Slope...").lower()
        
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
                            b64 = base64.b64encode(binary_data).decode()
                        js = f"""<button onclick="var target = window.parent || window; var w=target.open('about:blank'); w.document.write(atob('{b64}')); w.document.close();" style="width:100%; height:40px; background:#ff4b4b; color:white; border:none; border-radius:8px; cursor:pointer;">🚀 LAUNCH STEALTH</button>"""
                        st.components.v1.html(js, height=50)
                        st.download_button("📥 Download HTML", binary_data, file_name=file_name, key=f"dl_{file_name}")
    else:
        st.error("Game folder not found!")
