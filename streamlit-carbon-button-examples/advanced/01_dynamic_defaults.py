"""
Dynamic default button switching based on application state.
"""

import streamlit as st
from streamlit_carbon_button import carbon_button, CarbonIcons

st.title("Dynamic Default Buttons")
st.write("Change which button is marked as default based on your app's state.")

# Example 1: Form validation
st.header("1. Form Validation Example")

# Form inputs
name = st.text_input("Name *")
email = st.text_input("Email *")
message = st.text_area("Message *")

# Validation
is_valid = all([name, email, message])

# Buttons with dynamic default
col1, col2 = st.columns(2)

with col1:
    # Submit is only default when form is valid
    if carbon_button(
        "Submit",
        button_type="primary",
        icon=CarbonIcons.SUCCESS,
        is_default=is_valid,
        disabled=not is_valid,
    ):
        st.success("Form submitted successfully!")
        st.balloons()

with col2:
    # Clear is default when form is invalid
    if carbon_button("Clear", button_type="ghost", is_default=not is_valid):
        st.rerun()

if not is_valid:
    st.warning("Please fill in all required fields")

# Example 2: Multi-step process
st.divider()
st.header("2. Multi-Step Wizard")

# Initialize step
if "wizard_step" not in st.session_state:
    st.session_state.wizard_step = 1

# Progress bar
progress = st.session_state.wizard_step / 3
st.progress(progress)
st.write(f"Step {st.session_state.wizard_step} of 3")

# Step content
if st.session_state.wizard_step == 1:
    st.subheader("Select Plan")
    plan = st.radio("Choose your plan", ["Basic", "Pro", "Enterprise"])

elif st.session_state.wizard_step == 2:
    st.subheader("Billing Information")
    card_number = st.text_input("Card Number")
    expiry = st.text_input("Expiry Date")

else:
    st.subheader("Confirm Order")
    st.success("Ready to complete your order!")

# Navigation with dynamic defaults
col1, col2, col3 = st.columns(3)

with col1:
    if st.session_state.wizard_step > 1:
        if carbon_button("← Previous", button_type="ghost"):
            st.session_state.wizard_step -= 1
            st.rerun()

with col2:
    if st.session_state.wizard_step < 3:
        # Next is default for steps 1-2
        if carbon_button("Next →", button_type="primary", is_default=True):
            st.session_state.wizard_step += 1
            st.rerun()
    else:
        # Complete is default for final step
        if carbon_button(
            "Complete Order",
            button_type="primary",
            icon=CarbonIcons.SUCCESS,
            is_default=True,
        ):
            st.success("Order completed! 🎉")
            st.session_state.wizard_step = 1

with col3:
    if carbon_button("Cancel", button_type="ghost"):
        st.session_state.wizard_step = 1
        st.info("Wizard cancelled")
        st.rerun()

# Example 3: Save state indicator
st.divider()
st.header("3. Document Save State")

# Initialize state
if "doc_saved" not in st.session_state:
    st.session_state.doc_saved = True
if "doc_content" not in st.session_state:
    st.session_state.doc_content = "Initial content..."

# Document editor
new_content = st.text_area("Document", value=st.session_state.doc_content, height=150)

# Detect changes
has_changes = new_content != st.session_state.doc_content

# Status indicator
if has_changes:
    st.warning("📝 Unsaved changes")
else:
    st.success("✅ All changes saved")

# Action buttons
col1, col2, col3 = st.columns(3)

with col1:
    # Save is default when there are changes
    if carbon_button(
        "Save",
        icon=CarbonIcons.SAVE,
        button_type="primary",
        is_default=has_changes,
        disabled=not has_changes,
    ):
        st.session_state.doc_content = new_content
        st.success("Document saved!")
        st.rerun()

with col2:
    # Publish is default when saved
    if carbon_button(
        "Publish",
        icon=CarbonIcons.UPLOAD,
        button_type="secondary",
        is_default=not has_changes,
        disabled=has_changes,
    ):
        st.info("Document published!")

with col3:
    if carbon_button("Revert", button_type="ghost", disabled=not has_changes):
        st.rerun()

# Tips
st.divider()
st.info(
    """
**Dynamic Default Button Patterns:**

🔄 **State-based**: Use session state to track which action should be primary
✅ **Validation-based**: Enable and make default when form is complete
📊 **Progress-based**: Change default action as user progresses
💾 **Save indicators**: Make save default when there are unsaved changes

Remember: Only one button should be default at a time in each context!
"""
)
