# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui

class PlotWidget(QtGui.QGroupBox):
	"""
	This widget display several graphs.
	"""
    def __init__(self):
        super(PlotWidget, self).__init__('Graph')
        self.initUI()
        
    def initUI(self):
        self.setMinimumSize(QtCore.QSize(640*0.7, 480*0.7))
