# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'guiShift.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFrame,
    QGridLayout, QHBoxLayout, QLabel, QLayout,
    QMainWindow, QProgressBar, QPushButton, QSizePolicy,
    QTextEdit, QVBoxLayout, QWidget)

class Ui_GridEyeTerminal(object):
    def setupUi(self, GridEyeTerminal):
        if not GridEyeTerminal.objectName():
            GridEyeTerminal.setObjectName(u"GridEyeTerminal")
        GridEyeTerminal.setWindowModality(Qt.NonModal)
        GridEyeTerminal.resize(781, 640)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(GridEyeTerminal.sizePolicy().hasHeightForWidth())
        GridEyeTerminal.setSizePolicy(sizePolicy)
        GridEyeTerminal.setMinimumSize(QSize(780, 640))
        self.actionSettings = QAction(GridEyeTerminal)
        self.actionSettings.setObjectName(u"actionSettings")
        self.actionStart_Com = QAction(GridEyeTerminal)
        self.actionStart_Com.setObjectName(u"actionStart_Com")
        self.actionStop_Com = QAction(GridEyeTerminal)
        self.actionStop_Com.setObjectName(u"actionStop_Com")
        self.actionShowRawData = QAction(GridEyeTerminal)
        self.actionShowRawData.setObjectName(u"actionShowRawData")
        self.actionShowRawData.setCheckable(True)
        self.actionShowRawData.setChecked(True)
        self.actionTakePicture = QAction(GridEyeTerminal)
        self.actionTakePicture.setObjectName(u"actionTakePicture")
        self.actionCombineResults = QAction(GridEyeTerminal)
        self.actionCombineResults.setObjectName(u"actionCombineResults")
        self.centralwidget = QWidget(GridEyeTerminal)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy1)
        self.centralwidget.setMinimumSize(QSize(500, 500))
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(30, 30, 30, 30)
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_5.setContentsMargins(-1, -1, 0, -1)
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setSpacing(8)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.COMPortBox = QComboBox(self.centralwidget)
        self.COMPortBox.setObjectName(u"COMPortBox")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.COMPortBox.sizePolicy().hasHeightForWidth())
        self.COMPortBox.setSizePolicy(sizePolicy2)
        self.COMPortBox.setMinimumSize(QSize(0, 0))

        self.gridLayout_3.addWidget(self.COMPortBox, 0, 1, 1, 1)

        self.ComPort = QLabel(self.centralwidget)
        self.ComPort.setObjectName(u"ComPort")
        self.ComPort.setMinimumSize(QSize(65, 0))

        self.gridLayout_3.addWidget(self.ComPort, 0, 0, 1, 1)

        self.BaudRate = QLabel(self.centralwidget)
        self.BaudRate.setObjectName(u"BaudRate")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.BaudRate.sizePolicy().hasHeightForWidth())
        self.BaudRate.setSizePolicy(sizePolicy3)
        self.BaudRate.setMinimumSize(QSize(65, 0))

        self.gridLayout_3.addWidget(self.BaudRate, 1, 0, 1, 1)

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
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.BaudBox.sizePolicy().hasHeightForWidth())
        self.BaudBox.setSizePolicy(sizePolicy4)
        self.BaudBox.setLayoutDirection(Qt.LeftToRight)

        self.gridLayout_3.addWidget(self.BaudBox, 1, 1, 1, 1)


        self.verticalLayout_3.addLayout(self.gridLayout_3)

        self.checkBox = QCheckBox(self.centralwidget)
        self.checkBox.setObjectName(u"checkBox")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.checkBox.sizePolicy().hasHeightForWidth())
        self.checkBox.setSizePolicy(sizePolicy5)
        self.checkBox.setMinimumSize(QSize(100, 20))
        self.checkBox.setLayoutDirection(Qt.LeftToRight)
        self.checkBox.setIconSize(QSize(24, 24))
        self.checkBox.setChecked(False)

        self.verticalLayout_3.addWidget(self.checkBox)


        self.horizontalLayout_5.addLayout(self.verticalLayout_3)

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


        self.horizontalLayout_5.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.StartComButton = QPushButton(self.centralwidget)
        self.StartComButton.setObjectName(u"StartComButton")

        self.verticalLayout_2.addWidget(self.StartComButton)

        self.StopComButton = QPushButton(self.centralwidget)
        self.StopComButton.setObjectName(u"StopComButton")

        self.verticalLayout_2.addWidget(self.StopComButton)


        self.horizontalLayout_5.addLayout(self.verticalLayout_2)


        self.verticalLayout_5.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame_4 = QFrame(self.centralwidget)
        self.frame_4.setObjectName(u"frame_4")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy6)
        self.frame_4.setMinimumSize(QSize(200, 200))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)

        self.gridLayout.addWidget(self.frame_4, 1, 1, 1, 1)

        self.frame_3 = QFrame(self.centralwidget)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy6.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy6)
        self.frame_3.setMinimumSize(QSize(200, 200))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)

        self.gridLayout.addWidget(self.frame_3, 1, 0, 1, 1)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy6.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy6)
        self.frame_2.setMinimumSize(QSize(200, 200))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)

        self.gridLayout.addWidget(self.frame_2, 0, 1, 1, 1)

        self.frame_1 = QFrame(self.centralwidget)
        self.frame_1.setObjectName(u"frame_1")
        sizePolicy6.setHeightForWidth(self.frame_1.sizePolicy().hasHeightForWidth())
        self.frame_1.setSizePolicy(sizePolicy6)
        self.frame_1.setMinimumSize(QSize(200, 200))
        self.frame_1.setFrameShape(QFrame.StyledPanel)
        self.frame_1.setFrameShadow(QFrame.Raised)

        self.gridLayout.addWidget(self.frame_1, 0, 0, 1, 1)


        self.horizontalLayout_2.addLayout(self.gridLayout)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.frameFinal = QFrame(self.centralwidget)
        self.frameFinal.setObjectName(u"frameFinal")
        sizePolicy6.setHeightForWidth(self.frameFinal.sizePolicy().hasHeightForWidth())
        self.frameFinal.setSizePolicy(sizePolicy6)
        self.frameFinal.setMinimumSize(QSize(300, 300))
        self.frameFinal.setFrameShape(QFrame.StyledPanel)
        self.frameFinal.setFrameShadow(QFrame.Raised)

        self.verticalLayout_13.addWidget(self.frameFinal)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy1.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy1)
        self.pushButton.setMinimumSize(QSize(50, 50))
        self.pushButton.setAutoDefault(False)
        self.pushButton.setFlat(False)

        self.horizontalLayout.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        sizePolicy1.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy1)
        self.pushButton_2.setMinimumSize(QSize(200, 50))

        self.horizontalLayout.addWidget(self.pushButton_2)


        self.verticalLayout_13.addLayout(self.horizontalLayout)


        self.verticalLayout_4.addLayout(self.verticalLayout_13)


        self.horizontalLayout_2.addLayout(self.verticalLayout_4)


        self.verticalLayout_5.addLayout(self.horizontalLayout_2)


        self.gridLayout_2.addLayout(self.verticalLayout_5, 0, 0, 1, 1)

        self.textEdit = QTextEdit(self.centralwidget)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setEnabled(True)
        sizePolicy7 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy7.setHorizontalStretch(200)
        sizePolicy7.setVerticalStretch(200)
        sizePolicy7.setHeightForWidth(self.textEdit.sizePolicy().hasHeightForWidth())
        self.textEdit.setSizePolicy(sizePolicy7)
        self.textEdit.setMinimumSize(QSize(400, 100))
        self.textEdit.setReadOnly(True)

        self.gridLayout_2.addWidget(self.textEdit, 1, 0, 1, 1)

        GridEyeTerminal.setCentralWidget(self.centralwidget)

        self.retranslateUi(GridEyeTerminal)

        self.pushButton.setDefault(False)


        QMetaObject.connectSlotsByName(GridEyeTerminal)
    # setupUi

    def retranslateUi(self, GridEyeTerminal):
        GridEyeTerminal.setWindowTitle(QCoreApplication.translate("GridEyeTerminal", u"Grid-Eye Terminal", None))
        self.actionSettings.setText(QCoreApplication.translate("GridEyeTerminal", u"Settings", None))
        self.actionStart_Com.setText(QCoreApplication.translate("GridEyeTerminal", u"Start Com", None))
        self.actionStop_Com.setText(QCoreApplication.translate("GridEyeTerminal", u"Stop Com", None))
        self.actionShowRawData.setText(QCoreApplication.translate("GridEyeTerminal", u"ShowRawData", None))
        self.actionTakePicture.setText(QCoreApplication.translate("GridEyeTerminal", u"TakePicture", None))
        self.actionCombineResults.setText(QCoreApplication.translate("GridEyeTerminal", u"CombineResults", None))
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
        self.checkBox.setText(QCoreApplication.translate("GridEyeTerminal", u"Show raw data", None))
        self.StatusText.setText(QCoreApplication.translate("GridEyeTerminal", u"TextLabel", None))
        self.ProgressBar.setFormat(QCoreApplication.translate("GridEyeTerminal", u"%p%", None))
        self.StartComButton.setText(QCoreApplication.translate("GridEyeTerminal", u"Start COM", None))
        self.StopComButton.setText(QCoreApplication.translate("GridEyeTerminal", u"STOP", None))
        self.pushButton.setText(QCoreApplication.translate("GridEyeTerminal", u"Take readings", None))
        self.pushButton_2.setText(QCoreApplication.translate("GridEyeTerminal", u"Combine Images", None))
    # retranslateUi

