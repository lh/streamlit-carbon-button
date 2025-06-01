"""Test icon-only buttons with default feature"""

import streamlit as st
from briquette import carbon_button, CarbonIcons

st.set_page_config(page_title="Icon-Only Default Buttons", layout="wide")

st.title("🎯 Icon-Only Buttons with Default Feature")
st.write("Testing how the teal shadow works with icon-only buttons")

# Test 1: Toolbar with icon-only buttons
st.header("1. Toolbar Example")
st.write("Save button is marked as default")

col1, col2, col3, col4, col5, col6 = st.columns(6)

with col1:
    if carbon_button("", key="new_file", icon=CarbonIcons.ADD, button_type="secondary"):
        st.info("New file")
    st.caption("New")

with col2:
    if carbon_button("", key="open_file", icon=CarbonIcons.DOCUMENT, button_type="secondary"):
        st.info("Open file")
    st.caption("Open")

with col3:
    if carbon_button("", key="save_file", icon=CarbonIcons.SAVE, button_type="primary", is_default=True):
        st.success("File saved!")
    st.caption("**Save** ⭐")

with col4:
    if carbon_button("", key="copy_file", icon=CarbonIcons.COPY, button_type="secondary"):
        st.info("Copied")
    st.caption("Copy")

with col5:
    if carbon_button("", key="settings", icon=CarbonIcons.SETTINGS, button_type="ghost"):
        st.info("Settings")
    st.caption("Settings")

with col6:
    if carbon_button("", key="delete_file", icon=CarbonIcons.DELETE, button_type="danger"):
        st.error("Deleted")
    st.caption("Delete")

# Test 2: Media controls
st.header("2. Media Controls")
st.write("Play button is marked as default")

col1, col2, col3 = st.columns([1, 2, 1])

with col1:
    pass

with col2:
    # Center the controls
    c1, c2, c3, c4, c5 = st.columns(5)
    
    with c1:
        if carbon_button("", key="prev", icon=CarbonIcons.PLAY, button_type="ghost"):
            st.info("Previous")
        st.caption("Prev")
    
    with c2:
        if carbon_button("", key="stop", icon=CarbonIcons.CLOSE, button_type="secondary"):
            st.info("Stopped")
        st.caption("Stop")
    
    with c3:
        if carbon_button("", key="play", icon=CarbonIcons.PLAY, button_type="primary", is_default=True):
            st.success("Playing...")
        st.caption("**Play** ⭐")
    
    with c4:
        if carbon_button("", key="pause", icon=CarbonIcons.HELP, button_type="secondary"):
            st.info("Paused")
        st.caption("Pause")
    
    with c5:
        if carbon_button("", key="next", icon=CarbonIcons.PLAY, button_type="ghost"):
            st.info("Next")
        st.caption("Next")

with col3:
    pass

# Test 3: Mixed buttons (text vs icon-only)
st.header("3. Mixed Button Types")
st.write("Comparing default styling on text buttons vs icon-only buttons")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Text + Icon Buttons")
    if carbon_button("Save Document", key="save_text", icon=CarbonIcons.SAVE, button_type="primary", is_default=True):
        st.success("Saved with text!")
    
    if carbon_button("Delete Document", key="delete_text", icon=CarbonIcons.DELETE, button_type="danger"):
        st.error("Deleted with text!")

with col2:
    st.subheader("Icon-Only Buttons")
    cols = st.columns(2)
    
    with cols[0]:
        if carbon_button("", key="save_icon", icon=CarbonIcons.SAVE, button_type="primary", is_default=True):
            st.success("Saved!")
        st.caption("Save (default)")
    
    with cols[1]:
        if carbon_button("", key="delete_icon", icon=CarbonIcons.DELETE, button_type="danger"):
            st.error("Deleted!")
        st.caption("Delete")

# Test 4: Different button types as icon-only defaults
st.header("4. Icon-Only with Different Button Types")
st.write("Testing how teal shadow looks with different button types")

cols = st.columns(5)

button_configs = [
    ("Primary", "primary", CarbonIcons.SUCCESS),
    ("Secondary", "secondary", CarbonIcons.INFO),
    ("Danger", "danger", CarbonIcons.WARNING),
    ("Ghost", "ghost", CarbonIcons.HELP),
    ("Primary", "primary", CarbonIcons.HOME),
]

for i, (col, (btn_name, btn_type, icon)) in enumerate(zip(cols, button_configs)):
    with col:
        # Make the middle one (index 2) the default
        is_def = (i == 2)
        
        if carbon_button("", key=f"icon_type_{i}", button_type=btn_type, icon=icon, is_default=is_def):
            st.info(f"{btn_name} clicked")
        
        if is_def:
            st.caption(f"**{btn_name}** ⭐")
        else:
            st.caption(btn_name)

# Visual notes
st.divider()
st.info("""
**Icon-Only Button Observations:**

✅ **What works well:**
- Teal shadow is visible and distinctive on icon-only buttons
- The smaller size (equal padding) doesn't diminish the effect
- Shadow provides good visual hierarchy in toolbars

📐 **Design notes:**
- Icon-only buttons are perfect squares with equal padding
- The teal shadow adds ~4px visual space around the button
- Works especially well in toolbars and media controls

💡 **Use cases for icon-only defaults:**
- Play button in media controls
- Save button in toolbars
- Primary action in icon groups
- Most-used tool in a palette
""")

# Size comparison
st.header("5. Visual Size Comparison")

col1, col2, col3 = st.columns(3)

with col1:
    st.write("**Regular**")
    carbon_button("", key="size_regular", icon=CarbonIcons.SAVE, button_type="primary")
    st.caption("No shadow")

with col2:
    st.write("**Default**")
    carbon_button("", key="size_default", icon=CarbonIcons.SAVE, button_type="primary", is_default=True)
    st.caption("With teal shadow")

with col3:
    st.write("**For Reference**")
    carbon_button("Save File", key="size_text", icon=CarbonIcons.SAVE, button_type="primary", is_default=True)
    st.caption("Text button default")