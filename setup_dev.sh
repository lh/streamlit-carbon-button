#!/bin/bash

echo "Setting up development environment for streamlit-carbon-button..."

# Install the package in development mode with dev dependencies
echo "Installing package with development dependencies..."
pip install -e ".[dev]"

# Install pre-commit hooks
echo "Installing pre-commit hooks..."
pre-commit install

echo "Running initial tests to verify setup..."
pytest tests -v

echo "Development environment setup complete!"
echo ""
echo "To run tests manually: pytest"
echo "To run tests with coverage: pytest --cov=streamlit_carbon_button"
echo "To run pre-commit on all files: pre-commit run --all-files"
