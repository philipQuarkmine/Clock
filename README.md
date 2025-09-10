# Elegant Clock - Setup Instructions

A beautiful, customizable analog and digital clock with color controls that can run as a Progressive Web App (PWA).

## 📁 Files Included

- **`web_clock.html`** - Main clock application
- **`manifest.json`** - PWA configuration for app installation
- **`sw.js`** - Service worker for offline functionality

## 🚀 Quick Start

### Option 1: Simple HTML (Basic Use)
Just double-click `web_clock.html` to open in your browser.
- ✅ Full clock functionality
- ✅ Color customization
- ✅ Analog/Digital toggle
- ❌ No PWA features (install, offline)

### Option 2: PWA with Python Server (Recommended)

1. **Open Terminal/Command Prompt**
   - Windows: Press `Win + R`, type `cmd`, press Enter
   - Mac: Press `Cmd + Space`, type `terminal`
   - Linux: Press `Ctrl + Alt + T`

2. **Navigate to Clock Folder**
   ```bash
   cd "path/to/your/clock/folder"
   ```
   Example: `cd "C:\Users\YourName\Downloads"`

3. **Start Python Server**
   ```bash
   python3 -m http.server 8080
   ```

4. **Open in Browser**
   Go to: `http://localhost:8080/web_clock.html`

5. **Install as App (Optional)**
   - Look for install button (⊕) in browser address bar
   - Click "Install Elegant Clock"
   - Runs fullscreen without browser UI

6. **Stop Server**
   Press `Ctrl + C` in terminal when done

## 🎨 Features

- **Analog Clock**: Classic clock face with smooth hand movement
- **Digital Clock**: Large, responsive time display
- **Color Wheel**: 
  - Outer handle: Changes background color
  - Inner handle: Changes clock color
- **Responsive**: Automatically resizes to fit window
- **PWA Support**: Install as standalone app
- **Offline Ready**: Works without internet after installation

## 🔧 Requirements

- **Python 3.x** (for PWA features)
- **Modern Web Browser** (Chrome, Firefox, Edge, Safari)

Check Python version: `python3 --version`

## 🌐 Alternative Hosting

Upload all files to any web hosting service for permanent access:
- GitHub Pages (free)
- Netlify (free)
- Vercel (free)

## 💡 Tips

- **Bookmark**: Save `http://localhost:8080/web_clock.html` for quick access
- **Fullscreen**: Press `F11` for immersive experience
- **Color Reset**: Refresh page to reset colors to default
- **Mobile**: Works great on phones and tablets too

## 🐛 Troubleshooting

**"Python not found"**: Install from [python.org](https://python.org)
**"Address in use"**: Try different port: `python3 -m http.server 8081`
**Install button missing**: Make sure you're using `http://localhost` not `file://`

---
*Created: September 2025*
*Enjoy your beautiful clock! 🕐✨*
