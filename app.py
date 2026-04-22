import streamlit as st

st.set_page_config(page_title="Educational Research Portal", page_icon="📖")

st.title("Project Resource Gateway")
st.write("If local modules are restricted, use the Google Cloud Gateway to mirror the resource.")

# This trick uses Google Translate to 'cloak' the traffic.
# iboss sees 'google.com', not the game site.
def get_proxy_link(target_url):
    return f"https://google.com{target_url}"

# Mirror links (These are your 'Gateways')
gateways = {
    "Snow Rider 3D": "https://github.io",
    "Slope": "https://kdata1.com",
    "1v1.LOL": "https://1v1.lol"
}

col1, col2 = st.columns(2)
for i, (name, url) in enumerate(gateways.items()):
    with (col1 if i % 2 == 0 else col2):
        st.subheader(name)
        st.link_button(f"🌐 Launch via Google Mirror", get_proxy_link(url))

st.info("""
**How to use:**
1. Click the button to open the mirror.
2. If it asks to translate, click **'Original'** or **'View Original Page'** in the top bar.
3. This tunnels the game through Google Translate's servers.
""")
