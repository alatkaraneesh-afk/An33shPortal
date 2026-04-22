import streamlit as st
import os
import base64

# 1. Faster Page Config
st.set_page_config(page_title="AN33SH PORTAL", page_icon="🐦‍🔥", layout="wide")

# Custom CSS for better UI (Cards & Hover effects)
st.markdown("""
    <style>
    .stButton>button { width: 100%; border-radius: 10px; height: 3em; font-weight: bold; }
    .game-card { background-color: #262730; padding: 20px; border-radius: 15px; border: 1px solid #444; }
    div[data-testid="stExpander"] { border: none !important; box-shadow: none !important; }
    </style>
""", unsafe_allow_html=True)

# 2. Header & Branding
col1, col2 = st.columns([1, 5])
with col1:
    if os.path.exists("static/slope/an33shlogo.jpg"):
        st.image("static/slope/an33shlogo.jpg", width=100)
with col2:
    st.title("AN33SHPORTAL 🐦‍🔥")
    st.caption("Your boy noticed IBoss is blocking everything lately. Dont worry, take these 300+ games including Minecraft, Among us, etc. Remember to keep the url blank!")
    st.caption("Email me suggestions at alatkaraneesh@gmail.com")
# 3. Game Discovery
game_dir = "static/slope"
if os.path.exists(game_dir): 
    all_files = sorted([f for f in os.listdir(game_dir) if f.endswith(".html")])
    
    # Search & Pagination
    search_col, page_col = st.columns([3, 1])
    with search_col:
        query = st.text_input("🔍 Search games...", placeholder="FNAF, Slope, Soccer...").lower()
    
    filtered_games = [f for f in all_files if query in f.lower()]
    
    # PAGINATION: Show 12 games per page to prevent lag
    games_per_page = 12
    n_pages = (len(filtered_games) // games_per_page) + 1
    with page_col:
        page = st.number_input("Page", min_value=1, max_value=n_pages, step=1)
    
    start_idx = (page - 1) * games_per_page
    end_idx = start_idx + games_per_page
    display_list = filtered_games[start_idx:end_idx]

    # 4. Grid Display (3 Columns)
    cols = st.columns(3)
    for i, file_name in enumerate(display_list):
        display_name = file_name.replace(".html", "").replace("_", " ").title()
        with cols[i % 3]:
            with st.container(border=True):
                st.subheader(display_name)
                
                # LAZY LOADING: We only convert to Base64 inside this expander 
                # This keeps the main page load instant
                with st.expander("🎮 Play / Download"):
                    # Only read file when someone clicks the expander
                    file_path = os.path.join(game_dir, file_name)
                    with open(file_path, "rb") as f:
                        binary_data = f.read()
                        b64_content = base64.b64encode(binary_data).decode()

                    # Stealth Launch Button
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
