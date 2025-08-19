def load_fonts(ctk):
    ctk.FontManager.load_font("Inter 18pt Light.ttf")
    ctk.FontManager.load_font("Inter 18pt.ttf")
    
def fonts_variable():
    font = "Inter 18pt"
    light_font = "Inter 18pt Light"
    return font,light_font