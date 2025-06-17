"""
Standalone demo of default button animation concepts
Shows what the animations would look like
"""

import streamlit as st
from streamlit_carbon_button import carbon_button, CarbonIcons

st.set_page_config(page_title="Default Button Animations Demo", layout="wide")

st.title("🎯 Default Button Animation Concepts")
st.write("Visual demonstrations of how default buttons could be indicated")

# Add a toggle for base color approach
approach = st.radio(
    "Choose approach:",
    ["Same base color + effects", "Different base color (e.g., blue primary)"],
    horizontal=True,
    help="You can indicate default buttons with effects on the same color, or use a different base color",
)

# Add the CSS animations
if approach == "Same base color + effects":
    button_bg = "#e6e2e2"  # Same as Carbon primary
    button_color = "#1a1a1a"
    button_hover_bg = "#f5f5f5"
else:
    button_bg = "#0f62fe"  # Carbon blue for differentiation
    button_color = "white"
    button_hover_bg = "#0043ce"

st.markdown(
    f"""
<style>
/* Animation definitions */
@keyframes pulse {{
    0% {{ transform: scale(1); opacity: 1; }}
    50% {{ transform: scale(1.05); opacity: 0.9; }}
    100% {{ transform: scale(1); opacity: 1; }}
}}

@keyframes glow {{
    0% {{ box-shadow: 0 0 5px rgba(80, 228, 224, 0.5); }}
    50% {{ box-shadow: 0 0 20px rgba(80, 228, 224, 0.8), 0 0 30px rgba(80, 228, 224, 0.4); }}
    100% {{ box-shadow: 0 0 5px rgba(80, 228, 224, 0.5); }}
}}

@keyframes breathe {{
    0%, 100% {{ transform: scale(1); }}
    50% {{ transform: scale(1.02); }}
}}

/* Button mockups */
.button-demo {{
    display: inline-block;
    padding: 0.75rem 1rem;
    background: {button_bg};
    color: {button_color};
    font-family: "IBM Plex Sans", system-ui, -apple-system, sans-serif;
    font-size: 14px;
    font-weight: 400;
    border: none;
    cursor: pointer;
    transition: all 70ms cubic-bezier(0.2, 0, 0.38, 0.9);
}}

.button-secondary {{
    background: #e6e2e2;
    color: #1a1a1a;
}}

.button-demo:hover {{
    background: {button_hover_bg};
    transform: translateY(-1px);
    box-shadow: 0 2px 6px rgba(0, 0, 0, 0.15);
}}

.button-secondary:hover {{
    background: #f5f5f5;
}}

/* Animation classes */
.pulse-demo {{
    animation: pulse 2s ease-in-out infinite;
}}

.glow-demo {{
    animation: glow 2s ease-in-out infinite;
    border-radius: 2px;
}}

.breathe-demo {{
    animation: breathe 3s ease-in-out infinite;
}}

.elevated-demo {{
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
    transform: translateY(-2px);
}}

.ring-demo {{
    box-shadow: 0 0 0 3px rgba(80, 228, 224, 0.5);
    border-radius: 2px;
}}

.teal-shadow-demo {{
    box-shadow: 0 4px 12px rgba(80, 228, 224, 0.4);
    transform: translateY(-2px);
}}

/* Container for spacing */
.demo-container {{
    margin: 2rem 0;
    text-align: center;
}}

/* Respect reduced motion */
@media (prefers-reduced-motion: reduce) {{
    .pulse-demo,
    .glow-demo,
    .breathe-demo {{
        animation: none;
    }}
}}
</style>
""",
    unsafe_allow_html=True,
)

# Show CSS mock-ups first
st.header("1. Static Style Options (No Animation)")
if approach == "Same base color + effects":
    st.write(
        "These static styles are applied to buttons with the same base color as regular buttons:"
    )
else:
    st.write(
        "These show default buttons with a different base color (blue) plus static effects:"
    )

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(
        """
    <div class="demo-container">
        <div class="button-demo ring-demo">Get Started</div>
    </div>
    """,
        unsafe_allow_html=True,
    )
    st.caption("**Teal Ring**: Border indicator")

with col2:
    st.markdown(
        """
    <div class="demo-container">
        <div class="button-demo elevated-demo">Get Started</div>
    </div>
    """,
        unsafe_allow_html=True,
    )
    st.caption("**Shadow**: Classic elevation")

with col3:
    st.markdown(
        """
    <div class="demo-container">
        <div class="button-demo teal-shadow-demo">Get Started</div>
    </div>
    """,
        unsafe_allow_html=True,
    )
    st.caption("**Teal Shadow**: Colored elevation")

