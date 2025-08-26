from config.UX.screen.main import *
from config.UX.main import *
from config.UX.screen.UI.boxes.left_box import *
from config.UX.screen.UI.boxes.right_box import *
from config.UX.screen.UI.boxes.themes_box import *

def terms(app):
    app.main_box = ctk.CTkFrame(app, fg_color=app_background,
                            bg_color=app_background)
    app.main_box.place(relx=0.5, rely=0.5, anchor="center")
    app.main_box.propagate(True)

    left_box(app, app.main_box)
    right_box(app,app.main_box)
    
    
    logo_2nc = ctk.CTkLabel(app, text="2NC", font=(font_bold,20), 
                             text_color=background_colors[-1],fg_color=background_colors[1],bg_color=app_background,
                             corner_radius=10,height=30,width=50)
    logo_2nc.place(relx=1.0, rely=1.0, anchor="se", x=-20, y=-20)
    