import generate_key
from design.main_menu_design import Ui_MainWindow
from PyQt5.QtWidgets import *
from generate_key import *
from save_key import *


class MainPage(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.main_menu = Ui_MainWindow()
        self.main_menu.setupUi(self)