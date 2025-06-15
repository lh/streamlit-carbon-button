"""
Minimal test to debug the component
"""
import streamlit as st
import os

# Force production mode
os.environ["STREAMLIT_CARBON_BUTTON_DEV_MODE"] = "false"

st.title("Minimal Component Test")

# Show that we're in production mode
st.write("Dev mode:", os.environ.get("STREAMLIT_CARBON_BUTTON_DEV_MODE", "not set"))

# Try to import
try:
    from streamlit_carbon_button import carbon_button, CarbonIcons
    st.success("✅ Import successful")
    
    # Get component info
    import streamlit_carbon_button
    st.write("Module location:", briquette.__file__)
    
    # Check component function
    st.write("Component function type:", type(briquette._component_func))
    st.write("Component name:", briquette._component_func.name)
    st.write("Component path:", briquette._component_func.path)
    
    # Try the simplest possible button
    st.header("Test 1: Minimal Button")
    st.write("Creating button...")
    
    # Add a container to see if space is being allocated
    with st.container():
        st.write("Before button")
        result = carbon_button("Click Me", key="minimal_test")
        st.write("After button")
        st.write("Button result:", result)
    
    # Try with explicit parameters
    st.header("Test 2: Button with all params")
    result2 = carbon_button(
        label="Test Button",
        icon="",  # No icon
        key="test2",
        button_type="secondary",
        disabled=False,
        use_container_width=False
    )
    st.write("Result2:", result2)
    
except Exception as e:
    st.error(f"Error: {type(e).__name__}: {e}")
    import traceback
    st.code(traceback.format_exc())

# Test if Streamlit's built-in components work
st.header("Control Test: Regular Streamlit Button")
if st.button("Regular Button", key="regular"):
    st.write("Regular button clicked!")

st.divider()
st.info("Check browser console for any JavaScript errors!")