# Designing the cover Window

# Using Python Tkinter

# Importing Libraries
import tkinter as tk
from tkinter import ttk as ttk


# Creating Font types
LARGE_FONT = ("Verdana", 12)
MEDIUM_FONT = ("Vedrana" , 10)
SMALL_FONT = ("Verdana", 8)

# Creating Main class BRS

class BRS(tk.Tk) :
    
    def __init__(self, *args, **kwargs) :
        
        tk.Tk.__init__(self, *args, **kwargs)
        
        # Assigning Window Icon
        tk.Tk.iconbitmap(self, default="C:/Users/Aditya/Desktop/Projects/Bank Reconcilation System/assets/favicon.ico")
        
        # Assigning Window Title
        tk.Tk.wm_title(self, "Bank Reconcilation System")
        
        container = tk.Frame(self)

        container.pack(side = "top", fill = "both", expand = True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # Making Slot for multiple window transition
        self.frames = {}

        frame = StartPage(container, self)

        self.frames[StartPage] = frame

        frame.grid(row = 0, column = 0, sticky = "nsew")

        self.show_frame(StartPage)
    
    def show_frame (self, cont) :
        
        frame = self.frames[cont]
        frame.tkraise()
        
        
class StartPage(tk.Frame) :
    
    def __init__(self, parent, controller) :
        
        tk.Frame.__init__(self, parent)

        image = ImageTk.PhotoImage(file = "C:\Users\Aditya\Desktop\Projects\Bank Reconcilation System\assets\236073_1476770867.jpeg")
        
        button1 = ttk.Button(self, text = "Visit Page")
        button1.pack()
        
app = BRS()
app.geometry("1600x900")
app.mainloop()
