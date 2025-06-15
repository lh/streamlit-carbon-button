"""
Streamlit Carbon Button Component
Copyright (c) 2025 Luke Herbert
Licensed under MIT License

Icons from IBM Carbon Design System (Apache 2.0 License)
https://carbondesignsystem.com/
"""

import streamlit.components.v1 as components
import os

# Check if we're in development mode
_DEVELOP_MODE = os.getenv("STREAMLIT_CARBON_BUTTON_DEV_MODE", "").lower() == "true"

# Declare the component
if _DEVELOP_MODE:
    # In development, connect to the React dev server
    _component_func = components.declare_component(
        "carbon_button",
        url="http://localhost:3000",  # Default React dev server port
    )
else:
    # In production, use the built component
    parent_dir = os.path.dirname(os.path.abspath(__file__))
    build_dir = os.path.join(parent_dir, "frontend")
    _component_func = components.declare_component(
        "carbon_button", 
        path=build_dir
    )

def carbon_button(
    label: str,
    icon: str = "",
    key: str = None,
    button_type: str = "primary",
    disabled: bool = False,
    use_container_width: bool = False,
    colors: dict = None,
    is_default: bool = False,
    aria_label: str = None,
) -> bool:
    """
    Create a Carbon Design System button.
    
    Parameters
    ----------
    label : str
        The text to display on the button
    icon : str
        SVG string for the icon (optional)
    key : str
        An optional key that uniquely identifies this component
    button_type : str
        The button style - "primary", "secondary", "danger", or "ghost"
    disabled : bool
        If True, the button will be disabled
    use_container_width : bool
        If True, the button will expand to fill its container
    colors : dict
        Custom colors for the button states. Keys can include:
        - rest_bg, rest_text, rest_border
        - hover_bg, hover_text, hover_border
        - active_bg, active_text, active_border
    is_default : bool
        If True, the button will have a teal shadow to indicate it's the default action
    aria_label : str
        Accessibility label for screen readers (automatically set for icon-only buttons)
        
    Returns
    -------
    bool
        True if the button was clicked, False otherwise
    """
    import streamlit as st
    
    # Generate a unique key if not provided
    if key is None:
        key = f"carbon_button_{id(label)}"
    
    # Store the previous click count in session state
    prev_clicks_key = f"__carbon_button_prev_{key}"
    if prev_clicks_key not in st.session_state:
        st.session_state[prev_clicks_key] = 0
    
    # Call the React component
    component_value = _component_func(
        label=label,
        icon=icon,
        buttonType=button_type,
        disabled=disabled,
        useContainerWidth=use_container_width,
        colors=colors,
        isDefault=is_default,
        ariaLabel=aria_label,
        key=key,
        default=st.session_state[prev_clicks_key],  # Use previous value as default
    )
    
    # Check if there was a new click
    clicked = False
    if component_value is not None and component_value > st.session_state[prev_clicks_key]:
        clicked = True
        st.session_state[prev_clicks_key] = component_value
    
    return clicked

# Also export the raw function name for backward compatibility
carbon_button_raw = carbon_button

# Make the function available at package level
__all__ = ['carbon_button', 'CarbonIcons']


# Import Carbon icons from separate file
from .carbon_icons import CarbonIcons