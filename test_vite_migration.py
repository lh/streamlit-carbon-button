#!/usr/bin/env python3
"""
Comprehensive test suite for Vite migration
Tests all aspects of the carbon button component
"""

import streamlit as st
import time
import os
import subprocess
import sys
from pathlib import Path

# Page config
st.set_page_config(
    page_title="Carbon Button Vite Migration Test",
    page_icon="🧪",
    layout="wide"
)

st.title("🧪 Carbon Button Component - Vite Migration Test Suite")

# Test status tracking
if 'test_results' not in st.session_state:
    st.session_state.test_results = {}

# Helper function to run commands
def run_command(cmd, cwd=None):
    """Run a shell command and return output"""
    try:
        result = subprocess.run(
            cmd, 
            shell=True, 
            cwd=cwd,
            capture_output=True, 
            text=True,
            timeout=60
        )
        return result.returncode == 0, result.stdout, result.stderr
    except subprocess.TimeoutExpired:
        return False, "", "Command timed out"
    except Exception as e:
        return False, "", str(e)

# Sidebar for test controls
with st.sidebar:
    st.header("Test Controls")
    
    dev_mode = st.radio(
        "Component Mode",
        ["Production (Built)", "Development (Vite Dev Server)"],
        help="Test the component in different modes"
    )
    
    if dev_mode == "Development (Vite Dev Server)":
        os.environ["STREAMLIT_CARBON_BUTTON_DEV_MODE"] = "true"
        st.info("⚠️ Make sure Vite dev server is running:\n`cd frontend && npm start`")
    else:
        os.environ["STREAMLIT_CARBON_BUTTON_DEV_MODE"] = "false"
    
    if st.button("🔄 Clear Test Results"):
        st.session_state.test_results = {}
        st.rerun()

# Main test sections
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "1️⃣ Basic Tests", 
    "2️⃣ Visual Tests", 
    "3️⃣ Interaction Tests",
    "4️⃣ Build Tests",
    "5️⃣ Performance"
])

# Tab 1: Basic Tests
with tab1:
    st.header("Basic Functionality Tests")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Import Test")
        try:
            from briquette import carbon_button, CarbonIcons
            st.success("✅ Import successful")
            st.session_state.test_results['import'] = True
            
            # Show component info
            import briquette
            with st.expander("Component Info"):
                st.write("Module location:", briquette.__file__)
                st.write("Component function:", type(briquette._component_func))
                st.write("Dev mode:", os.environ.get("STREAMLIT_CARBON_BUTTON_DEV_MODE"))
        except Exception as e:
            st.error(f"❌ Import failed: {e}")
            st.session_state.test_results['import'] = False
            st.stop()
    
    with col2:
        st.subheader("Basic Button Test")
        if carbon_button("Test Button", key="basic_test"):
            st.success("✅ Button clicked!")
            st.session_state.test_results['basic_click'] = True
        
        # Session state test
        click_count = st.session_state.get('basic_test', 0)
        st.metric("Click Count", click_count)

# Tab 2: Visual Tests
with tab2:
    st.header("Visual Component Tests")
    
    # Button Types
    st.subheader("Button Types")
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        if carbon_button("Primary", key="vis_primary", button_type="primary"):
            st.caption("Primary clicked")
    
    with col2:
        if carbon_button("Secondary", key="vis_secondary", button_type="secondary"):
            st.caption("Secondary clicked")
    
    with col3:
        if carbon_button("Danger", key="vis_danger", button_type="danger"):
            st.caption("Danger clicked")
    
    with col4:
        if carbon_button("Ghost", key="vis_ghost", button_type="ghost"):
            st.caption("Ghost clicked")
    
    # Icons
    st.subheader("Icon Tests")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.caption("Icon + Text")
        if carbon_button("Save File", icon=CarbonIcons.SAVE, key="icon_text"):
            st.success("Save clicked")
    
    with col2:
        st.caption("Icon Only")
        if carbon_button("", icon=CarbonIcons.SETTINGS, key="icon_only"):
            st.success("Settings clicked")
    
    with col3:
        st.caption("Text Only")
        if carbon_button("No Icon", key="text_only"):
            st.success("Text clicked")
    
    # Full Width
    st.subheader("Layout Tests")
    if carbon_button("Full Width Button", key="full_width", use_container_width=True):
        st.success("Full width clicked")
    
    # Disabled
    col1, col2 = st.columns(2)
    with col1:
        carbon_button("Disabled Button", key="disabled", disabled=True)
    with col2:
        carbon_button("Enabled Button", key="enabled", disabled=False)
    
    # Custom Colors
    st.subheader("Custom Colors Test")
    custom_colors = {
        "rest_bg": "#ff6b6b",
        "rest_text": "#ffffff",
        "hover_bg": "#fa5252",
        "active_bg": "#e03131",
        "active_text": "#ffffff"
    }
    if carbon_button("Custom Colors", key="custom", colors=custom_colors):
        st.success("Custom button clicked")

