'''
Created on Jan 5, 2015

@author: ericrudisill
'''

class Device(object):

    def __init__(self):
        self.mac = "0000000000000000"
        self.rssi = 0
        self.batt = 0
        self.volts = 0.0
        self.count = 0
        self.observers = []
        
    def observe(self, callback):
        self.observers.append(callback)
        
    def update(self):
        # string volts = ((3 * (d.lastMessage.battery >> 4) * 1.24) / 2048).ToString("0.00 V");
        self.volts = ((3 * (self.batt >> 4) * 1.24) / 2048)
        for c in self.observers:
            c(self)