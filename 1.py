import sys
##from typing import Optional
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QFrame, QGridLayout
from PySide6.QtCore import Qt,QThread,Signal
from serial import Serial
from gui3 import *
from configDialoggui import *
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure
from matplotlib.axes import Axes
import numpy as np



class MplCanvas(FigureCanvasQTAgg):
    def __init__(self, width = 8, height = 8, dpi = 60):
        figure = Figure(figsize=(width,height),dpi=dpi)
        self.axes = figure.add_subplot(111) 
        super(MplCanvas, self).__init__(figure)
        

class MyForm(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_GridEyeTerminal()
        self.ui.setupUi(self)
        self.returnVal = None
        self.ui.BaudBox.setCurrentIndex(4)
        a = list_ports.comports()
        for i in a:
            self.ui.COMPortBox.addItem(str(i.device))
        self.returnVal = {}
        self.ui.StatusText.setText('COM is closed, please select port and baud rate.')
        self.ui.StatusText.setFrameStyle(QFrame.Box | QFrame.Sunken)
        self.ui.ProgressBar.setValue(0)
        self.ui.ProgressBar.setMinimum(0)
        self.ui.ProgressBar.setMaximum(1)
        self.ui.StopComButton.setEnabled(0)
        self.ui.StartComButton.setEnabled(1)
        ##self.ui.StatusText.setStyleSheet("color: darkgreen")
        ##self.ui.actionSettings.triggered.connect(self.config)
        ##self.ui.actionStart_Com.triggered.connect(self.open_Com)
        ##self.ui.actionStop_Com.triggered.connect(self.close_Com)
        self.ui.StartComButton.pressed.connect(self.open_Com)
        self.ui.StopComButton.pressed.connect(self.close_Com)
        
        self.canvas = MplCanvas()
        self.mpl = QGridLayout() #make a grid
        self.mpl.addWidget(self.canvas) #add the canvas figure to the grid
        self.ui.verticalLayout_3.addLayout(self.mpl) ## add the graph to the vertical layout
        self.zdata = np.array(np.array_split([0]*64, 8))
        self.canvas.axes.cla()
        self.canvas.axes.imshow(self.zdata)
        self.canvas.axes.set_title("Waiting for COM data...", fontsize = "20")
        ##
        
        self.ui.textEdit.append('Standby...')
        
    def open_Com(self):
        self.returnVal['com_port']=self.ui.COMPortBox.currentText()
        self.returnVal['baud_rate']=int(self.ui.BaudBox.currentText())
        self.tr = Worker(self.returnVal)
        self.tr.change_value.connect(self.print_data)
        self.tr.change_value.connect(self.update_graph)
        self.tr.error.connect(self.error)
        self.tr.start()
        self.ui.StatusText.setText(('Connected to '+self.returnVal['com_port']+'   Band rate: '+self.ui.BaudBox.currentText()))
        self.ui.StatusText.setStyleSheet("color: lightgreen; background-color: green")
        self.ui.ProgressBar.setMaximum(0)
        self.ui.StartComButton.setEnabled(0)
        self.ui.StopComButton.setEnabled(1)
        
    def close_Com(self):
        self.tr.exit()
        self.ui.StatusText.setText('COM port disconnected. Waiting for input...')
        self.ui.StatusText.setStyleSheet("color: black; background-color: yellow")
        self.ui.ProgressBar.setMaximum(1)
        self.ui.StopComButton.setEnabled(0)
        self.ui.StartComButton.setEnabled(1)
    
    def error(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Icon.Critical)
        msg.setText('Error')
        msg.setInformativeText('Unable to establish connection')
        msg.setWindowTitle('Error')
        msg.exec()

    def print_data(self,data):
        self.ui.textEdit.append(data)
        
    def update_graph(self,data):
        self.zdata = np.array([[0.8, 2.4, 2.5, 3.9, 0.0, 4.0, 0.0, 2.5],
                                [2.4, 0.0, 4.0, 1.0, 2.7, 0.0, 0.0, 4.0],
                                [1.1, 2.4, 0.8, 4.3, 1.9, 4.4, 0.0, 1.0],
                                [0.6, 0.0, 0.3, 0.0, 3.1, 0.0, 0.0, 2.0],
                                [0.7, 1.7, 0.6, 2.6, 2.2, 6.2, 0.0, 22.0],
                                [1.3, 1.2, 0.0, 0.0, 0.0, 3.2, 5.1, 2.0],
                                [0.1, 2.0, 0.0, 1.4, 0.0, 1.9, 6.3, 2.0],
                                [1,2,3,4,1,2,3,4]])
        rawdata = str(data)
        rawdata = rawdata.split(',')
        floatdata = np.asarray(rawdata, dtype=float)
        
        ##for i in rawdata:
        ##    i= float(i)
        ##rawdata = [int(i) for i in rawdata]
        self.canvas.axes.cla()
        self.zdata = np.array(np.array_split(floatdata,8))
        
        self.canvas.axes.imshow(self.zdata)
        ##try:
           ## rawdata = str(data)
           ## rawdata = rawdata.split(',')
           ## rawdata = [int(i) for i in rawdata]
          ##  (rawdata)
          ##  self.zdata = np.array(np.array_split(rawdata,8))
          ##  self.canvas.axes.imshow(self.zdata)
        ##except:
          ##  self.zdata = np.array(np.array_split([0]*64, 8))
        
        
        
        ##self.canvas.axes.cla()
        ##self.canvas.axes.imshow(self.zdata,data=float)
        l = range(8)
        for i in l:
            for j in l:
                print(self.zdata[i,j])
                text = self.canvas.axes.text(j,i,self.zdata[i,j], fontsize="15" , ha="center", va="center", color="w")
        
        self.canvas.axes.set_title("Displaying Graphical data", fontsize = "20")
        
        
        ##adding values to boxes
       
        
        self.canvas.axes.set_box_aspect(1)
        self.canvas.draw()
        
class Worker(QThread):
    change_value = Signal(str)
    error = Signal()
    
    def __init__(self, com_data):
        super().__init__()
        self.data = com_data
        self.com_port = com_data['com_port']
        self.baud_rate = com_data['baud_rate']
        
    def run(self):
        
        data = ''
        self.s= serial.Serial(self.com_port,self.baud_rate)
        while(self.s.is_open):
            try:
                data = self.s.readline().decode().rstrip()
                ##data = data.rstrip('\n')
                self.change_value.emit(data)
            except:
                self.error.emit()
                
    def exit(self):
        self.terminate()
        if self.s.is_open:
            self.s.close()
        
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec())