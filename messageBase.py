'''
Created on Jan 21, 2015

@author: ericrudisill
'''
import time

class MessageBase(object):

    def __init__(self):
        self.mac = "0000000000000000"
        self.rssi = 0
        self.rssi_dec = 0
        self.temp = 0
        self.batt = 0
        self.batt_hex = "0000"
        self.cs = 0
        self.ts = time.time()
     
    def __str__(self):
        return "M:{0} R:{1:02X} T:{2:04X} B:{3:04X} C:{4:02X} TS:{5}". \
                format(self.mac, self.rssi, self.temp, self.batt, self.cs, self.ts)