st.divider()

st.header("2. Animated Options (For Reference)")
st.write("You mentioned you don't prefer these, but showing for completeness:")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(
        """
    <div class="demo-container">
        <div class="button-demo pulse-demo">Get Started</div>
    </div>
    """,
        unsafe_allow_html=True,
    )
    st.caption("**Pulse**: Scale animation")

with col2:
    st.markdown(
        """
    <div class="demo-container">
        <div class="button-demo glow-demo">Get Started</div>
    </div>
    """,
        unsafe_allow_html=True,
    )
    st.caption("**Glow**: Animated shadow")

with col3:
    st.markdown(
        """
    <div class="demo-container">
        <div class="button-demo breathe-demo">Get Started</div>
    </div>
    """,
        unsafe_allow_html=True,
    )
    st.caption("**Breathe**: Gentle scale")

st.divider()

# Real component comparison
st.header("3. Component Comparison")
st.write("How the static styles would look in context with real Carbon buttons:")

# Form example
st.subheader("Form Context")
col1, col2, col3 = st.columns([3, 2, 2])

with col1:
    st.text_input("Enter your email", placeholder="you@example.com", key="email_demo")

with col2:
    st.markdown(
        """
    <div style="text-align: center;">
        <div class="button-demo teal-shadow-demo" style="margin-bottom: 0.5rem;">Subscribe</div>
    </div>
    """,
        unsafe_allow_html=True,
    )
    if carbon_button(
        "Subscribe", key="sub1", button_type="primary", icon=CarbonIcons.SUCCESS
    ):
        st.success("Subscribed!")
    st.caption("↑ Teal shadow style")

with col3:
    if carbon_button("Cancel", key="cancel1", button_type="ghost"):
        st.info("Cancelled")

# Action group example
st.subheader("Action Group Context")
col1, col2, col3, col4 = st.columns(4)

with col1:
    if carbon_button("Save Draft", key="draft", button_type="secondary"):
        st.info("Saved")

with col2:
    st.markdown(
        """
    <div style="text-align: center;">
        <div class="button-demo ring-demo" style="margin-bottom: 0.5rem;">Publish</div>
    </div>
    """,
        unsafe_allow_html=True,
    )
    if carbon_button(
        "Publish", key="pub", button_type="primary", icon=CarbonIcons.UPLOAD
    ):
        st.success("Published!")
    st.caption("↑ Teal ring style")

with col3:
    if carbon_button("Preview", key="prev", button_type="ghost"):
        st.info("Preview")

with col4:
    if carbon_button("Delete", key="del", button_type="danger"):
        st.error("Deleted")

st.divider()

# Implementation notes
st.header("4. Implementation Approach")

st.info(
    """
**To implement these animations in the actual component:**

1. **Add to CarbonButton.tsx**:
   - New props: `isDefault` and `defaultStyle`
   - Apply animation classes to the button element

2. **Add CSS animations to index.css**:
   - Define the keyframe animations
   - Create modifier classes

3. **Python API**:
   ```python
   carbon_button(
       "Get Started",
       is_default=True,
       default_style="pulse"  # or glow, breathe, elevated, ring
   )
   ```
"""
)

# Show side-by-side comparison
st.header("5. Side-by-Side Comparison")

st.subheader("Static Styles (Recommended)")
cols = st.columns(3)
styles = ["ring", "elevated", "teal-shadow"]
style_names = ["Teal Ring", "Shadow", "Teal Shadow"]

for i, (col, style, name) in enumerate(zip(cols, styles, style_names)):
    with col:
        st.write(f"**{name}**")
        st.markdown(
            f"""
        <div class="demo-container">
            <div class="button-demo {style}-demo">Default</div>
        </div>
        """,
            unsafe_allow_html=True,
        )

        # Regular button below for comparison
        carbon_button("Regular", key=f"compare_{i}", button_type="primary")

st.caption("Top: Styled default button | Bottom: Regular Carbon button")

# User preference
st.divider()
st.header("6. Which style do you prefer?")

preference = st.radio(
    "Select your favorite default button style:",
    ["Teal Ring", "Shadow", "Teal Shadow", "None - keep it simple"],
    horizontal=True,
    help="Based on your feedback, focusing on static styles",
)

if preference != "None - keep it simple":
    st.write(
        f"Great choice! The **{preference}** style would be perfect for indicating default actions."
    )

st.info(
    """
**Next Steps:**
1. Choose your preferred animation style
2. We'll implement it in the CarbonButton component
3. Add the `is_default` prop to the Python API
4. Test with real use cases
"""
)
