'''
Created on Dec 30, 2014

@author: ericrudisill
'''
from ui.MacListWidget import Ui_MacListWidget
from PyQt4 import QtGui
import time
from PyQt4.Qt import QTimer, pyqtSignal
from Device import Device

class MacListWidget(QtGui.QWidget, Ui_MacListWidget):
    
    activeStateChanged = pyqtSignal(int, Device)
    
    def __init__(self, device, parent = None):
        super(MacListWidget, self).__init__(parent)
        self.setupUi(self)
        
        self._cancelEmit = False
        
        self.device = device
        self.device.dataChanged.connect(self.refresh)
        self.refresh()
        self.lastUpdate = time.time()
        
        self.checkActive.stateChanged.connect(self.activeStateChangedEmit)
        
        self.timer = QTimer();
        self.timer.timeout.connect(self.updateAge)
        self.timer.start(1000)
        
    def refresh(self):
        self.labelMac.setText("{0}".format(self.device.mac))
        self.labelRSSI.setText("{0} dB".format(self.device.rssi))
        self.labelBatt.setText("{0:04X} {1:0.2f} V".format(self.device.batt,self.device.volts))
        self.labelCount.setText("{0}".format(self.device.count))
        self.labelAge.setText("--")
        self.lastUpdate = time.time()
        
    def updateAge(self):
        age = time.time() - self.lastUpdate     
        self.labelAge.setText("{0:0.0f} s".format(age))
        
    def activeStateChangedEmit(self, newState):
        if self._cancelEmit == False:
            self.activeStateChanged.emit(newState, self.device)
        
    def isActive(self):
        return self.checkActive.isChecked()
    
    def setActiveState(self, newState, cancelEmit = False):
        self._cancelEmit = cancelEmit
        self.checkActive.setCheckState(newState)
        self._cancelEmit = False
