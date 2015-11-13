# -*- coding: utf-8 -*-

import os
from PyQt4 import uic, QtCore
from aboutdialog import AboutDialog

path = os.path.dirname(os.path.abspath(__file__))
MainWindowUI, MainWindowBase = uic.loadUiType(
    os.path.join(path, "mainwindow.ui"))

class MainWindow(MainWindowBase, MainWindowUI):
    def __init__(self):
    	MainWindowBase.__init__(self)
    	self.setupUi(self)
    	self.showSidebar()
    	# disable first item
    	self.modelComboBox.setItemData(0, QtCore.QVariant(0),QtCore.Qt.UserRole -1)
    	# connect menu components with functions
    	self.openFileAction.triggered.connect(self.openFile)
    	self.saveAction.triggered.connect(self.save)
    	self.saveAsAction.triggered.connect(self.saveAs)
    	self.exportAction.triggered.connect(self.export)
    	self.exitAction.triggered.connect(self.close)
    	self.showSidebarAction.triggered.connect(self.showSidebar)
    	self.hideSidebarAction.triggered.connect(self.hideSidebar)
    	self.aboutAction.triggered.connect(self.showAbout)

    def openFile(self):
    	print "open file"
    def save(self):
    	print "save"
    def saveAs(self):
    	print "save as"
    def export(self):
    	print "export"
    def showSidebar(self):
    	self.sidebarGroupBox.setVisible(True)
    	self.showSidebarAction.setDisabled(True)
    	self.hideSidebarAction.setEnabled(True)
    def hideSidebar(self):
    	self.sidebarGroupBox.setVisible(False)
    	self.showSidebarAction.setDisabled(False)
    	self.hideSidebarAction.setEnabled(False)
    def showAbout(self):
    	aboutDialog = AboutDialog(self)
    	aboutDialog.show