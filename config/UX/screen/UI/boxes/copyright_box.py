from config.UX.main import *
from config.UX.themes.theme_handler import *
import customtkinter as ctk

def copyright_box(main_box):
    copyright_box = ctk.CTkFrame(main_box, height=30, width=1300, bg_color=app_background,
                                 fg_color=background_colors[0], corner_radius=30)
    copyright_box.pack(pady=(15, 0))
    copyright_box.pack_propagate(False)

    copyright_label = ctk.CTkLabel(copyright_box,
                                   text="All the code and rights belong to the github author BullStein @2025",
                                   font=(font_light, 25))
    copyright_label.pack()