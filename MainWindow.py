'''
Created on Dec 19, 2014

@author: ericrudisill
'''
from ui.MainWindow import Ui_MainWindow
from PyQt4 import QtCore, QtGui
from MacListWidget import MacListWidget

class MainWindow(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setCorner( QtCore.Qt.TopLeftCorner , QtCore.Qt.LeftDockWidgetArea );
        self.setCorner( QtCore.Qt.TopRightCorner, QtCore.Qt.RightDockWidgetArea );
        self.setCorner( QtCore.Qt.BottomLeftCorner, QtCore.Qt.LeftDockWidgetArea );
        self.setCorner( QtCore.Qt.BottomRightCorner, QtCore.Qt.RightDockWidgetArea );
        
        for i in range(10):
            w = MacListWidget()
            w.setMac("000000" + str(i) + str(i))
            w.setRSSI("-" + str(i) + str(i))
            w.setBatt(str(i) + str(i))
            wi = QtGui.QListWidgetItem(self.listWidget)
            wi.setSizeHint(w.sizeHint())
            self.listWidget.addItem(wi)
            self.listWidget.setItemWidget(wi, w)            
