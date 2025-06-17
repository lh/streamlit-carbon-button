"""
Demonstrates all four button types in the Carbon Design System.
"""

import streamlit as st
from streamlit_carbon_button import carbon_button

st.title("Carbon Button Types")
st.write(
    "Carbon Design System includes four button types, each with a specific purpose."
)

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.subheader("Primary")
    st.write("For main actions")
    if carbon_button("Save", key="primary"):
        st.success("Primary clicked!")

with col2:
    st.subheader("Secondary")
    st.write("For secondary actions")
    if carbon_button("Cancel", key="secondary", button_type="secondary"):
        st.info("Secondary clicked!")

with col3:
    st.subheader("Danger")
    st.write("For destructive actions")
    if carbon_button("Delete", key="danger", button_type="danger"):
        st.error("Danger clicked!")

with col4:
    st.subheader("Ghost")
    st.write("For minimal emphasis")
    if carbon_button("Learn more", key="ghost", button_type="ghost"):
        st.info("Ghost clicked!")

# Visual comparison
st.divider()
st.subheader("Visual Comparison")

# Show all types in a row
cols = st.columns(4)
types = ["primary", "secondary", "danger", "ghost"]

for col, btn_type in zip(cols, types):
    with col:
        carbon_button(
            f"{btn_type.title()} Button",
            key=f"compare_{btn_type}",
            button_type=btn_type,
        )

# Best practices
st.divider()
st.subheader("Best Practices")

st.info(
    """
**When to use each type:**

🔵 **Primary**: One per section, for the main action (Save, Submit, Continue)

⭕ **Secondary**: Alternative actions (Cancel, Back, Reset)

🔴 **Danger**: Destructive actions that can't be undone (Delete, Remove)

👻 **Ghost**: Low-emphasis actions (Help, Learn more, Advanced settings)
"""
)
