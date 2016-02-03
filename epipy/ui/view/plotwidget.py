from PyQt4 import QtGui, QtCore
from matplotlib.backends.backend_qt4 import NavigationToolbar2QT as NavigationToolbar
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure


class PlotView(QtGui.QWidget):
    """
    This class represents the plot view for plotting graphs.

    :returns: an instance of *PlotView*
    """

    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.figure = Figure(facecolor=(1, 1, 1), tight_layout=True)
        self.ax = self.figure.add_subplot(111)

        # Canvas
        self.canvas = FigureCanvas(self.figure)
        self.canvas.setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        self.canvas.updateGeometry()

        # Navigation
        self.navi_toolbar = NavigationToolbar(self.canvas, self)
        self.navi_toolbar.setOrientation(QtCore.Qt.Vertical)
        self.navi_toolbar.setFixedWidth(40)  # otherwise the navigation bar resize very crazy, don't know the problem

        self.vbl = QtGui.QHBoxLayout()
        self.vbl.addWidget(self.navi_toolbar)
        self.vbl.addWidget(self.canvas)
        self.setLayout(self.vbl)

    def plot(self, file_data, fitted_data, forecast_data):
        """
        This function plot given data sets on plot view.

        :param file_data: contain file data
        :type file_data: array
        :param fitted_data: contain fitted data
        :type fitted_data: array
        :param forecast_data: contain forecast data
        :type forecast_data: array
        """
        self.ax.clear()
        self.ax.grid(True)
        self.ax.plot(file_data[0], file_data[1], 'b^', label='Input Data')
        self.ax.plot(fitted_data[0], fitted_data[1], 'b-', label='Fitted Data')
        self.ax.plot(forecast_data[0], forecast_data[1], 'g-', label='Forecast')
        self.ax.legend()
        self.canvas.draw()
