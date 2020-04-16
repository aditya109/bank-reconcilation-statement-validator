import tkinter as tk 
from windows.home import HomeWindow
from utils.classLoader import Loader
class BRS(tk.Tk) :
    def __init__ (self, *args, **kwargs) :
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self) 
        
        container.pack(side = "top", fill = "both", expand = True)
        
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)


        self.frames = {}

        windows = Loader().set_window_list().get_window_list()
        for window in windows :
            frame = window(container, self)
            self.frames[window] = frame
            frame.grid (row = 0, column = 0, sticky = "nsew")

        self.show_frame(HomeWindow)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


