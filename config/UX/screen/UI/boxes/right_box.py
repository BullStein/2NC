import customtkinter as ctk
from config.UX.themes.theme_handler import *
def right_box(app,parent_box):
    app.right_box_frame = ctk.CTkFrame(
        parent_box,height=735,width=1000,fg_color=background_colors[0],corner_radius=40
        )
    app.right_box_frame.grid(row=0,column=1,padx=30)