# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created: Sun Nov  8 15:03:57 2015
#      by: PyQt4 UI code generator 4.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(885, 547)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.topLayout = QtGui.QHBoxLayout()
        self.topLayout.setObjectName(_fromUtf8("topLayout"))
        self.plotWidget = QtGui.QWidget(self.centralwidget)
        self.plotWidget.setMinimumSize(QtCore.QSize(640, 480))
        self.plotWidget.setMaximumSize(QtCore.QSize(668, 16777215))
        self.plotWidget.setObjectName(_fromUtf8("plotWidget"))
        self.topLayout.addWidget(self.plotWidget)
        self.optionPlotWidget = QtGui.QWidget(self.centralwidget)
        self.optionPlotWidget.setObjectName(_fromUtf8("optionPlotWidget"))
        self.gridLayout = QtGui.QGridLayout(self.optionPlotWidget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.fittingInfoLabel = QtGui.QLabel(self.optionPlotWidget)
        self.fittingInfoLabel.setObjectName(_fromUtf8("fittingInfoLabel"))
        self.gridLayout.addWidget(self.fittingInfoLabel, 5, 0, 1, 1)
        self.betaLabel = QtGui.QLabel(self.optionPlotWidget)
        self.betaLabel.setObjectName(_fromUtf8("betaLabel"))
        self.gridLayout.addWidget(self.betaLabel, 3, 0, 1, 1)
        self.fittingInfoTextEdit = QtGui.QPlainTextEdit(self.optionPlotWidget)
        self.fittingInfoTextEdit.setObjectName(_fromUtf8("fittingInfoTextEdit"))
        self.gridLayout.addWidget(self.fittingInfoTextEdit, 6, 0, 1, 3)
        self.betaLineEdit = QtGui.QLineEdit(self.optionPlotWidget)
        self.betaLineEdit.setObjectName(_fromUtf8("betaLineEdit"))
        self.gridLayout.addWidget(self.betaLineEdit, 3, 2, 1, 1)
        self.gammaLabel = QtGui.QLabel(self.optionPlotWidget)
        self.gammaLabel.setObjectName(_fromUtf8("gammaLabel"))
        self.gridLayout.addWidget(self.gammaLabel, 4, 0, 1, 1)
        self.gammaLineEdit = QtGui.QLineEdit(self.optionPlotWidget)
        self.gammaLineEdit.setObjectName(_fromUtf8("gammaLineEdit"))
        self.gridLayout.addWidget(self.gammaLineEdit, 4, 2, 1, 1)
        self.modelComboBox = QtGui.QComboBox(self.optionPlotWidget)
        self.modelComboBox.setObjectName(_fromUtf8("modelComboBox"))
        self.modelComboBox.addItem(_fromUtf8(""))
        self.modelComboBox.addItem(_fromUtf8(""))
        self.modelComboBox.addItem(_fromUtf8(""))
        self.modelComboBox.addItem(_fromUtf8(""))
        self.gridLayout.addWidget(self.modelComboBox, 2, 0, 1, 1)
        self.advanceBtn = QtGui.QPushButton(self.optionPlotWidget)
        self.advanceBtn.setObjectName(_fromUtf8("advanceBtn"))
        self.gridLayout.addWidget(self.advanceBtn, 2, 2, 1, 1)
        self.topLayout.addWidget(self.optionPlotWidget)
        self.verticalLayout.addLayout(self.topLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 885, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        self.menuHelp_2 = QtGui.QMenu(self.menubar)
        self.menuHelp_2.setObjectName(_fromUtf8("menuHelp_2"))
        MainWindow.setMenuBar(self.menubar)
        self.s = QtGui.QStatusBar(MainWindow)
        self.s.setObjectName(_fromUtf8("s"))
        MainWindow.setStatusBar(self.s)
        self.actionNew_File = QtGui.QAction(MainWindow)
        self.actionNew_File.setObjectName(_fromUtf8("actionNew_File"))
        self.actionOpen_File = QtGui.QAction(MainWindow)
        self.actionOpen_File.setObjectName(_fromUtf8("actionOpen_File"))
        self.actionClose = QtGui.QAction(MainWindow)
        self.actionClose.setObjectName(_fromUtf8("actionClose"))
        self.actionSave_as = QtGui.QAction(MainWindow)
        self.actionSave_as.setObjectName(_fromUtf8("actionSave_as"))
        self.actionSave = QtGui.QAction(MainWindow)
        self.actionSave.setObjectName(_fromUtf8("actionSave"))
        self.actionSave_As = QtGui.QAction(MainWindow)
        self.actionSave_As.setObjectName(_fromUtf8("actionSave_As"))
        self.actionExit = QtGui.QAction(MainWindow)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.actionExit_2 = QtGui.QAction(MainWindow)
        self.actionExit_2.setObjectName(_fromUtf8("actionExit_2"))
        self.actionShow_Sidebar = QtGui.QAction(MainWindow)
        self.actionShow_Sidebar.setObjectName(_fromUtf8("actionShow_Sidebar"))
        self.actionHide_Showbar = QtGui.QAction(MainWindow)
        self.actionHide_Showbar.setObjectName(_fromUtf8("actionHide_Showbar"))
        self.actionHide_Plot = QtGui.QAction(MainWindow)
        self.actionHide_Plot.setObjectName(_fromUtf8("actionHide_Plot"))
        self.actionEdit_Layout = QtGui.QAction(MainWindow)
        self.actionEdit_Layout.setObjectName(_fromUtf8("actionEdit_Layout"))
        self.actionRead_Layout = QtGui.QAction(MainWindow)
        self.actionRead_Layout.setObjectName(_fromUtf8("actionRead_Layout"))
        self.actionSI = QtGui.QAction(MainWindow)
        self.actionSI.setObjectName(_fromUtf8("actionSI"))
        self.actionSIR = QtGui.QAction(MainWindow)
        self.actionSIR.setObjectName(_fromUtf8("actionSIR"))
        self.actionSIR_2 = QtGui.QAction(MainWindow)
        self.actionSIR_2.setObjectName(_fromUtf8("actionSIR_2"))
        self.actionHow_to_use_EpiPy = QtGui.QAction(MainWindow)
        self.actionHow_to_use_EpiPy.setObjectName(_fromUtf8("actionHow_to_use_EpiPy"))
        self.actionAbout_EpiPy = QtGui.QAction(MainWindow)
        self.actionAbout_EpiPy.setObjectName(_fromUtf8("actionAbout_EpiPy"))
        self.actionExit_3 = QtGui.QAction(MainWindow)
        self.actionExit_3.setObjectName(_fromUtf8("actionExit_3"))
        self.menuFile.addAction(self.actionNew_File)
        self.menuFile.addAction(self.actionOpen_File)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSave_As)
        self.menuFile.addAction(self.actionExit)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit_2)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit_3)
        self.menuHelp.addAction(self.actionShow_Sidebar)
        self.menuHelp.addAction(self.actionHide_Showbar)
        self.menuHelp.addSeparator()
        self.menuHelp_2.addAction(self.actionAbout_EpiPy)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menubar.addAction(self.menuHelp_2.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.fittingInfoLabel.setText(_translate("MainWindow", "Fitting Information", None))
        self.betaLabel.setText(_translate("MainWindow", "Beta", None))
        self.gammaLabel.setText(_translate("MainWindow", "Gamma", None))
        self.modelComboBox.setItemText(0, _translate("MainWindow", "Choose a model", None))
        self.modelComboBox.setItemText(1, _translate("MainWindow", "SI", None))
        self.modelComboBox.setItemText(2, _translate("MainWindow", "IR", None))
        self.modelComboBox.setItemText(3, _translate("MainWindow", "SIR", None))
        self.advanceBtn.setText(_translate("MainWindow", "Advance", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.menuHelp.setTitle(_translate("MainWindow", "View", None))
        self.menuHelp_2.setTitle(_translate("MainWindow", "Help", None))
        self.actionNew_File.setText(_translate("MainWindow", "New File", None))
        self.actionOpen_File.setText(_translate("MainWindow", "Open File...", None))
        self.actionClose.setText(_translate("MainWindow", "Save", None))
        self.actionSave_as.setText(_translate("MainWindow", "Save As ...", None))
        self.actionSave.setText(_translate("MainWindow", "Open Folder...", None))
        self.actionSave_As.setText(_translate("MainWindow", "Save", None))
        self.actionExit.setText(_translate("MainWindow", "Save As...", None))
        self.actionExit_2.setText(_translate("MainWindow", "Export", None))
        self.actionShow_Sidebar.setText(_translate("MainWindow", "Show Sidebar", None))
        self.actionHide_Showbar.setText(_translate("MainWindow", "Hide Sidebar", None))
        self.actionHide_Plot.setText(_translate("MainWindow", "Hide Plot", None))
        self.actionEdit_Layout.setText(_translate("MainWindow", "Edit Layout", None))
        self.actionRead_Layout.setText(_translate("MainWindow", "Read Layout", None))
        self.actionSI.setText(_translate("MainWindow", "SI", None))
        self.actionSIR.setText(_translate("MainWindow", "IR", None))
        self.actionSIR_2.setText(_translate("MainWindow", "SIR", None))
        self.actionHow_to_use_EpiPy.setText(_translate("MainWindow", "EpiPy Help", None))
        self.actionAbout_EpiPy.setText(_translate("MainWindow", "About EpiPy", None))
        self.actionExit_3.setText(_translate("MainWindow", "Exit", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
