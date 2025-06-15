"""Test ARIA label support for accessibility"""

import streamlit as st
from streamlit_carbon_button import carbon_button, CarbonIcons

st.set_page_config(page_title="ARIA Labels Test", layout="wide")

st.title("♿ ARIA Label Support")
st.write("Testing accessibility features for screen readers")

# Test 1: Icon-only buttons with automatic ARIA labels
st.header("1. Icon-Only Buttons (Automatic ARIA)")
st.write("Icon-only buttons automatically get ARIA labels from the label parameter")

cols = st.columns(6)
icons = [
    ("Save document", CarbonIcons.SAVE),
    ("Upload file", CarbonIcons.UPLOAD),
    ("Delete item", CarbonIcons.DELETE),
    ("Open settings", CarbonIcons.SETTINGS),
    ("Search", CarbonIcons.SEARCH),
    ("Get help", CarbonIcons.HELP),
]

for col, (label, icon) in zip(cols, icons):
    with col:
        # Label is used as aria-label for icon-only buttons
        if carbon_button(label, icon=icon, button_type="ghost", key=f"auto_{label}"):
            st.toast(f"{label} clicked!")
        st.caption(label.split()[0])

# Test 2: Explicit ARIA labels
st.header("2. Explicit ARIA Labels")
st.write("You can override with custom ARIA labels for better context")

col1, col2, col3 = st.columns(3)

with col1:
    st.write("**Standard button**")
    if carbon_button(
        "Submit", 
        key="explicit1",
        button_type="primary",
        aria_label="Submit the application form"
    ):
        st.success("Form submitted!")

with col2:
    st.write("**Icon + text**")
    if carbon_button(
        "Save",
        icon=CarbonIcons.SAVE,
        key="explicit2", 
        aria_label="Save your work to cloud storage"
    ):
        st.success("Saved to cloud!")

with col3:
    st.write("**Icon only**")
    if carbon_button(
        "",
        icon=CarbonIcons.CLOSE,
        key="explicit3",
        button_type="danger",
        aria_label="Close dialog and discard changes"
    ):
        st.error("Dialog closed!")

# Test 3: Toolbar with descriptive ARIA labels
st.header("3. Accessible Toolbar")
st.write("Each icon button has a descriptive ARIA label for screen readers")

toolbar = st.columns(8)
toolbar_buttons = [
    ("", CarbonIcons.ADD, "Create new document", "New"),
    ("", CarbonIcons.DOCUMENT, "Open existing document", "Open"),
    ("", CarbonIcons.SAVE, "Save current document", "Save"),
    ("", CarbonIcons.COPY, "Copy selection to clipboard", "Copy"),
    ("", CarbonIcons.DELETE, "Move to trash", "Delete"),
    ("", CarbonIcons.UPLOAD, "Share document online", "Share"),
    ("", CarbonIcons.SETTINGS, "Document preferences", "Settings"),
    ("", CarbonIcons.INFO, "About this application", "About"),
]

for col, (label, icon, aria, caption) in zip(toolbar, toolbar_buttons):
    with col:
        btn_type = "primary" if caption == "Save" else "ghost"
        is_def = caption == "Save"
        
        if carbon_button(
            label,
            icon=icon,
            button_type=btn_type,
            is_default=is_def,
            aria_label=aria,
            key=f"toolbar_{caption}"
        ):
            st.toast(f"{aria}")
        st.caption(caption)

# Test 4: Dynamic ARIA labels
st.header("4. Dynamic ARIA Labels")
st.write("ARIA labels can change based on state")

if 'item_count' not in st.session_state:
    st.session_state.item_count = 0

col1, col2 = st.columns(2)

with col1:
    # Dynamic aria label based on count
    aria_text = f"Shopping cart with {st.session_state.item_count} items" if st.session_state.item_count > 0 else "Shopping cart is empty"
    
    if carbon_button(
        f"Cart ({st.session_state.item_count})",
        icon=CarbonIcons.CHART_BAR,
        button_type="secondary",
        aria_label=aria_text,
        key="cart"
    ):
        st.info(aria_text)

with col2:
    if carbon_button("Add Item", key="add_item"):
        st.session_state.item_count += 1
        st.rerun()

# Info section
st.divider()
st.info("""
**How ARIA Labels Work in Carbon Buttons:**

1. **Automatic for icon-only**: When you create an icon-only button with `carbon_button("Save", icon=...)`, 
   the label "Save" becomes the ARIA label automatically

2. **Explicit override**: Use `aria_label="Custom description"` to provide more context

3. **Best practices**:
   - Icon-only buttons should always have descriptive labels
   - Add context about what will happen ("Save document to cloud" vs just "Save")
   - Update dynamically for stateful buttons (e.g., "3 items in cart")
   
4. **Testing**: Use a screen reader or browser dev tools to verify ARIA labels

Example:
```python
# Icon-only with automatic ARIA
carbon_button("Delete item", icon=CarbonIcons.DELETE)

# Custom ARIA for more context  
carbon_button("Submit", aria_label="Submit job application form")
```
""")

# Developer note
with st.expander("🔧 Implementation Details"):
    st.code("""
// In React component:
const computedAriaLabel = ariaLabel || (isIconOnly ? label || "Icon button" : undefined)

<button aria-label={computedAriaLabel}>
    ...
</button>
    """, language="javascript")
    
    st.write("""
    The logic:
    1. If `aria_label` is explicitly provided, use it
    2. Else if button is icon-only, use the `label` as aria-label
    3. Else if no text at all, use "Icon button" as fallback
    4. For buttons with visible text, no aria-label needed (text is already accessible)
    """)