"""
Tests for streamlit-carbon-button component
"""

import pytest
from unittest.mock import patch
import streamlit as st
from streamlit_carbon_button import carbon_button, CarbonIcons


class TestCarbonButton:
    """Test the carbon_button function"""

    @pytest.fixture(autouse=True)
    def setup_session_state(self):
        """Setup mock session state before each test"""
        # Clear any existing session state
        if hasattr(st, "session_state"):
            for key in list(st.session_state.keys()):
                del st.session_state[key]

    @pytest.fixture
    def mock_component_func(self):
        """Mock the component function"""
        with patch("streamlit_carbon_button._component_func") as mock_func:
            mock_func.return_value = 0
            yield mock_func

    def test_basic_button_creation(self, mock_component_func):
        """Test creating a basic button"""
        result = carbon_button("Click Me")

        assert result is False
        mock_component_func.assert_called_once()

        # Check the arguments passed to component
        call_args = mock_component_func.call_args[1]
        assert call_args["label"] == "Click Me"
        assert call_args["buttonType"] == "primary"
        assert call_args["disabled"] is False
        assert call_args["useContainerWidth"] is False
        assert call_args["isDefault"] is False

    def test_button_with_icon(self, mock_component_func):
        """Test button with icon"""
        carbon_button("Save", icon=CarbonIcons.SAVE)

        call_args = mock_component_func.call_args[1]
        assert call_args["icon"] == CarbonIcons.SAVE
        assert "<svg" in call_args["icon"]

    def test_button_types(self, mock_component_func):
        """Test different button types"""
        button_types = ["primary", "secondary", "danger", "ghost"]

        for btn_type in button_types:
            carbon_button("Test", button_type=btn_type)
            call_args = mock_component_func.call_args[1]
            assert call_args["buttonType"] == btn_type

    def test_disabled_button(self, mock_component_func):
        """Test disabled button"""
        result = carbon_button("Disabled", disabled=True)

        call_args = mock_component_func.call_args[1]
        assert call_args["disabled"] is True
        assert result is False

    def test_custom_key(self, mock_component_func):
        """Test button with custom key"""
        carbon_button("Test", key="my_custom_key")

        call_args = mock_component_func.call_args[1]
        assert call_args["key"] == "my_custom_key"
        assert "__carbon_button_prev_my_custom_key" in st.session_state

    def test_auto_generated_key(self, mock_component_func):
        """Test button with auto-generated key"""
        carbon_button("Test")

        call_args = mock_component_func.call_args[1]
        assert call_args["key"].startswith("carbon_button_")

    def test_click_detection(self, mock_component_func):
        """Test click detection logic"""
        # First render - no click
        mock_component_func.return_value = 0
        result1 = carbon_button("Test", key="test_btn")
        assert result1 is False

        # Second render - clicked
        mock_component_func.return_value = 1
        result2 = carbon_button("Test", key="test_btn")
        assert result2 is True

        # Third render - no new click
        mock_component_func.return_value = 1
        result3 = carbon_button("Test", key="test_btn")
        assert result3 is False

    def test_container_width(self, mock_component_func):
        """Test use_container_width parameter"""
        carbon_button("Full Width", use_container_width=True)

        call_args = mock_component_func.call_args[1]
        assert call_args["useContainerWidth"] is True

    def test_custom_colors(self, mock_component_func):
        """Test custom colors"""
        custom_colors = {
            "rest_bg": "#000000",
            "rest_text": "#FFFFFF",
            "hover_bg": "#333333",
        }

        carbon_button("Custom", colors=custom_colors)

        call_args = mock_component_func.call_args[1]
        assert call_args["colors"] == custom_colors

    def test_default_button(self, mock_component_func):
        """Test default button with teal shadow"""
        carbon_button("Default Action", is_default=True)

        call_args = mock_component_func.call_args[1]
        assert call_args["isDefault"] is True

    def test_aria_label(self, mock_component_func):
        """Test ARIA label for accessibility"""
        carbon_button("", icon=CarbonIcons.SAVE, aria_label="Save document")

        call_args = mock_component_func.call_args[1]
        assert call_args["ariaLabel"] == "Save document"

    def test_session_state_isolation(self, mock_component_func):
        """Test that different buttons have isolated session state"""
        # Click button 1
        mock_component_func.return_value = 1
        result1 = carbon_button("Button 1", key="btn1")
        assert result1 is True

        # Button 2 should not be affected
        mock_component_func.return_value = 0
        result2 = carbon_button("Button 2", key="btn2")
        assert result2 is False

    def test_none_component_value(self, mock_component_func):
        """Test handling of None return value from component"""
        mock_component_func.return_value = None
        result = carbon_button("Test")
        assert result is False


