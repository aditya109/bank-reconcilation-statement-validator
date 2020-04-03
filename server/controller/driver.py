import tkinter as tk 
import server.windows.home as HomePage

class BRS(tk.TK) :
    def __init__ (self, *args, **kwargs) :
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self) 
        
        container.pack(side = "top", fill = "both", expand = True)
        
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)


        self.frames = {}

        frame = HomePage(container, self )

        self.frames[HomePage] = frame
        
        frame.grid (row = 0, column = 0, sticky = "nsew")

        self.show_frame(HomePage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


