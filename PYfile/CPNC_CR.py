import csv
import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import matplotlib.dates as dates
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
import matplotlib.animation as animation
from matplotlib import style

from datetime import datetime
import time
from threading import Thread
import threading 

import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style


import urllib
import json
import pandas as pd
import numpy as np

import tkinter as tk
from tkinter import ttk as ttk
from tkinter.filedialog import askopenfilename



import tkinter as tk
style.use("fivethirtyeight")

fig = plt.figure(figsize = (8,8))
ax1 = plt.subplot2grid((2,2),(0,0))

def animate(i) :
      graph_data=open("example.txt","r").read()
      lines=graph_data.split('\n')
      pie_slices= [[]]

      for line in lines :
            if len(line) > 1 :
                  pie_slices.append(line)
      plt.pie(pie_slices)

            
def crap() :      
     

      pd.options.mode.chained_assignment = None
      

      cpnc1 = pd.read_csv('cpnc1.csv',index_col='TRAN DATE',parse_dates=True)
      cpnc1.columns=['PAYSLIP','CHEQUE','AMOUNT']

      cr1 = pd.read_csv('cr1.csv', index_col='DATE',parse_dates=True)
      cr1.columns=['PAYSLIP','CHEQUE','AMOUNT']
      
      pie_Match_Frequency=[0,cpnc1['PAYSLIP'].size,0,cr1['PAYSLIP'].size]
      f=open("example.txt","a+")
      f.write(str(pie_Match_Frequency)+"\n")
      f.close()
     
      col_names =['TRAN DATE','PAYSLIP','CHEQUE','AMOUNT']

      list_REC_MATCHED = [[]]
      list_REC_UNMATCHED = [[]]
      for REC_cpnc1_TrDate, row_cpnc1 in cpnc1.iterrows():

            
            REC_cpnc1_PaySlip = row_cpnc1['PAYSLIP']
            REC_cpnc1_amount = row_cpnc1['AMOUNT']
            REC_cpnc1_Chq = row_cpnc1['CHEQUE']
            
            
            foundFlag = False

            for REC_cr1_TrDate, row_cr1 in cr1.iterrows() :

                  
                              
                  REC_cr1_PaySlip = row_cr1['PAYSLIP']
                  REC_cr1_amount = row_cr1['AMOUNT']
                  REC_cr1_Chq = row_cr1['CHEQUE']
                  
                  if (REC_cpnc1_Chq != 0 ) :     #checking if the transaction is cheque or cash

                        #   confirms that transaction is cheque

                        if(REC_cpnc1_Chq == REC_cr1_Chq and REC_cpnc1_amount == REC_cr1_amount) :     #Checking if both the cheque number and amounts match
                              
                              
                              foundFlag=True
                              
                              ## move this record
                              break
                        
                        elif (REC_cpnc1_amount == REC_cr1_amount) :  # transaction is cash

                              
                              foundFlag=True
                              ### move this record....

                              break
                  
           
           


            if(foundFlag==True) :
                  
                  print("MATCH FOUND! CHEQUE NO : " + str(REC_cpnc1_Chq))
                  
                  list_REC_MATCHED.append([REC_cpnc1_TrDate, REC_cpnc1_PaySlip, REC_cpnc1_Chq, REC_cpnc1_amount ])
                  pie_Match_Frequency[0] = pie_Match_Frequency[0]+1 # CPNC records matched frequency
                  pie_Match_Frequency[1] -= 1                       # CPNC records unmatched frequency
                  pie_Match_Frequency[2] = pie_Match_Frequency[2]+1 # CR records matched frequency
                  pie_Match_Frequency[3] -= 1                       # CR records unmatched frequency
                  
                  f=open("example.txt","a+")
                  f.write(str(pie_Match_Frequency)+"\n")
                  f.close()

                  
            else :
                  print("MATCH NOT FOUND! CHEQUE NO : " + str(REC_cpnc1_Chq))
                  list_REC_UNMATCHED.append ([REC_cpnc1_TrDate, REC_cpnc1_PaySlip, REC_cpnc1_Chq, REC_cpnc1_amount])
                  pie_Match_Frequency[1] = pie_Match_Frequency[1]-1 # CPNC records unmatched frequency
                  pie_Match_Frequency[3] = pie_Match_Frequency[3]-1 # CR records unmatched frequency

                  f=open("example.txt","a+")
                  f.write(str(pie_Match_Frequency)+"\n")
                  f.close()
                  
      df_REC_MATCHED = pd.DataFrame(list_REC_MATCHED , columns = col_names, index_col='TRAN DATE', parse_dates=True)
      df_REC_UNMATCHED = pd.DataFrame(list_REC_UNMATCHED, columns = col_names, index_col='TRAN DATE', parse_dates=True)

      df_REC_MATCHED.to_csv('CPNC_Matched.csv')
      df_REC_UNMATCHED.to_csv('CPNC_Unmatched.csv')

      
def shit() :
      ani = animation.FuncAnimation(fig, animate, interval = 1000)
      plt.show()

def pro () :
      root = tk.Tk()     
      pb = ttk.Progressbar(root, orient="horizontal", length=5000, mode="indeterminate")
      pb.pack()
      pb.start()
      root.mainloop()


def worker() :
##      Thread(target= crap).start()
##      Thread(target= pro).start()
      Thread(target= shit).start()

worker()
                  
