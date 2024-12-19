import sys
##from typing import Optional
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QFrame, QGridLayout
from PySide6.QtCore import Qt,QThread,Signal
from serial import Serial
from guiShift_ui import *
from configDialoggui import *
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure
from matplotlib.axes import Axes
import numpy as np


class MplCanvas(FigureCanvasQTAgg):
    def __init__(self, width = 8, height = 8, dpi = 60):
        figure = Figure(figsize=(width,height),dpi=dpi)
        self.axes = figure.add_subplot(111) 
        self.zdata = np.array(np.array_split([0]*64, 8))
        self.axes.cla()
        self.axes.imshow(self.zdata)
        self.axes.set_title("Waiting for data...", fontsize = "15")
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
        self.ui.textEdit.setVisible(False)
        ##self.ui.StatusText.setStyleSheet("color: darkgreen")
        ##self.ui.actionSettings.triggered.connect(self.config)
        ##self.ui.actionStart_Com.triggered.connect(self.open_Com)
        ##self.ui.actionStop_Com.triggered.connect(self.close_Com)
        self.ui.StartComButton.pressed.connect(self.open_Com)
        self.ui.StopComButton.pressed.connect(self.close_Com)
        self.ui.checkBox.stateChanged.connect(self.display_Raw_Data)
        self.ui.pushButton_2.pressed.connect(self.combine_images)
        
        self.canvas = MplCanvas()
        self.canvas2 = MplCanvas()
        self.canvas3 = MplCanvas()
        self.canvas4 = MplCanvas()
        self.canvasFin = MplCanvas()
        self.mpl = QGridLayout() #make a grid
        self.mpl2 = QGridLayout()
        self.mpl3 = QGridLayout()
        self.mpl4 = QGridLayout()
        self.mplfin = QGridLayout()
        
        self.mpl.addWidget(self.canvas) #add the canvas figure to the grid
        self.mpl2.addWidget(self.canvas2)
        self.mpl3.addWidget(self.canvas3)
        self.mpl4.addWidget(self.canvas4)
        self.mplfin.addWidget(self.canvasFin)
        
        self.ui.frame_1.setLayout(self.mpl) ## add the graph to the vertical layout
        self.ui.frame_2.setLayout(self.mpl2)
        self.ui.frame_3.setLayout(self.mpl3)
        self.ui.frame_4.setLayout(self.mpl4)
        self.ui.frameFinal.setLayout(self.mplfin)
        
        self.zdata = np.array(np.array_split([0]*64, 8))
        
        
        ##self.canvas.axes.set_title("Waiting for COM data...", fontsize = "20")
        ##
        
        self.ui.textEdit.append('Standby...')
        global passx 
        passx = 1
        global image1
        image1 = np.array(np.array_split([0]*64, 8)) 
        global image2 
        image2 = np.array(np.array_split([0]*64, 8)) 
        global image3
        image3 = np.array(np.array_split([0]*64, 8)) 
        global image4
        image4 = np.array(np.array_split([0]*64, 8)) 
           
    def open_Com(self):
        self.returnVal['com_port']=self.ui.COMPortBox.currentText()
        self.returnVal['baud_rate']=int(self.ui.BaudBox.currentText())
        self.tr = Worker(self.returnVal)
        ##self.tr.change_value.connect(self.print_data)
        self.tr.change_value.connect(self.update_graph)
        ##self.tr.error.connect(self.error)
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
        global passx
        global image1
        global image2
        global image3
        global image4
        """
        self.zdata = np.array([[0.8, 2.4, 2.5, 3.9, 0.0, 4.0, 0.0, 2.5],
                                [2.4, 0.0, 4.0, 1.0, 2.7, 0.0, 0.0, 4.0],
                                [1.1, 2.4, 0.8, 4.3, 1.9, 4.4, 0.0, 1.0],
                                [0.6, 0.0, 0.3, 0.0, 3.1, 0.0, 0.0, 2.0],
                                [0.7, 1.7, 0.6, 2.6, 2.2, 6.2, 0.0, 22.0],
                                [1.3, 1.2, 0.0, 0.0, 0.0, 3.2, 5.1, 2.0],
                                [0.1, 2.0, 0.0, 1.4, 0.0, 1.9, 6.3, 2.0],
                                [1,2,3,4,1,2,3,4]])
        """
        rawdata = str(data)
        rawdata = rawdata.split(',')
        floatdata = np.asarray(rawdata, dtype=float)
        ##self.ui.textEdit.append(str(passx))
        self.ui.textEdit.append(str(rawdata))
        ##for i in rawdata:
        ##    i= float(i)
        ##rawdata = [int(i) for i in rawdata]
        if passx==1:
            self.canvas = self.canvas
        elif passx==2:
            self.canvas = self.canvas2
        elif passx==3:
            self.canvas = self.canvas3
        elif passx==4:
            self.canvas = self.canvas4
            
        self.canvas.axes.cla()
        self.zdata = np.array(np.array_split(floatdata,8))
        
        
        ##Saving the matrices
        if passx==1:
            image1 = self.zdata
        elif passx==2:
            image2 = self.zdata
        elif passx==3:
            image3 = self.zdata
        elif passx==4:
            image4 = self.zdata
        
        
        
        
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
                ##print(self.zdata[i,j])
                text = self.canvas.axes.text(j,i,self.zdata[i,j], fontsize="15" , ha="center", va="center", color="w")
        
        self.canvas.axes.set_title(str("Displaying image:"+str(passx)), fontsize = "15")
        
        
        ##adding values to boxes
       
        
        self.canvas.axes.set_box_aspect(1)
        self.canvas.draw()
        
        passx=passx+1
        if passx == 5:
            passx = 1
        
    def display_Raw_Data(self):
        if self.ui.checkBox.isChecked():
            self.ui.textEdit.setVisible(True)
        else:
            self.ui.textEdit.setVisible(False)

    def combine_images(self):
        if image4.all() != 0:
            PixelShifted = np.array(np.array_split([0]*256,16))
            l = 16 #matrice size
            for i in range(0,l,2):
                for j in range(0,l,2):
                    k = i//2
                    n = j//2
                    PixelShifted[i,j] = image1[k,n]
                    PixelShifted[i,j+1] = image2[k,n]
                    PixelShifted[i+1,j] = image3[k,n]
                    PixelShifted[i+1,j+1] = image4[k,n]
            self.canvasFin.axes.cla()
            self.canvasFin.axes.imshow(PixelShifted)
            self.canvasFin.axes.set_box_aspect(1)
            self.canvasFin.draw()
            
        else:
            self.ui.textEdit.append("Not enough Images generated!!")
            return
        
        
        
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

