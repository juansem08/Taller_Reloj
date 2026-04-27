import customtkinter as ctk
from app.utils.config import Config

class ControlPanel(ctk.CTkFrame):
    def __init__(self, master, manager, theme_callback, add_city_callback, **kwargs):
        super().__init__(master, width=300, corner_radius=0, **kwargs)
        self.manager = manager
        self.theme_callback = theme_callback
        self.add_city_callback = add_city_callback
        
        self.setup_ui()

    def setup_ui(self):
        # Title
        title = ctk.CTkLabel(self, text="CONTROLES", font=("Inter", 20, "bold"))
        title.pack(pady=20, padx=20, anchor="w")

        # Time Adjustment Section
        adj_label = ctk.CTkLabel(self, text="AJUSTE MANUAL", font=("Inter", 12, "bold"), text_color="gray")
        adj_label.pack(pady=(10, 5), padx=20, anchor="w")
        
        self.hour_slider = ctk.CTkSlider(self, from_=0, to=23, number_of_steps=24)
        self.hour_slider.pack(pady=5, padx=20, fill="x")
        
        # World Clock Section
        world_label = ctk.CTkLabel(self, text="AÑADIR RELOJ MUNDIAL", font=("Inter", 12, "bold"), text_color="gray")
        world_label.pack(pady=(20, 5), padx=20, anchor="w")
        
        self.city_options = [c[0] for c in Config.WORLD_CITIES]
        self.city_combo = ctk.CTkComboBox(self, values=self.city_options)
        self.city_combo.pack(pady=5, padx=20, fill="x")
        
        add_btn = ctk.CTkButton(self, text="Añadir Reloj", command=self._on_add_city)
        add_btn.pack(pady=10, padx=20, fill="x")

        # Theme Section
        theme_label = ctk.CTkLabel(self, text="TEMA DE COLOR", font=("Inter", 12, "bold"), text_color="gray")
        theme_label.pack(pady=(20, 5), padx=20, anchor="w")
        
        self.theme_combo = ctk.CTkComboBox(self, values=list(Config.THEMES.keys()), command=self.theme_callback)
        self.theme_combo.set(Config.DEFAULT_THEME)
        self.theme_combo.pack(pady=5, padx=20, fill="x")

        # List of Clocks
        list_label = ctk.CTkLabel(self, text="RELOJES GESTIONADOS (LCDE)", font=("Inter", 12, "bold"), text_color="gray")
        list_label.pack(pady=(20, 5), padx=20, anchor="w")
        
        self.clock_list_box = ctk.CTkTextbox(self, height=150, font=("Inter", 12))
        self.clock_list_box.pack(pady=5, padx=20, fill="x")
        self.refresh_list()

    def _on_add_city(self):
        city_name = self.city_combo.get()
        # Find timezone
        timezone = next(c[1] for c in Config.WORLD_CITIES if c[0] == city_name)
        self.add_city_callback(city_name, timezone)
        self.refresh_list()

    def refresh_list(self):
        self.clock_list_box.configure(state="normal")
        self.clock_list_box.delete("1.0", "end")
        clocks = self.manager.get_all_clocks()
        for i, city in enumerate(clocks):
            self.clock_list_box.insert("end", f"{i+1}. {city}\n")
        self.clock_list_box.configure(state="disabled")
