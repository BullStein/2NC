from config.UX.themes.colors import *
from config.UX.themes.fonts.fonts import *

app_background,background_colors,font_colors = handle_theme()
font_bold, font_light = fonts_variable()

def change_theme(app,theme_name):
    data = read_data()
    data["data"]["user"]["theme"] = theme_name
    modify_data()
    handle_theme()