from design.main_menu_design import Ui_MainWindow
from PyQt5.QtWidgets import *
from db.database import get_user_data, get_key_data, activate_key
from datetime import date


class MainPage(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.main_menu = Ui_MainWindow()
        self.main_menu.setupUi(self)

        self.main_menu.check_button.clicked.connect(self.check_button_pressed)
        self.main_menu.add_key_button.clicked.connect(self.activate_button_pressed)

        self.msg_box = QMessageBox()


    def check_button_pressed(self):
        username = self.main_menu.username_box.text()
        data = get_user_data(username)
        key = data[0][5]
        self.main_menu.public_box.setText(str(key))
        if key is not None:
            key_data = get_key_data(key, username)
            self.main_menu.expdate_box.setText(str(key_data[0][4]))
        today = date.today()

        if today > key_data[0][4]:
            print("kullanamaz")
            msg = QMessageBox()
            msg.setWindowTitle("Warning")
            msg.setText("Your Key is out of date!")
            msg.exec_()
        else:
            print("kullanır")
            msg = QMessageBox()
            msg.setWindowTitle("Info")
            msg.setText("Your Key is valid!")
            msg.exec_()



    def activate_button_pressed(self):
        username = self.main_menu.username_box.text()
        key = self.main_menu.activate_key_box.text()
        activate_key(username, key)