'''
Created on Dec 19, 2014

@author: ericrudisill
'''
from PyQt4 import QtGui
from MainWindow import MainWindow

if __name__ == '__main__': 
    import sys
    app = QtGui.QApplication(sys.argv)
    
    window = MainWindow()
    window.show()
    
    sys.exit(app.exec_())