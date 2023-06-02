# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)
import resources

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(615, 485)
        MainWindow.setStyleSheet(u"QWidget {\n"
"background-color:qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0.198864 rgba(156, 156, 156, 255), stop:0.494318 rgba(214, 214, 214, 255), stop:1 rgba(63, 63, 63, 255));\n"
"font-family: Open Sans Light;\n"
"color: black;\n"
"font-size: 16pt;\n"
"margin: 10px;\n"
"}\n"
"QPushButton {\n"
"border: 2px solid black;\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"QPushPutton\n"
"#btn_search,\n"
"#btn_search,\n"
"#btn_tools,\n"
"#btn_library {\n"
"padding: 10px;}\n"
"\n"
" QPushButton:hover {\n"
"border-color: white;\n"
"}\n"
"\n"
"QPushButton: pressed {\n"
"border: 4px solid white;\n"
"}\n"
"\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")

        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.icon_lock = QPushButton(self.centralwidget)
        self.icon_lock.setObjectName(u"icon_lock")
        self.icon_lock.setStyleSheet(u"border: none;\n"
"background-color: None;")
        icon = QIcon()
        icon.addFile(u":/newPrefix/Icons/lock.svg", QSize(), QIcon.Disabled, QIcon.On)
        self.icon_lock.setIcon(icon)
        self.icon_lock.setIconSize(QSize(200, 200))

        self.horizontalLayout.addWidget(self.icon_lock)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setEnabled(True)
        self.lineEdit.setStyleSheet(u"QLineEdit {\n"
"border:2px solid black;\n"
"border-radius: 5px;\n"
"margin-right:0;\n"
"height: 50;\n"
"} \n"
"\n"
"QLineEdit: hover {\n"
"border-color: black;\n"
"}\n"
"")
        self.lineEdit.setMaxLength(1000)
        self.lineEdit.setClearButtonEnabled(True)

        self.horizontalLayout_2.addWidget(self.lineEdit)

        self.icon_search = QPushButton(self.centralwidget)
        self.icon_search.setObjectName(u"icon_search")
        self.icon_search.setStyleSheet(u"QPushButton {\n"
"height: 50;\n"
"Width: 50;\n"
"background-color: None;\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/newPrefix/Icons/123search.svg", QSize(), QIcon.Disabled, QIcon.On)
        self.icon_search.setIcon(icon1)
        self.icon_search.setIconSize(QSize(40, 40))

        self.horizontalLayout_2.addWidget(self.icon_search)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.layout_characters = QHBoxLayout()
        self.layout_characters.setObjectName(u"layout_characters")
        self.btn_tools = QPushButton(self.centralwidget)
        self.btn_tools.setObjectName(u"btn_tools")
        self.btn_tools.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(156, 156, 156, 255), stop:0.517045 rgba(255, 255, 255, 255), stop:1 rgba(165, 165, 165, 255))")
        self.btn_tools.setCheckable(True)

        self.layout_characters.addWidget(self.btn_tools)

        self.btn_create = QPushButton(self.centralwidget)
        self.btn_create.setObjectName(u"btn_create")
        self.btn_create.setStyleSheet(u"QPushButton {\n"
"Height: 44;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(156, 156, 156, 255), stop:0.517045 rgba(255, 255, 255, 255), stop:1 rgba(165, 165, 165, 255))\n"
"}")
        self.btn_create.setCheckable(True)

        self.layout_characters.addWidget(self.btn_create)

        self.btn_library = QPushButton(self.centralwidget)
        self.btn_library.setObjectName(u"btn_library")
        self.btn_library.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(156, 156, 156, 255), stop:0.517045 rgba(255, 255, 255, 255), stop:1 rgba(165, 165, 165, 255))\n"
"")
        self.btn_library.setCheckable(True)

        self.layout_characters.addWidget(self.btn_library)


        self.verticalLayout.addLayout(self.layout_characters)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"mnemosyne", None))
        self.icon_lock.setText("")
        self.icon_search.setText("")
        self.btn_tools.setText(QCoreApplication.translate("MainWindow", u"Tools", None))
        self.btn_create.setText(QCoreApplication.translate("MainWindow", u"create", None))
        self.btn_library.setText(QCoreApplication.translate("MainWindow", u"Library", None))
    # retranslateUi

