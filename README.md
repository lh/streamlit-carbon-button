# Streamlit Carbon Button Component

Beautiful, accessible buttons for Streamlit using IBM's Carbon Design System.

[![PyPI version](https://badge.fury.io/py/streamlit-carbon-button.svg)](https://pypi.org/project/streamlit-carbon-button/)
[![Live Demo](https://img.shields.io/badge/demo-streamlit-FF4B4B)](https://carbon-button-demo.streamlit.app/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Features

- 🎨 **Carbon Design** - Beautiful buttons following IBM's design system
- 🌓 **Dark Mode** - Automatic adaptation to system preferences
- 🎯 **200+ Icons** - Full Carbon icon library included
- ♿ **Accessible** - ARIA labels with automatic support for icon-only buttons
- ✨ **Default Button** - Visual "press me" indicator with teal shadow
- 🚀 **Easy Install** - Available on PyPI

## Installation

```bash
pip install streamlit-carbon-button
```

## Quick Start

```python
import streamlit as st
from streamlit_carbon_button import carbon_button, CarbonIcons

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

# Default button with visual indicator
carbon_button("Click Me First!", key="default", is_default=True)

# Full width button
carbon_button("Process All", key="process", use_container_width=True)
```

## Available Icons

```python
from streamlit_carbon_button import CarbonIcons

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
- `is_default` (bool, optional): Show visual indicator for default button
- `aria_label` (str, optional): Custom ARIA label for accessibility

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

See the [streamlit-carbon-button-examples](https://github.com/lh/streamlit-carbon-button-examples) repository for more usage patterns and demos.

## Acknowledgments

This component uses icons from the [IBM Carbon Design System](https://carbondesignsystem.com/):
- Carbon Icons are licensed under [Apache License 2.0](https://github.com/carbon-design-system/carbon/blob/main/LICENSE)
- Copyright © IBM Corp. 2016, 2023

Special thanks to the Carbon Design System team for creating such beautiful and accessible design resources.

## License

This project is licensed under the MIT License - see [LICENSE](LICENSE) file.

The Carbon icons included in this package are licensed under Apache License 2.0 by IBM.