# -*- coding: utf-8 -*-

import numpy as np
import os
import pyqtgraph as pg
from PyQt4 import uic, QtCore, QtGui

from epipy.ui.customviewbox import CustomViewBox
from epipy.model import sir
from epipy.utils import csvmanager
from epipy.utils import logger

from epipy.ui.optionsgroupbox import OptionsGroupBox
from epipy.ui.infogroupbox import InfoGroupBox
from epipy.ui.aboutdialog import AboutDialog

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
        self.openFileAction.triggered.connect(self.open_file)
        self.saveAction.triggered.connect(self.save)
        self.saveAsAction.triggered.connect(self.save_as)
        self.exportAction.triggered.connect(self.export)
        self.exitAction.triggered.connect(self.close)
        self.showFullscreenAction.triggered.connect(self.show_fullscreen)
        self.exitFullscreenAction.triggered.connect(self.exit_fullscreen)
        self.exitFullscreenAction.setVisible(False)
        self.showSidebarAction.triggered.connect(self.show_sidebar)
        self.hideSidebarAction.triggered.connect(self.hide_sidebar)
        self.showSidebarAction.setVisible(False)
        self.aboutAction.triggered.connect(self.show_about)

        # ===================
        # blank plot
        self.pw = pg.PlotWidget(title="", viewBox=CustomViewBox(), enableMenu=False)
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
        self.showFullscreenAction.setVisible(False)
        self.exitFullscreenAction.setVisible(True)
        self.showFullScreen()

    def exit_fullscreen(self):
        self.showFullscreenAction.setVisible(True)
        self.exitFullscreenAction.setVisible(False)
        self.showNormal()

    def show_sidebar(self):
        self.side_bar_widget.setVisible(True)
        self.showSidebarAction.setVisible(False)
        self.hideSidebarAction.setVisible(True)

    def hide_sidebar(self):
        self.side_bar_widget.setVisible(False)
        self.showSidebarAction.setVisible(True)
        self.hideSidebarAction.setVisible(False)

    def show_about(self):
        self.about_dialog.show()

    def plot(self, xdata, ydata, fitdata, title):
        self.pw = pg.PlotWidget(title=title, viewBox=CustomViewBox(), enableMenu=False)
        self.pw.plot(x=xdata, y=ydata, symbol='o')
        self.pw.plot(x=xdata, y=fitdata, pen="k")
        self.pw.setBackground(QtGui.QColor(255, 255, 255))
        self.splitter.insertWidget(0, pw)
