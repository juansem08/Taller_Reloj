import customtkinter as ctk
import math
from datetime import datetime

class AnalogClock(ctk.CTkCanvas):
    """
    A custom analog clock widget drawn on a Canvas.
    """
    def __init__(self, master, size=300, color_theme=None, **kwargs):
        super().__init__(master, width=size, height=size, highlightthickness=0, **kwargs)
        self.size = size
        self.center = size / 2
        self.radius = (size / 2) * 0.9
        self.theme = color_theme or {"accent": "#38bdf8", "text": "#f8fafc", "secondary": "#1e293b", "bg": "#0f172a"}
        self.configure(bg=self.theme["bg"])
        
        self.draw_face()

    def set_theme(self, theme):
        self.theme = theme
        self.configure(bg=self.theme["bg"])
        self.update_clock(datetime.now())

    def draw_face(self):
        self.delete("all")
        # Draw background circle
        self.create_oval(self.center - self.radius, self.center - self.radius,
                         self.center + self.radius, self.center + self.radius,
                         fill=self.theme["secondary"], outline=self.theme["accent"], width=2)
        
        # Draw hour marks
        for i in range(12):
            angle = math.radians(i * 30)
            x1 = self.center + (self.radius * 0.85) * math.sin(angle)
            y1 = self.center - (self.radius * 0.85) * math.cos(angle)
            x2 = self.center + self.radius * math.sin(angle)
            y2 = self.center - self.radius * math.cos(angle)
            self.create_line(x1, y1, x2, y2, fill=self.theme["accent"], width=3)

    def update_clock(self, time_obj):
        self.draw_face()
        
        # Get components
        hours = time_obj.hour % 12
        minutes = time_obj.minute
        seconds = time_obj.second
        
        # Angles
        h_angle = math.radians((hours * 30) + (minutes / 2))
        m_angle = math.radians(minutes * 6)
        s_angle = math.radians(seconds * 6)
        
        # Draw Hands
        self._draw_hand(h_angle, self.radius * 0.5, 6, self.theme["text"])   # Hour
        self._draw_hand(m_angle, self.radius * 0.8, 4, self.theme["text"])   # Minute
        self._draw_hand(s_angle, self.radius * 0.9, 2, self.theme["accent"]) # Second
        
        # Center dot
        self.create_oval(self.center - 5, self.center - 5, self.center + 5, self.center + 5,
                         fill=self.theme["accent"])

    def _draw_hand(self, angle, length, width, color):
        x = self.center + length * math.sin(angle)
        y = self.center - length * math.cos(angle)
        self.create_line(self.center, self.center, x, y, fill=color, width=width, capstyle="round")
