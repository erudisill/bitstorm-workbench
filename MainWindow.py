'''
Created on Dec 19, 2014

@author: ericrudisill
'''
from ui.MainWindow import Ui_MainWindow
from PyQt4 import QtCore, QtGui
from MacListWidget import MacListWidget
from BsClient import BsClient
from Device import Device
from PlotWindow import PlotWindow

class MainWindow(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        
        # Docking layout preferences
        self.setCorner( QtCore.Qt.TopLeftCorner , QtCore.Qt.LeftDockWidgetArea );
        self.setCorner( QtCore.Qt.TopRightCorner, QtCore.Qt.RightDockWidgetArea );
        self.setCorner( QtCore.Qt.BottomLeftCorner, QtCore.Qt.LeftDockWidgetArea );
        self.setCorner( QtCore.Qt.BottomRightCorner, QtCore.Qt.RightDockWidgetArea );
        
        # Sexxy
        # http://stackoverflow.com/questions/14330642/how-do-i-achieve-consistent-highlighting-of-qlistwidget-items-across-widget-stat
        self.setStyleSheet('''
            QListWidget:item:selected:active { background: lightblue }
            ''')
        
        # Mdi
        self.mdiArea.subWindowActivated.connect(self.subWindowActivated)
        self.mdiChildNumber = 0
        
        # Device List
        #self.listWidget.itemActivated.connect(self.deviceActivated)
        #self.listWidget.itemSelectionChanged.connect(self.deviceSelected)
        self.checkSelectAll.stateChanged.connect(self.checkSelectAllStateChanged)
        
        # Menu hookups
        self.actionRSSI_Histogram.triggered.connect(self.createRSSIHistogram)
        
        # Internal structures
        self.devices = []
        
        # Attach to the server
        self.clientThread = BsClient(BsClient.HOST, BsClient.PORT)
        self.clientThread.received.connect(self.updateMacList)
        self.clientThread.start()
        
    def updateMacList(self, record):
        try:
            device = next(d for d in self.devices if d.mac == record.mac)
        except Exception:
            # no record found, so create one as well as a widget
            device = Device()
            device.mac = record.mac
            self.devices.append(device)
            w = MacListWidget(device)
            w.activeStateChanged.connect(self.deviceActiveStateChanged)
            wi = QtGui.QListWidgetItem(self.listWidget)
            wi.setSizeHint(w.sizeHint())
            self.listWidget.addItem(wi)
            self.listWidget.setItemWidget(wi, w)
            
        device.rssi = record.rssi_dec
        device.batt = record.batt
        device.count = device.count + 1
        device.update()
    
    def getActiveDevices(self):
        i = 0
        devices = []
        while i < self.listWidget.count():
            item = self.listWidget.item(i)
            w = self.listWidget.itemWidget(item)
            if w.isActive():
                devices.append(w.device)
            i = i + 1
        return devices
        
    def subWindowActivated(self, window):    
        try:
            i = 0
            while i < self.listWidget.count():
                item = self.listWidget.item(i)
                w = self.listWidget.itemWidget(item)
                if w.device in window.widget().devices:
                    w.setActiveState(QtCore.Qt.Checked, cancelEmit=True)
                else:
                    w.setActiveState(QtCore.Qt.Unchecked, cancelEmit=True)
                i = i + 1
                
        except Exception:
            # sometimes window is nothing...why?
            pass
    
    def checkSelectAllStateChanged(self, newState):
        i = 0
        while i < self.listWidget.count():
            item = self.listWidget.item(i)
            w = self.listWidget.itemWidget(item)
            w.setActiveState(newState)
            i = i + 1
    
    def deviceActiveStateChanged(self, newState, device):
        w = self.mdiArea.activeSubWindow()
        if not w is None:
            if newState == QtCore.Qt.Unchecked:
                w.widget().removeDevice(device)
            else:
                w.widget().addDevice(device)
                
    
    def createRSSIHistogram(self):
        d = self.getActiveDevices()
        child = PlotWindow(devices=d)
        sub = self.mdiArea.addSubWindow(child)
        sub.setWindowTitle("RSSI Histogram " + str(self.mdiChildNumber))
        self.mdiChildNumber = self.mdiChildNumber + 1
        child.showMaximized()
    
#     def deviceActivated(self, item):
#         print "Activated " + str(item)
#         print "Widget: " + self.listWidget.itemWidget(item).device.mac
#         
#     def deviceSelected(self):
#         item = self.listWidget.currentItem()
#         print "Selected " + str(item)
#         print "Widget: " + self.listWidget.itemWidget(item).device.mac        
            