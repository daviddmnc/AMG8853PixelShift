# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'configDialog.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QGridLayout,
    QLabel, QPushButton, QSizePolicy, QSpacerItem,
    QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(300, 300)
        Dialog.setMinimumSize(QSize(300, 300))
        Dialog.setFocusPolicy(Qt.StrongFocus)
        Dialog.setWindowTitle(u"Config")
        Dialog.setSizeGripEnabled(False)
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.StopBit = QLabel(Dialog)
        self.StopBit.setObjectName(u"StopBit")
        self.StopBit.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.StopBit, 4, 0, 1, 1)

        self.BaudBox = QComboBox(Dialog)
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

        self.gridLayout.addWidget(self.BaudBox, 1, 1, 1, 1)

        self.verticalSpacer = QSpacerItem(10, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer, 5, 1, 1, 1)

        self.ParityBox = QComboBox(Dialog)
        self.ParityBox.addItem("")
        self.ParityBox.setObjectName(u"ParityBox")

        self.gridLayout.addWidget(self.ParityBox, 3, 1, 1, 1)

        self.BaudRate = QLabel(Dialog)
        self.BaudRate.setObjectName(u"BaudRate")
        self.BaudRate.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.BaudRate, 1, 0, 1, 1)

        self.Parity = QLabel(Dialog)
        self.Parity.setObjectName(u"Parity")
        self.Parity.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.Parity, 3, 0, 1, 1)

        self.pushButton = QPushButton(Dialog)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout.addWidget(self.pushButton, 7, 1, 1, 1)

        self.COMPortBox = QComboBox(Dialog)
        self.COMPortBox.setObjectName(u"COMPortBox")

        self.gridLayout.addWidget(self.COMPortBox, 0, 1, 1, 1)

        self.COMPort = QLabel(Dialog)
        self.COMPort.setObjectName(u"COMPort")
        self.COMPort.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.COMPort, 0, 0, 1, 1)

        self.StopBox = QComboBox(Dialog)
        self.StopBox.addItem("")
        self.StopBox.addItem("")
        self.StopBox.addItem("")
        self.StopBox.setObjectName(u"StopBox")

        self.gridLayout.addWidget(self.StopBox, 4, 1, 1, 1)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        self.StopBit.setText(QCoreApplication.translate("Dialog", u"Stop Bit", None))
        self.BaudBox.setItemText(0, QCoreApplication.translate("Dialog", u"600", None))
        self.BaudBox.setItemText(1, QCoreApplication.translate("Dialog", u"1200", None))
        self.BaudBox.setItemText(2, QCoreApplication.translate("Dialog", u"2400", None))
        self.BaudBox.setItemText(3, QCoreApplication.translate("Dialog", u"4800", None))
        self.BaudBox.setItemText(4, QCoreApplication.translate("Dialog", u"9600", None))
        self.BaudBox.setItemText(5, QCoreApplication.translate("Dialog", u"14400", None))
        self.BaudBox.setItemText(6, QCoreApplication.translate("Dialog", u"19200", None))
        self.BaudBox.setItemText(7, QCoreApplication.translate("Dialog", u"28800", None))
        self.BaudBox.setItemText(8, QCoreApplication.translate("Dialog", u"31250", None))
        self.BaudBox.setItemText(9, QCoreApplication.translate("Dialog", u"57600", None))
        self.BaudBox.setItemText(10, QCoreApplication.translate("Dialog", u"115200", None))

        self.BaudBox.setCurrentText(QCoreApplication.translate("Dialog", u"9600", None))
        self.ParityBox.setItemText(0, QCoreApplication.translate("Dialog", u"None", None))

        self.BaudRate.setText(QCoreApplication.translate("Dialog", u"Baud Rate", None))
        self.Parity.setText(QCoreApplication.translate("Dialog", u"Parity", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"OK", None))
        self.COMPort.setText(QCoreApplication.translate("Dialog", u"COM Port", None))
        self.StopBox.setItemText(0, QCoreApplication.translate("Dialog", u"1", None))
        self.StopBox.setItemText(1, QCoreApplication.translate("Dialog", u"1.5", None))
        self.StopBox.setItemText(2, QCoreApplication.translate("Dialog", u"2", None))

        pass
    # retranslateUi

