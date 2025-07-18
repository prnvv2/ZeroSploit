#!/bin/bash

# ZeroSploit Installation Script
# This script installs ZeroSploit and its dependencies

set -e

echo "=========================================="
echo "     ZeroSploit Installation Script      "
echo "=========================================="
echo ""

# Check if Python 3 is installed
if ! command -v python3 &> /dev/null; then
    echo "Error: Python 3 is required but not installed."
    echo "Please install Python 3.7 or higher first."
    exit 1
fi

# Check Python version
PYTHON_VERSION=$(python3 -c 'import sys; print(".".join(map(str, sys.version_info[:2])))')
echo "Python version: $PYTHON_VERSION"

# Check if pip is available
if ! command -v pip3 &> /dev/null; then
    echo "Error: pip3 is required but not installed."
    echo "Please install pip3 first."
    exit 1
fi

# Install system dependencies
echo "Installing system dependencies..."
if command -v apt-get &> /dev/null; then
    sudo apt-get update
    sudo apt-get install -y nmap
elif command -v yum &> /dev/null; then
    sudo yum install -y nmap
elif command -v pacman &> /dev/null; then
    sudo pacman -S nmap
else
    echo "Warning: Could not install nmap automatically."
    echo "Please install nmap manually for full functionality."
fi

# Install Python dependencies
echo "Installing Python dependencies..."
pip3 install -r requirements.txt

# Make the script executable
chmod +x zerosploit.py

echo ""
echo "=========================================="
echo "        Installation Complete!           "
echo "=========================================="
echo ""
echo "ZeroSploit has been installed successfully."
echo ""
echo "Usage:"
echo "  python3 zerosploit.py"
echo "  python3 zerosploit.py --target example.com"
echo "  python3 zerosploit.py --help"
echo ""
echo "IMPORTANT: This tool is for authorized security testing only."
echo "Only use on systems you own or have explicit permission to test."
echo ""
echo "For documentation, see:"
echo "  - README.md"
echo "  - docs/DOCUMENTATION.md"
echo "  - docs/FAQ.md"
echo ""
echo "Happy ethical hacking!"