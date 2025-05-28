from setuptools import setup, find_packages

setup(
    name="streamlit-carbon-button",
    version="1.1.0",
    author="Luke Herbert",
    author_email="your.email@example.com",
    description="Carbon Design System button component for Streamlit",
    long_description="A Streamlit component that implements IBM's Carbon Design System buttons with full SVG icon support. Perfect for creating beautiful, accessible buttons in your Streamlit apps.",
    long_description_content_type="text/plain",
    url="https://github.com/yourusername/streamlit-carbon-button",
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    install_requires=[
        "streamlit >= 0.63",
    ],
    package_data={
        "briquette": [
            "frontend/index.html",
            "frontend/asset-manifest.json",
            "frontend/static/css/*",
            "frontend/static/js/*",
        ],
    }
)