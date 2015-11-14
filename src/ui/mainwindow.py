# -*- coding: utf-8 -*-

import os
from PyQt4 import uic, QtCore, QtGui
from aboutdialog import AboutDialog
from utils import logger

filePath = os.path.abspath(__file__)
folderPath = os.path.dirname(filePath)
MainWindowUI, MainWindowBase = uic.loadUiType(
    os.path.join(folderPath, "mainwindow.ui"))

class MainWindow(MainWindowBase, MainWindowUI):
    def __init__(self):
    	MainWindowBase.__init__(self)
    	self.setupUi(self)
    	self.showSidebar()
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
    	self.modelComboBox.setItemData(0, QtCore.QVariant(0),QtCore.Qt.UserRole -1)
    	# fitting information groupbox
        self.clearButton.setIcon(QtGui.QIcon("../resources/clear.png"))
        self.clearButton.clicked.connect(self.infoTextEdit.clear)
        self.saveButton.setIcon(QtGui.QIcon("../resources/save.png"))
        self.searchLineEdit.returnPressed.connect(self.searchInfoText)

    def openFile(self):
    	logger.info("open file")
        self.infoTextEdit.appendPlainText(logger.info("open file"))
    
    def save(self):
    	logger.info("save")
        self.infoTextEdit.appendPlainText(logger.info("save"))
    
    def saveAs(self):
    	logger.info("save as")
        self.infoTextEdit.appendPlainText(logger.info("save as"))
    
    def export(self):
    	logger.info("export")
        self.infoTextEdit.appendPlainText(logger.info("export"))
    
    def showFullscreen(self):
        self.showFullscreenAction.setVisible(False)
        self.exitFullscreenAction.setVisible(True)
        self.showFullScreen()
    
    def exitFullscreen(self):
        self.showFullscreenAction.setVisible(True)
        self.exitFullscreenAction.setVisible(False)
        self.showNormal()
    
    def showSidebar(self):
    	self.sidebarGroupBox.setVisible(True)
    	self.showSidebarAction.setVisible(False)
    	self.hideSidebarAction.setVisible(True)
    
    def hideSidebar(self):
    	self.sidebarGroupBox.setVisible(False)
    	self.showSidebarAction.setVisible(True)
    	self.hideSidebarAction.setVisible(False)
    
    def showAbout(self):
    	AboutDialog(self).show()
    
    def searchInfoText(self):
        self.infoTextEdit.appendPlainText(logger.info("search"))