import streamlit as st
import os

# 1. Use a fake academic title to stay safe
st.set_page_config(page_title="Assignment Research Hub", page_icon="📝")

st.title("Resource Downloader 📥")
st.write("If the 'Launch' button is blocked, download the module to run it locally.")

# 2. Get your game files from the static folder
game_dir = "static/slope"
if os.path.exists(game_dir):
    all_files = sorted([f for f in os.listdir(game_dir) if f.endswith(".html")])
    selected = st.selectbox("Select Project Module:", all_files)

    file_path = os.path.join(game_dir, selected)
    
    # 3. Read the file as raw data
    with open(file_path, "rb") as f:
        file_data = f.read()
    
    # 4. Force a download instead of opening a tab
    # Schools almost never block downloading .html files for 'coding'
    st.download_button(
        label=f"💾 DOWNLOAD {selected.upper()} TO COMPUTER",
        data=file_data,
        file_name=f"Project_{selected}",
        mime="text/html"
    )

    st.warning("**HOW TO RUN (iBoss Proof):**")
    st.write("1. Click the **Download** button above.")
    st.write("2. Open your computer's **Downloads** folder.")
    st.write("3. Double-click the file to open it in Chrome/Firefox.")
    st.write("4. **Success!** Since the file is on your PC, iBoss cannot block it.")
else:
    st.error("Error: Game directory not found.")
