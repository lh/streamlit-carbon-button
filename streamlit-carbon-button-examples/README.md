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
