'''
Created on Dec 30, 2014

@author: ericrudisill
'''
from ui.MacListWidget import Ui_MacListWidget
from PyQt4 import QtGui
import time
from PyQt4.Qt import QTimer

class MacListWidget(QtGui.QWidget, Ui_MacListWidget):
    def __init__(self, device, parent = None):
        super(MacListWidget, self).__init__(parent)
        self.setupUi(self)
        self.device = device
        self.device.observe(self.refresh)
        self.refresh(self.device)
        self.lastUpdate = time.time()
        
        self.timer = QTimer();
        self.timer.timeout.connect(self.updateAge)
        self.timer.start(1000)
    
    def refresh(self, device = None):
        self.labelMac.setText("{0}".format(self.device.mac))
        self.labelRSSI.setText("{0} dB".format(self.device.rssi))
        self.labelBatt.setText("{0:04X} {1:0.2f} V".format(self.device.batt,self.device.volts))
        self.labelAge.setText("--")
        self.lastUpdate = time.time()
        
    def updateAge(self):
        age = time.time() - self.lastUpdate     
        self.labelAge.setText("{0:0.0f} s".format(age))
