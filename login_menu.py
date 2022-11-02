from design.login_menu_design import Ui_login_page
from register_menu import RegisterMenu
from admin_menu import AdminPage
from main_menu import MainPage
from PyQt5.QtWidgets import *
from db.database import login_check


class LoginMenu(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.login_menu = Ui_login_page()
        self.login_menu.setupUi(self)
        self.main_page = MainPage()
        self.register_page = RegisterMenu()
        self.admin_page = AdminPage()

        self.login_menu.register_button.clicked.connect(self.register_menu)
        self.login_menu.login_buton.clicked.connect(self.login)

    def register_menu(self):
        self.register_page.show()

    def login(self):
        username = self.login_menu.username_box.text()
        password = self.login_menu.password_box.text()
        if login_check(username, password):
            test = login_check(username, password)
            print(test)
            self.main_page.main_menu.id_box.setText(str(test[0]))
            self.main_page.main_menu.username_box.setText(str(test[1]))
            self.main_page.main_menu.authory_box.setText(str(test[6]))
            self.main_page.main_menu.secret_box.setText(str(test[4]))
            self.main_page.main_menu.public_box.setText(str(test[5]))
            if str(test[6]) == "Admin":
                self.admin_page.show()

            self.main_page.show()
            self.close()
        else:
            print("Giriş Başarısız")