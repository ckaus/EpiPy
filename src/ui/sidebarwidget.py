# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui

class SidebarWidget(QtGui.QGroupBox):

    def __init__(self):
        super(SidebarWidget, self).__init__('Options')
        self.initUI()
        
    def initUI(self):
        # basic layout
        self.setMaximumWidth(int(640*0.4))
        self.sidebarLayout = QtGui.QVBoxLayout(self)
        # model widget
        self.modelWidget = QtGui.QWidget(self)
        self.modelLayout = QtGui.QHBoxLayout(self.modelWidget)
        self.modelComboBox = QtGui.QComboBox(self.modelWidget)
        self.modelComboBox.addItem('Choose a model')
        self.modelComboBox.setItemData(0, QtCore.QVariant(0),QtCore.Qt.UserRole -1)
        self.modelComboBox.addItem('SI')
        self.modelComboBox.addItem('IR')
        self.modelComboBox.addItem('SIR')
        self.advanceBtn = QtGui.QPushButton('Advance', self.modelWidget)
        self.advanceBtn.clicked.connect(self.showAdvance)
        self.modelLayout.addWidget(self.modelComboBox)
        self.modelLayout.addWidget(self.advanceBtn)
        self.sidebarLayout.addWidget(self.modelWidget)
        # parameter widget
        self.parameterWidget = QtGui.QGroupBox('Parameter', self)
        self.parameterLayout = QtGui.QFormLayout(self.parameterWidget)
        self.betaLabel = QtGui.QLabel('Beta', self.parameterWidget)
        self.betaLineEdit = QtGui.QLineEdit(self.parameterWidget)
        self.parameterLayout.addRow(self.betaLabel, self.betaLineEdit)
        self.gammaLabel = QtGui.QLabel('Gamme', self.parameterWidget)
        self.gammaLineEdit = QtGui.QLineEdit(self.parameterWidget)
        self.parameterLayout.addRow(self.gammaLabel, self.gammaLineEdit)
        self.sidebarLayout.addWidget(self.parameterWidget)
        # fitting information widget
        self.fittingInfoWidget = QtGui.QGroupBox('Fitting Information', self)
        self.fittingInfoLayout = QtGui.QVBoxLayout(self.fittingInfoWidget)
        self.sidebarLayout.addWidget(self.fittingInfoWidget)
        self.fittingInfoTextEdit = QtGui.QPlainTextEdit(self.fittingInfoWidget)
        self.fittingInfoTextEdit.setReadOnly(True)
        self.fittingInfoLayout.addWidget(self.fittingInfoTextEdit)
    def showAdvance(self):
    	print 'show advance'
