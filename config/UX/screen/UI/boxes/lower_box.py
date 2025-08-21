from config.UX.main import *
from config.UX.themes.theme_handler import *
import customtkinter as ctk

def lower_box(main_box):

    lower_box = ctk.CTkFrame(main_box, height=540, width=1300, bg_color=app_background,
                            fg_color=background_colors[0], corner_radius=30)
    lower_box.pack(pady=(15, 0))
    lower_box.propagate(False)