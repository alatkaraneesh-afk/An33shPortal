import streamlit as st
import os
import base64
import random

# --- 1. NOTIFICATION SYSTEM (Reads from File) ---
NOTIF_FILE = "notifications.txt"

def get_latest_notif():
    if os.path.exists(NOTIF_FILE):
        with open(NOTIF_FILE, "r") as f:
            return f.read()
    return "No new updates."

def save_notif(text):
    # This only works if you are running locally or use GitHub API
    # For a quick fix, you can manually edit notifications.txt on GitHub
    with open(NOTIF_FILE, "w") as f:
        f.write(text)

# --- 2. SETUP & UI STYLE ---
if 'stealth_mode' not in st.session_state:
    st.session_state.stealth_mode = True

# [Keep your Page Config and CSS from the previous turn here]

# --- 3. SIDEBAR ---
with st.sidebar:
    if st.session_state.stealth_mode:
        st.markdown("### Resources")
        # [Keep your Resource Captions here]
    else:
        # SHOW THE BROADCAST TO USERS
        st.markdown("### 📢 SYSTEM BROADCAST")
        st.info(get_latest_notif())
        
        st.markdown('<div class="spy-warning">IF YOU SUSPECT A TEACHER IS SPYING...</div>', unsafe_allow_html=True)
        
        # SECRET ADMIN SECTION (Hidden at bottom of Game Sidebar)
        with st.expander("🛠️ DEV TOOLS"):
            new_msg = st.text_input("Type Broadcast Message:")
            if st.button("SEND TO ALL USERS"):
                # NOTE: Saving to file only works in your local dev or via GitHub Action
                # To make this live, you'd manually edit notifications.txt in GitHub
                st.success("Message Prepared! Update notifications.txt in GitHub.")

    # [Keep Ghost Bar logic here]

# --- 4. GAME HUB ---
if not st.session_state.stealth_mode:
    # This shows the notification as a "Toast" the second they unlock the portal
    st.toast(f"BROADCAST: {get_latest_notif()}", icon="📢")
    
    # [Keep the rest of your Game Hub code here]
