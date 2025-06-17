"""
Test script to demonstrate adding a new icon
"""

from streamlit_carbon_button import CarbonIcons

# This will fail the icon validation test if the icon is not properly formatted
# To test: Add a badly formatted icon to carbon_icons.py and run:
# pytest tests/test_carbon_button.py::TestCarbonIcons -v

print(
    "Current number of icons:",
    len([attr for attr in dir(CarbonIcons) if attr.isupper()]),
)
print("\nTo add a new icon:")
print("1. Add it to streamlit_carbon_button/carbon_icons.py")
print("2. Run: git add -A && git commit")
print("3. Pre-commit will automatically validate the icon")
print("4. If validation fails, fix the icon and try again")
