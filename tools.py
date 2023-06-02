# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tools.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QPushButton, QSizePolicy,
    QWidget)

class Ui_tools(QWidget):
    def setupUi(self, tools):
        if not tools.objectName():
            tools.setObjectName(u"tools")
        tools.resize(615, 487)
        tools.setStyleSheet(u"QWidget {\n"
"background-color:qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0.193182 rgba(111, 111, 111, 255), stop:0.5 rgba(50, 50, 50, 255), stop:1 rgba(124, 124, 124, 255));\n"
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
        self.CheckBox_auth = QCheckBox(tools)
        self.CheckBox_auth.setObjectName(u"CheckBox_auth")
        self.CheckBox_auth.setGeometry(QRect(130, 120, 361, 51))
        self.CheckBox_auth.setStyleSheet(u"\n"
"background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(184, 184, 184, 255), stop:0.482955 rgba(231, 231, 231, 255), stop:1 rgba(159, 159, 159, 255));\n"
"\n"
"")
        self.checkBox_Add = QCheckBox(tools)
        self.checkBox_Add.setObjectName(u"checkBox_Add")
        self.checkBox_Add.setGeometry(QRect(130, 170, 361, 51))
        self.checkBox_Add.setStyleSheet(u"background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(184, 184, 184, 255), stop:0.482955 rgba(231, 231, 231, 255), stop:1 rgba(159, 159, 159, 255))")
        self.checkBox_hide = QCheckBox(tools)
        self.checkBox_hide.setObjectName(u"checkBox_hide")
        self.checkBox_hide.setGeometry(QRect(130, 220, 361, 51))
        self.checkBox_hide.setStyleSheet(u"background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(184, 184, 184, 255), stop:0.482955 rgba(231, 231, 231, 255), stop:1 rgba(159, 159, 159, 255))")
        self.btn_cancel = QPushButton(tools)
        self.btn_cancel.setObjectName(u"btn_cancel")
        self.btn_cancel.setGeometry(QRect(130, 330, 181, 81))
        self.btn_cancel.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(145, 88, 89, 255), stop:0.869318 rgba(186, 186, 186, 255))")
        self.btn_key = QPushButton(tools)
        self.btn_key.setObjectName(u"btn_key")
        self.btn_key.setGeometry(QRect(310, 330, 191, 81))
        self.btn_key.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(97, 145, 145, 255), stop:0.869318 rgba(186, 186, 186, 255))")
        icon = QIcon()
        icon.addFile(u":/newPrefix/Icons/key.svg", QSize(), QIcon.Disabled, QIcon.On)
        self.btn_key.setIcon(icon)
        self.btn_key.setIconSize(QSize(60, 40))

        self.retranslateUi(tools)

        QMetaObject.connectSlotsByName(tools)
    # setupUi

    def retranslateUi(self, tools):
        tools.setWindowTitle(QCoreApplication.translate("tools", u"Form", None))
        self.CheckBox_auth.setText(QCoreApplication.translate("tools", u"    Password authorization", None))
        self.checkBox_Add.setText(QCoreApplication.translate("tools", u"    Add Password generator", None))
        self.checkBox_hide.setText(QCoreApplication.translate("tools", u"    hide passwords", None))
        self.btn_cancel.setText(QCoreApplication.translate("tools", u"Cancel", None))
        self.btn_key.setText(QCoreApplication.translate("tools", u"Accept", None))
    # retranslateUi

