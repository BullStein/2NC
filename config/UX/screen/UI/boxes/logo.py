import customtkinter as ctk
from config.UX.themes.theme_handler import *
from config.UX.screen.widgets import * 
from config.UX.themes.theme_handler import update_container_colors


def logo_box(app,parent_box):
    app.logo = ctk.CTkLabel(app, text="2NC", font=(font_bold,20), 
                             text_color=background_colors[-1],fg_color=background_colors[0],bg_color=app_background,
                             corner_radius=10,height=30,width=50)
    app.logo.place(relx=1.0, rely=1.0, anchor="se", x=-20, y=-20)
    