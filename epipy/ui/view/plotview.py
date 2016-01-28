from PyQt4 import QtGui
from matplotlib.backends.backend_qt4 import NavigationToolbar2QT as NavigationToolbar
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure


class PlotView(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.figure = Figure()

        # Canvas
        self.canvas = FigureCanvas(self.figure)
        self.canvas.setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        self.canvas.updateGeometry()

        # Navigation
        self.navi_toolbar = NavigationToolbar(self.canvas, self)

        self.vbl = QtGui.QVBoxLayout()
        self.vbl.addWidget(self.canvas)
        self.vbl.addWidget(self.navi_toolbar)
        self.setLayout(self.vbl)

    def plot(self, x=[], y=[], y_fitted=[], y_base=[]):
        self.figure.clear()
        self.ax = self.figure.add_subplot(111)
        self.ax.plot(x, y, 'o', label='Data')
        self.ax.plot(x, y_fitted, label='Fit')
        self.ax.plot(x, y_base, label='Base')
        self.canvas.draw()
