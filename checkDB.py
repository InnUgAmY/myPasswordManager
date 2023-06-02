from PyQt5 import QtCore,QtGui,QtWidgets
from DBhandler import *
class CheckThread(QtCore.QThread):
    mysignal = QtCore.pyqtSignal(str)

    def new_password(self,category,name,password):
         register(category,name,password,self.mysignal)

