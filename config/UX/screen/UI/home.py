from config.UX.screen.main import *
from config.UX.main import *
from config.UX.screen.UI.boxes.left_box import *
from config.UX.screen.UI.boxes.right_box import *
from config.UX.screen.UI.boxes.logo import *
from config.UX.screen.UI.boxes.logo import *

def terms(app):
    app.main_box = ctk.CTkFrame(app, fg_color=app_background,
                            bg_color=app_background)
    app.main_box.place(relx=0.5, rely=0.5, anchor="center")
    app.main_box.propagate(True)

    left_box(app, app.main_box)
    right_box(app,app.main_box)
    logo_box(app,app.main_box)
    
    