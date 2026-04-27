from datetime import datetime
import threading
import time

class AlarmService:
    """
    Service to manage and trigger alarms.
    """
    def __init__(self):
        self.running = True
        self.alarms = [] # List of tuples: (time_str, callback)
        self.active_alarms = set()
        
        # Start a background thread to check alarms
        self.thread = threading.Thread(target=self._check_alarms_loop, daemon=True)
        self.thread.start()

    def add_alarm(self, time_str, callback):
        """
        Add an alarm.
        time_str format: 'HH:MM'
        """
        self.alarms.append((time_str, callback))

    def remove_alarm(self, time_str):
        self.alarms = [a for a in self.alarms if a[0] != time_str]
        if time_str in self.active_alarms:
            self.active_alarms.remove(time_str)

    def _check_alarms_loop(self):
        while self.running:
            now = datetime.now()
            current_time_str = now.strftime("%H:%M")
            
            for alarm_time, callback in self.alarms:
                if current_time_str == alarm_time:
                    if alarm_time not in self.active_alarms:
                        # Trigger the alarm
                        callback()
                        self.active_alarms.add(alarm_time)
                else:
                    # Reset the alarm state if the time has passed
                    if alarm_time in self.active_alarms:
                        self.active_alarms.remove(alarm_time)
            
            time.sleep(1) # Check every second

    def stop(self):
        self.running = False
