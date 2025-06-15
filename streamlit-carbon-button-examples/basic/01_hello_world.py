"""
Simplest possible example of a Carbon button.
"""

import streamlit as st
from streamlit_carbon_button import carbon_button

st.title("Hello Carbon Button! 👋")

if carbon_button("Click me!"):
    st.balloons()
    st.success("🎉 You clicked the button!")
