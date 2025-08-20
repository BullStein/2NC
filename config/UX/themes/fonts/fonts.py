def load_fonts(ctk):
    ctk.FontManager.load_font("config/UX/themes/fonts/Inter 18pt Light.ttf")
    ctk.FontManager.load_font("config/UX/themes/fonts/Inter 18pt Bold.ttf")
def fonts_variable():
    font_bold = "Inter 18pt Bold"
    light_font = "Inter 18pt Light"
    return font_bold,light_font