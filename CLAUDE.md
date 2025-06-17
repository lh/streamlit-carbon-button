# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Streamlit custom component that provides Carbon Design System buttons. It consists of a Python wrapper (`streamlit_carbon_button/`) and a React/TypeScript frontend (`frontend/`).

## Build Commands

```bash
# Build the frontend (required after frontend changes)
./build.sh

# Install Python package in development mode
pip install -e .

# Build distribution packages
python -m build

# Run the main example app
streamlit run example_app.py

# Run specific test apps
streamlit run test_default_button.py
streamlit run test_aria_labels.py
streamlit run icon_showroom.py
```

## Architecture

### Component Communication
- Python side: `streamlit_carbon_button/__init__.py` contains the `carbon_button()` function
- Frontend: `frontend/src/CarbonButton.tsx` handles rendering and user interaction
- Communication uses Streamlit's component protocol with click state tracking via session state

### Key Design Patterns
1. **Click Handling**: Uses unique keys and session state to prevent duplicate click events
2. **Icon System**: Icons are stored as SVG strings in `carbon_icons.py` (100+ icons)
3. **Styling**: Inline styles in React component, no external CSS dependencies
4. **Dark Mode**: Automatic adaptation using CSS media queries
5. **Default Button**: Special teal shadow effect for default buttons

### Frontend Build System
- Uses Vite (recently migrated from webpack)
- TypeScript configuration in `frontend/tsconfig.json`
- Build output goes to `streamlit_carbon_button/frontend/`
- Pre-built files are included in the Python package distribution

## Testing Approach

### Automated Tests
```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=streamlit_carbon_button

# Run specific test class
pytest tests/test_carbon_button.py::TestCarbonIcons -v
```

### Manual Testing
- `test_*.py` files for specific feature testing
- `example_app.py` for comprehensive demo
- `icon_showroom.py` to browse available icons

### Pre-commit Hooks
Tests run automatically on commit. To set up:
```bash
pip install -e ".[dev]"
pre-commit install
```

## Important Notes

- Always run `./build.sh` after making frontend changes
- The package includes pre-built frontend files for PyPI distribution
- Version is managed in `pyproject.toml`
- Icons are defined in `streamlit_carbon_button/carbon_icons.py`
- When adding new icons, follow the existing pattern in `carbon_icons.py`
