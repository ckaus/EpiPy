#! /usr/bin/python

import sys
import os
from PyQt4 import QtCore, QtGui
from graphview import GraphView
from sidebarview import SideBarView

class MainView(QtGui.QMainWindow):

    def __init__(self):
        super(MainView, self).__init__()
        self.initUI()

    def initUI(self):
        self.setMinimumSize(QtCore.QSize(640, 480))
        self.setMaximumSize(QtCore.QSize(1600, 900))
        self.setWindowTitle('EpiPy')
        self.initMenuBar()
        # main widget
        self.centralwidget = QtGui.QWidget(self)
        self.mainLayout = QtGui.QHBoxLayout(self.centralwidget)
        # plot widget (left)
        self.mainLayout.addWidget(GraphView())
        # side bar widget (right)
        self.mainLayout.addWidget(SideBarView())
        self.setCentralWidget(self.centralwidget)
        self.show()

    def initMenuBar(self):
		menubar = self.menuBar()
		# Menu Bar -> File
		fileMenu = menubar.addMenu('&File')
		# Menu Bar -> File -> New File
		newFileAction = QtGui.QAction('New File', self)
		newFileAction.setShortcut('Ctrl+N')
		newFileAction.triggered.connect(self.newFile)
		fileMenu.addAction(newFileAction)
		# Menu Bar -> File -> Open File
		openFileAction = QtGui.QAction('Open File...', self)
		openFileAction.setShortcut('Ctrl+O')
		openFileAction.triggered.connect(self.openFile)
		fileMenu.addAction(openFileAction)
		# Menu Bar -> File -> Open Folder
		openFolderAction = QtGui.QAction('Open Folder...', self)
		openFolderAction.setShortcut('Ctrl+F')
		openFolderAction.triggered.connect(self.openFolder)
		fileMenu.addAction(openFolderAction)
		# Menu Bar -> File -> Separator
		fileMenu.addSeparator()
		# Menu Bar -> File -> Save
		saveAction = QtGui.QAction('Save', self)
		saveAction.setShortcut('Ctrl+S')
		saveAction.triggered.connect(self.save)
		fileMenu.addAction(saveAction)
		# Menu Bar -> File -> Save As...
		saveAsAction = QtGui.QAction('Save As...', self)
		saveAsAction.setShortcut('Shift+Ctrl+S')
		saveAsAction.triggered.connect(self.saveAs)
		fileMenu.addAction(saveAsAction)
		# Menu Bar -> File -> Separator
		fileMenu.addSeparator()
		# Menu Bar -> File -> Export
		exportAction = QtGui.QAction('Export', self)
		exportAction.setShortcut('Ctrl+E')
		exportAction.triggered.connect(self.export)
		fileMenu.addAction(exportAction)
		# Menu Bar -> File -> Separator
		fileMenu.addSeparator()
		# Menu Bar -> File -> Exit
		exitAction = QtGui.QAction('Exit', self)
		exitAction.setShortcut('Ctrl+Q')
		exitAction.triggered.connect(self.exit)
		fileMenu.addAction(exitAction)
		# Menu Bar -> View
		fileMenu = menubar.addMenu('&View')
		# Menu Bar -> View -> Show Side Bar
		showSideBarAction = QtGui.QAction('Show Side Bar', self)
		showSideBarAction.triggered.connect(self.showSideBar)
		fileMenu.addAction(showSideBarAction)
		# Menu Bar -> View -> Hide Side Bar
		hideSideBarAction = QtGui.QAction('Hide Side Bar', self)
		hideSideBarAction.triggered.connect(self.hideSideBar)
		fileMenu.addAction(hideSideBarAction)
		# Menu Bar -> Help
		fileMenu = menubar.addMenu('&Help')
		# Menu Bar -> View -> Show Side Bar
		aboutAction = QtGui.QAction('About EpiPy', self)
		aboutAction.triggered.connect(self.about)
		fileMenu.addAction(aboutAction)
		
	# dummy functions
    def newFile(self):
    	print 'open new file'
    def openFile(self):
    	print 'open file'
    def openFolder(self):
    	print 'open folder'
    def save(self):
    	print 'save'
    def saveAs(self):
    	print 'save as'
    def export(self):
    	print 'export'
    def exit(self):
    	print 'exit'
    def showSideBar(self):
    	print 'show side bar'
    def hideSideBar(self):
    	print 'hide side bar'
    def about(self):
    	print 'about'
    
def main():
    app = QtGui.QApplication(sys.argv)
    mainView = MainView()
    sys.exit(app.exec_())
    
if __name__ == '__main__':
    main()
