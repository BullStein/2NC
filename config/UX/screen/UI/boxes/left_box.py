import customtkinter as ctk
from config.UX.themes.theme_handler import *

def left_box(app,parent_box):
    app.left_box_frame = ctk.CTkFrame(parent_box, fg_color=app_background)
    app.left_box_frame.grid(row=0, column=0)
    app.left_box_frame.grid_propagate(False)

    app.left_box_header = ctk.CTkFrame(app.left_box_frame, height=50, width=300, fg_color=background_colors[0], corner_radius=30)
    app.left_box_server_frame = ctk.CTkFrame(app.left_box_frame, height=600, width=300, fg_color=background_colors[0], corner_radius=40)

    app.left_box_header.pack()
    app.left_box_header.pack_propagate(False)

    app.left_box_server_frame.pack(pady=20)
    app.left_box_server_frame.pack_propagate(False)
    
    app.left_box_themes = ctk.CTkFrame(app.left_box_frame, height=50, width=300, fg_color=background_colors[0], corner_radius=30)
    app.left_box_themes.pack(fill="x")
    app.left_box_themes.pack_propagate(False)

    radio_var = ctk.StringVar(value=read_theme())

    app.theme_radio_dark = ctk.CTkRadioButton(app.left_box_themes, text="", variable=radio_var, value="dark", font=(font_light, 15), text_color=background_colors[-1], width=10)
    app.theme_radio_dark.grid(row=0, column=0, padx=0, pady=10)

    app.theme_radio_light = ctk.CTkRadioButton(app.left_box_themes, text="", variable=radio_var, value="light", font=(font_light, 15), text_color=background_colors[-1], width=10)
    app.theme_radio_light.grid(row=0, column=1, padx=0, pady=10)

    app.theme_radio_purple = ctk.CTkRadioButton(app.left_box_themes, text="", variable=radio_var, value="purple", font=(font_light, 15), text_color=background_colors[-1], width=10)
    app.theme_radio_purple.grid(row=0, column=2, padx=0, pady=10)

    app.left_box_themes.grid_columnconfigure((0,1,2), weight=1)
