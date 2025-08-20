from config.UX.main import *
from config.UX.themes.theme_handler import *
import customtkinter as ctk

def upper_box(main_box):
    upper_box = ctk.CTkFrame(main_box, height=220, width=1300, bg_color=app_background,
                             fg_color=background_colors[0], corner_radius=30)
    upper_box.pack()
    upper_box.grid_propagate(False)

    user_box = ctk.CTkFrame(upper_box, height=150,width=300,bg_color=background_colors[0],
                            fg_color=background_colors[1],corner_radius=30  )
    user_box.grid(row=1,column=0,padx=(20),pady=((upper_box._current_height - user_box._current_height) // 2))
    user_box.pack_propagate(False)

    user_label = ctk.CTkLabel(user_box,text="USER",font=(font_bold,40))
    user_label.pack()

    user_entry = ctk.CTkEntry(user_box,width=120,height=20,bg_color=background_colors[0],fg_color=background_colors[-1],
                             border_color=background_colors[0],border_width=30)
    user_entry.pack()