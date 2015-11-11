# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui
from plotwidget import PlotWidget
from sidebarwidget import SidebarWidget

class MainWindow(QtGui.QMainWindow):
	"""
	Main window of EpiPy.
	"""
	def __init__(self):
		super(MainWindow, self).__init__()
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
		self.mainLayout.addWidget(PlotWidget())
		# sidebar widget (right)
		self.mainLayout.addWidget(SidebarWidget())
		self.setCentralWidget(self.centralwidget)
		self.show()

	def initMenuBar(self):
		menubar = self.menuBar()
		# File
		fileMenu = menubar.addMenu('&File')
		# File -> New File
		newFileAction = QtGui.QAction('New File', self)
		newFileAction.setShortcut('Ctrl+N')
		newFileAction.triggered.connect(self.newFile)
		fileMenu.addAction(newFileAction)
		# File -> Open File
		openFileAction = QtGui.QAction('Open File...', self)
		openFileAction.setShortcut('Ctrl+O')
		openFileAction.triggered.connect(self.openFile)
		fileMenu.addAction(openFileAction)
		# File -> Open Folder
		openFolderAction = QtGui.QAction('Open Folder...', self)
		openFolderAction.setShortcut('Ctrl+F')
		openFolderAction.triggered.connect(self.openFolder)
		fileMenu.addAction(openFolderAction)
		# File -> Separator
		fileMenu.addSeparator()
		# File -> Save
		saveAction = QtGui.QAction('Save', self)
		saveAction.setShortcut('Ctrl+S')
		saveAction.triggered.connect(self.save)
		fileMenu.addAction(saveAction)
		# File -> Save As...
		saveAsAction = QtGui.QAction('Save As...', self)
		saveAsAction.setShortcut('Shift+Ctrl+S')
		saveAsAction.triggered.connect(self.saveAs)
		fileMenu.addAction(saveAsAction)
		# File -> Separator
		fileMenu.addSeparator()
		# File -> Export
		exportAction = QtGui.QAction('Export', self)
		exportAction.setShortcut('Ctrl+E')
		exportAction.triggered.connect(self.export)
		fileMenu.addAction(exportAction)
		# File -> Separator
		fileMenu.addSeparator()
		# File -> Exit
		exitAction = QtGui.QAction('Exit', self)
		exitAction.setShortcut('Ctrl+Q')
		exitAction.triggered.connect(self.exit)
		fileMenu.addAction(exitAction)
		# View
		fileMenu = menubar.addMenu('&View')
		# View -> Show Side Bar
		showsidebarAction = QtGui.QAction('Show Side Bar', self)
		showsidebarAction.triggered.connect(self.showsidebar)
		fileMenu.addAction(showsidebarAction)
		# View -> Hide Side Bar
		hidesidebarAction = QtGui.QAction('Hide Side Bar', self)
		hidesidebarAction.triggered.connect(self.hidesidebar)
		fileMenu.addAction(hidesidebarAction)
		# Help
		fileMenu = menubar.addMenu('&Help')
		# View -> Show Side Bar
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
	def showsidebar(self):
		print 'show side bar'
	def hidesidebar(self):
		print 'hide side bar'
	def about(self):
		print 'about'