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
