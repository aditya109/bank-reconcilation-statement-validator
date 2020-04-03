import tkinter as tk
# import sys
# import os

# os.chdir("..")
# sys.path.append(os.getcwd()+"\\utils")

# import from user-defined modules 
from utils.helpers import Font 

class HomeWindow(tk.Frame) :
    def __init__(self, parent, controller) :
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text = "Home Page", font = Font.LARGE_FONT)
        label.pack(pady = 10, padx = 10)
