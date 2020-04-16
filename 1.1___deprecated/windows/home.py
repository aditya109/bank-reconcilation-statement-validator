import tkinter as tk
import sys
import tkinter.ttk as ttk
from windows.tutorial import TutorialWindow

from PIL import Image, ImageTk

BUTTON_TEXT = ("Bahnschrift", 18, "bold")
TITLE_FONT2 = ("Microsoft JhengHei Light", 50)
TEXT_FONT = ("Calibri Light", 20)
CHECKBOXTEXT_FONT = ("Calibri", 15)

class HomeWindow(tk.Frame) :

    def __init__(self, parent, controller) :
        tk.Frame.__init__(self, parent)
        
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

        s = ttk.Style()
        s.configure('Wild.TButton',
            highlightthickness='20',
            font=BUTTON_TEXT)
        s.map('Wild.TButton',
            foreground=[('pressed', '#303133'),
                        ('disabled', 'darkgrey'),
                        ('active', 'coral')],
            background=[('pressed', 'focus', '#FFA500'),
                        ('active', '#FFA500')],
            highlightcolor=[('focus', 'green'),
                            ('!focus', 'red')],
            relief=[('pressed', 'flat'),
                    ('!pressed', 'ridge')])
        click_to_proceed_btn = ttk.Button(self,
                                        text = "Click to Proceed >",
                                        style= "Wild.TButton",
                                        state=tk.DISABLED,
                                        command = lambda: controller.show_frame(Tutorial)
                                        cursor= "shuttle")

        check_agreement_variable = tk.StringVar()
        checkbox_agreement = tk.Checkbutton(self, 
                                            text="I agree to the above directives given by the developers.",
                                            bg = "#303133",
                                            fg = "#FFA500",
                                            offvalue = "OFF",
                                            variable=check_agreement_variable,
                                            # selectcolor = "white",
                                            state = "active",
                                            onvalue= "ON",
                                            command = lambda:self.switchButtonState(check_agreement_variable, click_to_proceed_btn),
                                            relief = "flat",
                                            font = CHECKBOXTEXT_FONT)
        checkbox_agreement.deselect()
        checkbox_agreement.pack(pady = 60, padx = 30)
        click_to_proceed_btn.pack(side="bottom", pady = 50, padx = 30)
 
        self.configure(bg="#2b2c2d")

    def switchButtonState(self, state, button) :
        if state.get() == "OFF" :
            button['state'] = tk.DISABLED
        else :
            button['state'] = tk.NORMAL
    
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()
