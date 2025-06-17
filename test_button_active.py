"""Quick test to check if buttons still turn teal when pressed"""

import streamlit as st
from streamlit_carbon_button import carbon_button, CarbonIcons

st.title("Test Button Active State")
st.write("Click and hold to see if button turns teal")

col1, col2, col3 = st.columns(3)

with col1:
    st.write("Primary Button")
    if carbon_button("Click & Hold", key="test1", button_type="primary"):
        st.success("Clicked!")

with col2:
    st.write("Secondary Button")
    if carbon_button("Click & Hold", key="test2", button_type="secondary"):
        st.success("Clicked!")

with col3:
    st.write("With Icon")
    if carbon_button(
        "Click & Hold", key="test3", button_type="primary", icon=CarbonIcons.UPLOAD
    ):
        st.success("Clicked!")

st.info("The button should turn teal (#50e4e0) when you click and hold it")
