# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtCore, QtGui
from ui import MainWindow

"""
EpiPy start point.
"""
def main():
    app = QtGui.QApplication(sys.argv)
    mainWindow = MainWindow()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()