class Config:
    APP_TITLE = "AstraClock - Sistema Avanzado LCDE"
    WINDOW_SIZE = "1100x700"
    
    # Themes
    THEMES = {
        "Océano Profundo": {
            "bg": "#0f172a",
            "accent": "#38bdf8",
            "text": "#f8fafc",
            "secondary": "#1e293b"
        },
        "Cyberpunk": {
            "bg": "#120422",
            "accent": "#ff00ff",
            "text": "#00ffff",
            "secondary": "#2d0a4e"
        },
        "Bosque": {
            "bg": "#052e16",
            "accent": "#4ade80",
            "text": "#f0fdf4",
            "secondary": "#064e3b"
        },
        "Atardecer": {
            "bg": "#450a0a",
            "accent": "#f97316",
            "text": "#fff7ed",
            "secondary": "#7c2d12"
        }
    }
    
    DEFAULT_THEME = "Océano Profundo"
    
    # Clock Sizes
    ANALOG_SIZE = 300
    
    # World Cities for easy selection
    WORLD_CITIES = [
        ("Bogotá", "America/Bogota"),
        ("Nueva York", "America/New_York"),
        ("Londres", "Europe/London"),
        ("Tokio", "Asia/Tokyo"),
        ("París", "Europe/Paris"),
        ("Sídney", "Australia/Sydney"),
        ("Dubái", "Asia/Dubai")
    ]
