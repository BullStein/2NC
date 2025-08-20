from config.UX.screen.main import *
from config.UX.themes.theme_handler import *
from config.UX.main import *
from config.UX.screen.UI.upper_box import *
from config.UX.screen.UI.lower_box import *
from config.UX.screen.UI.copyright_box import *

def terms(app):
    main_box = ctk.CTkFrame(app, fg_color=app_background,
                            bg_color=app_background)
    main_box.place(relx=0.5, rely=0.5, anchor="center")
    main_box.propagate(True)

    upper_box(main_box)
    
    lower_box(main_box)

    copyright_box(main_box)
    
