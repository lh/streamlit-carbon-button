"""Test the default button feature with teal shadow"""

import streamlit as st
from streamlit_carbon_button import carbon_button, CarbonIcons

st.set_page_config(page_title="Default Button Test", layout="wide")

st.title("🎯 Default Button Feature Test")
st.write("Testing the teal shadow indicator for default buttons")

st.info("Click and hold any button to see it turn teal. The default button has a teal shadow.")

# Test 1: Form context
st.header("1. Form Context")
st.write("The 'Submit' button is marked as the default action")

col1, col2, col3 = st.columns([3, 1, 1])

with col1:
    st.text_input("Enter your email", placeholder="you@example.com", key="email_test")

with col2:
    if carbon_button("Submit", key="submit", button_type="primary", icon=CarbonIcons.SUCCESS, is_default=True):
        st.success("Form submitted!")
        st.balloons()

with col3:
    if carbon_button("Cancel", key="cancel", button_type="ghost"):
        st.info("Cancelled")

# Test 2: Action group
st.header("2. Action Group")
st.write("The 'Publish' button is marked as the default action")

col1, col2, col3, col4 = st.columns(4)

with col1:
    if carbon_button("Save Draft", key="draft", button_type="secondary"):
        st.info("Draft saved")

with col2:
    if carbon_button("Publish", key="publish", button_type="primary", icon=CarbonIcons.UPLOAD, is_default=True):
        st.success("Published! 🎉")

with col3:
    if carbon_button("Preview", key="preview", button_type="ghost"):
        st.info("Opening preview...")

with col4:
    if carbon_button("Delete", key="delete", button_type="danger", icon=CarbonIcons.DELETE):
        st.error("Deleted")

# Test 3: Dialog buttons
st.header("3. Dialog Context")
st.write("The 'Yes, Delete' button is marked as default (even though it's dangerous)")

with st.container():
    st.warning("Are you sure you want to delete this item? This action cannot be undone.")
    
    col1, col2, col3 = st.columns([1, 1, 3])
    
    with col1:
        if carbon_button("Yes, Delete", key="confirm_delete", button_type="danger", is_default=True):
            st.error("Item deleted permanently!")
    
    with col2:
        if carbon_button("Cancel", key="cancel_delete", button_type="ghost"):
            st.info("Action cancelled")

# Test 4: Mixed button types
st.header("4. Different Button Types")
st.write("Testing default indicator with different button types")

cols = st.columns(4)

button_configs = [
    ("Primary Default", "primary", True),
    ("Secondary Default", "secondary", True),
    ("Regular Primary", "primary", False),
    ("Regular Secondary", "secondary", False),
]

for i, (col, (label, btn_type, is_def)) in enumerate(zip(cols, button_configs)):
    with col:
        st.write(f"**{label}**")
        if carbon_button(label, key=f"test_{i}", button_type=btn_type, is_default=is_def):
            st.success(f"{label} clicked!")

# Test 5: State changes
st.header("5. Button State Tests")
st.write("Verify hover and active states work correctly")

col1, col2 = st.columns(2)

with col1:
    st.write("**Regular Button States:**")
    st.caption("Normal → Hover (elevated) → Active (teal)")
    if carbon_button("Test States", key="state_regular", button_type="primary"):
        st.write("Regular button clicked")

with col2:
    st.write("**Default Button States:**")
    st.caption("Teal shadow → Enhanced hover → Active (teal)")
    if carbon_button("Test States", key="state_default", button_type="primary", is_default=True):
        st.write("Default button clicked")

# Visual guide
st.divider()
st.header("Visual Guide")

st.markdown("""
**What to look for:**

1. **Default buttons** have a subtle teal shadow and are slightly elevated
2. **On hover**, default buttons lift higher and the shadow intensifies
3. **When clicked**, all buttons turn teal (this is the existing behavior)
4. Only **one button per context** should be marked as default

**Use cases for default buttons:**
- Submit/Save buttons in forms
- Primary actions in dialogs
- The most likely next action in a workflow
- Dangerous actions that need confirmation (to prevent accidental clicks elsewhere)
""")

st.divider()
st.caption("💡 Tip: The teal shadow color matches the active state color, creating visual consistency")