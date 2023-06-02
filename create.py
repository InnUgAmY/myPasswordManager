# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Create.ui'
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
from PySide6.QtWidgets import (QApplication, QLineEdit, QPushButton, QSizePolicy,
    QWidget)
import resources

class Ui_Create_W(object):
    def setupUi(self, Create_W):
        if not Create_W.objectName():
            Create_W.setObjectName(u"Create_W")
        Create_W.resize(614, 487)
        Create_W.setBaseSize(QSize(4, 0))
        Create_W.setStyleSheet(u"QWidget {\n"
"background-color:qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0.198864 rgba(156, 156, 156, 255), stop:0.494318 rgba(214, 214, 214, 255), stop:1 rgba(63, 63, 63, 255));\n"
"font-family: Open Sans Light;\n"
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
        self.new_category = QLineEdit(Create_W)
        self.new_category.setObjectName(u"new_category")
        self.new_category.setGeometry(QRect(140, 40, 331, 61))
        self.new_category.setStyleSheet(u"QLineEdit {\n"
"border:2px solid black;\n"
"border-radius: 5px;\n"
"margin-right:0;\n"
"height: 50;\n"
"} \n"
"\n"
"QLineEdit: hover {\n"
"border-color: black;\n"
"}")
        self.new_category.setClearButtonEnabled(True)
        self.name = QLineEdit(Create_W)
        self.name.setObjectName(u"name")
        self.name.setGeometry(QRect(130, 170, 351, 81))
        self.name.setStyleSheet(u"QLineEdit {\n"
"border:2px solid black;\n"
"border-radius: 5px;\n"
"margin-right:0;\n"
"height: 50;\n"
"background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(184, 184, 184, 255), stop:0.482955 rgba(231, 231, 231, 255), stop:1 rgba(159, 159, 159, 255))\n"
"}\n"
"QLineEdit: hover {\n"
"border-color: white;\n"
"}\n"
"")
        self.name.setClearButtonEnabled(True)
        self.password = QLineEdit(Create_W)
        self.password.setObjectName(u"password")
        self.password.setGeometry(QRect(130, 250, 351, 81))
        self.password.setStyleSheet(u"QLineEdit {\n"
"border:2px solid black;\n"
"border-radius: 5px;\n"
"margin-right:0;\n"
"height: 50;\n"
"background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(184, 184, 184, 255), stop:0.482955 rgba(231, 231, 231, 255), stop:1 rgba(159, 159, 159, 255))\n"
"} \n"
"\n"
"QLineEdit: hover {\n"
"border-color: black;\n"
"}")
        self.password.setClearButtonEnabled(True)
        self.btn_cancel = QPushButton(Create_W)
        self.btn_cancel.setObjectName(u"btn_cancel")
        self.btn_cancel.setGeometry(QRect(130, 350, 181, 81))
        self.btn_cancel.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(145, 88, 89, 255), stop:0.869318 rgba(186, 186, 186, 255))")
        self.btn_key = QPushButton(Create_W)
        self.btn_key.setObjectName(u"btn_key")
        self.btn_key.setGeometry(QRect(300, 350, 191, 81))
        self.btn_key.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(97, 145, 145, 255), stop:0.869318 rgba(186, 186, 186, 255))")
        icon = QIcon()
        icon.addFile(u":/newPrefix/Icons/key.svg", QSize(), QIcon.Disabled, QIcon.On)
        self.btn_key.setIcon(icon)
        self.btn_key.setIconSize(QSize(60, 40))

        self.retranslateUi(Create_W)

        QMetaObject.connectSlotsByName(Create_W)
    # setupUi

    def retranslateUi(self, Create_W):
        Create_W.setWindowTitle(QCoreApplication.translate("Create_W", u"Create", None))
        self.new_category.setPlaceholderText(QCoreApplication.translate("Create_W", u"New category", None))
        self.name.setPlaceholderText(QCoreApplication.translate("Create_W", u"Name", None))
        self.password.setPlaceholderText(QCoreApplication.translate("Create_W", u"Password", None))
        self.btn_cancel.setText(QCoreApplication.translate("Create_W", u"Cancel", None))
        self.btn_key.setText("")
    # retranslateUi

