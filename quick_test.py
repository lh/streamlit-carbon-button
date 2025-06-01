"""Quick test of Vite-built carbon button"""
import streamlit as st
from briquette import carbon_button, CarbonIcons

st.title("🚀 Vite Migration Test")

st.write("Testing carbon button built with Vite...")

# Basic test
if carbon_button("Click me!", key="test1"):
    st.balloons()
    st.success("✅ Button works!")

# Test with icon
col1, col2, col3 = st.columns(3)

with col1:
    if carbon_button("Save", icon=CarbonIcons.SAVE, key="save"):
        st.write("Saved!")

with col2:
    if carbon_button("Download", icon=CarbonIcons.DOWNLOAD, key="download", button_type="secondary"):
        st.write("Downloading...")

with col3:
    if carbon_button("Delete", icon=CarbonIcons.DELETE, key="delete", button_type="danger"):
        st.write("Deleted!")

# Full width test
if carbon_button("Full Width Button", key="full", use_container_width=True):
    st.info("Full width clicked!")

# Counter test
if 'count' not in st.session_state:
    st.session_state.count = 0

if carbon_button("Count", key="counter"):
    st.session_state.count += 1

st.metric("Click Count", st.session_state.count)