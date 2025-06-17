# Hybrid Approach Implementation Plan

## Overview

We'll create three complementary resources:

1. **Main Development Repository** (`streamlit-carbon-button-dev`)
2. **Examples Repository** (`streamlit-carbon-button-examples`)
3. **PyPI Package** (`streamlit-carbon-button`)

## 1. Main Development Repository

**Repository**: `github.com/yourusername/streamlit-carbon-button-dev`

### Purpose
- Full source code for developers
- Build tools and development environment
- Comprehensive documentation
- Issue tracking and contributions

### Structure
```
streamlit-carbon-button-dev/
├── frontend/                    # React source code
│   ├── src/
│   ├── package.json
│   └── vite.config.ts
├── streamlit_carbon_button/     # Python package
│   ├── __init__.py
│   └── frontend/               # Built files (gitignored)
├── tests/                      # Comprehensive test suite
├── docs/                       # Development documentation
├── .github/
│   └── workflows/
│       ├── test.yml           # Run tests
│       └── publish.yml        # Publish to PyPI
├── setup.py
├── pyproject.toml
├── README.md                   # Developer-focused
├── CONTRIBUTING.md
├── LICENSE
└── CHANGELOG.md
```

### Key Features
- Automated testing on PR
- Automated publishing to PyPI on release
- Comprehensive developer documentation
- Migration guides (from CRA to Vite)

## 2. Examples Repository

**Repository**: `github.com/yourusername/streamlit-carbon-button-examples`

### Purpose
- Showcase all features
- Copy-paste examples
- Live demos
- No build dependencies needed

### Structure
```
streamlit-carbon-button-examples/
├── README.md                    # Links to all examples
├── requirements.txt             # Just: streamlit-carbon-button
├── basic/
│   ├── 01_hello_world.py      # Simplest example
│   ├── 02_button_types.py     # All button variants
│   ├── 03_with_icons.py       # Icon examples
│   └── 04_default_button.py   # Default button feature
├── advanced/
│   ├── 01_dynamic_defaults.py # State-based defaults
│   ├── 02_custom_colors.py    # Custom styling
│   ├── 03_forms.py           # Form integration
│   └── 04_toolbars.py        # Icon-only toolbars
├── real_world/
│   ├── dashboard.py           # Full dashboard example
│   ├── crud_app.py           # CRUD operations
│   └── wizard.py             # Multi-step form
└── assets/
    └── screenshots/           # Example screenshots
```

### Example Files

**basic/01_hello_world.py**:
```python
import streamlit as st
from streamlit_carbon_button import carbon_button

st.title("Hello Carbon Buttons!")

if carbon_button("Click me!"):
    st.balloons()
```

**basic/04_default_button.py**:
```python
import streamlit as st
from streamlit_carbon_button import carbon_button, CarbonIcons

st.title("Default Button Example")

col1, col2 = st.columns([3, 1])
with col1:
    email = st.text_input("Enter your email")
with col2:
    st.write("")  # Spacing
    if carbon_button("Submit", is_default=True, icon=CarbonIcons.SUCCESS):
        st.success(f"Welcome, {email}!")
```

## 3. PyPI Package

**Package Name**: `streamlit-carbon-button`
**Install**: `pip install streamlit-carbon-button`

### Package Contents
- Pre-built component files
- Python wrapper
- No development dependencies
- Minimal size (~500KB)

### Publishing Process

1. **Version Bump** (in main repo):
   ```bash
   # Update version in setup.py and __init__.py
   git tag v1.0.1
   git push origin v1.0.1
   ```

2. **GitHub Action** automatically:
   - Builds the component
   - Creates distribution
   - Publishes to PyPI

3. **Users Install**:
   ```bash
   pip install streamlit-carbon-button
   # or
   pip install --upgrade streamlit-carbon-button
   ```

## Maintenance Workflow

### For New Features:

1. **Develop** in main repository
2. **Test** thoroughly
3. **Release** to PyPI
4. **Add examples** to examples repository
5. **Update** documentation

### Version Synchronization:

- Main repo: Tagged releases (v1.0.0, v1.0.1, etc.)
- PyPI: Matches main repo tags
- Examples: Always uses latest PyPI version

### Documentation Strategy:

1. **Main Repository README**:
   - Development setup
   - Architecture overview
   - Contributing guidelines
   - Build instructions

2. **Examples Repository README**:
   - Quick start
   - Feature showcase
   - Links to live demos
   - Copy-paste snippets

3. **PyPI Description**:
   - Installation
   - Basic usage
   - API reference
   - Links to examples repo

## Timeline

1. **Week 1**: Set up main repository
   - Add GitHub Actions
   - Prepare for PyPI publishing
   - Write developer docs

2. **Week 2**: Create examples repository
   - Port all test files to examples
   - Add real-world examples
   - Create README with screenshots

3. **Week 3**: Publish to PyPI
   - Test package locally
   - Publish to Test PyPI first
   - Publish to production PyPI
   - Announce release

## Benefits of This Approach

✅ **For Users**:
- Simple installation: `pip install streamlit-carbon-button`
- Rich examples repository to learn from
- No need to understand React or build tools

✅ **For Contributors**:
- Clear separation of concerns
- Full development environment
- Easy to test and contribute

✅ **For Maintainers**:
- Automated publishing
- Version control
- Clear upgrade path