# Tab 3: Interaction Tests
with tab3:
    st.header("Interaction & State Tests")
    
    # Multiple buttons
    st.subheader("Multiple Button Independence")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if carbon_button("Button A", key="multi_a"):
            st.write("A clicked at", time.time())
    
    with col2:
        if carbon_button("Button B", key="multi_b"):
            st.write("B clicked at", time.time())
    
    with col3:
        if carbon_button("Button C", key="multi_c"):
            st.write("C clicked at", time.time())
    
    # Rapid clicking test
    st.subheader("Rapid Click Test")
    if 'rapid_clicks' not in st.session_state:
        st.session_state.rapid_clicks = 0
    
    if carbon_button("Click Rapidly!", key="rapid", button_type="primary"):
        st.session_state.rapid_clicks += 1
    
    st.metric("Rapid Clicks", st.session_state.rapid_clicks)
    if st.button("Reset Counter"):
        st.session_state.rapid_clicks = 0
        st.rerun()
    
    # Icon Grid
    st.subheader("All Icons Test")
    icons = [
        ("UPLOAD", CarbonIcons.UPLOAD),
        ("DOWNLOAD", CarbonIcons.DOWNLOAD),
        ("SAVE", CarbonIcons.SAVE),
        ("COPY", CarbonIcons.COPY),
        ("DELETE", CarbonIcons.DELETE),
        ("ADD", CarbonIcons.ADD),
        ("CLOSE", CarbonIcons.CLOSE),
        ("SETTINGS", CarbonIcons.SETTINGS),
        ("SEARCH", CarbonIcons.SEARCH),
        ("FILTER", CarbonIcons.FILTER),
        ("CHART_BAR", CarbonIcons.CHART_BAR),
        ("DOCUMENT", CarbonIcons.DOCUMENT),
        ("PLAY", CarbonIcons.PLAY),
        ("HELP", CarbonIcons.HELP),
        ("WARNING", CarbonIcons.WARNING),
        ("HOME", CarbonIcons.HOME),
        ("INFO", CarbonIcons.INFO),
        ("SUCCESS", CarbonIcons.SUCCESS),
    ]
    
    cols = st.columns(6)
    for i, (name, icon) in enumerate(icons):
        with cols[i % 6]:
            if carbon_button("", icon=icon, key=f"icon_{name}"):
                st.caption(f"{name} clicked")

