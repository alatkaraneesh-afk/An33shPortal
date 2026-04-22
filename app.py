import streamlit as st
import os
import base64

# 1. Use a completely fake name to stay under the radar
st.set_page_config(page_title="Math Resource Hub", page_icon="📈")

st.title("Resource Dashboard: Section 4")
st.write("---")

# 2. Get your game files
game_dir = "static/slope"
if os.path.exists(game_dir):
    all_files = sorted([f for f in os.listdir(game_dir) if f.endswith(".html")])
    selected = st.selectbox("Select Module to Review:", all_files)

    if st.button("🔓 AUTHORIZE AND OPEN"):
        file_path = os.path.join(game_dir, selected)
        
        with open(file_path, "r", encoding="utf-8") as f:
            html_content = f.read()
        
        # This turns the whole game into a giant string of random letters
        # iBoss cannot 'read' this code to see that it's a game
        b64 = base64.b64encode(html_content.encode()).decode()
        
        # The 'Ghost' link
        # It opens as a 'data' object, which has no URL for iBoss to block
        data_url = f"data:text/html;base64,{b64}"
        
        st.markdown(f"""
            <a href="{data_url}" target="_blank" style="text-decoration: none;">
                <div style="
                    background-color: #00c853; 
                    color: white; 
                    padding: 20px; 
                    text-align: center; 
                    border-radius: 10px; 
                    font-weight: bold; 
                    cursor: pointer;
                    box-shadow: 0px 4px 10px rgba(0,0,0,0.3);">
                    ✅ MODULE AUTHORIZED: CLICK HERE TO VIEW
                </div>
            </a>
        """, unsafe_allow_html=True)
        
        st.caption("If this fails, iBoss is blocking 'Data URLs'. Try a different browser like Edge or Chrome.")
else:
    st.error("Technical Error: Resource files missing.")
