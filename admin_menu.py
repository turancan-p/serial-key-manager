from design.admin_menu_design import Ui_admin_page
from PyQt5.QtWidgets import *
from db.database import add_key, get_secret_key_for_user, get_all_key_data
from generate_key import *
from datetime import date


class AdminPage(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.admin_menu = Ui_admin_page()
        self.admin_menu.setupUi(self)
        self.admin_menu.generate_button.clicked.connect(self.generate_and_save_key)

        self.today = date.today()
        self.admin_menu.exp_date.setDate(self.today)

        self.update_table()

    def generate_and_save_key(self):
        username = self.admin_menu.username_box.text()
        secret_key = str.encode(get_secret_key_for_user(username))
        if secret_key is not None:

            exp_date = self.admin_menu.exp_date.date().toPyDate()
            password = str.encode(str(exp_date))
            key = hashed_password(password, secret_key)
            if add_key(username, key, self.today, exp_date):
                print("Key Added")
                self.update_table()
            else:
                print("Failed")

    def update_table(self):
        datas = get_all_key_data()
        self.admin_menu.key_table.setRowCount(0)

        for row_number, row_data in enumerate(datas):
            self.admin_menu.key_table.insertRow(row_number)
            i = 0
            while i < 5:
                self.admin_menu.key_table.setItem(row_number, i, QTableWidgetItem(str(row_data[i])))  # id
                i += 1