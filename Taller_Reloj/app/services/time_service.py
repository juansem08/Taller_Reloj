import time
import threading
from datetime import datetime, timedelta

class TimeService:
    """
    Service for handling time-dependent logic: Stopwatch, Timer, and main loop.
    """
    def __init__(self):
        # Stopwatch state
        self.stopwatch_running = False
        self.stopwatch_start_time = 0
        self.stopwatch_elapsed = 0
        
        # Timer state
        self.timer_running = False
        self.timer_seconds = 0
        self.timer_callback = None

    # --- Stopwatch Methods ---
    def start_stopwatch(self):
        if not self.stopwatch_running:
            self.stopwatch_start_time = time.time() - self.stopwatch_elapsed
            self.stopwatch_running = True

    def stop_stopwatch(self):
        if self.stopwatch_running:
            self.stopwatch_elapsed = time.time() - self.stopwatch_start_time
            self.stopwatch_running = False

    def reset_stopwatch(self):
        self.stopwatch_running = False
        self.stopwatch_elapsed = 0

    def get_stopwatch_time(self):
        if self.stopwatch_running:
            return time.time() - self.stopwatch_start_time
        return self.stopwatch_elapsed

    # --- Timer Methods ---
    def start_timer(self, seconds, callback):
        self.timer_seconds = seconds
        self.timer_running = True
        self.timer_callback = callback
        threading.Thread(target=self._timer_thread, daemon=True).start()

    def stop_timer(self):
        self.timer_running = False

    def _timer_thread(self):
        while self.timer_seconds > 0 and self.timer_running:
            time.sleep(1)
            self.timer_seconds -= 1
        
        if self.timer_running and self.timer_callback:
            self.timer_callback()
        self.timer_running = False

    def get_timer_seconds(self):
        return self.timer_seconds

    # --- Utility ---
    @staticmethod
    def format_time(seconds):
        """Format seconds into HH:MM:SS.ms"""
        m, s = divmod(seconds, 60)
        h, m = divmod(m, 60)
        ms = int((s - int(s)) * 100)
        return f"{int(h):02d}:{int(m):02d}:{int(s):02d}.{ms:02d}"
