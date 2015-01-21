'''
Created on Jan 5, 2015

@author: ericrudisill
'''
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QT as NavigationToolbar
from PyQt4.Qt import  QWidget
from PyQt4 import QtGui
import random

class PlotWindow(QWidget):

    def __init__(self, parent=None, devices=None):
        super(PlotWindow, self).__init__(parent)
        
        # matplotlib stuff
        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        self.toolbar = NavigationToolbar(self.canvas, self)
        self.plot_layout = QtGui.QVBoxLayout()
        self.plot_layout.addWidget(self.toolbar)
        self.plot_layout.addWidget(self.canvas)
        
        self.setLayout(self.plot_layout)
        
        self.devices = []
        if not devices is None:
            for d in devices:
                self.addDevice(d)
        
#        self.updatePlot()

    def addDevice(self, device):
        if device not in self.devices:
            self.devices.append(device)
            device.dataChanged.connect(self.updateDevice)
        print "addDevice - new list:"
        for d in self.devices:
            print d.mac
        
    def removeDevice(self, device):
        try:
            self.devices.remove(device)
            device.dataChanged.disconnect(self.updateDevice)
        except Exception:
            pass
        print "removeDevice - new list:"
        for d in self.devices:
            print d.mac
            
    def updateDevice(self, device):
        self.data_x = []
        for d in self.devices:
            x = []
            for b in d.history:
                x.append(b.rssi)
            self.data_x.append(x)
        self.updatePlot()
        
    def updatePlot(self):
        self.figure.clear()
        self.axes = self.figure.add_subplot(111)
        #self.axes.plot(self.data_x1, self.data_y1, "ro")
        #self.axes.plot(self.data_x1, self.data_y2, "go")
        self.axes.hist(self.data_x)
        self.canvas.draw()
