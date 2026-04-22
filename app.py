import streamlit as st
import os

# 1. Page Configuration (Must be the very first Streamlit command)
st.set_page_config(page_title="An33shPortal", page_icon="🎮", layout="wide")

# 2. Custom CSS (Changed to st.html for better compatibility)
st.html("""
    <style>
    .main {
        background-color: #0e1117;
    }
    .stButton>button {
        width: 100%;
        border-radius: 10px;
        height: 3em;
        background-color: #262730;
        color: white;
        border: 1px solid #464b5d;
    }
    .stButton>button:hover {
        border-color: #ff4b4b;
        color: #ff4b4b;
    }
    </style>
""")

st.title("An33shPortal 🕹️")
st.write("---")

# 3. Path to your games
game_dir = "static/slope"

# 4. Logic to find and display games
if os.path.exists(game_dir):
    all_files = [f for f in os.listdir(game_dir) if f.endswith(".html") and f not in ["404.html", "index.html", "update.html", "detail.html", "list.html"]]
    
    search_query = st.text_input("🔍 Search over 100+ unblocked games...", "").lower()
    filtered_games = [f for f in all_files if search_query in f.lower()]
    
    st.write(f"Showing {len(filtered_games)} games")

    # 5. Display in a 3-column grid
    cols = st.columns(3)
    for i, file_name in enumerate(sorted(filtered_games)):
        clean_name = file_name.replace(".html", "").replace("-", " ").title()
        with cols[i % 3]:
            # The 'app/static/...' path is the magic link for Streamlit Cloud
            st.link_button(f"{clean_name}", f"app/static/slope/{file_name}")

else:
    st.error("⚠️ Error: 'static/slope' folder not found. Please check your GitHub folder structure.")
    st.info("Ensure you have a folder named 'static' and a folder inside it named 'slope'.")

st.write("---")
st.caption("An33shPortal | Unblocked for School Use")
