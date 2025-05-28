# Streamlit Carbon Button Component

Beautiful, accessible buttons for Streamlit using IBM's Carbon Design System.

[![Live Demo](https://img.shields.io/badge/demo-streamlit-FF4B4B)](https://carbon-button-demo.streamlit.app/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Features

- 🎨 **Subtle Styling** - Elegant grey buttons with teal accent
- 🌓 **Dark Mode** - Automatic adaptation to system preferences
- 🎯 **18 Carbon Icons** - Crisp SVG icons at 20px size
- ♿ **Accessible** - Following Carbon Design principles
- 🚀 **Easy Install** - No JavaScript build required

## Installation

```bash
pip install git+https://github.com/lh/streamlit-carbon-button.git
```

## Quick Start

```python
import streamlit as st
from briquette import carbon_button, CarbonIcons

# Basic button
if carbon_button("Click Me", key="button1"):
    st.success("Button clicked!")

# Button with icon
if carbon_button("Save Document", icon=CarbonIcons.SAVE, key="save"):
    st.success("Document saved!")

# Icon-only button
if carbon_button("", icon=CarbonIcons.SETTINGS, key="settings"):
    st.info("Settings opened")

# Different button types
carbon_button("Primary", key="p1", button_type="primary")
carbon_button("Secondary", key="p2", button_type="secondary")  
carbon_button("Danger", key="p3", button_type="danger")
carbon_button("Ghost", key="p4", button_type="ghost")

# Full width button
carbon_button("Process All", key="process", use_container_width=True)
```

## Available Icons

```python
from briquette import CarbonIcons

# File operations
CarbonIcons.UPLOAD      CarbonIcons.DOWNLOAD    CarbonIcons.SAVE
CarbonIcons.COPY        CarbonIcons.DELETE      CarbonIcons.DOCUMENT

# Navigation  
CarbonIcons.HOME        CarbonIcons.SEARCH      CarbonIcons.SETTINGS
CarbonIcons.FILTER      CarbonIcons.INFO        CarbonIcons.HELP

# Actions
CarbonIcons.ADD         CarbonIcons.CLOSE       CarbonIcons.PLAY
CarbonIcons.WARNING     CarbonIcons.SUCCESS     CarbonIcons.CHART_BAR
```

## Custom Colors

```python
custom_colors = {
    "rest_bg": "#e6e2e2",      # Background color
    "rest_text": "#1a1a1a",    # Text/icon color
    "hover_bg": "#f5f5f5",     # Hover background
    "active_bg": "#50e4e0",    # Click background (teal)
    "active_text": "#ffffff",  # Click text color
}

carbon_button("Custom Style", colors=custom_colors, key="custom")
```

## Parameters

- `label` (str): Button text
- `icon` (str, optional): SVG icon from CarbonIcons
- `key` (str): Unique identifier for the button
- `button_type` (str, optional): "primary", "secondary", "danger", or "ghost"
- `disabled` (bool, optional): Disable the button
- `use_container_width` (bool, optional): Expand to full container width
- `colors` (dict, optional): Custom color scheme

## Color Scheme

**Light Mode:**
- Background: `#e6e2e2` (warm grey)
- Hover: `#f5f5f5` (bright grey)
- Active: `#50e4e0` (teal accent)

**Dark Mode:**
- Background: `#ecdcdc` (pink-grey)
- Hover: `#f6f4f4` (very light)
- Active: `#67cccc` (darker teal)

## Examples

See the [examples](examples/) directory for more usage patterns.

## License

MIT License - see [LICENSE](LICENSE) file.

Icons from [IBM Carbon Design System](https://carbondesignsystem.com/) (Apache 2.0 License).