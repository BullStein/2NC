from config.UX.themes.colors import *
from config.UX.themes.fonts.fonts import *
import time

app_background, background_colors, font_colors = handle_theme()
font_bold, font_light = fonts_variable()
light_radio,dark_radio,purple_radio,red_radio,mint_radio = radio_colors()

def get_colors():
    global app_background, background_colors, font_colors, font_bold, font_light
    app_background, background_colors, font_colors = handle_theme()
    font_bold, font_light = fonts_variable()
    return app_background, background_colors, font_colors, font_bold, font_light

def change_theme(app, theme):
    data = read_data()
    data["data"]["user"]["theme"] = theme
    modify_data(data)
    app_background, background_colors, font_colors, font_bold, font_light = get_colors()
    time.sleep(0.1)
    
    app.configure(fg_color=app_background)
    
    update_container_colors(app, background_colors, font_colors, font_bold, font_light)
def update_logo_box_container_colors(app, background_colors):
    if hasattr(app,'logo'):
        app.logo.configure(fg_color=background_colors[0],bg_color=app_background)
def update_left_box_container_colors(app, background_colors, font_colors, font_bold, font_light):
    if hasattr(app, 'left_box_frame'):
        app.left_box_frame.configure(fg_color=app_background,bg_color=app_background)

    if hasattr(app, 'left_box_header'):
        app.left_box_header.configure(fg_color=background_colors[0],bg_color=app_background)
    
    if hasattr(app, 'left_box_server_frame'):
        app.left_box_server_frame.configure(fg_color=background_colors[0],bg_color=app_background)
    
    if hasattr(app, 'user_box'):
        app.user_box.configure(fg_color=background_colors[1])
    
    if hasattr(app, 'user_box_label'):
        app.user_box_label.configure(text_color=background_colors[-1])
    
    if hasattr(app, 'user_box_entry'):
        app.user_box_entry.configure(
            fg_color=background_colors[2],
            border_color=background_colors[1],
            text_color=background_colors[-1]
        )
    
    if hasattr(app, 'left_box_themes'):
        app.left_box_themes.configure(fg_color=background_colors[0],bg_color=app_background)
    
    if hasattr(app, 'theme_radio_dark'):
        app.theme_radio_dark.configure(text_color=background_colors[-1])
    if hasattr(app, 'theme_radio_light'):
        app.theme_radio_light.configure(text_color=background_colors[-1])
    if hasattr(app, 'theme_radio_purple'):
        app.theme_radio_purple.configure(text_color=background_colors[-1])

def update_right_box_container_colors(app, background_colors, font_colors, font_bold, font_light):
    if hasattr(app, 'right_box_frame'):
        app.right_box_frame.configure(bg_color=app_background,fg_color=background_colors[0])


def update_container_colors(app, background_colors, font_colors, font_bold, font_light):
    if hasattr(app, "main_box"):
        app.main_box.configure(bg_color=app_background,fg_color=app_background)

    update_left_box_container_colors(app, background_colors, font_colors, font_bold, font_light)
    update_right_box_container_colors(app, background_colors, font_colors, font_bold, font_light)
    update_logo_box_container_colors(app,background_colors)
