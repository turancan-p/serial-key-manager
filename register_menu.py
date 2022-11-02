from design.register_menu_design import Ui_register_page
from db.database import register
from PyQt5.QtWidgets import *


class RegisterMenu(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.register_menu = Ui_register_page()
        self.register_menu.setupUi(self)

        self.register_menu.register_button.clicked.connect(self.register)

    def register(self):
        username = self.register_menu.username_box.text()
        password = str.encode(self.register_menu.password_box.text())
        if register(username, password):
            print("Register Succesfully")
        else:
            print("Register Failed")
