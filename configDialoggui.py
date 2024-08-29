from PySide6.QtWidgets import QDialog
from configDialog import *
from serial.tools import list_ports
import serial

class ConfDiag(QDialog):
    def __init__(self):
        super().__init__()
        self.dialog = Ui_Dialog()
        self.dialog.setupUi(self)
        self.dialog.BaudBox.setCurrentIndex(4)
        a = list_ports.comports()
        for i in a:
            self.dialog.COMPortBox.addItem(str(i.device))
        self.returnVal = {}
        
    def get_data(self):
        self.returnVal['com_port']=self.dialog.COMPortBox.currentText()
        self.returnVal['baud_rate']=int(self.dialog.BaudBox.currentText())
        
        return self.returnVal