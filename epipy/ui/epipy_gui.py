# # -*- coding: utf-8 -*-

import numpy as np
import os
import pyqtgraph as pg
from PyQt4 import uic, QtCore, QtGui
from PyQt4.QtCore import pyqtSignature, Qt
import sys
import matplotlib
from path import path

import epipy.model
from epipy.utils import csvmanager, dateconverter
from epipy.utils import logger
from PyQt4.QtGui import QMessageBox
from numpy import nan, array, ma, arange

def get_args(*a, **k):
    return a, k

def find(array):
    return arange(len(array))[array]

class ParametersModel(QtCore.QAbstractTableModel):
    def __init__(self, model, parent=None):
        QtCore.QAbstractTableModel.__init__(self, parent)
        self.model = model
        clazz = getattr(model, 'Simple')
        self.parm_names = getattr(clazz, 'param')()
        self.parm_values = [0 for x in self.parm_names]

    def rowCount(self, idx=QtCore.QModelIndex()):
        return len(self.parm_names)

    def columnCount(self, idx=QtCore.QModelIndex()):
        return 2

    def headerData(self, section, orientation, role=Qt.DisplayRole):
        if role != Qt.DisplayRole:
            return
        if orientation == Qt.Horizontal:
            if section == 0:
                return "Parameter"
            elif section == 1:
                return "Value"

    def flags(self, index):
        if index.column() == 0:
            return Qt.ItemIsEnabled
        elif index.column() == 1:
            return Qt.ItemIsEnabled | Qt.ItemIsEditable
        return Qt.NoItemFlags

    def data(self, index, role=Qt.DisplayRole):
        r = index.row()
        c = index.column()
        if 0 <= r < len(self.parm_names) and 0 <= c < 2:
            if c == 0:
                if role == Qt.DisplayRole:
                    return self.parm_names[r]
            elif c == 1:
                if role == Qt.DisplayRole:
                    return "%g" % (self.parm_values[r],)
                elif role == Qt.EditRole:
                    return "%g" % (self.parm_values[r],)

    def setData(self, index, value, role=Qt.DisplayRole):
        r = index.row()
        c = index.column()
        if 0 <= r < len(self.parm_names) and 0 < c < 2:
            if c == 1 and role == Qt.EditRole:
                try:
                    f = float(value.toPyObject())
                    self.parm_values[r] = f
                    self.dataChanged.emit(index, index)
                    return True
                except ValueError:
                    print("Error, cannot convert value to double")
        return False


class InformationModel(QtCore.QAbstractTableModel):
    def __init__(self, items, parent=None):
        QtCore.QAbstractTableModel.__init__(self, parent)
        self.items = items
        self.parm_names = items.keys()
        self.parm_values = items.values()

    def rowCount(self, idx=QtCore.QModelIndex()):
        return len(self.parm_names)

    def columnCount(self, idx=QtCore.QModelIndex()):
        return 2

    def headerData(self, section, orientation, role=Qt.DisplayRole):
        if role != Qt.DisplayRole:
            return
        if orientation == Qt.Horizontal:
            if section == 0:
                return "Name"
            elif section == 1:
                return "Value"

    def flags(self, index):
        if index.column() == 0:
            return Qt.ItemIsEnabled
        elif index.column() == 1:
            return Qt.ItemIsEnabled
        return Qt.NoItemFlags

    def data(self, index, role=Qt.DisplayRole):
        r = index.row()
        c = index.column()
        if 0 <= r < len(self.parm_names) and 0 <= c < 2:
            if c == 0:
                if role == Qt.DisplayRole:
                    return self.parm_names[r]
            elif c == 1:
                if role == Qt.DisplayRole:
                    return "%g" % (self.parm_values[r],)
                elif role == Qt.EditRole:
                    return "%g" % (self.parm_values[r],)

class MainWindow(QtGui.QDialog):
    def __init__(self, *args, **kwords):
        QtGui.QDialog.__init__(self, *args, **kwords)
        p = (path(__file__).dirname() / 'epipy_gui.ui').abspath()
        uic.loadUi(p, self)
        self.validator = QtGui.QDoubleValidator()
        self.init()
        
    def init(self):
        self._inputParameters = None
        self._ouputParameters = None
        self._data = None
        self._fieldX = None
        self._fieldY = None
        self._xdata = None
        self._ydata = None
        self._model = None
        self._modelObject = None
        self._input = None   # input file name
        self._output = None  # output file name
        self._fittingInfo = None
        #self._scale = None
        self._header = None
        self._write = False
        self._formatDate = False
        self.setData(None, None)
        list_model = sorted(epipy.model.names())
        self.models.clear()
        self.models.addItems(list_model)
        self.models.setCurrentIndex(list_model.index("sir"))
        self.updateParameters(list_model.index("sir"))
        self.models.currentIndexChanged.connect(self.updateParameters)
        
        self.fitButton.clicked.connect(self.updateFit)

        # Default graph
        self.graph = pg.PlotWidget(title="Graph of Fit", enableMenu=False)
        self.verticalLayout_1.insertWidget(0, self.graph)
        header = ["Time", "I"]
        data = {"Time": np.array([0, 7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98, 105, 112, 119, 126, 133, 140, 147, 154,
                    161], dtype=float),
                    "I": np.array([113, 60, 70, 140, 385, 2900, 4600, 5400, 5300, 6350, 5350, 4400, 3570, 2300,
                                        1900, 2200, 1700, 1170, 830, 750, 770, 520, 550, 380], dtype=float)}
        self.setData(header, data)
        self.updateFit()
        
    @pyqtSignature("")
    def on_selectInputFile_clicked(self):
        filename = QtGui.QFileDialog.getOpenFileName(self, "Open CSV file",
                                                     filter="CSV file (*.csv);;All Files (*.*)")
        if filename:
            self.input = filename
            
    @pyqtSignature("")
    def on_selectOutputFile_clicked(self):
        filename = QtGui.QFileDialog.getSaveFileName(self, "Save CSV file",
                                                     filter="CSV file (*.csv);;All Files (*.*)")
        if filename:
            self.output = filename

    @pyqtSignature("const QString&")
    def on_fieldXbox_currentIndexChanged(self, txt):
        self.fieldX = txt

    @pyqtSignature("const QString&")
    def on_fieldYbox_currentIndexChanged(self, txt):
        self.fieldY = txt
    
    
    @pyqtSignature("const QString&")
    def on_inputFile_textChanged(self, txt):
        txt = path(txt)
        self.input = txt

    def _getInput(self):
        return self._input

    def _setInput(self, txt):
        txt = path(txt)
        if txt != self._input and txt.isfile():
            try:
                data = None
                header = None
                
                data = csvmanager.read(file_name=txt, seperator=";")
                header = data.keys()                
                
                if data is not None:
                    self._input = txt
                    print("input: {}".format(self._input))
                    if self._input != self.inputFile.text():
                        self.inputFile.setText(self._input)
                    self.setData(header, data)
                    
            except IOError:
                pass
                
    input = property(_getInput, _setInput)

    @pyqtSignature("bool")
    def on_formatDate_toggled(self):
        if self.formatDate.isChecked():
            self._formatDate = True
        else:
            self._formatDate = False
    
    def setData(self, header, data):
        if header is None or data is None:
            self._header = None
            self._data = None
            self.inputParameters.setModel(None)
            self.input_param_model = None
        else:
            self._header = header
            self._data = data
            self.fieldXbox.clear()
            self.fieldXbox.addItems(self._header)
            self.fieldYbox.clear()
            self.fieldYbox.addItems(self._header)
            self.fieldX = self._header[0]
            self.fieldY = self._header[1]

    def _getOutput(self):
        return self._output

    def _setOutput(self, txt):
        txt = path(txt)
        if self._output != txt:
            if txt and not txt.endswith(".csv"):
                txt += ".csv"
            self._output = txt
            if self._output != self.outputFile.text():
                self.outputFile.setText(self._output)
                
    output = property(_getOutput, _setOutput)

    def _getHeader(self):
        return self._header
        
    header = property(_getHeader)

    def _getFieldX(self):
        return self._fieldX

    def _setFieldX(self, txt):
        if txt != self._fieldX and txt in self.header:
            self._fieldX = txt
            if txt != self.fieldXbox.currentText():
                self.fieldXbox.setCurrentIndex(self.fieldXbox.findText(txt))
    
    fieldX = property(_getFieldX, _setFieldX)

    def _getFieldY(self):
        return self._fieldY

    def _setFieldY(self, txt):
        if txt != self._fieldY and txt in self.header:
            self._fieldY = txt
            if txt != self.fieldYbox.currentText():
                self.fieldYbox.setCurrentIndex(self.fieldYbox.findText(txt))

    fieldY = property(_getFieldY, _setFieldY)

    def updateParameters(self, i):
        self._model = str(self.models.itemText(i))
        print("New model: {}".format(self._model))
        mod = __import__('epipy.model', fromlist=[self._model])
        self._modelObject = getattr(mod, self._model)
        if self._modelObject is not None:
            self.input_param_model = ParametersModel(self._modelObject, parent=self)
            self.inputParameters.setModel(self.input_param_model)
            
    def updateFit(self):
        if self._data is None:
            QMessageBox.critical(self, "Error plotting", "Error, you don't have any data loaded")
        else:
            model = self._modelObject
            param_model = self.input_param_model
            xdata0 = self._data[str(self._fieldX)]
            ydata0 = self._data[str(self._fieldY)]

            if self._formatDate:
                xdata0 = dateconverter.convert(xdata0)

            xdata = array(xdata0, dtype=int)
            ydata = array(ydata0, dtype=float)
            print xdata
            print ydata

            fitted, param, rsquared, pvalue = model.Simple().fit(xdata, ydata, 1)
            self._fittingInfo = dict(zip(model.Simple().param(), param.tolist()))
            self._fittingInfo["R squared"] = rsquared 
            self._fittingInfo["P-value"] = pvalue
            self.updateInfo()

            self.graph.clear()
            self.graph.plot(x=xdata, y=ydata, symbol='o')
            self.graph.plot(x=xdata, y=fitted, pen="k")
            self.graph.setWindowTitle('pyqtgraph')
            self.graph.setBackground(QtGui.QColor(255, 255, 255))

    def updateInfo(self):
        if self._fittingInfo is not None:
            self.info_model = InformationModel(self._fittingInfo, parent=self)
            self.information.setModel(self.info_model)
            

def main():
    wnd = MainWindow()
    wnd.show()
    wnd.raise_()
    return wnd

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    wnd = main()
    app.exec_()