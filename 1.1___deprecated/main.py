from controller.driver import BRS
import sys
from utils.classLoader import Loader


if __name__ == "__main__" :
    
    app = BRS()
    app.title("Bank Reconciliation  Statement Validator")
    app.iconbitmap(sys.path[0]+"\\assets\\favicon.ico")
    # app.wm_attributes("-transparent", "#303133")
    app.geometry("1366x768")
    app.mainloop()
