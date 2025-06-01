#!/bin/bash

# Script to prepare the package for PyPI publishing
# This should be run from the main development repository

echo "🚀 Preparing streamlit-carbon-button for PyPI..."

# Check if we're in the right directory
if [ ! -f "setup.py" ] || [ ! -d "frontend" ]; then
    echo "❌ Error: Must run from the carbon-button-component directory"
    exit 1
fi

# Create streamlit_carbon_button directory structure
echo "📁 Setting up package structure..."
rm -rf streamlit_carbon_button
mkdir -p streamlit_carbon_button

# Copy Python files (renaming from briquette)
echo "📄 Copying Python module..."
cp briquette/__init__.py streamlit_carbon_button/

# Update import name in __init__.py if needed
sed -i.bak 's/briquette/streamlit_carbon_button/g' streamlit_carbon_button/__init__.py
rm streamlit_carbon_button/__init__.py.bak

# Build the frontend if needed
echo "🏗️  Building frontend..."
cd frontend
npm install
npm run build
cd ..

# Copy built frontend files
echo "📦 Copying built frontend files..."
mkdir -p streamlit_carbon_button/frontend
cp -r briquette/frontend/* streamlit_carbon_button/frontend/ 2>/dev/null || cp -r frontend/build/* streamlit_carbon_button/frontend/

# Create README_PYPI.md
echo "📝 Creating PyPI README..."
cat > README_PYPI.md << 'EOF'
# Streamlit Carbon Button

Beautiful Carbon Design System buttons for your Streamlit apps! 🎨

![Carbon Buttons](https://img.shields.io/badge/Carbon%20Design-System-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-Compatible-red)
![PyPI](https://img.shields.io/pypi/v/streamlit-carbon-button)

## Features

- 🎯 **Carbon Design System** - Professional IBM design language
- 🎨 **4 Button Types** - Primary, Secondary, Danger, and Ghost
- 🔧 **18 Carbon Icons** - Pre-integrated SVG icons
- ✨ **Default Button** - Teal shadow indicator for primary actions
- 📱 **Responsive** - Adapts to container width
- 🌓 **Dark Mode** - Automatic theme detection
- ♿ **Accessible** - Keyboard navigation and screen reader support

## Installation

```bash
pip install streamlit-carbon-button
```

## Quick Start

```python
import streamlit as st
from streamlit_carbon_button import carbon_button, CarbonIcons

# Simple button
if carbon_button("Click me!"):
    st.success("Button clicked!")

# Button with icon
if carbon_button("Save", icon=CarbonIcons.SAVE):
    st.success("Saved!")

# Default button with teal shadow
if carbon_button("Submit", is_default=True):
    st.balloons()
```

## Button Types

```python
# Primary (default) - Subtle grey
carbon_button("Primary", button_type="primary")

# Secondary - With border
carbon_button("Secondary", button_type="secondary")

# Danger - Red accent
carbon_button("Delete", button_type="danger")

# Ghost - Minimal style
carbon_button("Cancel", button_type="ghost")
```

## Icons

All 18 available Carbon icons:

```python
CarbonIcons.ADD        CarbonIcons.CLOSE      CarbonIcons.COPY
CarbonIcons.DELETE     CarbonIcons.DOWNLOAD   CarbonIcons.UPLOAD
CarbonIcons.SAVE       CarbonIcons.SEARCH     CarbonIcons.SETTINGS
CarbonIcons.FILTER     CarbonIcons.HOME       CarbonIcons.INFO
CarbonIcons.WARNING    CarbonIcons.SUCCESS    CarbonIcons.HELP
CarbonIcons.DOCUMENT   CarbonIcons.CHART_BAR  CarbonIcons.PLAY
```

## Default Button Feature

Mark important actions with a subtle teal shadow:

```python
col1, col2 = st.columns(2)

with col1:
    if carbon_button("Save", is_default=True):
        st.success("Saved!")
        
with col2:
    if carbon_button("Cancel", button_type="ghost"):
        st.info("Cancelled")
```

## Advanced Examples

### Icon-Only Buttons

```python
# Perfect for toolbars
cols = st.columns(4)

with cols[0]:
    if carbon_button("", icon=CarbonIcons.ADD):
        st.info("Add")
        
with cols[1]:
    if carbon_button("", icon=CarbonIcons.EDIT):
        st.info("Edit")
```

### Dynamic Default Buttons

```python
# Change default based on state
is_edited = st.session_state.get('edited', False)

if carbon_button("Save", is_default=is_edited):
    st.success("Saved!")
    st.session_state.edited = False
```

### Full Width Buttons

```python
if carbon_button("Submit Application", use_container_width=True):
    st.success("Submitted!")
```

## API Reference

```python
carbon_button(
    label: str,                       # Button text
    key: str = None,                  # Unique key
    button_type: str = "primary",     # primary|secondary|danger|ghost
    icon: str = None,                 # Icon from CarbonIcons
    disabled: bool = False,           # Disable state
    use_container_width: bool = False,# Full width
    is_default: bool = False,         # Teal shadow indicator
) -> bool                             # True when clicked
```

## Links

- 📚 [Examples Repository](https://github.com/yourusername/streamlit-carbon-button-examples)
- 🛠️ [Development Repository](https://github.com/yourusername/streamlit-carbon-button-dev)
- 🐛 [Issue Tracker](https://github.com/yourusername/streamlit-carbon-button-dev/issues)
- 📖 [Carbon Design System](https://carbondesignsystem.com/)

## License

MIT License - see [LICENSE](https://github.com/yourusername/streamlit-carbon-button-dev/blob/main/LICENSE) for details.

Carbon Design System icons are used under Apache 2.0 License.
EOF

# Create/update MANIFEST.in
echo "📋 Creating MANIFEST.in..."
cat > MANIFEST.in << 'EOF'
recursive-include streamlit_carbon_button/frontend *
include README_PYPI.md
include LICENSE
exclude *.pyc
exclude __pycache__
global-exclude *.py[co]
global-exclude .DS_Store
EOF

# Clean up any existing build artifacts
echo "🧹 Cleaning build artifacts..."
rm -rf build dist *.egg-info

# Build the package
echo "📦 Building package..."
python -m pip install --upgrade pip build
python -m build

# Check the package
echo "✅ Checking package..."
pip install twine
twine check dist/*

echo ""
echo "✨ Package prepared successfully!"
echo ""
echo "📁 Package structure:"
find streamlit_carbon_button -type f | head -20
echo ""
echo "📊 Package size:"
du -sh dist/*
echo ""
echo "Next steps:"
echo "1. Test locally: pip install dist/*.whl"
echo "2. Upload to Test PyPI: twine upload --repository testpypi dist/*"
echo "3. Test from Test PyPI: pip install -i https://test.pypi.org/simple/ streamlit-carbon-button"
echo "4. Upload to PyPI: twine upload dist/*"