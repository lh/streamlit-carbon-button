"""
Demonstrating the default button feature with teal shadow.
"""

import streamlit as st
from streamlit_carbon_button import carbon_button, CarbonIcons

st.title("Default Button Feature")
st.write("Use `is_default=True` to add a subtle teal shadow that indicates the primary action.")

# Simple example
st.subheader("Basic Usage")

col1, col2, col3 = st.columns([2, 1, 1])

with col1:
    email = st.text_input("Enter your email address")

with col2:
    # This button has the teal shadow
    if carbon_button("Subscribe", is_default=True, icon=CarbonIcons.SUCCESS):
        if email:
            st.balloons()
            st.success(f"✅ Subscribed {email} to our newsletter!")
        else:
            st.error("Please enter an email address")

with col3:
    if carbon_button("Cancel", button_type="ghost"):
        st.info("Cancelled")

# Form example
st.divider()
st.subheader("In a Form Context")

with st.form("login_form"):
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    remember = st.checkbox("Remember me")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        # Using form_submit_button for forms
        if st.form_submit_button("Sign In", type="primary"):
            st.success(f"Welcome back, {username}!")
    
    with col2:
        if st.form_submit_button("Reset Password", help="Click to reset password"):
            st.info("Password reset link sent!")

# Dynamic default
st.divider()
st.subheader("Dynamic Default Button")
st.write("The default button can change based on application state")

# Initialize state
if 'edit_mode' not in st.session_state:
    st.session_state.edit_mode = False

# Content area
content = st.text_area(
    "Document content",
    value="Edit this text to see the default button change...",
    disabled=not st.session_state.edit_mode
)

# Dynamic buttons
col1, col2, col3 = st.columns(3)

with col1:
    # Edit button is default when not in edit mode
    if carbon_button(
        "Edit",
        icon=CarbonIcons.SETTINGS,
        button_type="secondary",
        is_default=not st.session_state.edit_mode
    ):
        st.session_state.edit_mode = True
        st.rerun()

with col2:
    # Save button is default when in edit mode
    if carbon_button(
        "Save",
        icon=CarbonIcons.SAVE,
        button_type="primary",
        is_default=st.session_state.edit_mode,
        disabled=not st.session_state.edit_mode
    ):
        st.session_state.edit_mode = False
        st.success("Document saved!")
        st.rerun()

with col3:
    if carbon_button("Cancel", key="cancel_edit", button_type="ghost", disabled=not st.session_state.edit_mode):
        st.session_state.edit_mode = False
        st.rerun()

# Visual guide
st.divider()
st.info("""
**Default Button Best Practices:**

✅ **Do:**
- Use for the primary action users are most likely to take
- Have only one default button per context
- Use for form submissions, save actions, and confirmations

❌ **Don't:**
- Use for destructive actions (even if they're the primary action)
- Have multiple default buttons visible at once
- Use for cancel or close actions

The teal shadow color matches the button's active state, creating visual consistency.
""")
