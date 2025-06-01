#!/bin/bash

# Script to prepare the distribution repository
# This creates a minimal package with just the pre-built files

echo "Preparing streamlit-carbon-button distribution repository..."

# Create distribution directory
DIST_DIR="streamlit-carbon-button-dist"
rm -rf $DIST_DIR
mkdir -p $DIST_DIR

# Create package directory (renamed from briquette for clarity)
mkdir -p $DIST_DIR/streamlit_carbon_button

# Copy Python wrapper
cp briquette/__init__.py $DIST_DIR/streamlit_carbon_button/

# Copy pre-built frontend files
cp -r briquette/frontend $DIST_DIR/streamlit_carbon_button/

# Create simple setup.py
cat > $DIST_DIR/setup.py << 'EOF'
from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="streamlit-carbon-button",
    version="1.0.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="Carbon Design System buttons for Streamlit",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/streamlit-carbon-button",
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    install_requires=[
        "streamlit>=1.0.0",
    ],
    package_data={
        "streamlit_carbon_button": ["frontend/**/*"],
    },
)
EOF

# Create MANIFEST.in
cat > $DIST_DIR/MANIFEST.in << 'EOF'
recursive-include streamlit_carbon_button/frontend *
include README.md
include LICENSE
EOF

# Create simple requirements.txt
cat > $DIST_DIR/requirements.txt << 'EOF'
streamlit>=1.0.0
EOF

# Create user-friendly README
cat > $DIST_DIR/README.md << 'EOF'
# Streamlit Carbon Button

Beautiful Carbon Design System buttons for your Streamlit apps! 🎨

