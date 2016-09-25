# -*- coding: utf-8 -*-

from PyQt4 import QtGui, QtCore
from matplotlib.backends.backend_qt4\
    import NavigationToolbar2QT as NavigationToolbar
from matplotlib.backends.backend_qt4agg import\
    FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure


class PlotWidget(QtGui.QWidget):
    """This class represents the plot view for plotting graphs.

    :returns: an instance of *PlotWidget*
    """

    def __init__(self,):
        QtGui.QWidget.__init__(self)
        self.figure = Figure(facecolor=(1, 1, 1), tight_layout=True)

        self.ax = self.figure.add_subplot(111)

        # Canvas
        self.canvas = FigureCanvas(self.figure)
        self.canvas.setSizePolicy(QtGui.QSizePolicy.Expanding,
                                  QtGui.QSizePolicy.Expanding)
        self.canvas.updateGeometry()

        # Navigation
        self.navi_toolbar = NavigationToolbar(self.canvas, self)
        self.navi_toolbar.setOrientation(QtCore.Qt.Vertical)
        # Fixed with, otherwise navigation bar resize arbitrary
        self.navi_toolbar.setFixedWidth(40)

        self.vbl = QtGui.QHBoxLayout()
        self.vbl.addWidget(self.navi_toolbar)
        self.vbl.addWidget(self.canvas)
        self.setLayout(self.vbl)

    def plot(self, x_data_1, y_data_1, x_data_2, y_data_2):
        """Plot given data on *PlotWidget*.

        :param x_data_1: X-axis data for plot 1
        :type x_data_1: array_like
        :param y_data_1: Y-axis data for plot 1
        :type y_data_1: array_like
        :param x_data_2: X-axis data for plot 2
        :type x_data_2: array_like
        :param y_data_2: Y-axis data for plot 2
        :type y_data_2: array_like
        """
        self.ax.clear()
        self.ax.grid(True)
        self.ax.plot(x_data_1, y_data_1, 'b^', label='Input Data')
        self.ax.plot(x_data_2, y_data_2, 'b-', label='Fitted Data')
        self.ax.legend()
        self.canvas.draw()
