import os
from PIL import Image,ImageTk,ImageDraw

def image_path(app):
    image_path = os.path.join(os.path.dirname(__file__), "images", app.image_theme_path)
    return image_path
def load_image():
    img = Image.open(image_path)
    img = img.resize((500, 500), Image.Resampling.LANCZOS)
    return img
def create_image():
    mask = Image.new('L', load_image().size, 0)
    draw = ImageDraw.Draw(mask)
    draw.rounded_rectangle((0, 0, load_image().size[0], load_image().size[1]), radius=100, fill=255)
    load_image().putalpha(mask)
    
    img_tk = ImageTk.PhotoImage(load_image())