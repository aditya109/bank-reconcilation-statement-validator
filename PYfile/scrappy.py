##import tkinter as tk
##from tkinter import ttk
##
##
##class SampleApp(tk.Tk):
##
##    def __init__(self, *args, **kwargs):
##        tk.Tk.__init__(self, *args, **kwargs)
##        self.button = ttk.Button(text="start", command=self.start)
##        self.button.pack()
##        self.progress = ttk.Progressbar(self, orient="horizontal",
##                                        length=2000, mode="determinate")
##        self.progress.pack()
##
##        self.bytes = 0
##        self.maxbytes = 0
##
##    def start(self):
##        self.progress["value"] = 0
##        self.maxbytes = 50000
##        self.progress["maximum"] = 50000
##        self.read_bytes()
##
##    def read_bytes(self):
##        '''simulate reading 500 bytes; update progress bar'''
##        self.bytes += 5
##        self.progress["value"] = self.bytes
##        if self.bytes < self.maxbytes:
##            # read more bytes after 100 ms
##            self.after(100, self.read_bytes)
##
##app = SampleApp()
##app.mainloop()
# Test Code for Tkinter with threads
import tkinter as Tk
import multiprocessing
import queue
from queue import Empty, Full
import time

class GuiApp(object):
   def __init__(self,q):
      self.root = tk.Tk()
      self.root.geometry('300x100')
      self.text_wid = tk.Text(self.root,height=100,width=100)
      self.text_wid.pack(expand=1,fill=Tk.BOTH)
      self.root.after(100,self.CheckQueuePoll,q)

   def CheckQueuePoll(self,c_queue):
      try:
         str = c_queue.get(0)
         self.text_wid.insert('end',str)
      except Empty:
         pass
      finally:
         self.root.after(100, self.CheckQueuePoll, c_queue)

# Data Generator which will generate Data
def GenerateData(q):
   for i in range(10):
      print ("Generating Some Data, Iteration %s" %(i))
      time.sleep(2)
      q.put("Some Data from iteration %s \n" %(i))


if __name__ == '__main__':
# Queue which will be used for storing Data

   q = multiprocessing.Queue()
   q.cancel_join_thread() # or else thread that puts data will not term
   gui = GuiApp(q)
   t1 = multiprocessing.Process(target=GenerateData,args=(q,))
   t1.start()
   gui.root.mainloop()

   t1.join()
   t2.join()
