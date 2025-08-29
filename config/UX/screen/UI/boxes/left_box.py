import customtkinter as ctk
from config.UX.themes.theme_handler import *
from config.UX.screen.widgets import * 
from config.UX.themes.theme_handler import update_container_colors

def left_box(app,parent_box):
    boxes = [app.server_creation_box, app.user_box]

    app.left_box_frame = ctk.CTkFrame(parent_box, fg_color=app_background)
    app.left_box_frame.grid(row=0, column=0)
    app.left_box_frame.grid_propagate(False)

    app.left_box_header = ctk.CTkFrame(app.left_box_frame, height=50, width=300, fg_color=background_colors[0], corner_radius=30)
    app.left_box_server_frame = ctk.CTkFrame(app.left_box_frame, height=600, width=300, fg_color=background_colors[0], corner_radius=40)
    
    app.user_box = ctk.CTkFrame(
        app.left_box_server_frame,height=150,width=280,fg_color=background_colors[1],corner_radius=30
        )
    app.user_box.pack(
        pady=(centralize(app.left_box_server_frame,boxes,'y'))
        )
    app.user_box.pack_propagate(False)
    
    app.user_box_label = ctk.CTkLabel(app.user_box,text="NICKNAME",font=(font_bold,40),text_color=background_colors[-1])
    app.user_box_label.pack()

    app.user_box_entry = ctk.CTkEntry(
        app.user_box,placeholder_text="insert a nick",fg_color=background_colors[2],border_color=background_colors[1],
        font=(font_light,20), corner_radius=20,height=40,width=230,text_color=background_colors[-1],placeholder_text_color=font_colors[-1]
    )
    app.user_box_entry.pack()
    #?
    app.server_creation_box = ctk.CTkFrame(
        app.left_box_server_frame,height=150,width=280,fg_color=background_colors[1],corner_radius=30
        )
    app.server_creation_box.pack(
        pady=(centralize(app.left_box_server_frame,boxes,'y'))
        )
    app.user_box.pack_propagate(False)
    
    app.server_creation_box_label = ctk.CTkLabel(app.user_box,text="NICKNAME",font=(font_bold,40),text_color=background_colors[-1])
    app.server_creation_box_label.pack()

    app.user_box_entry = ctk.CTkEntry(
        app.user_box,placeholder_text="insert a nick",fg_color=background_colors[2],border_color=background_colors[1],
        font=(font_light,20), corner_radius=20,height=40,width=230,text_color=background_colors[-1],placeholder_text_color=font_colors[-1]
    )
    app.user_box_entry.pack()
    #? packs containers

    app.left_box_header.pack()
    app.left_box_header.pack_propagate(False)

    app.left_box_server_frame.pack(pady=20)
    app.left_box_server_frame.pack_propagate(False)

    app.server_creation_box.pack()
    app.server_creation_box.pack_propagate(False)
    #?
    app.left_box_themes = ctk.CTkFrame(app.left_box_frame, height=50, width=300, fg_color=background_colors[0], corner_radius=30)
    app.left_box_themes.pack(fill="x")
    app.left_box_themes.pack_propagate(False)

    radio_var = ctk.StringVar(value=read_theme())

    def on_theme_change():
        change_theme(app, radio_var.get())
    
    app.theme_radio_light = ctk.CTkRadioButton(
            app.left_box_themes, text="", variable=radio_var, value="light",
            font=(font_light, 15), text_color=background_colors[-1], width=10,
            command=on_theme_change, border_color=light_radio[0], fg_color=light_radio[1],
            radiobutton_height=30, radiobutton_width=30,border_width_unchecked=5,border_width_checked=7,
            hover_color="#C6C8C2"
        )
    app.theme_radio_light.grid(row=0, column=1, padx=0, pady=13)

    app.theme_radio_dark = ctk.CTkRadioButton(
            app.left_box_themes, text="", variable=radio_var, value="dark",
            font=(font_light, 15), text_color=background_colors[-1], width=10,
            command=on_theme_change, border_color=dark_radio[0], fg_color=dark_radio[0],
            radiobutton_height=30, radiobutton_width=30,border_width_unchecked=5,border_width_checked=7,
            hover_color="#4F5453"
        )
    app.theme_radio_dark.grid(row=0, column=2, padx=0, pady=13)

    app.theme_radio_red = ctk.CTkRadioButton(
            app.left_box_themes, text="", variable=radio_var, value="red",
            font=(font_light, 15), text_color=background_colors[-1], width=10,
            command=on_theme_change, border_color=red_radio[1], fg_color=red_radio[1],
            radiobutton_height=30, radiobutton_width=30,border_width_unchecked=5,border_width_checked=7,
            hover_color="#990B1E"
        )
    app.theme_radio_red.grid(row=0, column=3, padx=0, pady=13)

    app.theme_radio_purple = ctk.CTkRadioButton(
            app.left_box_themes, text="", variable=radio_var, value="purple",
            font=(font_light, 15), text_color=background_colors[-1], width=10,
            command=on_theme_change, border_color=purple_radio[0], fg_color=purple_radio[1],
            radiobutton_height=30, radiobutton_width=30,border_width_unchecked=5,border_width_checked=7,
            hover_color="#70718F"
        )
    app.theme_radio_purple.grid(row=0, column=4, padx=0, pady=13)

    app.theme_radio_mint = ctk.CTkRadioButton(
            app.left_box_themes, text="", variable=radio_var, value="mint",
            font=(font_light, 15), text_color=background_colors[-1], width=10,
            command=on_theme_change, border_color=mint_radio[0], fg_color=mint_radio[1],
            radiobutton_height=30, radiobutton_width=30,border_width_unchecked=5,border_width_checked=7,
            hover_color="#70718F"
        )
    app.theme_radio_mint.grid(row=0, column=5, padx=0, pady=13)

    app.left_box_themes.grid_columnconfigure((1,2,3,4,5), weight=1)
    update_container_colors(app, background_colors, font_colors, font_bold, font_light)
