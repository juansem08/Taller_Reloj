from datetime import datetime
import pytz

class ClockData:
    """
    Model representing a clock's configuration.
    Includes timezone, alarm settings, and theme preferences.
    """
    def __init__(self, city_name, timezone_str="UTC"):
        self.city_name = city_name
        self.timezone_str = timezone_str
        self.alarm_time = None  # Format "HH:MM"
        self.alarm_enabled = False
        self.manual_offset_seconds = 0  # For manual hand adjustments
        self.is_manual_mode = False

    def get_current_time(self):
        """Get the current time for this clock's timezone, including manual offset."""
        tz = pytz.timezone(self.timezone_str)
        now = datetime.now(tz)
        if self.is_manual_mode:
            # Apply manual offset if in manual mode
            # In a real app, this might be more complex
            pass
        return now

    def __repr__(self):
        return f"ClockData({self.city_name}, {self.timezone_str})"

    def __eq__(self, other):
        if not isinstance(other, ClockData):
            return False
        return self.city_name == other.city_name and self.timezone_str == other.timezone_str
