'''
Created on Dec 30, 2014

@author: ericrudisill
'''
from ui.MacListWidget import Ui_MacListWidget
from PyQt4 import QtGui

class MacListWidget(QtGui.QWidget, Ui_MacListWidget):
    def __init__(self, device, parent = None):
        super(MacListWidget, self).__init__(parent)
        self.setupUi(self)
        self.device = device
        self.device.observe(self.refresh)
        self.refresh(self.device)
    
    def refresh(self, device = None):
        self.setMac(self.device.mac)
        self.setRSSI(self.device.rssi)
        self.setBatt(self.device.batt)
    
    def setMac(self, mac):
        self.labelMac.setText("{0}".format(mac))
        
    def setRSSI(self, rssi):
        self.labelRSSI.setText("{0}".format(rssi))
        
    def setBatt(self, batt):
        self.labelBatt.setText("{0}".format(batt))