#!/usr/bin/env python3
"""
Interactive Terminal Clock for Chromebook
A simple clock that you can easily toggle between modes
"""

import time
import os
from datetime import datetime


class InteractiveClock:
    def __init__(self):
        self.is_analog = True

    def clear_screen(self):
        os.system('clear' if os.name == 'posix' else 'cls')

    def draw_simple_analog(self):
        now = datetime.now()
        hour = now.hour % 12
        minute = now.minute
        
        # Simple ASCII clock face
        print("        12")
        print("    9   ●   3")
        print("        6")
        print()
        
        # Show current time with hands position
        hour_pos = ["12", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11"][hour]
        minute_pos = f"{minute:02d}"
        
        print(f"Hour hand pointing to: {hour_pos}")
        print(f"Minute hand at: {minute_pos} minutes")
        print(f"Time: {now.strftime('%I:%M:%S %p')}")

    def draw_digital(self):
        now = datetime.now()
        
        # Big ASCII art time
        time_str = now.strftime("%H:%M:%S")
        print("┌─────────────────────────┐")
        print("│      DIGITAL CLOCK      │")
        print("├─────────────────────────┤")
        print(f"│         {time_str}         │")
        print("├─────────────────────────┤")
        print(f"│    {now.strftime('%A, %B %d')}     │")
        print(f"│         {now.strftime('%Y')}          │")
        print("└─────────────────────────┘")

    def show_menu(self):
        print("\n" + "="*40)
        print("  TERMINAL CLOCK CONTROLS")
        print("="*40)
        print("  [Enter] - Refresh")
        print("  [t] - Toggle Analog/Digital")
        print("  [q] - Quit")
        print("="*40)

    def run(self):
        self.clear_screen()
        print("🕐 Welcome to Terminal Clock!")
        print("This clock works perfectly on Chromebook!")
        
        while True:
            self.clear_screen()
            
            # Show current clock
            if self.is_analog:
                print("🕐 ANALOG CLOCK MODE")
                print("="*30)
                self.draw_simple_analog()
            else:
                print("🕐 DIGITAL CLOCK MODE")
                print("="*30)
                self.draw_digital()
            
            self.show_menu()
            
            # Get user input
            try:
                choice = input("\nYour choice: ").strip().lower()
                
                if choice == 't':
                    self.is_analog = not self.is_analog
                    print(f"\nSwitched to {'Analog' if self.is_analog else 'Digital'} mode!")
                    time.sleep(1)
                elif choice == 'q':
                    break
                elif choice == '':
                    # Just refresh (Enter key)
                    continue
                else:
                    print("Invalid choice. Try 't' to toggle or 'q' to quit.")
                    time.sleep(1)
                    
            except KeyboardInterrupt:
                break
        
        self.clear_screen()
        print("Thanks for using Terminal Clock! 🕐")
        print("Your clock is now ready for Chromebook! ✅")


def main():
    clock = InteractiveClock()
    clock.run()


if __name__ == "__main__":
    main()
