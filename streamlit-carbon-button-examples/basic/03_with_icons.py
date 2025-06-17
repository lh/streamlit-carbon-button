"""
Using Carbon icons with buttons.
"""

import streamlit as st
from streamlit_carbon_button import carbon_button, CarbonIcons

st.title("Carbon Buttons with Icons")
st.write("Enhance your buttons with 18 available Carbon icons.")

# Icon showcase
st.subheader("Available Icons")

# Group icons by category
icon_categories = {
    "File Operations": [
        ("Upload", CarbonIcons.UPLOAD),
        ("Download", CarbonIcons.DOWNLOAD),
        ("Save", CarbonIcons.SAVE),
        ("Copy", CarbonIcons.COPY),
        ("Document", CarbonIcons.DOCUMENT),
    ],
    "Actions": [
        ("Add", CarbonIcons.ADD),
        ("Delete", CarbonIcons.DELETE),
        ("Close", CarbonIcons.CLOSE),
        ("Search", CarbonIcons.SEARCH),
        ("Filter", CarbonIcons.FILTER),
        ("Play", CarbonIcons.PLAY),
    ],
    "UI Elements": [
        ("Settings", CarbonIcons.SETTINGS),
        ("Home", CarbonIcons.HOME),
        ("Chart", CarbonIcons.CHART_BAR),
    ],
    "Feedback": [
        ("Success", CarbonIcons.SUCCESS),
        ("Warning", CarbonIcons.WARNING),
        ("Info", CarbonIcons.INFO),
        ("Help", CarbonIcons.HELP),
    ],
}

for category, icons in icon_categories.items():
    st.write(f"**{category}**")
    cols = st.columns(len(icons))

    for col, (name, icon) in zip(cols, icons):
        with col:
            if carbon_button(name, icon=icon, key=f"icon_{name}"):
                st.success(f"{name} clicked!")

# Practical examples
st.divider()
st.subheader("Practical Examples")

col1, col2 = st.columns(2)

with col1:
    st.write("**File Operations**")
    if carbon_button("Upload File", icon=CarbonIcons.UPLOAD, button_type="primary"):
        st.info("Opening file picker...")

    if carbon_button(
        "Download Report", icon=CarbonIcons.DOWNLOAD, button_type="secondary"
    ):
        st.info("Downloading...")

with col2:
    st.write("**Form Actions**")
    if carbon_button("Save Draft", icon=CarbonIcons.SAVE, button_type="secondary"):
        st.success("Draft saved!")

    if carbon_button("Delete Draft", icon=CarbonIcons.DELETE, button_type="danger"):
        st.error("Draft deleted!")

# Icon-only buttons
st.divider()
st.subheader("Icon-Only Buttons")
st.write("Perfect for toolbars and compact interfaces")

toolbar_cols = st.columns(6)
toolbar_buttons = [
    ("New", CarbonIcons.ADD, "primary"),
    ("Open", CarbonIcons.DOCUMENT, "secondary"),
    ("Save", CarbonIcons.SAVE, "secondary"),
    ("Copy", CarbonIcons.COPY, "secondary"),
    ("Settings", CarbonIcons.SETTINGS, "ghost"),
    ("Delete", CarbonIcons.DELETE, "danger"),
]

for col, (name, icon, btn_type) in zip(toolbar_cols, toolbar_buttons):
    with col:
        if carbon_button("", icon=icon, button_type=btn_type, key=f"toolbar_{name}"):
            st.toast(f"{name} action triggered!")
        st.caption(name)
