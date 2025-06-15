"""
Basic usage example for Streamlit Carbon Button Component
"""

import streamlit as st
from streamlit_carbon_button import carbon_button, CarbonIcons

st.set_page_config(page_title="Carbon Button Example")

st.title("Carbon Button Examples")

# Basic button
if carbon_button("Click Me", key="basic"):
    st.success("Button clicked!")

# Button with icon
col1, col2, col3 = st.columns(3)

with col1:
    if carbon_button("Save", icon=CarbonIcons.SAVE, key="save"):
        st.info("Saved!")

with col2:
    if carbon_button("Upload", icon=CarbonIcons.UPLOAD, key="upload"):
        st.info("Uploaded!")

with col3:
    if carbon_button("Delete", icon=CarbonIcons.DELETE, key="delete", button_type="danger"):
        st.warning("Deleted!")

# Icon-only buttons
st.subheader("Icon Toolbar")
cols = st.columns(6)
icons = [
    (CarbonIcons.HOME, "home", "Home"),
    (CarbonIcons.SEARCH, "search", "Search"),
    (CarbonIcons.FILTER, "filter", "Filter"),
    (CarbonIcons.SETTINGS, "settings", "Settings"),
    (CarbonIcons.INFO, "info", "Info"),
    (CarbonIcons.HELP, "help", "Help"),
]

for i, (icon, key, label) in enumerate(icons):
    with cols[i]:
        if carbon_button("", icon=icon, key=key, button_type="ghost"):
            st.toast(label)

# Full width button
st.subheader("Full Width")
if carbon_button("Process All Files", icon=CarbonIcons.PLAY, key="process", use_container_width=True):
    with st.spinner("Processing..."):
        import time
        time.sleep(1)
    st.success("Complete!")