![Carbon Buttons Demo](https://raw.githubusercontent.com/yourusername/streamlit-carbon-button/main/demo.gif)

## Features

- 🎯 **Carbon Design System** styling
- 🎨 **Multiple button types**: primary, secondary, danger, ghost
- 🔧 **Icon support** with 18 pre-defined Carbon icons
- ✨ **Default button** indicator with teal shadow
- 📱 **Responsive** and accessible
- 🌓 **Dark mode** support

## Installation

```bash
pip install streamlit-carbon-button
```

Or install from this repository:

```bash
pip install .
```

## Quick Start

```python
import streamlit as st
from streamlit_carbon_button import carbon_button, CarbonIcons

# Simple button
if carbon_button("Click me!"):
    st.success("Button clicked!")

# Button with icon
if carbon_button("Save", icon=CarbonIcons.SAVE, button_type="primary"):
    st.success("Saved!")

# Default button with teal shadow
if carbon_button("Submit", is_default=True):
    st.balloons()

# Icon-only button
if carbon_button("", icon=CarbonIcons.SETTINGS, button_type="ghost"):
    st.info("Settings clicked")
```

## Button Types

- **Primary**: Main actions (subtle grey)
- **Secondary**: Secondary actions (with border)
- **Danger**: Destructive actions (red tones)
- **Ghost**: Minimal style (no background)

## Available Icons

```python
CarbonIcons.UPLOAD      CarbonIcons.DOWNLOAD    CarbonIcons.SAVE
CarbonIcons.COPY        CarbonIcons.DELETE      CarbonIcons.ADD
CarbonIcons.CLOSE       CarbonIcons.SETTINGS    CarbonIcons.SEARCH
CarbonIcons.FILTER      CarbonIcons.CHART_BAR   CarbonIcons.DOCUMENT
CarbonIcons.PLAY        CarbonIcons.HELP        CarbonIcons.WARNING
CarbonIcons.HOME        CarbonIcons.INFO        CarbonIcons.SUCCESS
```

## API Reference

```python
carbon_button(
    label: str,                    # Button text (empty string for icon-only)
    key: str = None,              # Unique key for the button
    button_type: str = "primary", # "primary", "secondary", "danger", or "ghost"
    icon: str = None,             # Icon from CarbonIcons
    disabled: bool = False,       # Disable the button
    use_container_width: bool = False,  # Full width button
    is_default: bool = False,     # Add teal shadow indicator
) -> bool:                        # Returns True when clicked
```

## Examples

### Form with Default Button

```python
with st.form("my_form"):
    st.text_input("Email")
    st.text_input("Password", type="password")
    
    col1, col2 = st.columns(2)
    with col1:
        submitted = carbon_button("Sign In", button_type="primary", is_default=True)
    with col2:
        carbon_button("Cancel", button_type="ghost")
```

### Toolbar with Icon Buttons

```python
col1, col2, col3, col4 = st.columns(4)

with col1:
    if carbon_button("", icon=CarbonIcons.ADD):
        st.info("New file")

with col2:
    if carbon_button("", icon=CarbonIcons.SAVE, is_default=True):
        st.success("Saved!")

with col3:
    if carbon_button("", icon=CarbonIcons.COPY):
        st.info("Copied")

with col4:
    if carbon_button("", icon=CarbonIcons.DELETE, button_type="danger"):
        st.error("Deleted")
```

## License

This project is licensed under the MIT License. Carbon Design System icons are used under the Apache 2.0 License.

## Credits

- Built with ❤️ using [Carbon Design System](https://carbondesignsystem.com/)
- Icon components from IBM Carbon
- Created for the Streamlit community
EOF

# Copy LICENSE file
cp LICENSE $DIST_DIR/ 2>/dev/null || echo "No LICENSE file found"

# Create a simple example
mkdir -p $DIST_DIR/example
cat > $DIST_DIR/example/demo.py << 'EOF'
"""
Simple demo of Streamlit Carbon Buttons
"""

import streamlit as st
from streamlit_carbon_button import carbon_button, CarbonIcons

st.set_page_config(page_title="Carbon Button Demo", page_icon="🎨")

st.title("🎨 Streamlit Carbon Buttons")
st.write("Beautiful buttons following IBM's Carbon Design System")

# Basic buttons
st.header("Button Types")
col1, col2, col3, col4 = st.columns(4)

with col1:
    if carbon_button("Primary", button_type="primary"):
        st.success("Primary clicked!")

with col2:
    if carbon_button("Secondary", button_type="secondary"):
        st.info("Secondary clicked!")

with col3:
    if carbon_button("Danger", button_type="danger"):
        st.error("Danger clicked!")

with col4:
    if carbon_button("Ghost", button_type="ghost"):
        st.info("Ghost clicked!")

# Buttons with icons
st.header("Buttons with Icons")
col1, col2, col3 = st.columns(3)

with col1:
    if carbon_button("Upload", icon=CarbonIcons.UPLOAD):
        st.success("Uploading...")

with col2:
    if carbon_button("Download", icon=CarbonIcons.DOWNLOAD, button_type="secondary"):
        st.info("Downloading...")

with col3:
    if carbon_button("Delete", icon=CarbonIcons.DELETE, button_type="danger"):
        st.error("Deleted!")

# Default button example
st.header("Default Button Indicator")
st.write("The submit button has a teal shadow to indicate it's the default action")

col1, col2 = st.columns([3, 1])
with col1:
    st.text_input("Enter your email")
with col2:
    st.write("")  # Spacing
    if carbon_button("Submit", is_default=True, icon=CarbonIcons.SUCCESS):
        st.balloons()

# Icon-only buttons
st.header("Icon-Only Buttons")
st.write("Perfect for toolbars and compact UIs")

cols = st.columns(6)
icons = [
    ("Add", CarbonIcons.ADD),
    ("Save", CarbonIcons.SAVE),
    ("Copy", CarbonIcons.COPY),
    ("Settings", CarbonIcons.SETTINGS),
    ("Help", CarbonIcons.HELP),
    ("Delete", CarbonIcons.DELETE),
]

for col, (name, icon) in zip(cols, icons):
    with col:
        if carbon_button("", icon=icon, button_type="ghost" if name != "Save" else "primary",
                        is_default=(name == "Save")):
            st.toast(f"{name} clicked!")
        st.caption(name)
EOF

# Create .gitignore for distribution repo
cat > $DIST_DIR/.gitignore << 'EOF'
*.pyc
__pycache__/
build/
dist/
*.egg-info/
.DS_Store
.pytest_cache/
.coverage
htmlcov/
EOF

echo "✅ Distribution repository prepared in: $DIST_DIR/"
echo ""
echo "Next steps:"
echo "1. cd $DIST_DIR"
echo "2. git init"
echo "3. git add ."
echo "4. git commit -m \"Initial commit\""
echo "5. Create a new GitHub repository and push"
echo ""
echo "To test the package locally:"
echo "cd $DIST_DIR && pip install -e ."