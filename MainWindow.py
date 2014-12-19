'''
Created on Dec 19, 2014

@author: ericrudisill
'''
from ui.MainWindow import Ui_MainWindow
from PyQt4 import QtGui

class MainWindow(Ui_MainWindow):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self._qMainWindow = QtGui.QMainWindow()
        self.setupUi(self._qMainWindow)
        self._qMainWindow.show()
        
    def show(self):
        self._qMainWindow.show()
