# Testing Guide

This document describes the testing setup for streamlit-carbon-button.

## Quick Start

```bash
# Install development dependencies
pip install -e ".[dev]"

# Install pre-commit hooks
pre-commit install

# Run all tests
pytest

# Run tests with coverage
pytest --cov=streamlit_carbon_button

# Run only icon validation tests
pytest tests/test_carbon_button.py::TestCarbonIcons -v
```

## Test Structure

### Unit Tests (`tests/test_carbon_button.py`)

1. **TestCarbonButton** - Tests the main button functionality:
   - Basic button creation
   - Click detection
   - Button types (primary, secondary, danger, ghost)
   - Custom styling
   - Accessibility features
   - Session state management

2. **TestCarbonIcons** - Validates icon integrity:
   - All icons are valid SVG strings
   - Common icons exist
   - Proper viewBox attributes
   - No duplicate icons

3. **TestComponentDeclaration** - Tests environment-specific behavior:
   - Production mode (uses built files)
   - Development mode (connects to React dev server)

## Pre-commit Hooks

The project uses pre-commit hooks to ensure code quality:

- **Code formatting**: Black
- **Linting**: Ruff
- **Tests**: Runs pytest on every commit
- **Icon validation**: Automatically validates icons when `carbon_icons.py` changes

To manually run pre-commit on all files:
```bash
pre-commit run --all-files
```

## Continuous Integration

GitHub Actions runs tests on:
- Python versions: 3.8, 3.9, 3.10, 3.11, 3.12
- Every push to main
- Every pull request

The CI pipeline:
1. Runs linting (Black + Ruff)
2. Runs all tests with coverage
3. Validates Carbon icons separately
4. Uploads coverage to Codecov (optional)

## Adding New Icons

When adding new icons to `carbon_icons.py`:

1. The pre-commit hook will automatically validate:
   - Icon is a valid SVG string
   - Has proper viewBox attribute
   - No duplicates

2. Tests will ensure:
   - Icon name follows UPPER_SNAKE_CASE convention
   - SVG is properly formatted

## Development Workflow

1. Make changes to the code
2. Run tests locally: `pytest`
3. Commit changes (pre-commit will run automatically)
4. Push to GitHub (CI will run full test suite)

## Troubleshooting

### Tests failing locally but not in CI?
- Check Python version: `python --version`
- Ensure clean environment: `pip install -e ".[dev]" --force-reinstall`

### Pre-commit hooks not running?
- Install hooks: `pre-commit install`
- Update hooks: `pre-commit autoupdate`

### Mock-related failures?
- The tests use mocks for Streamlit components
- Ensure you have the latest pytest version
