# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './ui/MacListWidget.ui'
#
# Created: Mon Jan  5 14:10:29 2015
#      by: PyQt4 UI code generator 4.11.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MacListWidget(object):
    def setupUi(self, MacListWidget):
        MacListWidget.setObjectName(_fromUtf8("MacListWidget"))
        MacListWidget.resize(248, 62)
        self.gridLayout = QtGui.QGridLayout(MacListWidget)
        self.gridLayout.setMargin(6)
        self.gridLayout.setVerticalSpacing(6)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.labelAge = QtGui.QLabel(MacListWidget)
        self.labelAge.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelAge.setObjectName(_fromUtf8("labelAge"))
        self.gridLayout.addWidget(self.labelAge, 3, 2, 1, 1)
        self.labelBatt = QtGui.QLabel(MacListWidget)
        self.labelBatt.setAlignment(QtCore.Qt.AlignCenter)
        self.labelBatt.setObjectName(_fromUtf8("labelBatt"))
        self.gridLayout.addWidget(self.labelBatt, 3, 1, 1, 1)
        self.labelRSSI = QtGui.QLabel(MacListWidget)
        self.labelRSSI.setObjectName(_fromUtf8("labelRSSI"))
        self.gridLayout.addWidget(self.labelRSSI, 3, 0, 1, 1)
        self.labelMac = QtGui.QLabel(MacListWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Menlo"))
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.labelMac.setFont(font)
        self.labelMac.setObjectName(_fromUtf8("labelMac"))
        self.gridLayout.addWidget(self.labelMac, 0, 0, 1, 3)
        self.line = QtGui.QFrame(MacListWidget)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.gridLayout.addWidget(self.line, 4, 0, 1, 3)

        self.retranslateUi(MacListWidget)
        QtCore.QMetaObject.connectSlotsByName(MacListWidget)

    def retranslateUi(self, MacListWidget):
        MacListWidget.setWindowTitle(_translate("MacListWidget", "Form", None))
        self.labelAge.setText(_translate("MacListWidget", "0 s", None))
        self.labelBatt.setText(_translate("MacListWidget", "0 V", None))
        self.labelRSSI.setText(_translate("MacListWidget", "0 dB", None))
        self.labelMac.setText(_translate("MacListWidget", "MAC", None))

