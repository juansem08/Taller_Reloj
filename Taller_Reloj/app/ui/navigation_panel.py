import customtkinter as ctk

class NavigationPanel(ctk.CTkFrame):
    def __init__(self, master, next_callback, prev_callback, **kwargs):
        super().__init__(master, fg_color="transparent", **kwargs)
        
        self.prev_btn = ctk.CTkButton(self, text="ANTERIOR", width=80, command=prev_callback, 
                                      font=("Inter", 14, "bold"))
        self.prev_btn.pack(side="left", padx=20)
        
        self.city_label = ctk.CTkLabel(self, text="CARGANDO...", font=("Inter", 28, "bold"))
        self.city_label.pack(side="left", expand=True)
        
        self.next_btn = ctk.CTkButton(self, text="SIGUIENTE", width=80, command=next_callback,
                                      font=("Inter", 14, "bold"))
        self.next_btn.pack(side="left", padx=20)

    def set_city(self, name):
        self.city_label.configure(text=name.upper())
