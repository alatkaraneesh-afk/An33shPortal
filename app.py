import streamlit as st
import os

# 1. Academic title to avoid attention
st.set_page_config(page_title="Data Archive Portal", page_icon="🗄️")

st.title("Resource Archive")
st.write("Authorized users: Download the source module to your local station.")

# 2. Path to your PURE game file
game_path = "static/slope/slopeoffline.html"

if os.path.exists(game_path):
    # Read the file on the SERVER (hidden from iBoss)
    with open(game_path, "rb") as f:
        file_data = f.read()
    
    # 3. Use the Streamlit native download button
    # This bypasses the browser's "New Tab" monitoring
    st.download_button(
        label="📥 DOWNLOAD SECURE MODULE (OFFLINE)",
        data=file_data,
        file_name="Module_Analysis_V4.html",
        mime="text/html"
    )

    st.success("✅ Ready for download.")
    st.info("""
    **UNBLOCKING STEPS:**
    1. Click the **Download** button.
    2. **Turn OFF your Wi-Fi** on the computer.
    3. Open the downloaded file from your 'Downloads' folder.
    4. Once the game loads, turn Wi-Fi back on. iBoss cannot stop a game that started offline!
    """)
else:
    st.error("Technical Error: File not found in static/slope/slopeoffline.html")
