'''
Created on Jan 5, 2015

@author: ericrudisill
'''

class Device(object):

    def __init__(self):
        self.mac = "0000000000000000"
        self.rssi = 0
        self.batt = 0
        self.count = 0
        self.observers = []
        
    def observe(self, callback):
        self.observers.append(callback)
        
    def update(self):
        for c in self.observers:
            c(self)