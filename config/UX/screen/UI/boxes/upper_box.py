from config.UX.main import *
from config.UX.themes.theme_handler import *
from config.UX.screen.widgets import *
import customtkinter as ctk

def upper_box(app, main_box):
    upper_box = ctk.CTkFrame(
        main_box, height=220, width=1300, 
        bg_color=app_background,
        fg_color=background_colors[0], 
        corner_radius=30
    )
    upper_box.pack()
    upper_box.pack_propagate(False)
    upper_box.grid_propagate(False)

    theme_box = ctk.CTkFrame(
        upper_box, height=200, width=300,
        bg_color=background_colors[0],
        fg_color=background_colors[1],
        corner_radius=30
    )

    user_box = ctk.CTkFrame(
        upper_box, height=130, width=300,
        bg_color=background_colors[0],
        fg_color=background_colors[1],
        corner_radius=30
    )

    app.padx_value = xcentralize(upper_box, user_box, theme_box)

    theme_box.grid(row=0, column=1, pady=ycentralize(upper_box, theme_box), padx=(app.padx_value))
    theme_box.pack_propagate(False)

    user_box.grid(row=0, column=0, pady=ycentralize(upper_box, user_box), padx=(app.padx_value))
    user_box.pack_propagate(False)

    user_label = ctk.CTkLabel(
        user_box, text="USERNAME", 
        font=(font_bold, 40), 
        text_color=background_colors[-1]
    )
    user_label.pack()

    app.user_entry = ctk.CTkEntry(
        user_box, width=250, height=50,
        bg_color=background_colors[1],
        fg_color=background_colors[2],
        placeholder_text="insert username",
        border_width=0, corner_radius=20
    )
    app.user_entry.pack()
    app.user_entry.pack_propagate(False)

    theme_label = ctk.CTkLabel(
        theme_box, text="THEMES",
        font=(font_bold, 25),
        text_color=background_colors[-1]
    )
    theme_label.pack(pady=(0,0), padx=0)
    
    radio_var = ctk.StringVar(value=read_theme())

    def theme_modify(app=app):
        change_theme(app, radio_var.get())

    theme_radios = ctk.CTkScrollableFrame(theme_box, fg_color=background_colors[2], width=180)
    theme_radios.pack()
    theme_radios.configure(height=50)   # agora o height funciona


    theme_radio_dark = ctk.CTkRadioButton(theme_radios, text="DARK", variable=radio_var, value="dark", command=theme_modify
    ,font=(font_light,15),text_color=background_colors[-1])
    theme_radio_dark.pack(pady=(0,5))

    theme_radio_light = ctk.CTkRadioButton(theme_radios, text="LIGHT", variable=radio_var, value="light", command=theme_modify
    ,font=(font_light,15),text_color=background_colors[-1])
    theme_radio_light.pack(pady=(0,5))

    theme_radio_purple = ctk.CTkRadioButton(theme_radios, text="PURPLE", variable=radio_var, value="purple", command=theme_modify
    ,font=(font_light,15),text_color=background_colors[-1])
    theme_radio_purple.pack(pady=(0,5))
