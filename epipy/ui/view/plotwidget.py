from PyQt4 import QtGui, QtCore
from matplotlib.backends.backend_qt4 import NavigationToolbar2QT as NavigationToolbar
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

from epipy.ui.controller.event import Event


class PlotWidget(QtGui.QWidget):
    """
    This class represents the plot view for plotting graphs.

    :returns: an instance of *PlotWidget*
    """

    def __init__(self, parent, controller):
        QtGui.QWidget.__init__(self, parent)
        self.figure = Figure(facecolor=(1, 1, 1), tight_layout=True)
        self.controller = controller
        self.controller.attach(self)
        self.model = self.controller.get_model().get_plot_model()

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

    def update(self, event):
        """
        This function plot given data sets on plot view.
        """
        if event == Event.PLOT:
            x_data_file, y_data_file = self.model.get_data()
            x_data_fitted, y_data_fitted = self.model.get_fitted()
            self.ax.clear()
            self.ax.grid(True)
            self.ax.plot(x_data_file, y_data_file, 'b^', label='Input Data')
            self.ax.plot(x_data_fitted, y_data_fitted, 'b-', label='Fitted Data')
            self.ax.legend()
            self.canvas.draw()
