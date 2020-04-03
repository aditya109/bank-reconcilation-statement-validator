# ------IMPORTING LIBRARIES---------

import tkinter as tk
from tkinter import ttk as ttk
import pandas as pd
import numpy as np

import matplotlib

matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure

from tkinter.filedialog import askopenfilename

import csv
import pandas as pd
from datetime import datetime
import time
import threading
from threading import Thread

# --------FONT----------------------

LARGE_FONT = ("Arial", 14)
NORMAL_FONT = ("MS Sans Serif", 10)
SMALL_FONT = ("Verdana", 8)
# --------Global Vars-----------------

File_list = []


# ------Main App Class--------------

class BRSO(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        tk.Tk.iconbitmap(self, default="favicon.ico")
        tk.Tk.wm_title(self, "Bank Reconcilation System Optimiser")
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        W = [LoginPage, disclaimerPage, SelectionPage, CPNC_CR_PAGE, CPNC_CR_FILE_ENTRY_PAGE, CPNC_CR_RESULT_ENTRY_PAGE]
        for F in W:
            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(LoginPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

#--------------Login Page----------------
class LoginPage(tk.Frame) :
    def __init__(self, parent, controller) :
        tk.Frame.__init__(self, parent)
        label1 = tk.Label(self, text="Login Page", font="Arial 30 bold underline")
        label1.pack(pady=50,padx=10)

        button1 = ttk.Button(self, text="Continue", command=lambda:controller.show_frame(disclaimerPage))
        button1.place(x=6, y=688)
        




# --------------Start Page---------------

class disclaimerPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label1 = tk.Label(self, text="Disclaimer", font="Arial 30 bold underline")
        label1.pack(pady=50, padx=10)

        label2 = tk.Label(self, justify="left", text='''\n\n\n\n\n\nThis Beta Software, is provided by programmer for the preview releases for quick bug fixes and access to the features.
Beta software is not fully tested by either the programmer, and may include significant issues.
It is your responsibility to protect system and your data when using Beta software with own products.
The programmer strongly recommends you BACK UP all of your data prior to using this Beta software.
This software is offered "AS-IS" and does not carry any warranties or support services.''', font="Verdana 12 ")
        label2.pack(padx=10)

        button1 = ttk.Button(self, text="Agree", command=lambda: controller.show_frame(SelectionPage))
        button1.place(x=6, y=688)

        button2 = ttk.Button(self, text="Disagree", command=quit)
        button2.place(x=941, y=688)

    def close_window(self):
        self.destroy()


# ----------OpenFile()-----------------------

def OpenFile():
    File = askopenfilename(filetypes=(("Text CSV (.csv)", "*.csv"), ("All Files", "*.*")), title="Choose a file.")
    return File


def P():
    File = OpenFile()
    File_list.append(File)
    print(File_list)

def Bleh() :
    pass

def CPNC_CR(pb, popup):
    # preparing cpnc1.csv for use

    cpnc1 = pd.read_csv(File_list[0], index_col='TRAN DATE', parse_dates=True)
    cpnc1.columns = ['PAYSLIP', 'CHEQUE', 'AMOUNT']

    # cpnc.csv prepared...!

    # preparing cr1.csv for use

    cr1 = pd.read_csv(File_list[1], index_col='DATE', parse_dates=True)
    cr1.columns = ['PAYSLIP', 'CHEQUE', 'AMOUNT']
    cr1['STATUS'] = 0

    # starting matchmaking here ... applying Linear Search

    col_names = ['TRAN DATE', 'PAYSLIP', 'CHEQUE', 'AMOUNT']

    list_REC_MATCHED = [[]]
    list_REC_UNMATCHED = [[]]

    for REC_cpnc1_TrDate, row_cpnc1 in cpnc1.iterrows():

        REC_cpnc1_PaySlip = row_cpnc1['PAYSLIP']
        REC_cpnc1_amount = row_cpnc1['AMOUNT']
        REC_cpnc1_Chq = row_cpnc1['CHEQUE']

        foundFlag = False

        for REC_cr1_TrDate, row_cr1 in cr1.iterrows():

            REC_cr1_PaySlip = row_cr1['PAYSLIP']
            REC_cr1_amount = row_cr1['AMOUNT']
            REC_cr1_Chq = row_cr1['CHEQUE']

            if (REC_cpnc1_Chq != 0):  # checking if the transaction is cheque or cash

                #   confirms that transaction is cheque

                if (REC_cpnc1_Chq == REC_cr1_Chq and REC_cpnc1_amount == REC_cr1_amount):  # Checking if both the cheque number and amounts match
                    
                    foundFlag = True
                    break

                elif (REC_cpnc1_amount == REC_cr1_amount):  # transaction is cash

                    foundFlag = True
                    break
        if (foundFlag == True):

            #print("MATCH FOUND! CHEQUE NO : " + str(REC_cpnc1_Chq))

            list_REC_MATCHED.append([REC_cpnc1_TrDate, REC_cpnc1_PaySlip, REC_cpnc1_Chq, REC_cpnc1_amount])

        else:

            #print("MATCH NOT FOUND! CHEQUE NO : " + str(REC_cpnc1_Chq))
            list_REC_UNMATCHED.append([REC_cpnc1_TrDate, REC_cpnc1_PaySlip, REC_cpnc1_Chq, REC_cpnc1_amount])

    df_REC_MATCHED = pd.DataFrame(list_REC_MATCHED, columns=col_names)
    df_REC_MATCHED.set_index('TRAN DATE')
    df_REC_UNMATCHED = pd.DataFrame(list_REC_UNMATCHED, columns=col_names)
    df_REC_UNMATCHED.set_index('TRAN DATE')

    df_REC_MATCHED.to_csv('CPNC_Matched.csv')
    df_REC_UNMATCHED.to_csv('CPNC_Unmatched.csv')

    pb.pack_forget()

    label1 = tk.Label(popup, text="The Match Selected for Cheque-Paid-Not-Encashed to Credit has been complete...  ", font="Verdana 10 bold underline")
    label1.pack(pady=50, padx=10)

    b = tk.Button(popup, text="", command=lambda: Bleh())
    b.pack()



def popupStatus_Result(target1):
      popup = tk.Tk()
      popup.iconbitmap("popup.ico")
      popup.wm_title("Processing the Work..")

      label1 = tk.Label(popup, text ="Please Wait Patiently while The App Does the Work for You...", font = NORMAL_FONT)
      label1.pack(side="top", fill="x", pady = 10)

      pb = ttk.Progressbar(popup, orient="horizontal", value=0, maximum=100, length=200, mode="indeterminate")
      pb.pack()
      pb.start()
      thread1 = Thread(target=target1,args=(pb, popup,))
      thread1.start()
      popup.mainloop()


def Work_Master (target2) :
    thread2 = Thread(target = target2, args = (CPNC_CR,))
    thread2.start()

# --------CreateToolTip()----------------------

class CreateToolTip(object):
    def __init__(self, widget, text='widget info'):
        self.waittime = 500
        self.wraplength = 180
        self.widget = widget
        self.text = text
        self.widget.bind("<Enter>", self.enter)
        self.widget.bind("<Leave>", self.leave)
        self.widget.bind("<ButtonPress>", self.leave)
        self.id = None
        self.tw = None

    def enter(self, event=None):
        self.schedule()

    def leave(self, event=None):
        self.unschedule()
        self.hidetip()

    def schedule(self):
        self.unschedule()
        self.id = self.widget.after(self.waittime, self.showtip)

    def unschedule(self):
        id = self.id
        self.id = None
        if id:
            self.widget.after_cancel(id)

    def showtip(self, event=None):
        x = y = 0
        x, y, cx, cy = self.widget.bbox("insert")
        x += self.widget.winfo_rootx() + 25
        y += self.widget.winfo_rooty() + 20
        self.tw = tk.Toplevel(self.widget)

        self.tw.wm_overrideredirect(True)
        self.tw.wm_geometry("+%d+%d" % (x, y))
        label = tk.Label(self.tw, text=self.text, justify='left', background="#ffffff", relief='solid', borderwidth=1,
                         wraplength=self.wraplength)
        label.pack(ipadx=1)

    def hidetip(self):
        tw = self.tw
        self.tw = None
        if tw:
            tw.destroy()


# --------CPNC_CR Page----------------

class CPNC_CR_PAGE(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label1 = tk.Label(self, text="Cheque-Paid-Not-Encashed to Credit", font="Arial 30 bold underline")
        label1.pack(pady=50, padx=10)

        labelframe = tk.LabelFrame(self, bg="white", height=50, width=100, relief="groove",
                                   text="Please read the instructions before proceeding forward :", font="Verdana 15 ")
        labelframe.pack(fill="both", expand="yes", pady=20, padx=10)

        label3 = tk.Label(labelframe, justify="left", bg="white", text="""Here the records of the CPNC spreadsheet will be matched to CR spreadsheet linearly.

                          The matched records of CPNC file will then be moved to CPNC_matched.csv.

                          The unmatched ones will be moved to CPNC_unmatched.csv.

                          The same will be done with CR spreadsheet.

                          Now that you have the understood the mode of operation of the software, please click on \"Next >>\".

                          Please keep in mind that the original files you will be providing will remain untouched.\n""",
                          font="Verdana 12")
        label3.pack(side="top", pady=10, padx=7)

        button1 = ttk.Button(self, text="Next>>", command=lambda: controller.show_frame(CPNC_CR_FILE_ENTRY_PAGE))
        button1.pack(pady=50, padx=10)


# --------CPNC_CR_FILE_ENTRY PAGE-------------

class CPNC_CR_FILE_ENTRY_PAGE(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        status = tk.Label(self, text="Preparing to do nothing...", bd=2, relief="sunken", anchor="w")
        status.pack(side="bottom", fill="x")

        label1 = tk.Label(self, justify="left", text="Enter the path of the CPNC spreadsheet : ", font=LARGE_FONT)
        label1.place(x=39, y=45)

        def update_status_CPNC(msg):
            P()
            current_status = status["text"]

            # call the open file function

            status["text"] = msg

        button1 = ttk.Button(self, text="Browse",
                             command=lambda: update_status_CPNC("The spreadsheet for CPNC has been received"))
        button1.place(x=450, y=45)

        label2 = tk.Label(self, justify="left", text="Enter the path of the CR spreadsheet : ", font=LARGE_FONT)
        label2.place(x=39, y=90)

        def update_status_CR(msg):
            P()
            current_status = status["text"]

            # call the open file function

            status["text"] = msg

        button2 = ttk.Button(self, text="Browse",
                             command=lambda: update_status_CR("The spreadsheet for CR has been received"))
        button2.place(x=450, y=90)

        button3 = ttk.Button(self, text="Next>>", command=lambda:Work_Master(popupStatus_Result))
        button3.place(x=930, y=135)


# --------CPNC_CR_RESULT PAGE-----------
class CPNC_CR_RESULT_ENTRY_PAGE(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        button1 = ttk.Button(self, text="Next>>", command=lambda: CPNC_CR(File_list[0], File_list[1]))
        button1.place(x=930, y=135)


# --------Selection Page-----------------------

class SelectionPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label1 = tk.Label(self, text="Spreadsheet Type Selection", font="Arial 20 bold")
        label1.pack(pady=50, padx=10)

        label1 = tk.Label(self, text="Select your Match_Line Key :", font="Arial 14")
        label1.pack(pady=50, padx=10)

        button1 = ttk.Button(self, text="Cheque-Paid-Not-Encashed -> Credit ",
                             command=lambda: controller.show_frame(CPNC_CR_PAGE))
        button1.place(x=150, y=300)
        button1_ttp = CreateToolTip(button1, "Click this button to match CPNC with CR spreadsheet")

        button2 = ttk.Button(self, text="Cheque-Dishonored-Action -> Debit ",
                             command=lambda: controller.show_frame(SelectionPage))
        button2.place(x=150, y=350)
        button2_ttp = CreateToolTip(button2, "Click this button to match CDA with DR spreadsheet")

        button3 = ttk.Button(self, text="Cheque-Paid-Not-Encashed -> Cheque-Dishonored-Action ",
                             command=lambda: controller.show_frame(SelectionPage))
        button3.place(x=150, y=400)
        button3_ttp = CreateToolTip(button3, "Click this button to match CPNC with CDA spreadsheet")

        button4 = ttk.Button(self, text="Credit -> Debit ", command=lambda: controller.show_frame(SelectionPage))
        button4.place(x=150, y=450)
        button4_ttp = CreateToolTip(button4, "Click this button to match CR with DR spreadsheet")

        label4 = tk.Label(self, text="Note", font="Verdana 9 bold underline")
        label4.pack(padx=10, pady=10)
        label4.place(x=2, y=650)

        label5 = tk.Label(self, text=" :", font="Verdana 9 bold")
        label5.pack(padx=10, pady=10)
        label5.place(x=36, y=650)

        label2 = tk.Label(self,
                          text="The Item to the left of the arrow represent the spreadsheet from which the records will be matched. ",
                          font=SMALL_FONT)
        label2.pack(padx=10, pady=10)
        label2.place(x=2, y=675)

        label3 = tk.Label(self,
                          text="The Item to the right of the arrow represents the spreadsheet into which the records from the former spreadsheet will be matched",
                          font=SMALL_FONT)
        label3.pack(padx=10, pady=10)
        label3.place(x=2, y=691)


class PageOne(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Page One", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        f = Figure(figsize=(5, 5), dpi=100)
        a = f.add_subplot(111)
        a.plot([1, 2, 3, 4, 5], [5, 2, 3, 6, 11])

        canvas = FigureCanvasTkAgg(f, self)
        canvas.show()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2TkAgg(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack()

        button1 = ttk.Button(self, text="Back To Home", command=lambda: controller.show_frame(StartPage))
        button1.pack()


app = BRSO()
app.geometry("1024x720")
app.mainloop()
