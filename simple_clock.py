import math
import tkinter as tk
from datetime import datetime


BG_COLOR = "#0b66ff"  # Blue background
HAND_COLOR = "#ffffff"  # White hands


class SimpleClock:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("Simple Clock")
        self.root.geometry("400x450")
        self.root.resizable(True, True)
        self.root.configure(bg=BG_COLOR)
        
        # Track display mode
        self.is_analog = True
        
        # Create toggle button
        self.toggle_btn = tk.Button(
            root,
            text="Switch to Digital",
            command=self.toggle_mode,
            bg="white",
            fg="black",
            font=("Arial", 12)
        )
        self.toggle_btn.pack(pady=10)
        
        # Main display frame
        self.display_frame = tk.Frame(root, bg=BG_COLOR)
        self.display_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Initialize display
        self.setup_analog()
        self.update_clock()

    def toggle_mode(self):
        self.is_analog = not self.is_analog
        
        # Clear current display
        for widget in self.display_frame.winfo_children():
            widget.destroy()
        
        if self.is_analog:
            self.toggle_btn.config(text="Switch to Digital")
            self.setup_analog()
        else:
            self.toggle_btn.config(text="Switch to Analog")
            self.setup_digital()

    def setup_analog(self):
        self.canvas = tk.Canvas(
            self.display_frame,
            bg=BG_COLOR,
            highlightthickness=0
        )
        self.canvas.pack(fill=tk.BOTH, expand=True)
        
        # Bind resize event
        self.canvas.bind('<Configure>', self.on_canvas_resize)

    def setup_digital(self):
        self.time_label = tk.Label(
            self.display_frame,
            text="",
            bg=BG_COLOR,
            fg=HAND_COLOR,
            font=("Arial", 48, "bold")
        )
        self.time_label.pack(expand=True)

    def on_canvas_resize(self, event):
        # Redraw analog clock when canvas is resized
        if self.is_analog:
            self.draw_analog_clock()

    def draw_analog_clock(self):
        if not hasattr(self, 'canvas'):
            return
            
        self.canvas.delete("all")
        
        # Get current canvas size
        canvas_width = self.canvas.winfo_width()
        canvas_height = self.canvas.winfo_height()
        
        if canvas_width <= 1 or canvas_height <= 1:
            return
        
        # Calculate center and radius based on current size
        self.center_x = canvas_width // 2
        self.center_y = canvas_height // 2
        self.radius = min(self.center_x, self.center_y) - 20
        
        if self.radius <= 0:
            return
        
        # Draw clock face
        self.canvas.create_oval(
            self.center_x - self.radius,
            self.center_y - self.radius,
            self.center_x + self.radius,
            self.center_y + self.radius,
            outline=HAND_COLOR,
            width=2
        )
        
        # Draw hour marks
        for h in range(12):
            angle = math.radians(h * 30)
            x_outer = self.center_x + (self.radius - 10) * math.sin(angle)
            y_outer = self.center_y - (self.radius - 10) * math.cos(angle)
            x_inner = self.center_x + (self.radius - 20) * math.sin(angle)
            y_inner = self.center_y - (self.radius - 20) * math.cos(angle)
            self.canvas.create_line(x_inner, y_inner, x_outer, y_outer, fill=HAND_COLOR, width=2)

    def draw_hands(self):
        if not self.is_analog or not hasattr(self, 'canvas'):
            return
            
        # Remove old hands
        self.canvas.delete("hands")
        
        now = datetime.now()
        h = now.hour % 12
        m = now.minute
        s = now.second + now.microsecond / 1_000_000

        # Calculate angles
        hour_angle = (h + m / 60 + s / 3600) * 30
        minute_angle = (m + s / 60) * 6
        second_angle = s * 6

        # Draw hands
        self.draw_hand(hour_angle, self.radius * 0.5, 4, "hands")
        self.draw_hand(minute_angle, self.radius * 0.7, 2, "hands") 
        self.draw_hand(second_angle, self.radius * 0.8, 1, "hands")

    def draw_hand(self, angle_degrees, length, width, tag):
        if not hasattr(self, 'center_x'):
            return
            
        rad = math.radians(angle_degrees)
        x = self.center_x + length * math.sin(rad)
        y = self.center_y - length * math.cos(rad)
        
        self.canvas.create_line(
            self.center_x, self.center_y, x, y,
            fill=HAND_COLOR, width=width, tags=tag, capstyle=tk.ROUND
        )

    def update_clock(self):
        if self.is_analog:
            self.draw_analog_clock()
            self.draw_hands()
        else:
            now = datetime.now()
            time_str = now.strftime("%H:%M:%S")
            if hasattr(self, 'time_label'):
                self.time_label.config(text=time_str)
        
        # Update every second
        self.root.after(1000, self.update_clock)


def main():
    root = tk.Tk()
    SimpleClock(root)
    root.mainloop()


if __name__ == "__main__":
    main()
