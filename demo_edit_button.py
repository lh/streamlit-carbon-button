import streamlit as st
from streamlit_carbon_button import carbon_button, CarbonIcons

st.title("Edit Button Demo")

st.write("Testing the new EDIT icon:")

# Basic edit button
if carbon_button("Edit", icon=CarbonIcons.EDIT):
    st.success("Edit button clicked!")

# Different button types with edit icon
col1, col2, col3, col4 = st.columns(4)

with col1:
    if carbon_button("Edit", icon=CarbonIcons.EDIT, button_type="primary", key="edit1"):
        st.info("Primary edit clicked")

with col2:
    if carbon_button("Edit", icon=CarbonIcons.EDIT, button_type="secondary", key="edit2"):
        st.info("Secondary edit clicked")

with col3:
    if carbon_button("Edit", icon=CarbonIcons.EDIT, button_type="danger", key="edit3"):
        st.info("Danger edit clicked")

with col4:
    if carbon_button("Edit", icon=CarbonIcons.EDIT, button_type="ghost", key="edit4"):
        st.info("Ghost edit clicked")

# Full width edit button
st.write("Full width edit button:")
if carbon_button("Edit Document", icon=CarbonIcons.EDIT, use_container_width=True, key="edit_full"):
    st.success("Full width edit button clicked!")

# Edit button with custom colors
st.write("Custom colored edit button:")
custom_colors = {
    "rest_bg": "#2E7D32",
    "rest_text": "#FFFFFF",
    "hover_bg": "#388E3C",
    "hover_text": "#FFFFFF",
    "active_bg": "#1B5E20",
    "active_text": "#FFFFFF"
}
if carbon_button("Edit", icon=CarbonIcons.EDIT, colors=custom_colors, key="edit_custom"):
    st.success("Custom edit button clicked!")