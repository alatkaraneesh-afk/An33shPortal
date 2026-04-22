import streamlit as st
import os

# 1. Page Configuration
st.set_page_config(page_title="An33shPortal", page_icon="🎮", layout="wide")

# Custom CSS to make it look like a gaming site
st.markdown("""
    <style>
    .main {
        background-color: #0e1117;
    }
    stButton>button {
        width: 100%;
        border-radius: 10px;
        height: 3em;
        background-color: #262730;
        color: white;
        border: 1px solid #464b5d;
    }
    stButton>button:hover {
        border-color: #ff4b4b;
        color: #ff4b4b;
    }
    </style>
    """, unsafe_allow_index=True)

st.title("An33shPortal 🕹️")
st.write("---")

# 2. Path to your games
# Streamlit looks in 'static/slope' on GitHub
game_dir = "static/slope"

# 3. Logic to find and display games
if os.path.exists(game_dir):
    # Get all .html files but skip technical ones like 404 or index
    all_files = [f for f in os.listdir(game_dir) if f.endswith(".html") and f not in ["404.html", "index.html", "update.html", "detail.html", "list.html"]]
    
    # Search bar
    search_query = st.text_input("🔍 Search over 100+ unblocked games...", "").lower()
    
    # Filter games based on search
    filtered_games = [f for f in all_files if search_query in f.lower()]
    
    st.write(f"Showing {len(filtered_games)} games")

    # 4. Display in a 3-column grid
    cols = st.columns(3)
    for i, file_name in enumerate(sorted(filtered_games)):
        # Clean up the name (e.g., 'subway-surfers.html' -> 'Subway Surfers')
        clean_name = file_name.replace(".html", "").replace("-", " ").title()
        
        with cols[i % 3]:
            # The 'app/static/...' path is the magic link for Streamlit Cloud
            st.link_button(f"{clean_name}", f"app/static/slope/{file_name}")

else:
    st.error("⚠️ Error: 'static/slope' folder not found. Please check your GitHub folder structure.")
    st.info("Make sure you have a folder named 'static' and a folder inside it named 'slope'.")

# 5. Footer
st.write("---")
st.caption("An33shPortal | Hosted on Streamlit | Unblocked for School Use")
