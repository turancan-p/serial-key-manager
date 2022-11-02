from design.admin_menu_design import Ui_admin_page
from PyQt5.QtWidgets import *
from db.database import add_key, get_secret_key_for_user
from generate_key import *
from save_key import *
from datetime import date


class AdminPage(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.admin_menu = Ui_admin_page()
        self.admin_menu.setupUi(self)

        self.admin_menu.generate_button.clicked.connect(self.generate_and_save_key)

    def generate_and_save_key(self):
        username = self.admin_menu.username_box.text()
        print(username)
        secret_key = str.encode(get_secret_key_for_user(username))
        print(secret_key)
        self.admin_menu.keypass_box.setText("test")
        if secret_key is not None:
            today = str(date.today())
            password = str.encode(self.admin_menu.keypass_box.text())
            print(password)
            key = hashed_password(password, secret_key)
            print(key)
