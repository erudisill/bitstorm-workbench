'''
Created on Jan 5, 2015

@author: ericrudisill
'''
import socket
from MessageAsciiFactory import MessageAsciiFactory
from PyQt4 import QtCore
from PyQt4.Qt import pyqtSignal
from BleMessageAscii import BleMessageAscii
from copy import copy

class BsClient(QtCore.QThread):
    
    HOST, PORT = "localhost", 1337
    
    received = pyqtSignal(BleMessageAscii)

    def __init__(self, ip, port):
        super(BsClient, self).__init__()
        self.ip = ip
        self.port = port

    def run(self):
        print "BsClient running"
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((self.ip, self.port))
        maf = MessageAsciiFactory()
        try:
            while True:
                response = sock.recv(1024)
                if not response: 
                    break
                records = maf.receive(response)
                for r in records:
                    self.received.emit(copy(r))
                        
        except Exception as ex:
            print "BsClient exception: " + str(ex)
            pass
        finally:
            print "BsClient exiting"
            try:
                sock.close()
            except Exception:
                # socket may already be closed, so just ignore
                pass        