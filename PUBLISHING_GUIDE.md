# Publishing Guide for streamlit-carbon-button

This guide walks you through publishing the streamlit-carbon-button package to PyPI.

## Package Status

✅ **Package is ready for publishing!**

- Built successfully: `streamlit_carbon_button-1.0.0-py3-none-any.whl`
- Tested locally: All imports and functionality working
- Frontend assets: Bundled correctly with Vite
- Python wrapper: Working with proper imports
- Examples: Prepared in separate repository structure

## Prerequisites

1. **PyPI Account**: Create an account at https://pypi.org/account/register/
2. **API Token**: Generate an API token at https://pypi.org/manage/account/token/
3. **Install twine**: `pip install twine`

## Publishing Steps

### 1. Final Package Check

```bash
# Verify the package structure
unzip -l dist/streamlit_carbon_button-1.0.0-py3-none-any.whl

# Check package metadata
twine check dist/*
```

### 2. Upload to Test PyPI (Optional)

First test on TestPyPI to ensure everything works:

```bash
# Upload to TestPyPI
twine upload --repository testpypi dist/*

# Test installation from TestPyPI
pip install --index-url https://test.pypi.org/simple/ streamlit-carbon-button
```

### 3. Upload to PyPI

```bash
# Upload to PyPI
twine upload dist/*

# You'll be prompted for:
# Username: __token__
# Password: [paste your API token here]
```

### 4. Verify Installation

```bash
# Install from PyPI
pip install streamlit-carbon-button

# Test it works
python -c "from streamlit_carbon_button import carbon_button, CarbonIcons; print('Success!')"
```

## Post-Publishing Tasks

### 1. Create GitHub Repositories

1. **Main Repository** (streamlit-carbon-button):
   ```bash
   git init
   git add .
   git commit -m "Initial commit: streamlit-carbon-button v1.0.0"
   git branch -M main
   git remote add origin https://github.com/YOUR_USERNAME/streamlit-carbon-button.git
   git push -u origin main
   ```

2. **Examples Repository** (streamlit-carbon-button-examples):
   ```bash
   cd streamlit-carbon-button-examples
   git init
   git add .
   git commit -m "Initial commit: Examples for streamlit-carbon-button"
   git branch -M main
   git remote add origin https://github.com/YOUR_USERNAME/streamlit-carbon-button-examples.git
   git push -u origin main
   ```

### 2. Create GitHub Release

1. Go to your repository's releases page
2. Click "Create a new release"
3. Tag: `v1.0.0`
4. Title: `streamlit-carbon-button v1.0.0`
5. Description: Include features, installation, and usage
6. Attach the wheel file from `dist/`

### 3. Update Documentation

Add badges to your README:

```markdown
[![PyPI version](https://badge.fury.io/py/streamlit-carbon-button.svg)](https://badge.fury.io/py/streamlit-carbon-button)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
```

### 4. Announce the Release

- Post on Streamlit forum: https://discuss.streamlit.io/
- Share on social media
- Update any existing projects to use the PyPI package

## Maintenance

### Version Updates

1. Update version in `setup.py` and `pyproject.toml`
2. Update `frontend/package.json` version
3. Rebuild frontend: `cd frontend && npm run build`
4. Rebuild package: `./prepare_pypi_package.sh`
5. Upload new version: `twine upload dist/*`

### Responding to Issues

- Monitor GitHub issues
- Test reported bugs
- Release patches as needed (1.0.1, 1.0.2, etc.)

## Troubleshooting

### Common Issues

1. **"Invalid distribution file"**: Ensure wheel is built correctly
2. **"Package already exists"**: Increment version number
3. **"Authentication failed"**: Check API token is correct
4. **Import errors**: Verify MANIFEST.in includes all files

### Support

- PyPI documentation: https://packaging.python.org/
- Twine documentation: https://twine.readthedocs.io/
- Streamlit Components: https://docs.streamlit.io/library/components

## Summary

Your package is ready! Just:
1. Create PyPI account and get API token
2. Run `twine upload dist/*`
3. Create GitHub repos and push code
4. Announce your awesome component! 🎉