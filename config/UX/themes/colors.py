import customtkinter as ctk
from config.data.main import *
#not a big fan of colors when the subject is minimalist chats
#? background colors

milkish_white = "#E8EBE4"
milkish_white_relative = "#B7BBB3"
grayish_blue = "#D2D5DD"
whiteish_blue = "#b8bacf"
light_purple = "#999ac6"
light_blackish = "#333630"

#? text colors
white = light_blackish
black = milkish_white
purple = light_purple

#? button colors
accept_button = "#36376D"


#? entry camps colors
ligh_blackish_entry = "#222420"
light_purple_entry = "#7B7C9F"

#? about list: 1-background 2-container color 3- container darker color 4-container shadow 5-container shadow relative  
#? 6-placholder button 7-deny button 8-agree button
def handle_theme():
    data = read_data()
    path = data["data"]["user"]["theme"]
    if path == "light":
        theme = light_theme()
    elif path == "purple":
        pass
        # theme = purple_theme()
    return theme
def light_theme():
    #?                    background     
    bakground_colors = [milkish_white,milkish_white_relative,light_blackish,ligh_blackish_entry,accept_button]
    font_colors = [white,black,purple]
    return bakground_colors,font_colors
