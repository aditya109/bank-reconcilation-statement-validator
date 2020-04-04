import tkinter as tk
import sys
import tkinter.ttk as ttk
# import os

# os.chdir("..")
# sys.path.append(os.getcwd()+"\\utils")

# import from user-defined modules 
from utils.helpers import Font 
from PIL import Image, ImageTk


TITLE_FONT = ("Bernard MT Condensed", 50)
TITLE_FONT2 = ("Microsoft JhengHei Light", 50)
TEXT_FONT = ("Yu Gothic Light", 25)

class HomeWindow(tk.Frame) :
    def __init__(self, parent, controller) :
        tk.Frame.__init__(self, parent)
        # photo = Image.open(f"{sys.path[0]}\\assets\\try.jpg")
        # renderphoto = ImageTk.PhotoImage(photo)
        # img = tk.Label(self, image=renderphoto)
        # img.image = renderphoto
        # img.place(x=0, y=0)

        

        title_label = tk.Label(self, 
                        text = "Bank Reconciliation Statement Validator ", 
                        font = TITLE_FONT2,
                        fg="#FFA500", 
                        bg="#303133")
        title_label.pack(pady = 30, padx = 10)
        
        disclaimer_text = "This software is in alpha phase. \nPlease don't try to tamper it or induce malicious code in any manner.\nHope you have and make use of this software to fullest of your needs.\nIf you find any sort of discrepancies, please share on the feedback page."
        disclaimer = tk.Text(self, 
                            height = 6,
                            width = 55,
                            font = TEXT_FONT,
                            relief = "flat",
                            fg="#FFA500", 
                            bg="#303133")
        disclaimer.insert(tk.END, disclaimer_text)
        disclaimer.pack(pady=25, padx=10)

        click_to_proceed_btn = ttk.Button(self,
                                        text = "Click to Proceed >",
                                        state= "active")
        click_to_proceed_btn.pack(pady = 60, padx = 30)
    








        self.configure(bg="#2b2c2d")