# Tab 4: Build Tests
with tab4:
    st.header("Build & Infrastructure Tests")
    
    # Check Node/npm
    st.subheader("Environment Check")
    col1, col2 = st.columns(2)
    
    with col1:
        success, stdout, stderr = run_command("node --version")
        if success:
            st.success(f"✅ Node.js: {stdout.strip()}")
        else:
            st.error("❌ Node.js not found")
    
    with col2:
        success, stdout, stderr = run_command("npm --version")
        if success:
            st.success(f"✅ npm: {stdout.strip()}")
        else:
            st.error("❌ npm not found")
    
    # Check Vite installation
    st.subheader("Vite Status")
    frontend_dir = Path("frontend")
    
    if (frontend_dir / "node_modules").exists():
        st.success("✅ node_modules exists")
        
        # Check for Vite
        if (frontend_dir / "node_modules" / "vite").exists():
            st.success("✅ Vite is installed")
        else:
            st.error("❌ Vite not found in node_modules")
    else:
        st.warning("⚠️ node_modules not found. Run `npm install` in frontend/")
    
    # Build test
    st.subheader("Build Test")
    if st.button("🔨 Run Production Build"):
        with st.spinner("Building with Vite..."):
            success, stdout, stderr = run_command("npm run build", cwd="frontend")
            
            if success:
                st.success("✅ Build successful!")
                with st.expander("Build Output"):
                    st.code(stdout)
                
                # Check build output
                build_dir = frontend_dir / "build"
                if build_dir.exists():
                    files = list(build_dir.rglob("*"))
                    st.write(f"Build contains {len(files)} files")
                    
                    # Check for key files
                    has_index = (build_dir / "index.html").exists()
                    has_js = any(f.suffix == ".js" for f in files)
                    has_css = any(f.suffix == ".css" for f in files)
                    
                    col1, col2, col3 = st.columns(3)
                    with col1:
                        if has_index:
                            st.success("✅ index.html")
                        else:
                            st.error("❌ index.html")
                    with col2:
                        if has_js:
                            st.success("✅ JavaScript")
                        else:
                            st.error("❌ JavaScript")
                    with col3:
                        if has_css:
                            st.success("✅ CSS")
                        else:
                            st.error("❌ CSS")
            else:
                st.error("❌ Build failed!")
                with st.expander("Error Output"):
                    st.code(stderr)

# Tab 5: Performance
with tab5:
    st.header("Performance Metrics")
    
    # Bundle size comparison
    st.subheader("Bundle Size Analysis")
    
    build_dir = Path("frontend/build")
    if build_dir.exists():
        total_size = 0
        js_size = 0
        css_size = 0
        
        for file in build_dir.rglob("*"):
            if file.is_file():
                size = file.stat().st_size
                total_size += size
                if file.suffix == ".js":
                    js_size += size
                elif file.suffix == ".css":
                    css_size += size
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Total Build Size", f"{total_size / 1024:.1f} KB")
        with col2:
            st.metric("JavaScript", f"{js_size / 1024:.1f} KB")
        with col3:
            st.metric("CSS", f"{css_size / 1024:.1f} KB")
        
        # Expected improvements
        st.info("""
        **Expected improvements with Vite:**
        - 50-70% smaller bundle size
        - 10-100x faster development builds
        - Near-instant HMR
        """)
    else:
        st.warning("No build found. Run build test first.")
    
    # Component render test
    st.subheader("Render Performance Test")
    
    num_buttons = st.slider("Number of buttons to render", 1, 50, 10)
    
    start_time = time.time()
    cols = st.columns(5)
    for i in range(num_buttons):
        with cols[i % 5]:
            carbon_button(f"Button {i}", key=f"perf_{i}")
    
    render_time = time.time() - start_time
    st.metric("Render Time", f"{render_time * 1000:.1f} ms")

# Summary
st.divider()
st.header("📊 Test Summary")

if st.session_state.test_results:
    passed = sum(1 for v in st.session_state.test_results.values() if v)
    total = len(st.session_state.test_results)
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Tests Passed", f"{passed}/{total}")
    with col2:
        if passed == total:
            st.success("✅ All tests passed!")
        else:
            st.warning(f"⚠️ {total - passed} tests failed")
else:
    st.info("Run tests to see results")

# Debug info
with st.expander("🔧 Debug Information"):
    st.write("Session State:", dict(st.session_state))
    st.write("Environment:", {
        "STREAMLIT_CARBON_BUTTON_DEV_MODE": os.environ.get("STREAMLIT_CARBON_BUTTON_DEV_MODE"),
        "Python": sys.version,
        "Streamlit": st.__version__,
        "Working Directory": os.getcwd()
    })