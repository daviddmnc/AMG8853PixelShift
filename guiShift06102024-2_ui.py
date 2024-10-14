# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'guiShift06102024-2.ui'
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
    QSpacerItem, QTextEdit, QVBoxLayout, QWidget)

from mplwidget import Mplwidget

class Ui_GridEyeTerminal(object):
    def setupUi(self, GridEyeTerminal):
        if not GridEyeTerminal.objectName():
            GridEyeTerminal.setObjectName(u"GridEyeTerminal")
        GridEyeTerminal.setWindowModality(Qt.NonModal)
        GridEyeTerminal.resize(780, 640)
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
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_5.setContentsMargins(-1, -1, 5, -1)
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.ComPort = QLabel(self.centralwidget)
        self.ComPort.setObjectName(u"ComPort")

        self.horizontalLayout_3.addWidget(self.ComPort)

        self.COMPortBox = QComboBox(self.centralwidget)
        self.COMPortBox.setObjectName(u"COMPortBox")

        self.horizontalLayout_3.addWidget(self.COMPortBox)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.BaudRate = QLabel(self.centralwidget)
        self.BaudRate.setObjectName(u"BaudRate")

        self.horizontalLayout_4.addWidget(self.BaudRate)

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

        self.horizontalLayout_4.addWidget(self.BaudBox)


        self.verticalLayout_3.addLayout(self.horizontalLayout_4)

        self.checkBox = QCheckBox(self.centralwidget)
        self.checkBox.setObjectName(u"checkBox")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.checkBox.sizePolicy().hasHeightForWidth())
        self.checkBox.setSizePolicy(sizePolicy2)
        self.checkBox.setMinimumSize(QSize(50, 20))
        self.checkBox.setLayoutDirection(Qt.LeftToRight)
        self.checkBox.setIconSize(QSize(24, 24))
        self.checkBox.setChecked(False)

        self.verticalLayout_3.addWidget(self.checkBox)


        self.horizontalLayout_5.addLayout(self.verticalLayout_3)

        self.horizontalSpacer = QSpacerItem(13, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer)

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
        self.graphicsView = Mplwidget(self.centralwidget)
        self.graphicsView.setObjectName(u"graphicsView")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.graphicsView.sizePolicy().hasHeightForWidth())
        self.graphicsView.setSizePolicy(sizePolicy3)
        self.graphicsView.setMinimumSize(QSize(200, 200))

        self.gridLayout.addWidget(self.graphicsView, 0, 0, 1, 1)

        self.graphicsView_2 = Mplwidget(self.centralwidget)
        self.graphicsView_2.setObjectName(u"graphicsView_2")
        sizePolicy3.setHeightForWidth(self.graphicsView_2.sizePolicy().hasHeightForWidth())
        self.graphicsView_2.setSizePolicy(sizePolicy3)
        self.graphicsView_2.setMinimumSize(QSize(200, 200))

        self.gridLayout.addWidget(self.graphicsView_2, 0, 1, 1, 1)

        self.graphicsView_3 = Mplwidget(self.centralwidget)
        self.graphicsView_3.setObjectName(u"graphicsView_3")
        sizePolicy3.setHeightForWidth(self.graphicsView_3.sizePolicy().hasHeightForWidth())
        self.graphicsView_3.setSizePolicy(sizePolicy3)
        self.graphicsView_3.setMinimumSize(QSize(200, 200))

        self.gridLayout.addWidget(self.graphicsView_3, 1, 0, 1, 1)

        self.graphicsView_4 = Mplwidget(self.centralwidget)
        self.graphicsView_4.setObjectName(u"graphicsView_4")
        sizePolicy3.setHeightForWidth(self.graphicsView_4.sizePolicy().hasHeightForWidth())
        self.graphicsView_4.setSizePolicy(sizePolicy3)
        self.graphicsView_4.setMinimumSize(QSize(200, 200))

        self.gridLayout.addWidget(self.graphicsView_4, 1, 1, 1, 1)


        self.horizontalLayout_2.addLayout(self.gridLayout)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout_13.setContentsMargins(5, 5, 5, 5)
        self.graphicsView_5 = Mplwidget(self.centralwidget)
        self.graphicsView_5.setObjectName(u"graphicsView_5")
        sizePolicy3.setHeightForWidth(self.graphicsView_5.sizePolicy().hasHeightForWidth())
        self.graphicsView_5.setSizePolicy(sizePolicy3)
        self.graphicsView_5.setMinimumSize(QSize(300, 300))

        self.verticalLayout_13.addWidget(self.graphicsView_5)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 5, 0, 5)
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        sizePolicy1.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy1)
        self.pushButton_2.setMinimumSize(QSize(0, 50))

        self.horizontalLayout.addWidget(self.pushButton_2)

        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy1.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy1)
        self.pushButton.setMinimumSize(QSize(200, 50))

        self.horizontalLayout.addWidget(self.pushButton)


        self.verticalLayout_13.addLayout(self.horizontalLayout)


        self.verticalLayout_4.addLayout(self.verticalLayout_13)


        self.horizontalLayout_2.addLayout(self.verticalLayout_4)


        self.verticalLayout_5.addLayout(self.horizontalLayout_2)


        self.gridLayout_2.addLayout(self.verticalLayout_5, 0, 0, 1, 1)

        self.textEdit = QTextEdit(self.centralwidget)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setEnabled(True)
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy4.setHorizontalStretch(200)
        sizePolicy4.setVerticalStretch(200)
        sizePolicy4.setHeightForWidth(self.textEdit.sizePolicy().hasHeightForWidth())
        self.textEdit.setSizePolicy(sizePolicy4)
        self.textEdit.setMinimumSize(QSize(400, 100))
        self.textEdit.setReadOnly(True)

        self.gridLayout_2.addWidget(self.textEdit, 1, 0, 1, 1)

        GridEyeTerminal.setCentralWidget(self.centralwidget)

        self.retranslateUi(GridEyeTerminal)

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
        self.pushButton_2.setText(QCoreApplication.translate("GridEyeTerminal", u"Take image", None))
        self.pushButton.setText(QCoreApplication.translate("GridEyeTerminal", u"Combine results", None))
    # retranslateUi

