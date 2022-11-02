# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_menu.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 320)
        MainWindow.setMinimumSize(QtCore.QSize(500, 320))
        MainWindow.setMaximumSize(QtCore.QSize(500, 320))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI Light")
        font.setPointSize(10)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.main_page = QtWidgets.QTabWidget(self.centralwidget)
        self.main_page.setObjectName("main_page")
        self.generate_tab = QtWidgets.QWidget()
        self.generate_tab.setObjectName("generate_tab")
        self.id_box = QtWidgets.QLineEdit(self.generate_tab)
        self.id_box.setGeometry(QtCore.QRect(100, 10, 30, 25))
        self.id_box.setReadOnly(True)
        self.id_box.setPlaceholderText("")
        self.id_box.setObjectName("id_box")
        self.username_box = QtWidgets.QLineEdit(self.generate_tab)
        self.username_box.setGeometry(QtCore.QRect(100, 50, 100, 25))
        self.username_box.setReadOnly(True)
        self.username_box.setPlaceholderText("")
        self.username_box.setObjectName("username_box")
        self.label = QtWidgets.QLabel(self.generate_tab)
        self.label.setGeometry(QtCore.QRect(10, 10, 16, 25))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.generate_tab)
        self.label_2.setGeometry(QtCore.QRect(10, 50, 65, 25))
        self.label_2.setObjectName("label_2")
        self.label_9 = QtWidgets.QLabel(self.generate_tab)
        self.label_9.setGeometry(QtCore.QRect(10, 90, 86, 25))
        self.label_9.setObjectName("label_9")
        self.authory_box = QtWidgets.QLineEdit(self.generate_tab)
        self.authory_box.setGeometry(QtCore.QRect(100, 90, 100, 25))
        self.authory_box.setReadOnly(True)
        self.authory_box.setPlaceholderText("")
        self.authory_box.setObjectName("authory_box")
        self.secret_box = QtWidgets.QLineEdit(self.generate_tab)
        self.secret_box.setGeometry(QtCore.QRect(240, 50, 211, 25))
        self.secret_box.setReadOnly(True)
        self.secret_box.setObjectName("secret_box")
        self.public_box = QtWidgets.QLineEdit(self.generate_tab)
        self.public_box.setGeometry(QtCore.QRect(10, 170, 453, 25))
        self.public_box.setReadOnly(True)
        self.public_box.setObjectName("public_box")
        self.label_10 = QtWidgets.QLabel(self.generate_tab)
        self.label_10.setGeometry(QtCore.QRect(310, 20, 61, 25))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.generate_tab)
        self.label_11.setGeometry(QtCore.QRect(200, 140, 61, 25))
        self.label_11.setObjectName("label_11")
        self.expdate_box = QtWidgets.QLineEdit(self.generate_tab)
        self.expdate_box.setGeometry(QtCore.QRect(100, 220, 160, 25))
        self.expdate_box.setReadOnly(True)
        self.expdate_box.setObjectName("expdate_box")
        self.label_12 = QtWidgets.QLabel(self.generate_tab)
        self.label_12.setGeometry(QtCore.QRect(10, 220, 86, 25))
        self.label_12.setObjectName("label_12")
        self.check_button = QtWidgets.QPushButton(self.generate_tab)
        self.check_button.setGeometry(QtCore.QRect(320, 220, 75, 27))
        self.check_button.setObjectName("check_button")
        self.main_page.addTab(self.generate_tab, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.activate_key_box = QtWidgets.QLineEdit(self.tab)
        self.activate_key_box.setGeometry(QtCore.QRect(10, 70, 452, 25))
        self.activate_key_box.setObjectName("activate_key_box")
        self.add_key_button = QtWidgets.QPushButton(self.tab)
        self.add_key_button.setGeometry(QtCore.QRect(190, 140, 90, 30))
        self.add_key_button.setObjectName("add_key_button")
        self.main_page.addTab(self.tab, "")
        self.verticalLayout.addWidget(self.main_page)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.main_page.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "User Panel"))
        self.label.setText(_translate("MainWindow", "ID"))
        self.label_2.setText(_translate("MainWindow", "Username"))
        self.label_9.setText(_translate("MainWindow", "Authorization"))
        self.label_10.setText(_translate("MainWindow", "Secret Key"))
        self.label_11.setText(_translate("MainWindow", "Serial Key"))
        self.label_12.setText(_translate("MainWindow", "Exp Date"))
        self.check_button.setText(_translate("MainWindow", "Check"))
        self.main_page.setTabText(self.main_page.indexOf(self.generate_tab), _translate("MainWindow", "Account Details"))
        self.add_key_button.setText(_translate("MainWindow", "Activate Key"))
        self.main_page.setTabText(self.main_page.indexOf(self.tab), _translate("MainWindow", "Add Key"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
