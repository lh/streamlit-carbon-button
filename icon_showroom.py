#!/usr/bin/env python3
"""
Carbon Button Icon Showroom
Interactive gallery to browse all available Carbon Design System icons
"""

import streamlit as st
from streamlit_carbon_button import carbon_button, CarbonIcons
import inspect

# Page config
st.set_page_config(
    page_title="Carbon Button Icon Showroom",
    page_icon="🎨",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better layout
st.markdown("""
<style>
    .icon-grid {
        display: grid;
        grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
        gap: 1rem;
        padding: 1rem 0;
    }
    .stButton > button {
        width: 100%;
    }
</style>
""", unsafe_allow_html=True)

st.title("🎨 Carbon Button Icon Showroom")
st.markdown("Browse all available Carbon Design System icons for `streamlit-carbon-button`")

# Get all icon names and their SVG content
all_icons = []
for name, value in inspect.getmembers(CarbonIcons):
    if not name.startswith('_') and isinstance(value, str) and value.startswith('<svg'):
        all_icons.append((name, value))

# Sort alphabetically
all_icons.sort(key=lambda x: x[0])

# Sidebar controls
with st.sidebar:
    st.header("🔍 Filter Icons")
    
    # Search box
    search_term = st.text_input("Search icons", placeholder="Type to search...")
    
    # Button type selector
    button_style = st.selectbox(
        "Button Style",
        ["primary", "secondary", "tertiary", "danger", "ghost"]
    )
    
    # Layout options
    cols_per_row = st.slider("Icons per row", 3, 8, 5)
    show_labels = st.checkbox("Show icon names", value=True)
    show_code = st.checkbox("Show code snippets", value=False)
    
    st.divider()
    
    # Stats
    st.metric("Total Icons", len(all_icons))
    
    if search_term:
        filtered = [icon for icon in all_icons if search_term.lower() in icon[0].lower()]
        st.metric("Filtered Icons", len(filtered))

# Filter icons based on search
if search_term:
    display_icons = [(name, svg) for name, svg in all_icons if search_term.lower() in name.lower()]
else:
    display_icons = all_icons

# Main content
if not display_icons:
    st.warning(f"No icons found matching '{search_term}'")
else:
    # Category detection based on icon names
    categories = {
        "File Types": ["PDF", "ZIP", "DOC", "XLS", "PPT", "CSV", "TXT", "SQL", "JSON", "XML"],
        "Actions": ["ADD", "DELETE", "EDIT", "SAVE", "DOWNLOAD", "UPLOAD", "COPY", "CUT", "PASTE"],
        "Navigation": ["HOME", "BACK", "FORWARD", "MENU", "ARROW", "CHEVRON", "CARET"],
        "View/Display": ["VIEW", "EXPAND", "COLLAPSE", "ZOOM", "SCREEN", "PANEL"],
        "Media": ["PLAY", "PAUSE", "STOP", "SKIP", "MICROPHONE", "VOLUME"],
        "Status": ["CHECKMARK", "WARNING", "ERROR", "INFO", "HELP"],
        "Communication": ["EMAIL", "CHAT", "SEND", "NOTIFICATION"],
        "Data": ["CHART", "ANALYTICS", "DATA", "TABLE", "FILTER", "SORT"],
        "User": ["USER", "LOGIN", "LOGOUT", "ACCOUNT", "AVATAR"],
        "Settings": ["SETTINGS", "CONFIGURE", "TOOLS", "BUILD"],
        "Other": []
    }
    
    # Categorize icons
    categorized = {cat: [] for cat in categories}
    for name, svg in display_icons:
        placed = False
        for category, keywords in categories.items():
            if category != "Other" and any(keyword in name for keyword in keywords):
                categorized[category].append((name, svg))
                placed = True
                break
        if not placed:
            categorized["Other"].append((name, svg))
    
    # Display icons by category
    for category, icons in categorized.items():
        if icons:  # Only show categories with icons
            with st.expander(f"{category} ({len(icons)} icons)", expanded=True):
                # Create grid layout
                cols = st.columns(cols_per_row)
                for idx, (name, svg) in enumerate(icons):
                    col_idx = idx % cols_per_row
                    with cols[col_idx]:
                        # Display button
                        clicked = carbon_button(
                            name.replace('_', ' ').title() if show_labels else "",
                            icon=getattr(CarbonIcons, name),
                            button_type=button_style,
                            key=f"btn_{category}_{name}"
                        )
                        
                        if show_code:
                            st.code(f"CarbonIcons.{name}", language="python")
                        
                        if clicked:
                            st.success(f"Clicked: {name}")
                            
                            # Show full code example in a modal-like container
                            with st.container():
                                st.markdown("### 📋 Copy this code:")
                                st.code(f"""
from streamlit_carbon_button import carbon_button, CarbonIcons

if carbon_button("Click me!", icon=CarbonIcons.{name}):
    st.write("Button clicked!")
""", language="python")

# Footer
st.divider()
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("**Total Icons:** " + str(len(all_icons)))
with col2:
    st.markdown("**Package:** `streamlit-carbon-button`")
with col3:
    st.markdown("**Version:** 1.3.0")

# Instructions
with st.expander("📚 How to use these icons"):
    st.markdown("""
    ### Installation
    ```bash
    pip install streamlit-carbon-button
    ```
    
    ### Basic Usage
    ```python
    import streamlit as st
    from streamlit_carbon_button import carbon_button, CarbonIcons
    
    # Simple button with icon
    if carbon_button("Save", icon=CarbonIcons.SAVE):
        st.success("Saved!")
    
    # Different button types
    carbon_button("Primary", button_type="primary")
    carbon_button("Secondary", button_type="secondary")
    carbon_button("Danger", icon=CarbonIcons.DELETE, button_type="danger")
    carbon_button("Ghost", button_type="ghost")
    
    # Icon-only button (no label)
    carbon_button("", icon=CarbonIcons.SETTINGS)
    ```
    
    ### Button Types
    - **primary**: Blue button for primary actions
    - **secondary**: Gray button for secondary actions
    - **tertiary**: Minimal button style
    - **danger**: Red button for destructive actions
    - **ghost**: Transparent button with border
    
    ### Tips
    - Use meaningful icon names (e.g., `SAVE` for save actions)
    - Icon-only buttons work great for toolbars
    - Combine with columns for button groups
    - File type icons (PDF, ZIP) contain text in the SVG itself
    """)