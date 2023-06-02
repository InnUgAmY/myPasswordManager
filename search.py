# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'search.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QSizePolicy, QWidget)

class Ui_search(object):
    def setupUi(self, search):
        if not search.objectName():
            search.setObjectName(u"search")
        search.resize(615, 211)
        search.setStyleSheet(u"QWidget {\n"
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
"")
        self.info = QLabel(search)
        self.info.setObjectName(u"info")
        self.info.setGeometry(QRect(30, 70, 561, 81))
        self.info.setStyleSheet(u"background-color: None;")

        self.retranslateUi(search)

        QMetaObject.connectSlotsByName(search)
    # setupUi

    def retranslateUi(self, search):
        search.setWindowTitle(QCoreApplication.translate("search", u"search", None))
        self.info.setText("")
    # retranslateUi

