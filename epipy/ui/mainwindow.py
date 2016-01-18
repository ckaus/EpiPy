# -*- coding: utf-8 -*-

import numpy as np
import os
import pyqtgraph as pg
from PyQt4 import uic, QtGui

from epipy.ui.aboutdialog import AboutDialog
from epipy.ui.customviewbox import CustomViewBox
from epipy.ui.infogroupbox import InfoGroupBox
from epipy.ui.optionsgroupbox import OptionsGroupBox
from epipy.utils import logger

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
        # Data 1
        # ======================
        # data_set_1 = csvmanager.read(file_name="data1.csv", seperator=";", column=["Time", "I"])
        # ydata_1 = np.array(data_set_1["I"], dtype=float)
        # xdata_1 = np.array(data_set_1["Time"], dtype=float)
        # result_1 = sir.Simple().fit(xdata=xdata_1, ydata=ydata_1, N=1)
        # ======================
        # Data 2
        # ======================
        xdata_2 = np.array([0, 7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98, 105, 112, 119, 126, 133, 140,
                            147, 154, 161], dtype=float)

        ydata_2 = np.array([113, 60, 70, 140, 385, 2900, 4600, 5400, 5300, 6350, 5350, 4400, 3570, 2300, 1900, 2200,
                            1700, 1170, 830, 750, 770, 520, 550, 380], dtype=float)
        # ======================

        data_set_2 = {'Time': xdata_2, 'I': ydata_2}

        ydata_2 = np.array(data_set_2["I"], dtype=float)
        xdata_2 = np.array(data_set_2["Time"], dtype=float)
        population = 10000
        self.current_data_set = xdata_2, ydata_2, population
        # ===================
        # plot widget
        custom_view_box = CustomViewBox()
        pw = pg.PlotWidget(viewBox=custom_view_box, enableMenu=False)
        self.splitter.insertWidget(0, pw)
        pw.setBackground(QtGui.QColor(255, 255, 255))
        self.plot_1 = pw.plot(symbol='o')
        self.plot_2 = pw.plot(pen='b')
        legend1 = pg.LegendItem()
        legend1.addItem(self.plot_1, "Data")
        legend1.addItem(self.plot_2, "Fit")
        legend1.setParentItem(custom_view_box)
        legend1.anchor((0, 0), (0.4, 0))

        # ===================
        # side bar
        self.options_group_box = OptionsGroupBox(self)
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

    def fit(self, **param):
        xdata = self.current_data_set[0]
        ydata = self.current_data_set[1]
        population = self.current_data_set[2]
        result = self.options_group_box.model.fit(xdata, ydata, N=population, **param)
        self.update_plot(ydata, result)

    def update_plot(self, ydata, fit_data):
        self.plot_1.setData(x=self.current_data_set[0], y=self.current_data_set[1])
        self.plot_2.setData(x=self.current_data_set[0], y=fit_data)

    def update_parameters(self, param):
        # SIR Simple beta=0.13577472  gamma=0.02448539
        self.fit(**param)
