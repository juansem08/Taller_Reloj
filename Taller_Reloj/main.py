import customtkinter as ctk
from app.ui.app_window import AppWindow

def main():
    # Set appearance mode
    ctk.set_appearance_mode("Dark")
    
    # Create and run application
    app = AppWindow()
    app.mainloop()

if __name__ == "__main__":
    main()
