'''
Created on Jan 5, 2015

@author: ericrudisill
'''
from PyQt4.Qt import QObject, pyqtSignal
import time

class DeviceHistory(object):
    def __init__(self):
        self.ts = time.time()
        self.rssi = 0
        self.batt = 0
        self.volts = 0.0

class Device(QObject):

    dataChanged = pyqtSignal(object)

    def __init__(self, parent=None):
        super(Device, self).__init__(parent)
        self.mac = "0000000000000000"
        self.rssi = 0
        self.batt = 0
        self.volts = 0.0
        self.count = 0
        self.history = []
        
    def update(self):
        self.volts = ((3 * (self.batt >> 4) * 1.24) / 2048)
        h = DeviceHistory()
        h.rssi = self.rssi
        h.batt = self.batt
        h.volts = self.volts
        self.history.append(h)
        self.dataChanged.emit(self)
