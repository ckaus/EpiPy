#! /usr/bin/python

from PyQt4 import QtCore, QtGui

class SideBarView(QtGui.QGroupBox):

    def __init__(self):
        super(SideBarView, self).__init__()
        self.setTitle('Options')
        self.initUI()
        
    def initUI(self):
        self.setMaximumWidth(int(640*0.4))
        self.sideBarLayout = QtGui.QVBoxLayout(self)

        self.modelWidget = QtGui.QWidget(self)
        self.modelLayout = QtGui.QHBoxLayout(self.modelWidget)
        self.modelComboBox = QtGui.QComboBox(self.modelWidget)
        self.modelComboBox.addItem('Choose a model')
        # disable first item
        self.modelComboBox.setItemData(0, QtCore.QVariant(0),QtCore.Qt.UserRole -1)
        self.modelComboBox.addItem('SI')
        self.modelComboBox.addItem('IR')
        self.modelComboBox.addItem('SIR')
        # advanve button
        self.advanceBtn = QtGui.QPushButton('Advance', self.modelWidget)
        self.advanceBtn.clicked.connect(self.showAdvance)
        self.modelLayout.addWidget(self.modelComboBox)
        self.modelLayout.addWidget(self.advanceBtn)
        self.sideBarLayout.addWidget(self.modelWidget)
        # parameter widget
        self.parameterWidget = QtGui.QGroupBox('Parameter', self)
        self.parameterLayout = QtGui.QFormLayout(self.parameterWidget)
        # beta label and line edit
        self.betaLabel = QtGui.QLabel('Beta', self.parameterWidget)
        self.betaLineEdit = QtGui.QLineEdit(self.parameterWidget)
        self.parameterLayout.addRow(self.betaLabel, self.betaLineEdit)
        # gamma label and line edit
        self.gammaLabel = QtGui.QLabel('Gamme', self.parameterWidget)
        self.gammaLineEdit = QtGui.QLineEdit(self.parameterWidget)
        self.parameterLayout.addRow(self.gammaLabel, self.gammaLineEdit)
        self.sideBarLayout.addWidget(self.parameterWidget)
        # fitting information widget
        self.fittingInfoWidget = QtGui.QGroupBox('Fitting Information', self)
        self.fittingInfoLayout = QtGui.QVBoxLayout(self.fittingInfoWidget)
        self.sideBarLayout.addWidget(self.fittingInfoWidget)
        self.fittingInfoTextEdit = QtGui.QPlainTextEdit(self.fittingInfoWidget)
        self.fittingInfoTextEdit.setReadOnly(True)
        self.fittingInfoLayout.addWidget(self.fittingInfoTextEdit)
    def showAdvance(self):
    	print 'show advance'
