from setuptools import setup, find_packages
import os

# Read version from package
version = "1.0.0"

# Use README_PYPI.md if it exists, otherwise fall back to README.md
readme_file = "README_PYPI.md" if os.path.exists("README_PYPI.md") else "README.md"
if os.path.exists(readme_file):
    with open(readme_file, "r", encoding="utf-8") as fh:
        long_description = fh.read()
else:
    long_description = """
# Streamlit Carbon Button

Beautiful Carbon Design System buttons for your Streamlit apps!

## Features
- 🎯 Carbon Design System styling
- 🎨 Multiple button types: primary, secondary, danger, ghost  
- 🔧 Icon support with 18 pre-defined Carbon icons
- ✨ Default button indicator with teal shadow
- 📱 Responsive and accessible
- 🌓 Dark mode support

## Installation
```bash
pip install streamlit-carbon-button
```

## Quick Start
```python
import streamlit as st
from streamlit_carbon_button import carbon_button, CarbonIcons

if carbon_button("Click me!"):
    st.success("Button clicked!")
```

For more examples, visit: https://github.com/yourusername/streamlit-carbon-button-examples
"""

setup(
    name="streamlit-carbon-button",
    version=version,
    author="Your Name",
    author_email="your.email@example.com",
    description="Carbon Design System buttons for Streamlit",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/streamlit-carbon-button-dev",
    project_urls={
        "Documentation": "https://github.com/yourusername/streamlit-carbon-button-examples",
        "Source": "https://github.com/yourusername/streamlit-carbon-button-dev",
        "Tracker": "https://github.com/yourusername/streamlit-carbon-button-dev/issues",
        "Examples": "https://github.com/yourusername/streamlit-carbon-button-examples",
    },
    packages=["streamlit_carbon_button"],
    include_package_data=True,
    package_data={
        "streamlit_carbon_button": ["frontend/**/*"],
    },
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Software Development :: User Interfaces",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    install_requires=[
        "streamlit>=1.0.0",
    ],
    keywords="streamlit carbon button ui component design-system",
)