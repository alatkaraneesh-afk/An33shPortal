import streamlit as st
import streamlit.components.v1 as components

# Page config for a gaming feel
st.set_page_config(page_title="An33shPortal", page_icon="🎮", layout="wide")

st.title("An33shPortal 🕹️")

# Sidebar navigation for games
game = st.sidebar.selectbox(
    "Select a Game",
    ["Home", "Snow Rider 3D", "Slope", "1v1.LOL"]
)

if game == "Home":
    st.write("### Welcome to the Portal!")
    st.info("Select a game from the sidebar to start playing immediately.")
    st.image("https://unsplash.com", caption="Level Up Your Gaming")

elif game == "Snow Rider 3D":
    st.subheader("Playing: Snow Rider 3D")
    # Embedding from a common unblocked source
    components.iframe("https://snowrider3d-online.gitlab.io/", height=600, scrolling=False)

elif game == "Slope":
    st.subheader("Playing: Slope")
    # Embedding Slope game
    components.iframe("https://kdata1.com", height=600, scrolling=False)

elif game == "1v1.LOL":
    st.subheader("Playing: 1v1.LOL")
    components.iframe("https://1v1.lol", height=600, scrolling=False)
