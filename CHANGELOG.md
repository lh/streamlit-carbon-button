# Changelog

## [1.4.0] - 2025-06-17

### Added
- 🧪 **Automated Testing Suite**: Comprehensive pytest-based tests for all button functionality
- 🔒 **Pre-commit Hooks**: Automatic code quality checks with Black, Ruff, and pytest
- 🚀 **CI/CD Pipeline**: GitHub Actions workflow for testing across Python 3.8-3.12
- 🔧 **INVISIBLE Icon**: New utility icon (`CarbonIcons.INVISIBLE`) for aligning text-only buttons with icon buttons
- 📚 **Development Documentation**: TESTING.md guide and improved CLAUDE.md
- 🛠️ **Developer Tools**: setup_dev.sh script for easy development environment setup

### Changed
- Updated development dependencies structure in pyproject.toml
- Enhanced icon showroom with special handling for utility icons
- Improved test coverage for icon validation

### Fixed
- Fixed import order issues with proper E402 handling
- Removed JSON comments from tsconfig.json for better compatibility
- Cleaned up trailing whitespace and file endings

### Developer Experience
- Run `pip install -e ".[dev]"` to get all development tools
- Pre-commit automatically validates icons when carbon_icons.py changes
- Tests run automatically on every commit to prevent regressions

## [1.3.0] - Previous
- Added 102 high-value icons
- Enhanced demo applications

## [1.2.0] - Previous
- Added 40 view/display icons
- Improved icon categorization

## [1.1.0] - Previous
- Added 100+ Carbon icons in separate module
- Improved organization and imports

## [1.0.4] - Previous
- Initial stable release with core button functionality
