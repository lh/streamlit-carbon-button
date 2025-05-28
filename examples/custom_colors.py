"""
Custom color example for Streamlit Carbon Button Component
"""

import streamlit as st
from briquette import carbon_button, CarbonIcons

st.set_page_config(page_title="Custom Color Carbon Buttons")

st.title("Custom Color Carbon Buttons")

# Default styling
st.subheader("Default Styling")
if carbon_button("Default Button", icon=CarbonIcons.PLAY, key="default"):
    st.write("Using default grey with teal accent")

# Custom purple theme
st.subheader("Purple Theme")
purple_colors = {
    "rest_bg": "#6929c4",
    "rest_text": "#ffffff",
    "hover_bg": "#491d8b",
    "hover_text": "#ffffff",
    "active_bg": "#31135e",
    "active_text": "#ffffff"
}

if carbon_button("Purple Button", icon=CarbonIcons.STAR, colors=purple_colors, key="purple"):
    st.write("Custom purple theme!")

# Custom teal theme (matching logo)
st.subheader("Teal Theme")
teal_colors = {
    "rest_bg": "#009d9a",
    "rest_text": "#ffffff",
    "hover_bg": "#007d79",
    "hover_text": "#ffffff",
    "active_bg": "#005a5a",
    "active_text": "#ffffff"
}

if carbon_button("Teal Button", icon=CarbonIcons.SUCCESS, colors=teal_colors, key="teal"):
    st.write("Teal to match your logo!")

# Minimal grey theme
st.subheader("Minimal Grey")
grey_colors = {
    "rest_bg": "#f4f4f4",
    "rest_text": "#161616",
    "hover_bg": "#e0e0e0",
    "hover_text": "#161616",
    "active_bg": "#161616",
    "active_text": "#ffffff"
}

if carbon_button("Minimal Grey", icon=CarbonIcons.DOCUMENT, colors=grey_colors, key="grey"):
    st.write("Ultra minimal style!")

# Create your own
st.subheader("Create Your Own")
st.code("""
custom_colors = {
    "rest_bg": "#your_color",      # Normal background
    "rest_text": "#your_color",    # Normal text/icon
    "hover_bg": "#your_color",     # Hover background
    "hover_text": "#your_color",   # Hover text/icon
    "active_bg": "#your_color",    # Click background
    "active_text": "#your_color"   # Click text/icon
}

carbon_button("Custom", colors=custom_colors, key="custom")
""")