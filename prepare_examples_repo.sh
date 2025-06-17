#!/bin/bash

# Script to create the streamlit-carbon-button-examples repository
# This creates a clean examples repository for users

echo "📚 Creating streamlit-carbon-button-examples repository..."

# Create directory
EXAMPLES_DIR="streamlit-carbon-button-examples"
rm -rf $EXAMPLES_DIR
mkdir -p $EXAMPLES_DIR

# Create directory structure
mkdir -p $EXAMPLES_DIR/{basic,advanced,real_world,assets/screenshots}

# Create README
cat > $EXAMPLES_DIR/README.md << 'EOF'
# Streamlit Carbon Button Examples

Welcome to the examples repository for `streamlit-carbon-button`! 🎨

This repository contains comprehensive examples showing how to use Carbon Design System buttons in your Streamlit applications.

## 🚀 Quick Start

1. **Install the package**:
   ```bash
   pip install streamlit-carbon-button
   ```

2. **Run an example**:
   ```bash
   streamlit run basic/01_hello_world.py
   ```

## 📁 Repository Structure

### Basic Examples (`basic/`)
- `01_hello_world.py` - Simplest possible example
- `02_button_types.py` - All button variants (primary, secondary, danger, ghost)
- `03_with_icons.py` - Using Carbon icons
- `04_default_button.py` - Default button with teal shadow
- `05_icon_only.py` - Icon-only buttons for toolbars

### Advanced Examples (`advanced/`)
- `01_dynamic_defaults.py` - Changing default button based on state
- `02_custom_colors.py` - Custom color schemes
- `03_forms.py` - Integration with Streamlit forms
- `04_toolbars.py` - Building toolbars with icon buttons
- `05_responsive.py` - Responsive button layouts

### Real World Examples (`real_world/`)
- `dashboard.py` - Complete dashboard with Carbon buttons
- `crud_app.py` - CRUD application example
- `wizard.py` - Multi-step form wizard
- `file_manager.py` - File management interface

## 🎯 Featured Examples

### Hello World
The simplest example to get started:

```python
import streamlit as st
from streamlit_carbon_button import carbon_button

if carbon_button("Click me!"):
    st.balloons()
```

### Form with Default Button
Shows how to use the default button indicator:

```python
with st.form("login"):
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if carbon_button("Sign In", is_default=True):
        st.success(f"Welcome, {username}!")
```

### Icon Toolbar
Create a toolbar with icon-only buttons:

```python
cols = st.columns(4)
actions = [
    ("New", CarbonIcons.ADD),
    ("Save", CarbonIcons.SAVE),
    ("Share", CarbonIcons.UPLOAD),
    ("Delete", CarbonIcons.DELETE)
]

for col, (name, icon) in zip(cols, actions):
    with col:
        if carbon_button("", icon=icon):
            st.info(f"{name} clicked")
```

## 🔗 Useful Links

