'''
Created on Dec 30, 2014

@author: ericrudisill
'''
from ui.MacListWidget import Ui_MacListWidget
from PyQt4 import QtGui

class MacListWidget(QtGui.QWidget, Ui_MacListWidget):
    def __init__(self, parent = None):
        super(MacListWidget, self).__init__(parent)
        self.setupUi(self)
    
    def setMac(self, mac):
        self.labelMac.setText(mac)
        
    def setRSSI(self, rssi):
        self.labelRSSI.setText(rssi)
        
    def setBatt(self, batt):
        self.labelBatt.setText(batt)