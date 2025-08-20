from config.UX.screen.main import *
from config.UX.themes.theme_handler import *
from config.UX.main import *

def terms(app):
    main_box = ctk.CTkFrame(app, fg_color=app_background, height=1200, width=1800, 
                           border_color=background_colors[1], border_width=1)
    main_box.place(relx=0.5, rely=0.5, anchor="center")
    main_box.grid_propagate(False)
    main_box.grid_rowconfigure((0, 1, 2), weight=1)
    main_box.grid_columnconfigure(0, weight=1)

    upper_shadow = ctk.CTkFrame(main_box, height=200, width=1600, 
                               fg_color=background_colors[1], corner_radius=30)
    upper_shadow.grid(row=0, column=0, padx=100, pady=(100, 15), sticky="n")

    lower_shadow = ctk.CTkFrame(main_box, height=600, width=1600, 
                               fg_color=background_colors[1], corner_radius=30)
    lower_shadow.grid(row=1, column=0, padx=100, pady=15, sticky="n")

    copyright_shadow = ctk.CTkFrame(main_box, height=30, width=1600, 
                                   fg_color=background_colors[1], corner_radius=30)
    copyright_shadow.grid(row=2, column=0, padx=100, pady=(15, 100), sticky="n")

    upper_box = ctk.CTkFrame(main_box, height=200, width=1600, 
                            fg_color=background_colors[0], corner_radius=30)
    upper_box.grid(row=0, column=0, padx=100, pady=(100, 15), sticky="n")
    
    lower_box = ctk.CTkFrame(main_box, height=600, width=1600, 
                            fg_color=background_colors[0], corner_radius=30)
    lower_box.grid(row=1, column=0, padx=100, pady=15, sticky="n")
    
    copyright_box = ctk.CTkFrame(main_box, height=30, width=1600, 
                                fg_color=background_colors[0], corner_radius=30)
    copyright_box.grid(row=2, column=0, padx=100, pady=(15, 100), sticky="n")
    copyright_box.pack_propagate(False)

    copyright_label = ctk.CTkLabel(copyright_box, 
                                  text="All the code and rights belong to the github author BullStein @2025",
                                  font=(font_light, 25))
    copyright_label.pack()