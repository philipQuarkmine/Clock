#!/bin/bash

# X11 Forwarding Setup for Chromebook
# This script helps set up X11 forwarding to display GUI apps

echo "=== X11 Forwarding Setup for Chromebook ==="
echo ""

echo "Option 1: Using X11 forwarding with SSH"
echo "  1. Install an X server on your Chromebook (like VcXsrv or Xming)"
echo "  2. SSH with X11 forwarding: ssh -X username@hostname"
echo "  3. Export DISPLAY: export DISPLAY=localhost:10.0"
echo "  4. Run: python3 simple_clock.py"
echo ""

echo "Option 2: Using Crostini with GUI support"
echo "  1. Enable Linux GUI support in Chrome OS settings"
echo "  2. Install gui support: sudo apt install x11-apps"
echo "  3. Run: python3 simple_clock.py"
echo ""

echo "Option 3: Web-based clock (Recommended)"
echo "  1. Open web_clock.html in Chrome browser"
echo "  2. Works perfectly without any setup!"
echo ""

echo "Option 4: VNC Server"
echo "  1. Install VNC: sudo apt install tightvncserver"
echo "  2. Start VNC: vncserver :1"
echo "  3. Connect via VNC viewer"
echo "  4. Run: DISPLAY=:1 python3 simple_clock.py"
echo ""

echo "Choose the option that works best for your Chromebook setup!"
