import customtkinter as ctk

class DigitalClock(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, fg_color="transparent", **kwargs)
        
        self.time_label = ctk.CTkLabel(self, text="00:00:00", font=("Orbitron", 64, "bold"))
        self.time_label.pack(pady=10)
        
        self.date_label = ctk.CTkLabel(self, text="Lunes, 01 de Enero", font=("Inter", 20))
        self.date_label.pack()

    def update_time(self, time_obj):
        self.time_label.configure(text=time_obj.strftime("%H:%M:%S"))
        
        # Spanish localization for date
        days = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
        months = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", 
                  "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
        
        day_name = days[time_obj.weekday()]
        month_name = months[time_obj.month - 1]
        
        date_str = f"{day_name}, {time_obj.day} de {month_name} {time_obj.year}"
        self.date_label.configure(text=date_str)
