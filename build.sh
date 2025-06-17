#!/bin/bash

echo "Building Carbon Button Component..."

# Build the frontend
cd frontend
echo "Installing dependencies..."
npm install

echo "Building React app..."
npm run build

# Copy build files to Python package
echo "Copying build files..."
rm -rf ../briquette/frontend
mkdir -p ../briquette/frontend

# Copy the built static files
cp -r build/* ../briquette/frontend/

echo "Build complete!"
echo ""
echo "To install the component:"
echo "  pip install ."
echo ""
echo "To use in development mode:"
echo "  export STREAMLIT_CARBON_BUTTON_DEV_MODE=true"
echo "  cd frontend && npm start"