- 📦 [PyPI Package](https://pypi.org/project/streamlit-carbon-button/)
- 🛠️ [Development Repository](https://github.com/yourusername/streamlit-carbon-button-dev)
- 📖 [Carbon Design System](https://carbondesignsystem.com/)
- 🎨 [Streamlit Gallery](https://streamlit.io/gallery)

## 🤝 Contributing

Found a bug or have a feature request? Please open an issue in the [main repository](https://github.com/yourusername/streamlit-carbon-button-dev/issues).

Want to contribute an example? We'd love to have it! Please submit a PR.

## 📄 License

All examples are provided under the MIT License.
EOF

# Create requirements.txt
cat > $EXAMPLES_DIR/requirements.txt << 'EOF'
streamlit>=1.0.0
streamlit-carbon-button
pandas  # For dashboard examples
plotly  # For dashboard examples
EOF

# Create basic examples
cat > $EXAMPLES_DIR/basic/01_hello_world.py << 'EOF'
"""
Simplest possible example of a Carbon button.
"""

import streamlit as st
from streamlit_carbon_button import carbon_button

st.title("Hello Carbon Button! 👋")

if carbon_button("Click me!"):
    st.balloons()
    st.success("🎉 You clicked the button!")
EOF

cat > $EXAMPLES_DIR/basic/02_button_types.py << 'EOF'
"""
Demonstrates all four button types in the Carbon Design System.
"""

import streamlit as st
from streamlit_carbon_button import carbon_button

st.title("Carbon Button Types")
st.write("Carbon Design System includes four button types, each with a specific purpose.")

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
            button_type=btn_type
        )

# Best practices
st.divider()
st.subheader("Best Practices")

st.info("""
**When to use each type:**

🔵 **Primary**: One per section, for the main action (Save, Submit, Continue)

⭕ **Secondary**: Alternative actions (Cancel, Back, Reset)

🔴 **Danger**: Destructive actions that can't be undone (Delete, Remove)

👻 **Ghost**: Low-emphasis actions (Help, Learn more, Advanced settings)
""")
EOF

cat > $EXAMPLES_DIR/basic/03_with_icons.py << 'EOF'
"""
Using Carbon icons with buttons.
"""

import streamlit as st
from streamlit_carbon_button import carbon_button, CarbonIcons

st.title("Carbon Buttons with Icons")
st.write("Enhance your buttons with 18 available Carbon icons.")

# Icon showcase
st.subheader("Available Icons")

# Group icons by category
icon_categories = {
    "File Operations": [
        ("Upload", CarbonIcons.UPLOAD),
        ("Download", CarbonIcons.DOWNLOAD),
        ("Save", CarbonIcons.SAVE),
        ("Copy", CarbonIcons.COPY),
        ("Document", CarbonIcons.DOCUMENT),
    ],
    "Actions": [
        ("Add", CarbonIcons.ADD),
        ("Delete", CarbonIcons.DELETE),
        ("Close", CarbonIcons.CLOSE),
        ("Search", CarbonIcons.SEARCH),
        ("Filter", CarbonIcons.FILTER),
        ("Play", CarbonIcons.PLAY),
    ],
    "UI Elements": [
        ("Settings", CarbonIcons.SETTINGS),
        ("Home", CarbonIcons.HOME),
        ("Chart", CarbonIcons.CHART_BAR),
    ],
    "Feedback": [
        ("Success", CarbonIcons.SUCCESS),
        ("Warning", CarbonIcons.WARNING),
        ("Info", CarbonIcons.INFO),
        ("Help", CarbonIcons.HELP),
    ],
}

for category, icons in icon_categories.items():
    st.write(f"**{category}**")
    cols = st.columns(len(icons))

    for col, (name, icon) in zip(cols, icons):
        with col:
            if carbon_button(name, icon=icon, key=f"icon_{name}"):
                st.success(f"{name} clicked!")

# Practical examples
st.divider()
st.subheader("Practical Examples")

col1, col2 = st.columns(2)

with col1:
    st.write("**File Operations**")
    if carbon_button("Upload File", icon=CarbonIcons.UPLOAD, button_type="primary"):
        st.info("Opening file picker...")

    if carbon_button("Download Report", icon=CarbonIcons.DOWNLOAD, button_type="secondary"):
        st.info("Downloading...")

with col2:
    st.write("**Form Actions**")
    if carbon_button("Save Draft", icon=CarbonIcons.SAVE, button_type="secondary"):
        st.success("Draft saved!")

    if carbon_button("Delete Draft", icon=CarbonIcons.DELETE, button_type="danger"):
        st.error("Draft deleted!")

# Icon-only buttons
st.divider()
st.subheader("Icon-Only Buttons")
st.write("Perfect for toolbars and compact interfaces")

toolbar_cols = st.columns(6)
toolbar_buttons = [
    ("New", CarbonIcons.ADD, "primary"),
    ("Open", CarbonIcons.DOCUMENT, "secondary"),
    ("Save", CarbonIcons.SAVE, "secondary"),
    ("Copy", CarbonIcons.COPY, "secondary"),
    ("Settings", CarbonIcons.SETTINGS, "ghost"),
    ("Delete", CarbonIcons.DELETE, "danger"),
]

for col, (name, icon, btn_type) in zip(toolbar_cols, toolbar_buttons):
    with col:
        if carbon_button("", icon=icon, button_type=btn_type, key=f"toolbar_{name}"):
            st.toast(f"{name} action triggered!")
        st.caption(name)
EOF

cat > $EXAMPLES_DIR/basic/04_default_button.py << 'EOF'
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
        # Sign In is the default action
        submitted = st.form_submit_button("Sign In")
        if submitted and carbon_button("Sign In", is_default=True, icon=CarbonIcons.SUCCESS):
            st.success(f"Welcome back, {username}!")

    with col2:
        if carbon_button("Forgot Password?", button_type="ghost"):
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
    if carbon_button("Cancel", button_type="ghost", disabled=not st.session_state.edit_mode):
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
EOF

cat > $EXAMPLES_DIR/basic/05_icon_only.py << 'EOF'
"""
Icon-only buttons for toolbars and compact interfaces.
"""

import streamlit as st
from streamlit_carbon_button import carbon_button, CarbonIcons

st.title("Icon-Only Buttons")
st.write("Create compact, professional toolbars with icon-only Carbon buttons.")

# Basic toolbar
st.subheader("📊 Document Toolbar")

toolbar = st.columns(8)
tools = [
    ("New", CarbonIcons.ADD, "secondary", False),
    ("Open", CarbonIcons.DOCUMENT, "secondary", False),
    ("Save", CarbonIcons.SAVE, "primary", True),  # Default button
    ("Copy", CarbonIcons.COPY, "secondary", False),
    ("Cut", CarbonIcons.CLOSE, "secondary", False),
    ("Paste", CarbonIcons.ADD, "secondary", False),
    ("Undo", CarbonIcons.PLAY, "ghost", False),
    ("Delete", CarbonIcons.DELETE, "danger", False),
]

for col, (name, icon, btn_type, is_default) in zip(toolbar, tools):
    with col:
        if carbon_button("", icon=icon, button_type=btn_type, is_default=is_default, key=f"tool_{name}"):
            st.toast(f"{name}")
        st.caption(name)

# Media controls
st.divider()
st.subheader("🎵 Media Player Controls")

col1, col2, col3 = st.columns([1, 3, 1])

with col2:
    media_controls = st.columns(5)

    # Previous
    with media_controls[0]:
        if carbon_button("", icon=CarbonIcons.PLAY, button_type="ghost", key="prev"):
            st.info("⏮️ Previous track")

    # Stop
    with media_controls[1]:
        if carbon_button("", icon=CarbonIcons.CLOSE, button_type="secondary", key="stop"):
            st.info("⏹️ Stopped")

    # Play (default)
    with media_controls[2]:
        if carbon_button("", icon=CarbonIcons.PLAY, button_type="primary", is_default=True, key="play"):
            st.success("▶️ Playing...")

    # Pause
    with media_controls[3]:
        if carbon_button("", icon=CarbonIcons.HELP, button_type="secondary", key="pause"):
            st.info("⏸️ Paused")

    # Next
    with media_controls[4]:
        if carbon_button("", icon=CarbonIcons.PLAY, button_type="ghost", key="next"):
            st.info("⏭️ Next track")

# Floating action buttons
st.divider()
st.subheader("➕ Floating Action Buttons")

col1, col2 = st.columns([4, 1])

with col1:
    st.write("Main content area...")
    st.write("Lorem ipsum dolor sit amet, consectetur adipiscing elit.")

with col2:
    st.write("**Quick Actions**")

    if carbon_button("", icon=CarbonIcons.ADD, button_type="primary", is_default=True, key="fab_add"):
        st.success("Creating new item...")

    if carbon_button("", icon=CarbonIcons.UPLOAD, button_type="secondary", key="fab_upload"):
        st.info("Upload dialog opened")

    if carbon_button("", icon=CarbonIcons.SETTINGS, button_type="ghost", key="fab_settings"):
        st.info("Settings panel opened")

# Icon grid
st.divider()
st.subheader("🎨 Icon Palette")
st.write("All available icons in a grid layout")

all_icons = [
    ("Upload", CarbonIcons.UPLOAD),
    ("Download", CarbonIcons.DOWNLOAD),
    ("Save", CarbonIcons.SAVE),
    ("Copy", CarbonIcons.COPY),
    ("Delete", CarbonIcons.DELETE),
    ("Add", CarbonIcons.ADD),
    ("Close", CarbonIcons.CLOSE),
    ("Settings", CarbonIcons.SETTINGS),
    ("Search", CarbonIcons.SEARCH),
    ("Filter", CarbonIcons.FILTER),
    ("Chart", CarbonIcons.CHART_BAR),
    ("Document", CarbonIcons.DOCUMENT),
    ("Play", CarbonIcons.PLAY),
    ("Help", CarbonIcons.HELP),
    ("Warning", CarbonIcons.WARNING),
    ("Home", CarbonIcons.HOME),
    ("Info", CarbonIcons.INFO),
    ("Success", CarbonIcons.SUCCESS),
]

# Create a 6-column grid
for i in range(0, len(all_icons), 6):
    cols = st.columns(6)
    for j, col in enumerate(cols):
        if i + j < len(all_icons):
            name, icon = all_icons[i + j]
            with col:
                if carbon_button("", icon=icon, button_type="ghost", key=f"grid_{name}"):
                    st.code(f"CarbonIcons.{name.upper()}")
                st.caption(name)

# Tips
st.divider()
st.info("""
**Tips for Icon-Only Buttons:**

💡 Always include captions or tooltips for accessibility
🎯 Use `is_default=True` on the primary action (like Save or Play)
📐 Icon-only buttons are perfect squares with equal padding
🎨 Mix button types to create visual hierarchy
♿ Consider adding aria-labels for screen readers (future feature)
""")
EOF

# Create advanced examples
cat > $EXAMPLES_DIR/advanced/01_dynamic_defaults.py << 'EOF'
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
        disabled=not is_valid
    ):
        st.success("Form submitted successfully!")
        st.balloons()

with col2:
    # Clear is default when form is invalid
    if carbon_button(
        "Clear",
        button_type="ghost",
        is_default=not is_valid
    ):
        st.rerun()

if not is_valid:
    st.warning("Please fill in all required fields")

# Example 2: Multi-step process
st.divider()
st.header("2. Multi-Step Wizard")

# Initialize step
if 'wizard_step' not in st.session_state:
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
        if carbon_button(
            "Next →",
            button_type="primary",
            is_default=True
        ):
            st.session_state.wizard_step += 1
            st.rerun()
    else:
        # Complete is default for final step
        if carbon_button(
            "Complete Order",
            button_type="primary",
            icon=CarbonIcons.SUCCESS,
            is_default=True
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
if 'doc_saved' not in st.session_state:
    st.session_state.doc_saved = True
if 'doc_content' not in st.session_state:
    st.session_state.doc_content = "Initial content..."

# Document editor
new_content = st.text_area(
    "Document",
    value=st.session_state.doc_content,
    height=150
)

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
        disabled=not has_changes
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
        disabled=has_changes
    ):
        st.info("Document published!")

with col3:
    if carbon_button("Revert", button_type="ghost", disabled=not has_changes):
        st.rerun()

# Tips
st.divider()
st.info("""
**Dynamic Default Button Patterns:**

🔄 **State-based**: Use session state to track which action should be primary
✅ **Validation-based**: Enable and make default when form is complete
📊 **Progress-based**: Change default action as user progresses
💾 **Save indicators**: Make save default when there are unsaved changes

Remember: Only one button should be default at a time in each context!
""")
EOF

# Create a simple shell script to run examples
cat > $EXAMPLES_DIR/run_examples.sh << 'EOF'
#!/bin/bash

echo "🎨 Streamlit Carbon Button Examples"
echo ""
echo "Choose an example to run:"
echo ""
echo "Basic Examples:"
echo "  1) Hello World"
echo "  2) Button Types"
echo "  3) With Icons"
echo "  4) Default Button"
echo "  5) Icon Only"
echo ""
echo "Advanced Examples:"
echo "  6) Dynamic Defaults"
echo ""

read -p "Enter number (1-6): " choice

case $choice in
    1) streamlit run basic/01_hello_world.py ;;
    2) streamlit run basic/02_button_types.py ;;
    3) streamlit run basic/03_with_icons.py ;;
    4) streamlit run basic/04_default_button.py ;;
    5) streamlit run basic/05_icon_only.py ;;
    6) streamlit run advanced/01_dynamic_defaults.py ;;
    *) echo "Invalid choice"; exit 1 ;;
esac
EOF

chmod +x $EXAMPLES_DIR/run_examples.sh

# Create .gitignore
cat > $EXAMPLES_DIR/.gitignore << 'EOF'
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
env/
venv/
.venv

# Streamlit
.streamlit/

# IDE
.vscode/
.idea/
*.swp
*.swo

# OS
.DS_Store
Thumbs.db

# Temporary
*.log
*.tmp
EOF

echo "✅ Examples repository created in: $EXAMPLES_DIR/"
echo ""
echo "Repository structure:"
tree $EXAMPLES_DIR -I '__pycache__|*.pyc' 2>/dev/null || find $EXAMPLES_DIR -type f | grep -v __pycache__ | sort
echo ""
echo "Next steps:"
echo "1. cd $EXAMPLES_DIR"
echo "2. git init"
echo "3. git add ."
echo "4. git commit -m 'Initial examples'"
echo "5. Create GitHub repo 'streamlit-carbon-button-examples'"
echo "6. git remote add origin <your-repo-url>"
echo "7. git push -u origin main"
