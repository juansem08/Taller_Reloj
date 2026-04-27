import customtkinter as ctk
from app.ui.analog_clock import AnalogClock
from app.ui.digital_clock import DigitalClock
from app.ui.control_panel import ControlPanel
from app.ui.navigation_panel import NavigationPanel
from app.services.clock_manager import ClockManager
from app.services.time_service import TimeService
from app.services.alarm_service import AlarmService
from app.utils.config import Config
import pytz
from datetime import datetime

class AppWindow(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        self.title(Config.APP_TITLE)
        self.geometry(Config.WINDOW_SIZE)
        
        # Core Services
        self.manager = ClockManager()
        self.time_service = TimeService()
        self.alarm_service = AlarmService()
        self.current_theme = Config.THEMES[Config.DEFAULT_THEME]
        
        # Main Layout
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)
        
        # UI Components
        self.control_panel = ControlPanel(self, self.manager, self.change_theme, self.add_clock)
        self.control_panel.grid(row=0, column=0, sticky="nsw")
        
        self.right_container = ctk.CTkFrame(self, fg_color="transparent")
        self.right_container.grid(row=0, column=1, sticky="nsew", padx=40, pady=40)
        
        self.nav_panel = NavigationPanel(self.right_container, self.next_clock, self.prev_clock)
        self.nav_panel.pack(fill="x", pady=(0, 40))
        
        self.analog_clock = AnalogClock(self.right_container, color_theme=self.current_theme)
        self.analog_clock.pack(pady=20)
        
        self.digital_clock = DigitalClock(self.right_container)
        self.digital_clock.pack(pady=20)
        
        # Initialize
        self.update_ui_with_current_clock()
        self.run_clock_loop()

    def add_clock(self, city, timezone):
        self.manager.add_clock(city, timezone)
        self.control_panel.refresh_list()

    def next_clock(self):
        self.manager.next_clock()
        self.update_ui_with_current_clock()

    def prev_clock(self):
        self.manager.previous_clock()
        self.update_ui_with_current_clock()

    def update_ui_with_current_clock(self):
        clock_data = self.manager.get_current_clock()
        if clock_data:
            self.nav_panel.set_city(clock_data.city_name)

    def change_theme(self, theme_name):
        self.current_theme = Config.THEMES[theme_name]
        self.configure(fg_color=self.current_theme["bg"])
        self.control_panel.configure(fg_color=self.current_theme["secondary"])
        self.analog_clock.set_theme(self.current_theme)

    def run_clock_loop(self):
        clock_data = self.manager.get_current_clock()
        if clock_data:
            tz = pytz.timezone(clock_data.timezone_str)
            now = datetime.now(tz)
            
            self.analog_clock.update_clock(now)
            self.digital_clock.update_time(now)
        
        # Schedule next update
        self.after(1000, self.run_clock_loop)
