from PyQt4 import QtGui, QtCore
from matplotlib.backends.backend_qt4 import NavigationToolbar2QT as NavigationToolbar
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure


class PlotView(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.figure = Figure(facecolor=(1,1,1), tight_layout=True)
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

    def plot(self, x=[], y=[], y_fitted=[]):
        self.ax.clear()
        self.ax.grid(True)
        self.ax.plot(x, y, 'o', label='Data')
        self.ax.plot(x, y_fitted, label='Fit')
        self.ax.legend()
        self.canvas.draw()
