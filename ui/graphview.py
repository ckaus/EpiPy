#! /usr/bin/python

from PyQt4 import QtCore, QtGui

class GraphView(QtGui.QGroupBox):

    def __init__(self):
        super(GraphView, self).__init__()
        self.initUI()
        
    def initUI(self):
        self.plotWidget = QtGui.QGroupBox('Graph', self)
        self.plotWidget.setMinimumSize(QtCore.QSize(640*0.7, 480*0.7))
