import math
import tkinter as tk
from datetime import datetime


WINDOW_SIZE = 300
CENTER = WINDOW_SIZE // 2
RADIUS = CENTER - 15
BG_COLOR = "#0b66ff"  # Blue background
HAND_COLOR = "#ffffff"  # White hands


class AnalogClock:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("Blue Analog Clock")
        self.root.geometry(f"{WINDOW_SIZE}x{WINDOW_SIZE}")
        self.root.resizable(False, False)
        self.root.configure(bg=BG_COLOR)

        self.canvas = tk.Canvas(
            root,
            width=WINDOW_SIZE,
            height=WINDOW_SIZE,
            bg=BG_COLOR,
            highlightthickness=0,
        )
        self.canvas.pack(fill=tk.BOTH, expand=True)

        # Draw clock face (outer ring)
        self.canvas.create_oval(
            CENTER - RADIUS,
            CENTER - RADIUS,
            CENTER + RADIUS,
            CENTER + RADIUS,
            outline=HAND_COLOR,
            width=2,
        )

        # Hour marks (simple dots)
        for h in range(12):
            angle = math.radians(h * 30)
            x_outer = CENTER + (RADIUS - 6) * math.sin(angle)
            y_outer = CENTER - (RADIUS - 6) * math.cos(angle)
            x_inner = CENTER + (RADIUS - 16) * math.sin(angle)
            y_inner = CENTER - (RADIUS - 16) * math.cos(angle)
            self.canvas.create_line(x_inner, y_inner, x_outer, y_outer, fill=HAND_COLOR, width=2)

        # Initialize hands; keep references to update efficiently
        self.hour_hand = self.canvas.create_line(CENTER, CENTER, CENTER, CENTER - RADIUS * 0.5, fill=HAND_COLOR, width=5, capstyle=tk.ROUND)
        self.minute_hand = self.canvas.create_line(CENTER, CENTER, CENTER, CENTER - RADIUS * 0.75, fill=HAND_COLOR, width=3, capstyle=tk.ROUND)
        self.second_hand = self.canvas.create_line(CENTER, CENTER, CENTER, CENTER - RADIUS * 0.85, fill=HAND_COLOR, width=1, capstyle=tk.ROUND)

        self.update_clock()

    def _hand_endpoint(self, length: float, angle_degrees: float):
        # Angle 0 is 12 o'clock; canvas y increases downward
        rad = math.radians(angle_degrees)
        x = CENTER + length * math.sin(rad)
        y = CENTER - length * math.cos(rad)
        return x, y

    def update_clock(self):
        now = datetime.now()
        h = now.hour % 12
        m = now.minute
        s = now.second + now.microsecond / 1_000_000

        # Calculate angles
        hour_angle = (h + m / 60 + s / 3600) * 30  # 360/12
        minute_angle = (m + s / 60) * 6  # 360/60
        second_angle = s * 6

        # Update hand positions
        hx, hy = self._hand_endpoint(RADIUS * 0.5, hour_angle)
        mx, my = self._hand_endpoint(RADIUS * 0.75, minute_angle)
        sx, sy = self._hand_endpoint(RADIUS * 0.85, second_angle)

        self.canvas.coords(self.hour_hand, CENTER, CENTER, hx, hy)
        self.canvas.coords(self.minute_hand, CENTER, CENTER, mx, my)
        self.canvas.coords(self.second_hand, CENTER, CENTER, sx, sy)

        # Smooth updates; refresh ~30 fps
        self.root.after(33, self.update_clock)


def main():
    root = tk.Tk()
    AnalogClock(root)
    root.mainloop()


if __name__ == "__main__":
    main()

