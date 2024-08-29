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
from PySide6.QtWidgets import (QApplication, QComboBox, QFormLayout, QFrame,
    QGridLayout, QHBoxLayout, QLabel, QLayout,
    QMainWindow, QProgressBar, QPushButton, QSizePolicy,
    QSpacerItem, QStatusBar, QTextEdit, QVBoxLayout,
    QWidget)

class Ui_GridEyeTerminal(object):
    def setupUi(self, GridEyeTerminal):
        if not GridEyeTerminal.objectName():
            GridEyeTerminal.setObjectName(u"GridEyeTerminal")
        GridEyeTerminal.resize(500, 800)
        self.actionSettings = QAction(GridEyeTerminal)
        self.actionSettings.setObjectName(u"actionSettings")
        self.actionStart_Com = QAction(GridEyeTerminal)
        self.actionStart_Com.setObjectName(u"actionStart_Com")
        self.actionStop_Com = QAction(GridEyeTerminal)
        self.actionStop_Com.setObjectName(u"actionStop_Com")
        self.centralwidget = QWidget(GridEyeTerminal)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setEnabled(True)
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout_3.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.ComPort = QLabel(self.centralwidget)
        self.ComPort.setObjectName(u"ComPort")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.ComPort)

        self.COMPortBox = QComboBox(self.centralwidget)
        self.COMPortBox.setObjectName(u"COMPortBox")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.COMPortBox)

        self.BaudRate = QLabel(self.centralwidget)
        self.BaudRate.setObjectName(u"BaudRate")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.BaudRate)

        self.BaudBox = QComboBox(self.centralwidget)
        self.BaudBox.addItem("")
        self.BaudBox.addItem("")
        self.BaudBox.addItem("")
        self.BaudBox.addItem("")
        self.BaudBox.addItem("")
        self.BaudBox.addItem("")
        self.BaudBox.addItem("")
        self.BaudBox.addItem("")
        self.BaudBox.addItem("")
        self.BaudBox.addItem("")
        self.BaudBox.addItem("")
        self.BaudBox.setObjectName(u"BaudBox")
        self.BaudBox.setLayoutDirection(Qt.LeftToRight)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.BaudBox)


        self.horizontalLayout.addLayout(self.formLayout)

        self.horizontalSpacer = QSpacerItem(13, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.StatusText = QLabel(self.centralwidget)
        self.StatusText.setObjectName(u"StatusText")
        font = QFont()
        font.setBold(False)
        self.StatusText.setFont(font)
        self.StatusText.setFrameShape(QFrame.Box)
        self.StatusText.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.StatusText)

        self.ProgressBar = QProgressBar(self.centralwidget)
        self.ProgressBar.setObjectName(u"ProgressBar")
        self.ProgressBar.setValue(100)
        self.ProgressBar.setTextVisible(False)
        self.ProgressBar.setOrientation(Qt.Horizontal)

        self.verticalLayout.addWidget(self.ProgressBar)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.StartComButton = QPushButton(self.centralwidget)
        self.StartComButton.setObjectName(u"StartComButton")

        self.verticalLayout_2.addWidget(self.StartComButton)

        self.StopComButton = QPushButton(self.centralwidget)
        self.StopComButton.setObjectName(u"StopComButton")

        self.verticalLayout_2.addWidget(self.StopComButton)


        self.horizontalLayout.addLayout(self.verticalLayout_2)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.textEdit = QTextEdit(self.centralwidget)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setReadOnly(True)

        self.verticalLayout_3.addWidget(self.textEdit)


        self.gridLayout.addLayout(self.verticalLayout_3, 0, 0, 1, 1)

        GridEyeTerminal.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(GridEyeTerminal)
        self.statusbar.setObjectName(u"statusbar")
        GridEyeTerminal.setStatusBar(self.statusbar)

        self.retranslateUi(GridEyeTerminal)

        QMetaObject.connectSlotsByName(GridEyeTerminal)
    # setupUi

    def retranslateUi(self, GridEyeTerminal):
        GridEyeTerminal.setWindowTitle(QCoreApplication.translate("GridEyeTerminal", u"Grid-Eye Terminal", None))
        self.actionSettings.setText(QCoreApplication.translate("GridEyeTerminal", u"Settings", None))
        self.actionStart_Com.setText(QCoreApplication.translate("GridEyeTerminal", u"Start Com", None))
        self.actionStop_Com.setText(QCoreApplication.translate("GridEyeTerminal", u"Stop Com", None))
        self.ComPort.setText(QCoreApplication.translate("GridEyeTerminal", u"COM Port:", None))
        self.BaudRate.setText(QCoreApplication.translate("GridEyeTerminal", u"Baud Rate:", None))
        self.BaudBox.setItemText(0, QCoreApplication.translate("GridEyeTerminal", u"600", None))
        self.BaudBox.setItemText(1, QCoreApplication.translate("GridEyeTerminal", u"1200", None))
        self.BaudBox.setItemText(2, QCoreApplication.translate("GridEyeTerminal", u"2400", None))
        self.BaudBox.setItemText(3, QCoreApplication.translate("GridEyeTerminal", u"4800", None))
        self.BaudBox.setItemText(4, QCoreApplication.translate("GridEyeTerminal", u"9600", None))
        self.BaudBox.setItemText(5, QCoreApplication.translate("GridEyeTerminal", u"14400", None))
        self.BaudBox.setItemText(6, QCoreApplication.translate("GridEyeTerminal", u"19200", None))
        self.BaudBox.setItemText(7, QCoreApplication.translate("GridEyeTerminal", u"28800", None))
        self.BaudBox.setItemText(8, QCoreApplication.translate("GridEyeTerminal", u"31250", None))
        self.BaudBox.setItemText(9, QCoreApplication.translate("GridEyeTerminal", u"57600", None))
        self.BaudBox.setItemText(10, QCoreApplication.translate("GridEyeTerminal", u"115200", None))

        self.BaudBox.setCurrentText(QCoreApplication.translate("GridEyeTerminal", u"600", None))
        self.StatusText.setText(QCoreApplication.translate("GridEyeTerminal", u"TextLabel", None))
        self.ProgressBar.setFormat(QCoreApplication.translate("GridEyeTerminal", u"%p%", None))
        self.StartComButton.setText(QCoreApplication.translate("GridEyeTerminal", u"Start COM", None))
        self.StopComButton.setText(QCoreApplication.translate("GridEyeTerminal", u"STOP", None))
    # retranslateUi

