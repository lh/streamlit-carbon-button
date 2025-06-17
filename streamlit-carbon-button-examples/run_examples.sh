#!/bin/bash

echo "🎨 Streamlit Carbon Button Examples"
echo ""
echo "Choose an example to run:"
echo ""
echo "Basic Examples:"
echo "  1) Hello World"
echo "  2) Button Types"
echo "  3) With Icons"
echo "  4) Default Button"
echo "  5) Icon Only"
echo ""
echo "Advanced Examples:"
echo "  6) Dynamic Defaults"
echo ""

read -p "Enter number (1-6): " choice

case $choice in
    1) streamlit run basic/01_hello_world.py ;;
    2) streamlit run basic/02_button_types.py ;;
    3) streamlit run basic/03_with_icons.py ;;
    4) streamlit run basic/04_default_button.py ;;
    5) streamlit run basic/05_icon_only.py ;;
    6) streamlit run advanced/01_dynamic_defaults.py ;;
    *) echo "Invalid choice"; exit 1 ;;
esac
