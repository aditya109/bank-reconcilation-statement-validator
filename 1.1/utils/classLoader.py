from windows.home import HomeWindow
from windows.dfloader import DFLoadingWindow
from windows.matchoptions import MatchOptionsWindow
from windows.nav import NavWindow
from windows.report import ReportWindow
from windows.search import SearchWindow
from windows.tutorial import TutorialWindow
from windows.warning import WarningWindow

class Loader :
    def __init__(self):
        self.window_list = []

    # fluent
    def set_window_list(self) :

        self.window_list = [HomeWindow,
        # DFLoadingWindow,
        # MatchOptionsWindow,
        # NavWindow,
        # ReportWindow,
        # SearchWindow,
        # TutorialWindow,
        # WarningWindow,
        ]

        return self

    def get_window_list(self):
        return self.window_list