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


# Carbon icon definitions
class CarbonIcons:
    """Pre-defined Carbon Design System icons"""
    
    UPLOAD = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32"><path d="M26 24v4H6v-4H4v4a2 2 0 0 0 2 2h20a2 2 0 0 0 2-2v-4z"/><path d="M6 12l1.41 1.41L15 5.83V24h2V5.83l7.59 7.58L26 12 16 2 6 12z"/></svg>'
    DOWNLOAD = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32"><path d="M26 24v4H6v-4H4v4a2 2 0 0 0 2 2h20a2 2 0 0 0 2-2v-4z"/><path d="M26 14l-1.41-1.41L17 20.17V2h-2v18.17l-7.59-7.58L6 14l10 10l10-10z"/></svg>'
    SAVE = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32"><path d="M27.71 9.29l-5-5A1 1 0 0 0 22 4H6a2 2 0 0 0-2 2v20a2 2 0 0 0 2 2h20a2 2 0 0 0 2-2V10a1 1 0 0 0-.29-.71zM12 6h8v6h-8zm8 20h-8v-8h8zm2 0v-8a2 2 0 0 0-2-2h-8a2 2 0 0 0-2 2v8H6V6h4v6a2 2 0 0 0 2 2h8a2 2 0 0 0 2-2V6.41l4 4V26z"/></svg>'
    COPY = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32"><path d="M28 10v18H10V10h18m0-2H10a2 2 0 0 0-2 2v18a2 2 0 0 0 2 2h18a2 2 0 0 0 2-2V10a2 2 0 0 0-2-2z"/><path d="M4 18H2V4a2 2 0 0 1 2-2h14v2H4z"/></svg>'
    DELETE = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32"><path d="M12 12h2v12h-2zm6 0h2v12h-2z"/><path d="M4 6v2h2v20a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2V8h2V6zm4 22V8h16v20zm4-26h8v2h-8z"/></svg>'
    ADD = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32"><path d="M17 15V8h-2v7H8v2h7v7h2v-7h7v-2z"/></svg>'
    CLOSE = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32"><path d="M24 9.4L22.6 8 16 14.6 9.4 8 8 9.4 14.6 16 8 22.6 9.4 24 16 17.4 22.6 24 24 22.6 17.4 16 24 9.4z"/></svg>'
    SETTINGS = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32"><path d="M27 16.76c0-.25 0-.5 0-.76s0-.51 0-.77l1.92-1.68A2 2 0 0 0 29.3 11L26.94 7a2 2 0 0 0-1.73-1 2 2 0 0 0-.64.1l-2.43.82a11.35 11.35 0 0 0-1.31-.75l-.51-2.52a2 2 0 0 0-2-1.61h-4.68a2 2 0 0 0-2 1.61l-.51 2.52a11.48 11.48 0 0 0-1.32.75l-2.38-.82A2 2 0 0 0 6.79 6a2 2 0 0 0-1.73 1L2.7 11a2 2 0 0 0 .41 2.51L5 15.24c0 .25 0 .5 0 .76s0 .51 0 .77l-1.92 1.68A2 2 0 0 0 2.7 21l2.36 4a2 2 0 0 0 1.73 1 2 2 0 0 0 .64-.1l2.43-.82a11.35 11.35 0 0 0 1.31.75l.51 2.52a2 2 0 0 0 2 1.61h4.72a2 2 0 0 0 2-1.61l.51-2.52a11.48 11.48 0 0 0 1.32-.75l2.42.82a2 2 0 0 0 .64.1 2 2 0 0 0 1.73-1l2.28-4a2 2 0 0 0-.41-2.51zM25.21 24l-3.43-1.16a8.86 8.86 0 0 1-2.71 1.57L18.36 28h-4.72l-.71-3.55a9.36 9.36 0 0 1-2.7-1.57L6.79 24l-2.36-4 2.72-2.4a8.9 8.9 0 0 1 0-3.13L4.43 12l2.36-4 3.43 1.16a8.86 8.86 0 0 1 2.71-1.57L13.64 4h4.72l.71 3.55a9.36 9.36 0 0 1 2.7 1.57L25.21 8l2.36 4-2.72 2.4a8.9 8.9 0 0 1 0 3.13L27.57 20z"/><path d="M16 22a6 6 0 1 1 6-6 6 6 0 0 1-6 6zm0-10a4 4 0 1 0 4 4 4 4 0 0 0-4-4z"/></svg>'
    SEARCH = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32"><path d="M29 27.5858l-7.5521-7.5521a11.0177 11.0177 0 1 0-1.4142 1.4142L27.5858 29zM4 13a9 9 0 1 1 9 9 9.01 9.01 0 0 1-9-9z"/></svg>'
    FILTER = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32"><path d="M2 7v2h28V7zm4 7h20v-2H6zm5 7h10v-2H11z"/></svg>'
    CHART_BAR = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32"><path d="M27 25V6h-6v19H11V14H5v11H2v2h28v-2zM7 25V16h2v9zm6 0V8h6v17z"/></svg>'
    DOCUMENT = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32"><path d="M25.7 9.3l-7-7c-.2-.2-.4-.3-.7-.3H8c-1.1 0-2 .9-2 2v24c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V10c0-.3-.1-.5-.3-.7zM18 4.4l5.6 5.6H18V4.4zM24 28H8V4h8v6c0 1.1.9 2 2 2h6v16z"/><path d="M10 22h12v2H10zm0-6h12v2H10z"/></svg>'
    PLAY = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32"><path d="M11 23a1 1 0 0 1-1-1V10a1 1 0 0 1 1.4473-.8945l12 6a1 1 0 0 1 0 1.789l-12 6A1.001 1.001 0 0 1 11 23zm1-11.3821v8.764L20.764 16z"/></svg>'
    HELP = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32"><path d="M16 2a14 14 0 1 0 14 14A14 14 0 0 0 16 2zm0 26a12 12 0 1 1 12-12 12 12 0 0 1-12 12z"/><path d="M17.5 23h-3v-2c0-2.1 1.6-3.1 2.9-3.9 1.2-.7 2.1-1.3 2.1-2.1 0-1.7-1.3-3-3-3-1.4 0-2.6 1-2.9 2.3L11.8 14c.5-2.3 2.5-4 4.7-4 2.8 0 5 2.2 5 5 0 2.1-1.6 3.1-2.9 3.9-1.2.7-2.1 1.3-2.1 2.1v2z"/><circle cx="16" cy="26.5" r="1.5"/></svg>'
    WARNING = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32"><path d="M16 2C8.3 2 2 8.3 2 16s6.3 14 14 14 14-6.3 14-14S23.7 2 16 2zm-1.1 6h2.2v11h-2.2V8zM16 25c-.8 0-1.5-.7-1.5-1.5S15.2 22 16 22s1.5.7 1.5 1.5S16.8 25 16 25z"/></svg>'
    HOME = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32"><path d="M16.612 2.214a1.01 1.01 0 0 0-1.242 0L1 13.419l1.243 1.572L4 13.621V26a2.004 2.004 0 0 0 2 2h20a2.004 2.004 0 0 0 2-2V13.63L29.757 15 31 13.428zM18 26h-4v-8h4zm2 0v-8a2.002 2.002 0 0 0-2-2h-4a2.002 2.002 0 0 0-2 2v8H6V12.062l10-7.79 10 7.8V26z"/></svg>'
    INFO = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32"><path d="M16 2a14 14 0 1 0 14 14A14 14 0 0 0 16 2zm0 26a12 12 0 1 1 12-12 12 12 0 0 1-12 12z"/><path d="M16 11a1.5 1.5 0 1 0 1.5-1.5A1.5 1.5 0 0 0 16 11zm-1.125 3h2.25v9h-2.25z"/></svg>'
    SUCCESS = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32"><path d="M16 2a14 14 0 1 0 14 14A14 14 0 0 0 16 2zm0 26a12 12 0 1 1 12-12 12 12 0 0 1-12 12z"/><path d="M14 21.5l-5-5.6 1.6-1.4 3.4 3.9 7.4-8.9 1.6 1.3z"/></svg>'