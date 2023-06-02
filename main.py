import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QWidget
from ui_main import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
import PySide6
#---------------------------------------------

from create import Ui_Create_W
from ui_main import Ui_MainWindow
from checkDB import *
from tools import Ui_tools
from library import Ui_library
from search import Ui_search

class search(QWidget):
    def __init__(self):
        super(search, self).__init__()
        self.ui = Ui_search()
        self.ui.setupUi(self)
class library(QWidget):
    def __init__(self):
        super(library, self).__init__()
        self.ui = Ui_library()
        self.ui.setupUi(self)
        self.loaddata()
    def loaddata(self):
        con = sqlite3.connect('C:/Users/Dani/PycharmProjects/Mnemosyne/PassDB.db')
        cur = con.cursor()
        sqlquery = "SELECT * FROM data"
        print(cur.execute(sqlquery))
        self.ui.table.setRowCount(15)
        tablerow = 0
        for row in cur.execute(sqlquery):
            print(row)
            self.ui.table.setItem(tablerow, 0, PySide6.QtWidgets.QTableWidgetItem(row[0]))
            self.ui.table.setItem(tablerow, 1, PySide6.QtWidgets.QTableWidgetItem(row[1]))
            self.ui.table.setItem(tablerow, 2, PySide6.QtWidgets.QTableWidgetItem(row[2]))
            tablerow+=1
class tools(QWidget):
    def __init__(self):
        super(tools, self).__init__()
        self.ui = Ui_tools()
        self.ui.setupUi(self)
        self.ui.btn_cancel.clicked.connect(self.closeW)
        self.ui.btn_key.clicked.connect(self.closeW)
    def closeW(self):
        self.close()
class Create(QWidget):
    def __init__(self):
        super(Create, self).__init__()
        self.ui = Ui_Create_W()
        self.ui.setupUi(self)
        self.ui.btn_cancel.clicked.connect(self.closeW)
        self.ui.btn_key.clicked.connect(self.addPassword)
        self.base_Lines_edit = [self.ui.new_category, self.ui.name, self.ui.password]
        self.checkDB = CheckThread()
    # проверка правильности ввода
    def closeW(self):
        self.close()
    def input_check(funct):
        def wrapper(self):
            for line_edit in self.base_Lines_edit:
                if len(line_edit.text()) == 0:
                    return
            funct(self)
        return wrapper


    @input_check
    def addPassword(self):
        category = self.ui.new_category.text()
        name = self.ui.name.text()
        password = self.ui.password.text()
        self.checkDB.new_password(category, name, password)
        self.close()

class Main(QMainWindow):
    def __init__(self):
        super(Main,self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btn_create.clicked.connect(self.open_create)
        self.ui.btn_tools.clicked.connect(self.open_tools)
        self.ui.btn_library.clicked.connect(self.open_library)
        self.ui.icon_search.clicked.connect(self.open_search)

    def open_create(self):
        self.w2 = Create()
        self.w2.show()
    def open_tools(self):
        self.w2 = tools()
        self.w2.show()
    def open_library(self):
        self.w2 = library()
        self.w2.show()
    def open_search(self):
        self.w2 = search()
        self.w2.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Main()
    window.show()
    sys.exit(app.exec())

