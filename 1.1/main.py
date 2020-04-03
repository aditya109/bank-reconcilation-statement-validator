from controller.driver import BRS
import sys
from utils.classLoader import Loader


if __name__ == "__main__" :
    
    app = BRS()
    app.title("Bank Reconcilation Statement Validator")
    app.iconbitmap(sys.path[0]+"\\assets\\favicon.ico")
    app.geometry("1366x768")
    app.mainloop()
