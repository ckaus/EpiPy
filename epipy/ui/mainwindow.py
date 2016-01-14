# # -*- coding: utf-8 -*-

import os, sys
from PyQt4 import uic, QtCore, QtGui
from aboutdialog import AboutDialog
from customviewbox import CustomViewBox

import pyqtgraph as pg
import numpy as np
from epipy.model.sir import SIR
from epipy.utils import logger
from epipy.utils import CSV_Manager
from customviewbox import CustomViewBox

filePath = os.path.abspath(__file__)
folderPath = os.path.dirname(filePath)
MainWindowUI, MainWindowBase = uic.loadUiType(
    os.path.join(folderPath, "mainwindow.ui"))

class MainWindow(MainWindowBase, MainWindowUI):
    def __init__(self):
    	MainWindowBase.__init__(self)
    	self.setupUi(self)

        self.aboutDialog = uic.loadUi(os.path.join(folderPath,'aboutdialog.ui'))
        self.aboutDialog.closeButton.clicked.connect(self.aboutDialog.close)

        self.optionsgb = uic.loadUi(os.path.join(folderPath,'optionsgroupbox.ui'))
        self.sirgb = uic.loadUi(os.path.join(folderPath,'sirgroupbox.ui'))
        self.infogb = uic.loadUi(os.path.join(folderPath,'infogroupbox.ui'))
        
        self.infogb.clearBtn.clicked.connect(self.clearFittingInfo)

        self.optionsgb.layout().addRow(self.sirgb)
        self.leftwidget.layout().addWidget(self.optionsgb)
        self.leftwidget.layout().addWidget(self.infogb)
        self.splitter.insertWidget(1, self.leftwidget)

        content = CSV_Manager().read(
            file_name="data1.csv",
            seperator=";", column=["Time", "I"])
        
        ydata = np.array(content['I'], dtype=float)
        xdata = np.array(content['Time'], dtype=float)
        sir = SIR(xdata, ydata)
        fitted = sir.fit()
        self.sirgb.betaSpinBox.setValue(sir.popt[0]) # beta
        self.sirgb.gammaSpinBox.setValue(sir.popt[1]) # gamma
        self.infogb.infoPlainTextEdit.appendPlainText("pcov="+str(sir.pcov))

        # ====plot==========
        self.pw = pg.PlotWidget(title="SIR", viewBox=CustomViewBox(), enableMenu=False)
        self.pw.plot(x=xdata, y=ydata, symbol='o')
        self.pw.plot(x=xdata, y=fitted, pen="k")
        self.pw.setWindowTitle('pyqtgraph example: customPlot')
        self.pw.setBackground(QtGui.QColor(255, 255, 255))
        self.splitter.insertWidget(0,self.pw)
        # ==================
        # menu
        # connect menu components with functions
        self.openFileAction.triggered.connect(self.openFile)
        self.saveAction.triggered.connect(self.save)
        self.saveAsAction.triggered.connect(self.saveAs)
        self.exportAction.triggered.connect(self.export)
        self.exitAction.triggered.connect(self.close)
        self.showFullscreenAction.triggered.connect(self.showFullscreen)
        self.exitFullscreenAction.triggered.connect(self.exitFullscreen)
        self.exitFullscreenAction.setVisible(False)
        self.showSidebarAction.triggered.connect(self.showSidebar)
        self.hideSidebarAction.triggered.connect(self.hideSidebar)
        self.showSidebarAction.setVisible(False)
        self.aboutAction.triggered.connect(self.showAbout)
        # side bar
        # disable first item of model box in option groupbox
    	self.optionsgb.modelComboBox.setItemData(0, QtCore.QVariant(0),QtCore.Qt.UserRole -1)
    	# fitting information groupbox

    def openFile(self):
    	logger.info("open file")
        self.infogb.infoPlainTextEdit.appendPlainText("open file")
    
    def save(self):
    	logger.info("save")
        self.infogb.infoPlainTextEdit.appendPlainText("save")
    
    def saveAs(self):
    	logger.info("save as")
        self.infogb.infoPlainTextEdit.appendPlainText("save as")
    
    def export(self):
    	logger.info("export")
        self.infogb.infoPlainTextEdit.appendPlainText("export")
    
    def showFullscreen(self):
        self.showFullscreenAction.setVisible(False)
        self.exitFullscreenAction.setVisible(True)
        self.showFullScreen()
    
    def exitFullscreen(self):
        self.showFullscreenAction.setVisible(True)
        self.exitFullscreenAction.setVisible(False)
        self.showNormal()
    
    def showSidebar(self):
    	self.leftwidget.setVisible(True)
    	self.showSidebarAction.setVisible(False)
    	self.hideSidebarAction.setVisible(True)
    
    def hideSidebar(self):
    	self.leftwidget.setVisible(False)
    	self.showSidebarAction.setVisible(True)
    	self.hideSidebarAction.setVisible(False)
    
    def showAbout(self):
    	self.aboutDialog.show()

    def clearFittingInfo(self):
        reply = QtGui.QMessageBox.question(self, 'Message', "Are you sure to clear the fitting information?", 
            QtGui.QMessageBox.Yes | QtGui.QMessageBox.No, QtGui.QMessageBox.No)
        if reply == QtGui.QMessageBox.Yes:
            self.infogb.infoPlainTextEdit.clear()