# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './ui/MacListWidget.ui'
#
# Created: Tue Dec 30 15:51:39 2014
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
        MacListWidget.resize(225, 56)
        self.gridLayout = QtGui.QGridLayout(MacListWidget)
        self.gridLayout.setMargin(6)
        self.gridLayout.setVerticalSpacing(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setSpacing(-1)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_2 = QtGui.QLabel(MacListWidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout.addWidget(self.label_2)
        self.labelRSSI = QtGui.QLabel(MacListWidget)
        self.labelRSSI.setObjectName(_fromUtf8("labelRSSI"))
        self.horizontalLayout.addWidget(self.labelRSSI)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label = QtGui.QLabel(MacListWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.labelBatt = QtGui.QLabel(MacListWidget)
        self.labelBatt.setObjectName(_fromUtf8("labelBatt"))
        self.horizontalLayout.addWidget(self.labelBatt)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.gridLayout.addLayout(self.horizontalLayout, 2, 0, 1, 1)
        self.labelMac = QtGui.QLabel(MacListWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.labelMac.setFont(font)
        self.labelMac.setObjectName(_fromUtf8("labelMac"))
        self.gridLayout.addWidget(self.labelMac, 0, 0, 1, 1)
        self.line = QtGui.QFrame(MacListWidget)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setLineWidth(1)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.gridLayout.addWidget(self.line, 3, 0, 1, 1)

        self.retranslateUi(MacListWidget)
        QtCore.QMetaObject.connectSlotsByName(MacListWidget)

    def retranslateUi(self, MacListWidget):
        MacListWidget.setWindowTitle(_translate("MacListWidget", "Form", None))
        self.label_2.setText(_translate("MacListWidget", "RSSI:", None))
        self.labelRSSI.setText(_translate("MacListWidget", "0", None))
        self.label.setText(_translate("MacListWidget", "Batt:", None))
        self.labelBatt.setText(_translate("MacListWidget", "0", None))
        self.labelMac.setText(_translate("MacListWidget", "MAC", None))

