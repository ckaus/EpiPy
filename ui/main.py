#! /usr/bin/python

import sys
import os
from PyQt4 import QtCore, QtGui

class MainView(QtGui.QMainWindow):

    def __init__(self):
        super(MainView, self).__init__()
        self.initUI()

    def initUI(self):
        # minumim width / length
        minW=640
        minL=480
        # maxmimum width / length
        maxW=1600 
        maxL=900
        self.setMinimumSize(QtCore.QSize(minW, minL))
        self.setMaximumSize(QtCore.QSize(maxW, maxL))
        self.setWindowTitle('EpiPy')
        self.initMenuBar()

        # main widget
        self.centralwidget = QtGui.QWidget(self)
        self.mainLayout = QtGui.QHBoxLayout(self.centralwidget)

        # plot widget (left)
        self.plotWidget = QtGui.QGroupBox('Graph', self.centralwidget)
        self.plotWidget.setMinimumSize(QtCore.QSize(minW*0.7, minL*0.7))
        self.mainLayout.addWidget(self.plotWidget)
        
        # side bar widget (right)
        self.sideBarWidget = QtGui.QWidget(self.centralwidget)
        self.sideBarWidget.setMaximumWidth(int(minW*0.5))
        self.sideBarLayout = QtGui.QVBoxLayout(self.sideBarWidget)
        # model widget
        self.modelWidget = QtGui.QGroupBox('Model', self.sideBarWidget)
        self.modelLayout = QtGui.QFormLayout(self.modelWidget)
        # model combo box
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
        self.modelLayout.addRow(self.modelComboBox, self.advanceBtn)
        self.sideBarLayout.addWidget(self.modelWidget)

        # parameter widget
        self.parameterWidget = QtGui.QGroupBox('Parameter', self.sideBarWidget)
        self.parameterLayout = QtGui.QFormLayout(self.parameterWidget)
        self.sideBarLayout.addWidget(self.parameterWidget)
        # beta label and line edit
        self.betaLabel = QtGui.QLabel('Beta', self.parameterWidget)
        self.betaLineEdit = QtGui.QLineEdit(self.parameterWidget)
        self.parameterLayout.addRow(self.betaLabel, self.betaLineEdit)
        # gamma label and line edit
        self.gammaLabel = QtGui.QLabel('Gamme', self.parameterWidget)
        self.gammaLineEdit = QtGui.QLineEdit(self.parameterWidget)
        self.parameterLayout.addRow(self.gammaLabel, self.gammaLineEdit)

        # fitting information widget
        self.fittingInfoWidget = QtGui.QGroupBox('Fitting Information', self.sideBarWidget)
        self.fittingInfoLayout = QtGui.QVBoxLayout(self.fittingInfoWidget)
        self.sideBarLayout.addWidget(self.fittingInfoWidget)
        self.fittingInfoTextEdit = QtGui.QPlainTextEdit(self.fittingInfoWidget)
        self.fittingInfoLayout.addWidget(self.fittingInfoTextEdit)

        self.mainLayout.addWidget(self.sideBarWidget)
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
    def showAdvance(self):
    	print 'show advance'

def main():
    app = QtGui.QApplication(sys.argv)
    mainView = MainView()
    sys.exit(app.exec_())
    
if __name__ == '__main__':
    main()
