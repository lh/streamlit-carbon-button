"""Demo showing dynamic default button switching"""

import streamlit as st
from streamlit_carbon_button import carbon_button, CarbonIcons

st.set_page_config(page_title="Dynamic Default Button", layout="wide")

st.title("🔄 Dynamic Default Button Switching")
st.write("Shows how to change which button is the default based on application state")

# Example 1: Save workflow
st.header("1. Save Workflow Example")

# Initialize state
if 'unsaved_changes' not in st.session_state:
    st.session_state.unsaved_changes = False
if 'confirm_mode' not in st.session_state:
    st.session_state.confirm_mode = False

# Simulate making changes
col1, col2 = st.columns([3, 1])
with col1:
    text = st.text_area("Document content", value="Edit this text to enable save...", key="doc_content")
    
    # Detect changes
    if 'last_content' not in st.session_state:
        st.session_state.last_content = text
    
    if text != st.session_state.last_content:
        st.session_state.unsaved_changes = True

with col2:
    if st.session_state.unsaved_changes:
        st.warning("Unsaved changes")
    else:
        st.success("All saved")

# Button row
col1, col2, col3 = st.columns(3)

with col1:
    # Save button is default when there are unsaved changes and we're not in confirm mode
    if carbon_button(
        "Save", 
        key="save_btn",
        button_type="primary",
        icon=CarbonIcons.SAVE,
        is_default=st.session_state.unsaved_changes and not st.session_state.confirm_mode,
        disabled=not st.session_state.unsaved_changes
    ):
        st.session_state.confirm_mode = True

with col2:
    # This button becomes default when in confirm mode
    if st.session_state.confirm_mode:
        if carbon_button(
            "Are you sure?", 
            key="confirm_save",
            button_type="danger",
            icon=CarbonIcons.WARNING,
            is_default=True
        ):
            st.session_state.last_content = text
            st.session_state.unsaved_changes = False
            st.session_state.confirm_mode = False
            st.success("Document saved!")
            st.rerun()

with col3:
    if carbon_button("Cancel", key="cancel_save", button_type="ghost"):
        st.session_state.confirm_mode = False
        st.rerun()

# Example 2: Multi-step form
st.header("2. Multi-Step Form Example")

# Initialize step
if 'form_step' not in st.session_state:
    st.session_state.form_step = 1

# Progress indicator
progress = st.session_state.form_step / 3
st.progress(progress)
st.write(f"Step {st.session_state.form_step} of 3")

# Different content for each step
if st.session_state.form_step == 1:
    st.subheader("Personal Information")
    name = st.text_input("Full Name", key="form_name")
    email = st.text_input("Email", key="form_email")
    
elif st.session_state.form_step == 2:
    st.subheader("Preferences")
    st.selectbox("Favorite Color", ["Red", "Blue", "Green"], key="form_color")
    st.slider("Experience Level", 1, 10, 5, key="form_level")
    
else:
    st.subheader("Review & Submit")
    st.write("**Summary:**")
    st.write(f"- Name: {st.session_state.get('form_name', 'Not provided')}")
    st.write(f"- Email: {st.session_state.get('form_email', 'Not provided')}")
    st.write(f"- Color: {st.session_state.get('form_color', 'Not selected')}")
    st.write(f"- Level: {st.session_state.get('form_level', 'Not set')}")

# Navigation buttons
col1, col2, col3 = st.columns(3)

with col1:
    if st.session_state.form_step > 1:
        if carbon_button("Previous", key="prev_step", button_type="ghost"):
            st.session_state.form_step -= 1
            st.rerun()

with col2:
    # The primary action changes based on the step
    if st.session_state.form_step < 3:
        # "Next" is default for steps 1 and 2
        if carbon_button(
            "Next", 
            key="next_step",
            button_type="primary",
            icon=CarbonIcons.PLAY,
            is_default=True
        ):
            st.session_state.form_step += 1
            st.rerun()
    else:
        # "Submit" is default for the final step
        if carbon_button(
            "Submit", 
            key="submit_form",
            button_type="primary",
            icon=CarbonIcons.SUCCESS,
            is_default=True
        ):
            st.success("Form submitted successfully! 🎉")
            st.balloons()
            # Reset form
            st.session_state.form_step = 1

with col3:
    if carbon_button("Cancel", key="cancel_form", button_type="ghost"):
        st.session_state.form_step = 1
        st.info("Form cancelled")
        st.rerun()

# Example 3: Dynamic action based on selection
st.header("3. Context-Sensitive Default")

# Selection changes the default action
action = st.radio(
    "What would you like to do?",
    ["View Report", "Edit Data", "Delete Record"],
    horizontal=True
)

col1, col2, col3, col4 = st.columns(4)

with col1:
    if carbon_button(
        "View", 
        key="view_btn",
        button_type="primary" if action == "View Report" else "secondary",
        icon=CarbonIcons.DOCUMENT,
        is_default=action == "View Report"
    ):
        st.info("Viewing report...")

with col2:
    if carbon_button(
        "Edit", 
        key="edit_btn",
        button_type="primary" if action == "Edit Data" else "secondary",
        icon=CarbonIcons.SETTINGS,
        is_default=action == "Edit Data"
    ):
        st.info("Opening editor...")

with col3:
    if carbon_button(
        "Delete", 
        key="delete_btn",
        button_type="danger",
        icon=CarbonIcons.DELETE,
        is_default=action == "Delete Record"
    ):
        st.error("Record deleted!")

with col4:
    if carbon_button("Cancel", key="cancel_action", button_type="ghost"):
        st.info("Action cancelled")

# Tips
st.divider()
st.info("""
**How Dynamic Default Buttons Work:**

1. **State-based**: Use `st.session_state` to track which button should be default
2. **Conditional**: Pass `is_default=condition` where condition evaluates to True/False
3. **Reactive**: Buttons automatically update their appearance when state changes
4. **Flexible**: Can change based on user input, form validation, workflow steps, etc.

**Best Practices:**
- Only one button should have `is_default=True` at a time in each context
- Use `st.rerun()` when needed to update button states
- Consider the user's most likely next action
- Default can change based on form completion, validation state, or user choices
""")