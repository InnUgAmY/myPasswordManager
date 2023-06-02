# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'library.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHeaderView, QSizePolicy,
    QTableWidget, QTableWidgetItem, QWidget)

class Ui_library(QWidget):
    def setupUi(self, library):
        if not library.objectName():
            library.setObjectName(u"library")
        library.resize(617, 484)
        library.setSizeIncrement(QSize(10, 10))
        library.setBaseSize(QSize(0, 0))
        library.setStyleSheet(u"QWidget {\n"
"background-color:qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0.198864 rgba(156, 156, 156, 255), stop:0.494318 rgba(214, 214, 214, 255), stop:1 rgba(63, 63, 63, 255));\n"
"font-family: Open Sans Light;\n"
"\n"
"}\n"
"\n"
"")
        self.table = QTableWidget(library)
        if (self.table.columnCount() < 3):
            self.table.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.table.setObjectName(u"table")
        self.table.setGeometry(QRect(40, 30, 541, 421))
        self.table.setStyleSheet(u"\n"
"background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(184, 184, 184, 255), stop:0.482955 rgba(231, 231, 231, 255), stop:1 rgba(159, 159, 159, 255));\n"
"\n"
"")
        self.table.setFrameShape(QFrame.StyledPanel)
        self.table.setIconSize(QSize(0, 0))
        self.table.setTextElideMode(Qt.ElideLeft)
        self.table.horizontalHeader().setMinimumSectionSize(40)

        self.retranslateUi(library)

        QMetaObject.connectSlotsByName(library)
    # setupUi

    def retranslateUi(self, library):
        library.setWindowTitle(QCoreApplication.translate("library", u"Form", None))
        ___qtablewidgetitem = self.table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("library", u"Category", None));
        ___qtablewidgetitem1 = self.table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("library", u"Name", None));
        ___qtablewidgetitem2 = self.table.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("library", u"Password", None));
    # retranslateUi

