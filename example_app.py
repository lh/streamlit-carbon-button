#!/usr/bin/env python3
"""
Simple example app demonstrating carbon-button usage
"""

import streamlit as st
from streamlit_carbon_button import carbon_button, CarbonIcons

st.set_page_config(page_title="Carbon Button Examples", page_icon="🔘")

st.title("🔘 Carbon Button Examples")
st.markdown("Quick examples of `streamlit-carbon-button` in action")

# Basic buttons
st.header("Basic Button Types")
col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    if carbon_button("Primary", button_type="primary"):
        st.success("Primary clicked!")

with col2:
    if carbon_button("Secondary", button_type="secondary"):
        st.info("Secondary clicked!")

with col3:
    if carbon_button("Tertiary", button_type="tertiary"):
        st.info("Tertiary clicked!")

with col4:
    if carbon_button("Danger", button_type="danger"):
        st.error("Danger clicked!")

with col5:
    if carbon_button("Ghost", button_type="ghost"):
        st.info("Ghost clicked!")

# Icon buttons
st.header("Icon Buttons")
col1, col2, col3, col4 = st.columns(4)

with col1:
    if carbon_button("Save", icon=CarbonIcons.SAVE, button_type="primary"):
        st.success("Saved!")

with col2:
    if carbon_button("Delete", icon=CarbonIcons.DELETE, button_type="danger"):
        st.error("Deleted!")

with col3:
    if carbon_button("Download", icon=CarbonIcons.DOWNLOAD):
        st.info("Downloading...")

with col4:
    if carbon_button("Settings", icon=CarbonIcons.SETTINGS):
        st.info("Opening settings...")

# Icon-only buttons
st.header("Icon-Only Buttons (No Labels)")
cols = st.columns(8)
icons = [
    (CarbonIcons.ADD, "Add"),
    (CarbonIcons.EDIT, "Edit"),
    (CarbonIcons.COPY, "Copy"),
    (CarbonIcons.DELETE, "Delete"),
    (CarbonIcons.SAVE, "Save"),
    (CarbonIcons.VIEW, "View"),
    (CarbonIcons.FILTER, "Filter"),
    (CarbonIcons.SEARCH, "Search"),
]

for idx, (icon, name) in enumerate(icons):
    with cols[idx]:
        if carbon_button("", icon=icon, key=f"icon_{name}"):
            st.toast(f"{name} clicked!")

# Practical example
st.header("Practical Example: Data Table Actions")

# Mock data
data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Status": ["Active", "Inactive", "Active"],
    "Score": [95, 82, 88],
}

for idx, name in enumerate(data["Name"]):
    col1, col2, col3, col4, col5 = st.columns([3, 2, 1, 1, 1])

    with col1:
        st.write(f"**{name}**")

    with col2:
        st.write(data["Status"][idx])

    with col3:
        st.write(data["Score"][idx])

    with col4:
        if carbon_button(
            "", icon=CarbonIcons.EDIT, key=f"edit_{idx}", button_type="ghost"
        ):
            st.info(f"Edit {name}")

    with col5:
        if carbon_button(
            "", icon=CarbonIcons.DELETE, key=f"delete_{idx}", button_type="ghost"
        ):
            st.warning(f"Delete {name}")

# File operations
st.header("File Operations")
col1, col2, col3 = st.columns(3)

with col1:
    if carbon_button("Upload CSV", icon=CarbonIcons.CSV, button_type="secondary"):
        st.info("Upload dialog would open...")

with col2:
    if carbon_button("Export PDF", icon=CarbonIcons.PDF, button_type="secondary"):
        st.info("Generating PDF...")

with col3:
    if carbon_button("Download ZIP", icon=CarbonIcons.ZIP, button_type="secondary"):
        st.info("Creating archive...")

# View controls
st.header("View Controls")
view_cols = st.columns(6)

with view_cols[0]:
    if carbon_button("", icon=CarbonIcons.ZOOM_IN):
        st.toast("Zoom in")

with view_cols[1]:
    if carbon_button("", icon=CarbonIcons.ZOOM_OUT):
        st.toast("Zoom out")

with view_cols[2]:
    if carbon_button("", icon=CarbonIcons.ZOOM_FIT):
        st.toast("Fit to screen")

with view_cols[3]:
    if carbon_button("", icon=CarbonIcons.EXPAND_ALL):
        st.toast("Expand all")

with view_cols[4]:
    if carbon_button("", icon=CarbonIcons.COLLAPSE_ALL):
        st.toast("Collapse all")

with view_cols[5]:
    if carbon_button("", icon=CarbonIcons.VIEW):
        st.toast("Toggle view")
