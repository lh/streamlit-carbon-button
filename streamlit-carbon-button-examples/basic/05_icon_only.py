"""
Icon-only buttons for toolbars and compact interfaces.
"""

import streamlit as st
from briquette import carbon_button, CarbonIcons

st.title("Icon-Only Buttons")
st.write("Create compact, professional toolbars with icon-only Carbon buttons.")

# Basic toolbar
st.subheader("📊 Document Toolbar")

toolbar = st.columns(8)
tools = [
    ("New", CarbonIcons.ADD, "secondary", False),
    ("Open", CarbonIcons.DOCUMENT, "secondary", False),
    ("Save", CarbonIcons.SAVE, "primary", True),  # Default button
    ("Copy", CarbonIcons.COPY, "secondary", False),
    ("Cut", CarbonIcons.CLOSE, "secondary", False),
    ("Paste", CarbonIcons.ADD, "secondary", False),
    ("Undo", CarbonIcons.PLAY, "ghost", False),
    ("Delete", CarbonIcons.DELETE, "danger", False),
]

for col, (name, icon, btn_type, is_default) in zip(toolbar, tools):
    with col:
        if carbon_button("", icon=icon, button_type=btn_type, is_default=is_default, key=f"tool_{name}"):
            st.toast(f"{name}")
        st.caption(name)

# Media controls
st.divider()
st.subheader("🎵 Media Player Controls")

col1, col2, col3 = st.columns([1, 3, 1])

with col2:
    media_controls = st.columns(5)
    
    # Previous
    with media_controls[0]:
        if carbon_button("", icon=CarbonIcons.PLAY, button_type="ghost", key="prev"):
            st.info("⏮️ Previous track")
    
    # Stop
    with media_controls[1]:
        if carbon_button("", icon=CarbonIcons.CLOSE, button_type="secondary", key="stop"):
            st.info("⏹️ Stopped")
    
    # Play (default)
    with media_controls[2]:
        if carbon_button("", icon=CarbonIcons.PLAY, button_type="primary", is_default=True, key="play"):
            st.success("▶️ Playing...")
    
    # Pause
    with media_controls[3]:
        if carbon_button("", icon=CarbonIcons.HELP, button_type="secondary", key="pause"):
            st.info("⏸️ Paused")
    
    # Next
    with media_controls[4]:
        if carbon_button("", icon=CarbonIcons.PLAY, button_type="ghost", key="next"):
            st.info("⏭️ Next track")

# Floating action buttons
st.divider()
st.subheader("➕ Floating Action Buttons")

col1, col2 = st.columns([4, 1])

with col1:
    st.write("Main content area...")
    st.write("Lorem ipsum dolor sit amet, consectetur adipiscing elit.")

with col2:
    st.write("**Quick Actions**")
    
    if carbon_button("", icon=CarbonIcons.ADD, button_type="primary", is_default=True, key="fab_add"):
        st.success("Creating new item...")
    
    if carbon_button("", icon=CarbonIcons.UPLOAD, button_type="secondary", key="fab_upload"):
        st.info("Upload dialog opened")
    
    if carbon_button("", icon=CarbonIcons.SETTINGS, button_type="ghost", key="fab_settings"):
        st.info("Settings panel opened")

# Icon grid
st.divider()
st.subheader("🎨 Icon Palette")
st.write("All available icons in a grid layout")

all_icons = [
    ("Upload", CarbonIcons.UPLOAD),
    ("Download", CarbonIcons.DOWNLOAD),
    ("Save", CarbonIcons.SAVE),
    ("Copy", CarbonIcons.COPY),
    ("Delete", CarbonIcons.DELETE),
    ("Add", CarbonIcons.ADD),
    ("Close", CarbonIcons.CLOSE),
    ("Settings", CarbonIcons.SETTINGS),
    ("Search", CarbonIcons.SEARCH),
    ("Filter", CarbonIcons.FILTER),
    ("Chart", CarbonIcons.CHART_BAR),
    ("Document", CarbonIcons.DOCUMENT),
    ("Play", CarbonIcons.PLAY),
    ("Help", CarbonIcons.HELP),
    ("Warning", CarbonIcons.WARNING),
    ("Home", CarbonIcons.HOME),
    ("Info", CarbonIcons.INFO),
    ("Success", CarbonIcons.SUCCESS),
]

# Create a 6-column grid
for i in range(0, len(all_icons), 6):
    cols = st.columns(6)
    for j, col in enumerate(cols):
        if i + j < len(all_icons):
            name, icon = all_icons[i + j]
            with col:
                if carbon_button("", icon=icon, button_type="ghost", key=f"grid_{name}"):
                    st.code(f"CarbonIcons.{name.upper()}")
                st.caption(name)

# Tips
st.divider()
st.info("""
**Tips for Icon-Only Buttons:**

💡 Always include captions or tooltips for accessibility
🎯 Use `is_default=True` on the primary action (like Save or Play)
📐 Icon-only buttons are perfect squares with equal padding
🎨 Mix button types to create visual hierarchy
♿ Consider adding aria-labels for screen readers (future feature)
""")
