from PyQt5.QtWidgets import QApplication
from login_menu import LoginMenu

app = QApplication([])


window = LoginMenu()
window.show()
app.exec_()