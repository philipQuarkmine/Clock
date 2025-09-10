#!/usr/bin/env python3
"""
Terminal Clock for Chromebook
A simple analog and digital clock that runs in the terminal
"""

import time
import math
import os
import sys
from datetime import datetime


class TerminalClock:
    def __init__(self, width=60, height=30):
        self.width = width
        self.height = height
        self.is_analog = True
        self.center_x = width // 2
        self.center_y = height // 2
        self.radius = min(self.center_x, self.center_y) - 2

    def clear_screen(self):
        os.system('clear' if os.name == 'posix' else 'cls')

    def toggle_mode(self):
        self.is_analog = not self.is_analog

    def draw_analog_clock(self):
        # Create a 2D grid
        grid = [[' ' for _ in range(self.width)] for _ in range(self.height)]
        
        # Draw clock circle
        for angle in range(0, 360, 5):
            rad = math.radians(angle)
            x = int(self.center_x + self.radius * math.cos(rad))
            y = int(self.center_y + self.radius * math.sin(rad))
            if 0 <= x < self.width and 0 <= y < self.height:
                grid[y][x] = '●'
        
        # Draw hour marks
        for h in range(12):
            angle = h * 30
            rad = math.radians(angle)
            x = int(self.center_x + (self.radius - 1) * math.cos(rad))
            y = int(self.center_y + (self.radius - 1) * math.sin(rad))
            if 0 <= x < self.width and 0 <= y < self.height:
                grid[y][x] = str(12 if h == 0 else h)
        
        # Get current time
        now = datetime.now()
        hours = now.hour % 12
        minutes = now.minute
        seconds = now.second
        
        # Draw hour hand
        hour_angle = (hours + minutes / 60) * 30 - 90
        hour_length = self.radius * 0.5
        self.draw_hand(grid, hour_angle, hour_length, 'H')
        
        # Draw minute hand
        minute_angle = minutes * 6 - 90
        minute_length = self.radius * 0.7
        self.draw_hand(grid, minute_angle, minute_length, 'M')
        
        # Draw second hand
        second_angle = seconds * 6 - 90
        second_length = self.radius * 0.8
        self.draw_hand(grid, second_angle, second_length, 'S')
        
        # Draw center
        grid[self.center_y][self.center_x] = '●'
        
        return grid

    def draw_hand(self, grid, angle_degrees, length, char):
        rad = math.radians(angle_degrees)
        steps = int(length)
        for i in range(1, steps):
            x = int(self.center_x + i * math.cos(rad))
            y = int(self.center_y + i * math.sin(rad))
            if 0 <= x < self.width and 0 <= y < self.height:
                grid[y][x] = char

    def display_digital_clock(self):
        now = datetime.now()
        time_str = now.strftime("%H:%M:%S")
        date_str = now.strftime("%Y-%m-%d")
        day_str = now.strftime("%A")
        
        # Create centered display
        lines = []
        lines.append("=" * self.width)
        lines.append(" " * ((self.width - len("DIGITAL CLOCK")) // 2) + "DIGITAL CLOCK")
        lines.append("=" * self.width)
        lines.append("")
        lines.append(" " * ((self.width - len(date_str)) // 2) + date_str)
        lines.append(" " * ((self.width - len(day_str)) // 2) + day_str)
        lines.append("")
        
        # Big time display
        big_time = self.make_big_text(time_str)
        for line in big_time:
            lines.append(" " * ((self.width - len(line)) // 2) + line)
        
        lines.append("")
        lines.append("=" * self.width)
        
        return lines

    def make_big_text(self, text):
        # Simple ASCII art for numbers and colon
        patterns = {
            '0': ['███', '█ █', '█ █', '█ █', '███'],
            '1': [' █ ', '██ ', ' █ ', ' █ ', '███'],
            '2': ['███', '  █', '███', '█  ', '███'],
            '3': ['███', '  █', '███', '  █', '███'],
            '4': ['█ █', '█ █', '███', '  █', '  █'],
            '5': ['███', '█  ', '███', '  █', '███'],
            '6': ['███', '█  ', '███', '█ █', '███'],
            '7': ['███', '  █', '  █', '  █', '  █'],
            '8': ['███', '█ █', '███', '█ █', '███'],
            '9': ['███', '█ █', '███', '  █', '███'],
            ':': [' ', '█', ' ', '█', ' ']
        }
        
        lines = ['', '', '', '', '']
        for char in text:
            if char in patterns:
                pattern = patterns[char]
                for i in range(5):
                    lines[i] += pattern[i] + ' '
        
        return lines

    def run(self):
        print("Terminal Clock - Press Ctrl+C to exit")
        print("Commands: 't' = toggle mode, 'q' = quit")
        print("Starting in analog mode...")
        time.sleep(2)
        
        import threading
        import select
        import sys
        
        # Flag to control the display loop
        self.running = True
        self.input_ready = False
        
        def input_handler():
            while self.running:
                try:
                    if sys.stdin in select.select([sys.stdin], [], [], 0.1)[0]:
                        line = sys.stdin.readline().strip().lower()
                        if line == 't':
                            self.toggle_mode()
                        elif line == 'q':
                            self.running = False
                            break
                except:
                    break
        
        # Start input handler in a separate thread
        input_thread = threading.Thread(target=input_handler, daemon=True)
        input_thread.start()
        
        try:
            while self.running:
                self.clear_screen()
                
                if self.is_analog:
                    print("🕐 ANALOG CLOCK")
                    print("Commands: 't' = switch to digital, 'q' = quit")
                    print("=" * self.width)
                    grid = self.draw_analog_clock()
                    for row in grid:
                        print(''.join(row))
                else:
                    print("🕐 DIGITAL CLOCK")
                    print("Commands: 't' = switch to analog, 'q' = quit")
                    lines = self.display_digital_clock()
                    for line in lines:
                        print(line)
                
                print("=" * self.width)
                print("Current time:", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
                print("Type 't' + Enter to toggle, 'q' + Enter to quit")
                
                # Update every second
                time.sleep(1)
                
        except KeyboardInterrupt:
            self.running = False
        
        self.clear_screen()
        print("Clock stopped. Goodbye!")


def main():
    clock = TerminalClock()
    
    # Check if user wants to toggle mode
    if len(sys.argv) > 1 and sys.argv[1] == 'digital':
        clock.is_analog = False
    
    clock.run()


if __name__ == "__main__":
    main()
