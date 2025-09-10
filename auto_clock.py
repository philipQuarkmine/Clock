#!/usr/bin/env python3
"""
Auto-updating Terminal Clock
Refreshes automatically, press any key to toggle or 'q' to quit
"""

import time
import os
import sys
import threading
from datetime import datetime


def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')


def display_clock(is_analog=True):
    clear_screen()
    now = datetime.now()
    
    if is_analog:
        print("🕐 ANALOG CLOCK - Press 't' for digital, 'q' to quit")
        print("="*50)
        
        # Simple analog representation
        hour = now.hour % 12
        minute = now.minute
        
        clock_face = [
            "        12        ",
            "    11      1     ",
            "  10          2   ",
            "9       ●       3 ",
            "  8           4   ",
            "    7       5     ",
            "        6         "
        ]
        
        for line in clock_face:
            print("    " + line)
        
        print(f"\n    Hour hand → {hour if hour != 0 else 12}")
        print(f"    Minute hand → {minute:02d}")
        print(f"    Current time: {now.strftime('%I:%M:%S %p')}")
        
    else:
        print("🕐 DIGITAL CLOCK - Press 't' for analog, 'q' to quit")
        print("="*50)
        
        # Digital display
        print()
        print("    ┌─────────────────────┐")
        print("    │                     │")
        print(f"    │    {now.strftime('%H:%M:%S')}          │")
        print("    │                     │")
        print(f"    │  {now.strftime('%A')}        │")
        print(f"    │  {now.strftime('%B %d, %Y')}     │")
        print("    │                     │")
        print("    └─────────────────────┘")
    
    print("\n" + "="*50)
    print("Commands: 't' = toggle mode, 'q' = quit, Enter = refresh")


def main():
    is_analog = True
    running = True
    
    def get_input():
        nonlocal is_analog, running
        while running:
            try:
                choice = input().strip().lower()
                if choice == 't':
                    is_analog = not is_analog
                elif choice == 'q':
                    running = False
                    break
            except:
                break
    
    # Start input thread
    input_thread = threading.Thread(target=get_input, daemon=True)
    input_thread.start()
    
    print("Starting Terminal Clock...")
    time.sleep(1)
    
    try:
        while running:
            display_clock(is_analog)
            
            # Update every 2 seconds
            for _ in range(20):  # Check 10 times per second for responsiveness
                if not running:
                    break
                time.sleep(0.1)
                
    except KeyboardInterrupt:
        running = False
    
    clear_screen()
    print("Terminal Clock stopped. Goodbye! 👋")


if __name__ == "__main__":
    main()
