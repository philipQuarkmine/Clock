#!/usr/bin/env python3
"""
Chromebook Clock - Complete Standalone Version
All-in-one clock application adapted from Windows to Chromebook

Usage:
  python3 chromebook_clock.py            # Auto-updating terminal clock
  python3 chromebook_clock.py --gui      # GUI version (requires Linux GUI)
  python3 chromebook_clock.py --web      # Creates web version file
"""

import time
import os
import sys
import threading
from datetime import datetime


class ChromebookClock:
    def __init__(self):
        self.is_analog = True
        self.running = True

    def clear_screen(self):
        os.system('clear' if os.name == 'posix' else 'cls')

    def display_terminal_clock(self):
        self.clear_screen()
        now = datetime.now()
        
        print("🕐 CHROMEBOOK CLOCK 🕐")
        print("Adapted from Windows to work perfectly on Chromebook!")
        print()
        
        if self.is_analog:
            print("📱 ANALOG MODE - Press 't' for digital, 'q' to quit")
            print("="*60)
            
            hour = now.hour % 12
            minute = now.minute
            
            # ASCII analog clock
            clock_lines = [
                "            12            ",
                "        11      1         ",
                "      10          2       ",
                "    9       ●       3     ",
                "      8           4       ",
                "        7       5         ",
                "            6             "
            ]
            
            for line in clock_lines:
                print("    " + line)
            
            print(f"\n    🕐 Hour hand pointing to: {hour if hour != 0 else 12}")
            print(f"    🕐 Minute hand at: {minute:02d} minutes")
            print(f"    🕐 Second hand at: {now.second:02d} seconds")
            print(f"    ⏰ Current time: {now.strftime('%I:%M:%S %p')}")
            
        else:
            print("💻 DIGITAL MODE - Press 't' for analog, 'q' to quit")
            print("="*60)
            print()
            
            # Digital clock display
            time_str = now.strftime("%H:%M:%S")
            date_str = now.strftime("%A, %B %d, %Y")
            
            print("        ┌─────────────────────────┐")
            print("        │                         │")
            print(f"        │       {time_str}         │")
            print("        │                         │")
            print(f"        │    {now.strftime('%A')}          │")
            print(f"        │  {now.strftime('%B %d, %Y')}       │")
            print("        │                         │")
            print("        └─────────────────────────┘")
        
        print("\n" + "="*60)
        print("✅ This clock now works perfectly on your Chromebook!")
        print("Commands: 't' + Enter = toggle mode, 'q' + Enter = quit")

    def run_terminal_clock(self):
        def get_input():
            while self.running:
                try:
                    choice = input().strip().lower()
                    if choice == 't':
                        self.is_analog = not self.is_analog
                    elif choice == 'q':
                        self.running = False
                        break
                except:
                    break
        
        # Start input handler
        input_thread = threading.Thread(target=get_input, daemon=True)
        input_thread.start()
        
        print("🚀 Starting Chromebook Clock...")
        time.sleep(1)
        
        try:
            while self.running:
                self.display_terminal_clock()
                
                # Update every 2 seconds
                for _ in range(20):
                    if not self.running:
                        break
                    time.sleep(0.1)
                    
        except KeyboardInterrupt:
            self.running = False
        
        self.clear_screen()
        print("🕐 Chromebook Clock stopped. Thanks for using it! 👋")
        print("✅ Your Windows clock has been successfully adapted for Chromebook!")

    def create_gui_version(self):
        gui_code = '''#!/usr/bin/env python3
"""
Chromebook GUI Clock - Tkinter Version
"""

import math
import tkinter as tk
from datetime import datetime

BG_COLOR = "#0b66ff"  # Blue background
HAND_COLOR = "#ffffff"  # White hands

class ChromebookGUIClock:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("Chromebook Clock")
        self.root.geometry("400x450")
        self.root.resizable(True, True)
        self.root.configure(bg=BG_COLOR)
        
        self.is_analog = True
        
        # Toggle button
        self.toggle_btn = tk.Button(
            root, text="Switch to Digital", command=self.toggle_mode,
            bg="white", fg="black", font=("Arial", 12)
        )
        self.toggle_btn.pack(pady=10)
        
        # Display frame
        self.display_frame = tk.Frame(root, bg=BG_COLOR)
        self.display_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        self.setup_analog()
        self.update_clock()

    def toggle_mode(self):
        self.is_analog = not self.is_analog
        for widget in self.display_frame.winfo_children():
            widget.destroy()
        
        if self.is_analog:
            self.toggle_btn.config(text="Switch to Digital")
            self.setup_analog()
        else:
            self.toggle_btn.config(text="Switch to Analog")
            self.setup_digital()

    def setup_analog(self):
        self.canvas = tk.Canvas(self.display_frame, bg=BG_COLOR, highlightthickness=0)
        self.canvas.pack(fill=tk.BOTH, expand=True)
        self.canvas.bind('<Configure>', self.on_resize)

    def setup_digital(self):
        self.time_label = tk.Label(
            self.display_frame, text="", bg=BG_COLOR, fg=HAND_COLOR, 
            font=("Arial", 48, "bold")
        )
        self.time_label.pack(expand=True)

    def on_resize(self, event):
        if self.is_analog:
            self.draw_analog()

    def draw_analog(self):
        if not hasattr(self, 'canvas'):
            return
        self.canvas.delete("all")
        
        w, h = self.canvas.winfo_width(), self.canvas.winfo_height()
        if w <= 1 or h <= 1:
            return
        
        self.center_x, self.center_y = w // 2, h // 2
        self.radius = min(self.center_x, self.center_y) - 20
        
        if self.radius <= 0:
            return
        
        # Clock face
        self.canvas.create_oval(
            self.center_x - self.radius, self.center_y - self.radius,
            self.center_x + self.radius, self.center_y + self.radius,
            outline=HAND_COLOR, width=2
        )
        
        # Hour marks
        for h in range(12):
            angle = math.radians(h * 30)
            x1 = self.center_x + (self.radius - 10) * math.sin(angle)
            y1 = self.center_y - (self.radius - 10) * math.cos(angle)
            x2 = self.center_x + (self.radius - 20) * math.sin(angle)
            y2 = self.center_y - (self.radius - 20) * math.cos(angle)
            self.canvas.create_line(x2, y2, x1, y1, fill=HAND_COLOR, width=2)

    def draw_hands(self):
        if not self.is_analog or not hasattr(self, 'canvas'):
            return
        
        self.canvas.delete("hands")
        now = datetime.now()
        h, m, s = now.hour % 12, now.minute, now.second + now.microsecond / 1_000_000
        
        hour_angle = (h + m / 60 + s / 3600) * 30
        minute_angle = (m + s / 60) * 6
        second_angle = s * 6
        
        self.draw_hand(hour_angle, self.radius * 0.5, 4)
        self.draw_hand(minute_angle, self.radius * 0.7, 2)
        self.draw_hand(second_angle, self.radius * 0.8, 1)

    def draw_hand(self, angle_degrees, length, width):
        if not hasattr(self, 'center_x'):
            return
        rad = math.radians(angle_degrees)
        x = self.center_x + length * math.sin(rad)
        y = self.center_y - length * math.cos(rad)
        self.canvas.create_line(
            self.center_x, self.center_y, x, y,
            fill=HAND_COLOR, width=width, tags="hands", capstyle=tk.ROUND
        )

    def update_clock(self):
        if self.is_analog:
            self.draw_analog()
            self.draw_hands()
        else:
            if hasattr(self, 'time_label'):
                self.time_label.config(text=datetime.now().strftime("%H:%M:%S"))
        self.root.after(1000, self.update_clock)

def main():
    root = tk.Tk()
    ChromebookGUIClock(root)
    root.mainloop()

if __name__ == "__main__":
    main()
'''
        
        with open('chromebook_gui_clock.py', 'w') as f:
            f.write(gui_code)
        print("✅ Created chromebook_gui_clock.py")
        print("   Run with: python3 chromebook_gui_clock.py")

    def create_web_version(self):
        web_code = '''<!DOCTYPE html>
<html>
<head>
    <title>Chromebook Clock</title>
    <style>
        body { background: #0b66ff; color: white; font-family: Arial; text-align: center; margin: 0; padding: 20px; }
        .button { background: white; color: black; padding: 10px 20px; border: none; font-size: 16px; cursor: pointer; margin: 20px; }
        #time { font-size: 48px; font-weight: bold; margin: 50px 0; }
        .info { font-size: 14px; margin: 20px 0; }
    </style>
</head>
<body>
    <h1>🕐 Chromebook Clock</h1>
    <p class="info">✅ Successfully adapted from Windows to Chromebook!</p>
    <button class="button" onclick="toggleFormat()">Toggle Format</button>
    <div id="time"></div>
    <p class="info">This clock works perfectly in Chrome browser on your Chromebook</p>

    <script>
        let is24Hour = true;
        function toggleFormat() { is24Hour = !is24Hour; }
        function updateTime() {
            const now = new Date();
            document.getElementById('time').textContent = now.toLocaleTimeString('en-US', { 
                hour12: !is24Hour, hour: '2-digit', minute: '2-digit', second: '2-digit' 
            });
        }
        setInterval(updateTime, 1000);
        updateTime();
    </script>
</body>
</html>'''
        
        with open('chromebook_web_clock.html', 'w') as f:
            f.write(web_code)
        print("✅ Created chromebook_web_clock.html")
        print("   Open in Chrome browser on your Chromebook!")


def main():
    clock = ChromebookClock()
    
    if len(sys.argv) > 1:
        if sys.argv[1] == '--gui':
            clock.create_gui_version()
            print("\nTo run GUI version:")
            print("1. Enable Linux GUI support in Chrome OS")
            print("2. Run: python3 chromebook_gui_clock.py")
            return
        elif sys.argv[1] == '--web':
            clock.create_web_version()
            return
        elif sys.argv[1] == '--help':
            print(__doc__)
            return
    
    # Default: run terminal clock
    clock.run_terminal_clock()


if __name__ == "__main__":
    main()
