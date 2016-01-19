# -*- coding: utf-8 -*-

import os
import pyqtgraph as pg
from PyQt4 import uic, QtGui

from epipy.ui.view.aboutdialog import AboutDialog
from epipy.ui.view.customviewbox import CustomViewBox
from epipy.ui.view.infogroupbox import InfoGroupBox
from epipy.ui.view.optionsgroupbox import OptionsGroupBox

dir_name = os.path.dirname
folder_path = os.path.join(dir_name(__file__), '')
MainWindowUI, MainWindowBase = uic.loadUiType(os.path.join(folder_path, "mainwindow.ui"))


class MainWindow(MainWindowBase, MainWindowUI):
    def __init__(self):
        MainWindowBase.__init__(self)
        self.setupUi(self)
        self.current_model_gb = None
        self.current_advanced_dialog = None
        # some components
        self.about_dialog = AboutDialog()

        # ===================
        # plot widget
        self.custom_view_box = CustomViewBox()
        self.pw = pg.PlotWidget(viewBox=self.custom_view_box, enableMenu=False)
        self.splitter.insertWidget(0, self.pw)
        self.pw.setBackground(QtGui.QColor(255, 255, 255))
        self.plot_1 = self.pw.plot(symbol='o')
        self.plot_2 = self.pw.plot(pen='b')
        legend1 = pg.LegendItem()
        legend1.addItem(self.plot_1, "Data")
        legend1.addItem(self.plot_2, "Fit")
        legend1.setParentItem(self.custom_view_box)
        legend1.anchor((0, 0), (0.4, 0))
        # ===================
        # side bar
        self.options_group_box = OptionsGroupBox()
        self.side_bar_widget.layout().addWidget(self.options_group_box)

        self.info_group_box = InfoGroupBox()

        self.side_bar_widget.layout().addWidget(self.options_group_box)
        self.side_bar_widget.layout().addWidget(self.info_group_box)
        self.splitter.insertWidget(1, self.side_bar_widget)
