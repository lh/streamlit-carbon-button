"""
Demo: Using invisible icon to make text-only buttons same height as icon buttons
"""

import streamlit as st
from streamlit_carbon_button import carbon_button, CarbonIcons

st.set_page_config(page_title="Invisible Icon Demo", layout="wide")

st.title("Invisible Icon Demo")
st.write("Using `CarbonIcons.INVISIBLE` to align button heights")

st.markdown("---")

# Problem demonstration
st.subheader("❌ Problem: Misaligned button heights")
col1, col2, col3 = st.columns(3)

with col1:
    if carbon_button("Save", icon=CarbonIcons.SAVE, key="save1"):
        st.success("Saved!")

with col2:
    if carbon_button("No Icon", key="noicon1"):
        st.info("Clicked!")

with col3:
    if carbon_button("Delete", icon=CarbonIcons.DELETE, key="delete1"):
        st.error("Deleted!")

st.caption("Notice how the middle button (without icon) is shorter")

st.markdown("---")

# Solution
st.subheader("✅ Solution: Use invisible icon for text-only buttons")
col1, col2, col3 = st.columns(3)

with col1:
    if carbon_button("Save", icon=CarbonIcons.SAVE, key="save2"):
        st.success("Saved!")

with col2:
    if carbon_button("No Icon", icon=CarbonIcons.INVISIBLE, key="noicon2"):
        st.info("Clicked!")

with col3:
    if carbon_button("Delete", icon=CarbonIcons.DELETE, key="delete2"):
        st.error("Deleted!")

st.caption("Now all buttons have the same height!")

st.markdown("---")

# More examples
st.subheader("More Examples")

# Form example
st.write("**Form with aligned buttons:**")
col1, col2, col3, col4 = st.columns(4)

with col1:
    if carbon_button("Submit", icon=CarbonIcons.SUCCESS, key="submit", is_default=True):
        st.success("Submitted!")

with col2:
    if carbon_button(
        "Reset", icon=CarbonIcons.INVISIBLE, key="reset", button_type="secondary"
    ):
        st.info("Form reset")

with col3:
    if carbon_button(
        "Cancel", icon=CarbonIcons.INVISIBLE, key="cancel", button_type="ghost"
    ):
        st.info("Cancelled")

with col4:
    if carbon_button("Help", icon=CarbonIcons.HELP, key="help", button_type="ghost"):
        st.info("Opening help...")

st.markdown("---")

# Code example
st.subheader("How to use:")
st.code(
    """
from streamlit_carbon_button import carbon_button, CarbonIcons

# Regular button with icon
carbon_button("Save", icon=CarbonIcons.SAVE)

# Text-only button with invisible icon for consistent height
carbon_button("Text Only", icon=CarbonIcons.INVISIBLE)
""",
    language="python",
)

st.info(
    """
**Benefits of using invisible icon:**
- All buttons have consistent height
- Better visual alignment in button groups
- No need for CSS hacks or custom styling
- Works with all button types and states
"""
)
