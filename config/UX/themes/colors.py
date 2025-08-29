import customtkinter as ctk
from config.data.main import *
#not a big fan of colors when the subject is minimalist chats
#? background colors light

milkish_white = "#E8EBE4"
milkish_white_relative = "#B7BBB3"
grayish_blue = "#D2D5DD"
whiteish_blue = "#b8bacf"
light_blackish = "#333630"
shady_gray = "#848781"


#? background colors purple
light_purple = "#999ac6"
light_purple_relative = "#787899"
purple_ocean = "#4A4A5D"


#? text colors
black = light_blackish
white = milkish_white
purple = light_purple

#? bakcground colors red
bright_red = "#BB0A21"
wine_red = "#9B0E21"
weak_blue = "#4B88A2"
cherry_red = "#7B0F1E"

#? background colors pink
sakura_pink = "#EFC7E5"
pink = "#EEB1D5"
lolipop_pink = "#CD9FBA"
weak_pink = "#A87F98"
black_pink = "#4C3B4D" # BLACK PINK!?

#? background colors dark
gray = "#6A706E"
rock_gray = "#575955"
light_blackish = light_blackish

#? background colors mint
bush_green = "#C9EDDC"
light_green = "#839E91"
viridian = "#4C6157"
grayish_turquise = "#27332E"

#? placeholder
place_holder_entry_white = "#E8EBE4"

#? font colors
font_colors_list = [white,black,purple,place_holder_entry_white]

#? button colors
accept_button_purple = "#3E2B5B"
accept_button_dark = "#E8EBE4"
accept_button_light = "#5B5D58"
accept_button_red = "#601429"
accept_button_mint = "#1A1F16"

#? entry camps colors
ligh_blackish_entry = "#222420"
light_purple_entry = "#7B7C9F"
blackish_mint_entry = "#27332E"
purple_entry = "#232630"
dexter_blood_entry = "#5B0D18"
light_white_entry = "#5D5F5B"


#? about list: 0-background 0-container color 1- container darker color 2-container shadow 3-container shadow relative  
#? 4-placeholder button 5-deny button 6-agree button
def read_theme():
    data = read_data()
    theme_name = data["data"]["user"]["theme"]
    return theme_name
def handle_theme():
    data = read_data()
    theme_name = data["data"]["user"]["theme"]
    
    theme_handlers = {
        "light": light_theme,
        "purple": purple_theme,
        "red" : red_theme,
        "dark" : dark_theme,
        "mint" : mint_theme
    }
    
    if theme_name in theme_handlers:
        return theme_handlers[theme_name]()
    else:
        return light_theme()
def light_theme():
    font_colors = font_colors_list
    app_background = milkish_white
    background_colors = [
        milkish_white_relative,
        shady_gray,
        light_white_entry,
        accept_button_light,
        white
    ]
    return app_background, background_colors, font_colors
def purple_theme():
    font_colors = font_colors_list
    app_background = light_purple
    background_colors = [
        light_purple_relative,
        purple_ocean,
        purple_entry,
        accept_button_purple,
        light_purple,
        white 
    ]
    return app_background, background_colors, font_colors
def red_theme():
    font_colors = font_colors_list
    app_background = bright_red
    background_colors = [
        wine_red,
        cherry_red,
        dexter_blood_entry,
        accept_button_red,
        white
    ]
    return app_background, background_colors, font_colors
def dark_theme():
    font_colors = font_colors_list
    app_background = gray
    background_colors = [
        rock_gray,
        light_blackish,
        ligh_blackish_entry,
        accept_button_dark,
        white
    ]
    return app_background, background_colors, font_colors
def mint_theme():
    font_colors = font_colors_list
    app_background = bush_green
    background_colors = [
        light_green,
        viridian,
        grayish_turquise,
        accept_button_mint,
        blackish_mint_entry,
        white
    ]
    return app_background, background_colors, font_colors

def radio_colors():
    first_radio = [milkish_white_relative, milkish_white]
    second_radio = [gray, rock_gray]
    third_radio = [light_purple_relative, light_purple]
    fourth_radio = [wine_red, bright_red]
    fifth_radio = [light_green, bush_green]
    radios = [first_radio, second_radio, third_radio, fourth_radio, fifth_radio]
    for radio in radios:
        yield radio