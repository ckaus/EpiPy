# -*- coding: utf-8 -*-

import os
import numpy as np
import pyqtgraph as pg
from PyQt4 import uic, QtGui

from epipy.ui.aboutdialog import AboutDialog
from epipy.ui.customviewbox import CustomViewBox
from epipy.ui.infogroupbox import InfoGroupBox
from epipy.ui.optionsgroupbox import OptionsGroupBox
from epipy.utils import logger
from epipy.model import sir
from epipy.utils import csvmanager

dir_name = os.path.dirname
folder_path = os.path.join(dir_name(dir_name(__file__)), 'resources/ui')
MainWindowUI, MainWindowBase = uic.loadUiType(os.path.join(folder_path, "mainwindow.ui"))


class MainWindow(MainWindowBase, MainWindowUI):
    def __init__(self):
        MainWindowBase.__init__(self)
        self.setupUi(self)
        self.current_model_gb = None
        self.current_advanced_dialog = None

        # some components
        self.about_dialog = AboutDialog()

        # ==================
        # menu
        self.open_file_action.triggered.connect(self.open_file)
        self.save_action.triggered.connect(self.save)
        self.save_as_action.triggered.connect(self.save_as)
        self.export_action.triggered.connect(self.export)
        self.exit_action.triggered.connect(self.close)
        self.show_fullscreen_action.triggered.connect(self.show_fullscreen)
        self.exit_fullscreen_action.triggered.connect(self.exit_fullscreen)
        self.exit_fullscreen_action.setVisible(False)
        self.show_sidebar_action.triggered.connect(self.show_sidebar)
        self.hide_sidebar_action.triggered.connect(self.hide_sidebar)
        self.show_sidebar_action.setVisible(False)
        self.about_action.triggered.connect(self.show_about)

        # ===================
        # sample plot
        # ======================
        # data_set_1 = csvmanager.read(file_name="data1.csv", seperator=";", column=["Time", "I"])
        # ======================
        xdata_2 = np.array([0, 7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98, 105, 112, 119, 126, 133, 140,
                            147, 154, 161], dtype=float)

        ydata_2 = np.array([113, 60, 70, 140, 385, 2900, 4600, 5400, 5300, 6350, 5350, 4400, 3570, 2300, 1900, 2200,
                            1700, 1170, 830, 750, 770, 520, 550, 380], dtype=float)
        # ======================

        data_set_2 = {'Time': xdata_2 , 'I': ydata_2}

        ydata = np.array(data_set_2["I"], dtype=float)
        xdata = np.array(data_set_2["Time"], dtype=float)
        result = sir.Simple().fit(xdata=xdata, ydata=ydata, N=10000)

        cv = CustomViewBox()
        self.pw = pg.PlotWidget(title="SIR", viewBox=cv, enableMenu=False)
        self.pw.setBackground(QtGui.QColor(255, 255, 255))

        plot_1 = self.pw.plot(x=xdata, y=ydata, symbol='o')
        plot_2 = self.pw.plot(x=xdata, y=result, pen='b')
        legend1 = pg.LegendItem()
        legend1.addItem(plot_1, "Data")
        legend1.addItem(plot_2, "Fit")
        legend1.setParentItem(cv)
        legend1.anchor((0, 0), (0.4, 0))

        self.pw.setBackground(QtGui.QColor(255, 255, 255))
        self.splitter.insertWidget(0, self.pw)

        # ===================
        # side bar
        self.options_group_box = OptionsGroupBox()
        self.info_group_box = InfoGroupBox()

        self.side_bar_widget.layout().addWidget(self.options_group_box)
        self.side_bar_widget.layout().addWidget(self.info_group_box)
        self.splitter.insertWidget(1, self.side_bar_widget)

    def open_file(self):
        logger.info("open file")
        self.info_group_box.info_plain_text_edit.appendPlainText("open file")

    def save(self):
        logger.info("save")
        self.info_group_box.info_plain_text_edit.appendPlainText("save")

    def save_as(self):
        logger.info("save as")
        self.info_group_box.info_plain_text_edit.appendPlainText("save as")

    def export(self):
        logger.info("export")
        self.info_group_box.info_plain_text_edit.appendPlainText("export")

    def show_fullscreen(self):
        self.show_fullscreen_action.setVisible(False)
        self.exit_fullscreen_action.setVisible(True)
        self.showFullScreen()

    def exit_fullscreen(self):
        self.show_fullscreen_action.setVisible(True)
        self.exit_fullscreen_action.setVisible(False)
        self.showNormal()

    def show_sidebar(self):
        self.side_bar_widget.setVisible(True)
        self.show_sidebar_action.setVisible(False)
        self.hide_sidebar_action.setVisible(True)

    def hide_sidebar(self):
        self.side_bar_widget.setVisible(False)
        self.show_sidebar_action.setVisible(True)
        self.hide_sidebar_action.setVisible(False)

    def show_about(self):
        self.about_dialog.show()

    def plot(self, xdata, ydata, fit_data, title):
        self.pw = pg.PlotWidget(title=title, viewBox=CustomViewBox(), enableMenu=False)
        self.pw.plot(x=xdata, y=ydata, symbol='o')
        self.pw.plot(x=xdata, y=fit_data, pen="k")
        self.pw.setBackground(QtGui.QColor(255, 255, 255))
        self.splitter.insertWidget(0, self.pw)