class TestCarbonIcons:
    """Test the CarbonIcons class"""

    def test_icons_are_svg_strings(self):
        """Test that all icons are valid SVG strings"""
        icon_attrs = [
            attr
            for attr in dir(CarbonIcons)
            if not attr.startswith("_") and attr.isupper()
        ]

        assert len(icon_attrs) > 0, "No icons found"

        for attr_name in icon_attrs:
            icon_value = getattr(CarbonIcons, attr_name)
            assert isinstance(icon_value, str), f"{attr_name} is not a string"
            assert icon_value.startswith("<svg") or icon_value.startswith(
                "<?xml"
            ), f"{attr_name} doesn't start with valid SVG tag"
            assert icon_value.endswith("</svg>"), f"{attr_name} doesn't end with </svg>"

    def test_common_icons_exist(self):
        """Test that common icons are available"""
        common_icons = [
            "UPLOAD",
            "DOWNLOAD",
            "SAVE",
            "COPY",
            "DELETE",
            "ADD",
            "CLOSE",
            "SETTINGS",
            "SEARCH",
            "FILTER",
            "CHART_BAR",
            "DOCUMENT",
            "PLAY",
            "HELP",
            "WARNING",
            "HOME",
            "INFO",
            "SUCCESS",
            "EDIT",
        ]

        for icon_name in common_icons:
            assert hasattr(CarbonIcons, icon_name), f"Missing common icon: {icon_name}"

    def test_icon_viewbox(self):
        """Test that icons have proper viewBox attribute"""
        # Test a few key icons
        test_icons = ["UPLOAD", "DOWNLOAD", "SAVE"]

        for icon_name in test_icons:
            icon_svg = getattr(CarbonIcons, icon_name)
            assert (
                'viewBox="0 0 32 32"' in icon_svg
            ), f"{icon_name} doesn't have correct viewBox"

    def test_no_duplicate_icons(self):
        """Test that there are no duplicate icon definitions"""
        icon_attrs = [
            attr
            for attr in dir(CarbonIcons)
            if not attr.startswith("_") and attr.isupper()
        ]

        icon_values = {}
        for attr_name in icon_attrs:
            icon_value = getattr(CarbonIcons, attr_name)
            if icon_value in icon_values:
                assert (
                    False
                ), f"Duplicate icon: {attr_name} has same SVG as {icon_values[icon_value]}"
            icon_values[icon_value] = attr_name


class TestComponentDeclaration:
    """Test component declaration logic"""

    def test_production_mode(self):
        """Test component declaration in production mode"""
        with patch.dict("os.environ", {}, clear=True):
            with patch("streamlit.components.v1.declare_component") as mock_declare:
                # Re-import to trigger module-level code
                import importlib
                import streamlit_carbon_button

                importlib.reload(streamlit_carbon_button)

                mock_declare.assert_called()
                call_args = mock_declare.call_args
                assert "path" in call_args[1]
                assert "url" not in call_args[1]

    def test_development_mode(self):
        """Test component declaration in development mode"""
        with patch.dict("os.environ", {"STREAMLIT_CARBON_BUTTON_DEV_MODE": "true"}):
            with patch("streamlit.components.v1.declare_component") as mock_declare:
                # Re-import to trigger module-level code
                import importlib
                import streamlit_carbon_button

                importlib.reload(streamlit_carbon_button)

                mock_declare.assert_called()
                call_args = mock_declare.call_args
                assert "url" in call_args[1]
                assert call_args[1]["url"] == "http://localhost:3000"
