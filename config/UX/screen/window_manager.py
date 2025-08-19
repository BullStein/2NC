from config.UX.screen.UI.terms import *
from config.data.data_manager import * 

def window_config(app):
    title(app)
    window_size(app)
    
def title(app):
    app.title("2NC") 

def window_size(app=None):
    data = app.data #! data getted of the data handler function on the new object main app
    height = data["data"]["window"]["window_height"]
    width = data["data"]["window"]["window_width"]

    app.geometry(f"{width}x{height}")

def UI(app):
    data = read_data()
    if data["data"]["user"]["terms"] == "not accepted":
        terms(app)