from config.UX.main import *
from config.data.main import *

load_fonts(ctk)

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.data_handler()
        self.UX_handler()

    def data_handler(self):
        self.data = read_data()

    def UX_handler(self):
        self.Inter,self.Inter_light = fonts_variable()
        window_config(self)
        UI(self)
    def start(self):
        self.mainloop()
        

if __name__ == "__main__":
    app = App()
    app.start()
