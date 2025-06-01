"""Test the installed streamlit-carbon-button package"""

import streamlit as st

# Import from the installed package
from streamlit_carbon_button import carbon_button, CarbonIcons

st.title("🎉 Installed Package Test")
st.write("Testing streamlit-carbon-button from PyPI package")

# Test basic button
if carbon_button("It works!", button_type="primary", is_default=True):
    st.balloons()
    st.success("Package installed successfully!")

# Test with icon
if carbon_button("Save", icon=CarbonIcons.SAVE, button_type="secondary"):
    st.info("Save button clicked")

# Test icon-only with aria
if carbon_button("Delete item", icon=CarbonIcons.DELETE, button_type="danger", aria_label="Delete selected items permanently"):
    st.error("Delete clicked")

st.success("✅ All imports working from streamlit_carbon_button package!")