# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'gui.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QMainWindow, QMenu,
    QMenuBar, QSizePolicy, QStatusBar, QTextEdit,
    QWidget)

class Ui_GridEyeTerminal(object):
    def setupUi(self, GridEyeTerminal):
        if not GridEyeTerminal.objectName():
            GridEyeTerminal.setObjectName(u"GridEyeTerminal")
        GridEyeTerminal.resize(957, 704)
        self.actionSettings = QAction(GridEyeTerminal)
        self.actionSettings.setObjectName(u"actionSettings")
        self.actionStart_Com = QAction(GridEyeTerminal)
        self.actionStart_Com.setObjectName(u"actionStart_Com")
        self.actionStop_Com = QAction(GridEyeTerminal)
        self.actionStop_Com.setObjectName(u"actionStop_Com")
        self.centralwidget = QWidget(GridEyeTerminal)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.textEdit = QTextEdit(self.centralwidget)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setReadOnly(True)

        self.gridLayout.addWidget(self.textEdit, 0, 0, 1, 1)

        GridEyeTerminal.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(GridEyeTerminal)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 957, 21))
        self.menuI2C = QMenu(self.menubar)
        self.menuI2C.setObjectName(u"menuI2C")
        GridEyeTerminal.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(GridEyeTerminal)
        self.statusbar.setObjectName(u"statusbar")
        GridEyeTerminal.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuI2C.menuAction())
        self.menuI2C.addAction(self.actionSettings)
        self.menuI2C.addAction(self.actionStart_Com)
        self.menuI2C.addAction(self.actionStop_Com)

        self.retranslateUi(GridEyeTerminal)

        QMetaObject.connectSlotsByName(GridEyeTerminal)
    # setupUi

    def retranslateUi(self, GridEyeTerminal):
        GridEyeTerminal.setWindowTitle(QCoreApplication.translate("GridEyeTerminal", u"Grid-Eye Terminal", None))
        self.actionSettings.setText(QCoreApplication.translate("GridEyeTerminal", u"Settings", None))
        self.actionStart_Com.setText(QCoreApplication.translate("GridEyeTerminal", u"Start Com", None))
        self.actionStop_Com.setText(QCoreApplication.translate("GridEyeTerminal", u"Stop Com", None))
        self.menuI2C.setTitle(QCoreApplication.translate("GridEyeTerminal", u"I2C", None))
    # retranslateUi

