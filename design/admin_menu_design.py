# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'admin_menu.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_admin_page(object):
    def setupUi(self, admin_page):
        admin_page.setObjectName("admin_page")
        admin_page.resize(1060, 600)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI Light")
        font.setPointSize(10)
        admin_page.setFont(font)
        self.verticalLayout = QtWidgets.QVBoxLayout(admin_page)
        self.verticalLayout.setObjectName("verticalLayout")
        self.scrollArea = QtWidgets.QScrollArea(admin_page)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1040, 580))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.key_table = QtWidgets.QTableWidget(self.scrollAreaWidgetContents)
        self.key_table.setMinimumSize(QtCore.QSize(0, 350))
        self.key_table.setMaximumSize(QtCore.QSize(16777215, 350))
        self.key_table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.key_table.setObjectName("key_table")
        self.key_table.setColumnCount(5)
        self.key_table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.key_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.key_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.key_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.key_table.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.key_table.setHorizontalHeaderItem(4, item)
        self.verticalLayout_2.addWidget(self.key_table, 0, QtCore.Qt.AlignTop)
        self.tabWidget = QtWidgets.QTabWidget(self.scrollAreaWidgetContents)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.username_box = QtWidgets.QLineEdit(self.tab)
        self.username_box.setGeometry(QtCore.QRect(60, 70, 141, 25))
        self.username_box.setObjectName("username_box")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(10, 70, 47, 25))
        self.label.setObjectName("label")
        self.exp_date = QtWidgets.QDateEdit(self.tab)
        self.exp_date.setGeometry(QtCore.QRect(290, 70, 110, 25))
        self.exp_date.setDateTime(QtCore.QDateTime(QtCore.QDate(2022, 11, 2), QtCore.QTime(0, 0, 0)))
        self.exp_date.setCalendarPopup(True)
        self.exp_date.setObjectName("exp_date")
        self.label_4 = QtWidgets.QLabel(self.tab)
        self.label_4.setGeometry(QtCore.QRect(220, 70, 70, 25))
        self.label_4.setObjectName("label_4")
        self.generate_button = QtWidgets.QPushButton(self.tab)
        self.generate_button.setGeometry(QtCore.QRect(430, 70, 100, 27))
        self.generate_button.setObjectName("generate_button")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.ID_box = QtWidgets.QLineEdit(self.tab_2)
        self.ID_box.setGeometry(QtCore.QRect(60, 70, 100, 25))
        self.ID_box.setObjectName("ID_box")
        self.label_2 = QtWidgets.QLabel(self.tab_2)
        self.label_2.setGeometry(QtCore.QRect(10, 70, 20, 25))
        self.label_2.setObjectName("label_2")
        self.delete_button = QtWidgets.QPushButton(self.tab_2)
        self.delete_button.setGeometry(QtCore.QRect(200, 70, 75, 27))
        self.delete_button.setObjectName("delete_button")
        self.tabWidget.addTab(self.tab_2, "")
        self.verticalLayout_2.addWidget(self.tabWidget)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)

        self.retranslateUi(admin_page)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(admin_page)

    def retranslateUi(self, admin_page):
        _translate = QtCore.QCoreApplication.translate
        admin_page.setWindowTitle(_translate("admin_page", "Admin Panel"))
        item = self.key_table.horizontalHeaderItem(0)
        item.setText(_translate("admin_page", "ID"))
        item = self.key_table.horizontalHeaderItem(1)
        item.setText(_translate("admin_page", "USER"))
        item = self.key_table.horizontalHeaderItem(2)
        item.setText(_translate("admin_page", "KEY"))
        item = self.key_table.horizontalHeaderItem(3)
        item.setText(_translate("admin_page", "CREATE DATE"))
        item = self.key_table.horizontalHeaderItem(4)
        item.setText(_translate("admin_page", "EXP DATE"))
        self.label.setText(_translate("admin_page", "User"))
        self.exp_date.setDisplayFormat(_translate("admin_page", "dd.MM.yyyy"))
        self.label_4.setText(_translate("admin_page", "Expiration"))
        self.generate_button.setText(_translate("admin_page", "Generate"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("admin_page", "Generate Key"))
        self.label_2.setText(_translate("admin_page", "ID"))
        self.delete_button.setText(_translate("admin_page", "Delete"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("admin_page", "Delete Key"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    admin_page = QtWidgets.QWidget()
    ui = Ui_admin_page()
    ui.setupUi(admin_page)
    admin_page.show()
    sys.exit(app.exec_())
