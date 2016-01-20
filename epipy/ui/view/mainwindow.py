# -*- coding: utf-8 -*-

import os
import pyqtgraph as pg
from PyQt4 import uic, QtGui

from epipy.ui.model.mainmodel import Event
from epipy.ui.view.aboutdialog import AboutDialog
from epipy.ui.view.customviewbox import CustomViewBox
from epipy.ui.view.infogroupbox import InfoGroupBox
from epipy.ui.view.inputgroupbox import InputGroupBox
from epipy.ui.view.optionsgroupbox import OptionsGroupBox

dir_name = os.path.dirname
folder_path = os.path.join(dir_name(__file__), '')
MainWindowUI, MainWindowBase = uic.loadUiType(os.path.join(folder_path, "mainwindow.ui"))


class MainWindow(MainWindowBase, MainWindowUI):
    def __init__(self, controller):
        MainWindowBase.__init__(self)
        self.setupUi(self)
        self.controller = controller

        controller.attach(self)

        # Bottom
        self.info_group_box = InfoGroupBox(self.controller)
        self.v_splitter.insertWidget(1, self.info_group_box)

        # Side Bar
        self.input_group_box = InputGroupBox(self.controller)
        self.options_group_box = OptionsGroupBox(self.controller)
        self.side_bar_widget.layout().addWidget(self.input_group_box)
        self.side_bar_widget.layout().addWidget(self.options_group_box)
        self.spacer = QtGui.QSpacerItem(0, 0, 0, QtGui.QSizePolicy.Expanding)
        self.side_bar_widget.layout().addItem(self.spacer)

        # Side Bar Bottom
        self.side_bar_bottom_widget = QtGui.QWidget(self.side_bar_widget)
        self.side_bar_bottom_layout = QtGui.QHBoxLayout(self.side_bar_bottom_widget)
        self.spacer = QtGui.QSpacerItem(0, 0, QtGui.QSizePolicy.Expanding, 0)
        self.side_bar_bottom_layout.addSpacerItem(self.spacer)
        self.fit_btn = QtGui.QPushButton('Fit')
        self.fit_btn.clicked.connect(self.controller.fit_data)
        self.fit_btn.setEnabled(False)
        self.side_bar_bottom_layout.addWidget(self.fit_btn)
        self.reset_btn = QtGui.QPushButton('Reset')
        # connect RESET Button
        self.side_bar_bottom_layout.addWidget(self.reset_btn)
        self.reset_btn.clicked.connect(self.controller.reset_data)
        self.side_bar_widget.layout().addWidget(self.side_bar_bottom_widget)

        self.about_dialog = AboutDialog()
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
        self.about_action.triggered.connect(self.about_dialog.show)

        # ===================
        # plot widget
        self.custom_view_box = CustomViewBox()
        self.pw = pg.PlotWidget(viewBox=self.custom_view_box, enableMenu=False)
        self.h_splitter.insertWidget(0, self.pw)
        self.pw.setBackground(QtGui.QColor(255, 255, 255))
        self.plot_1 = self.pw.plot(symbol='o')
        self.plot_2 = self.pw.plot(pen="b")
        legend1 = pg.LegendItem()
        legend1.addItem(self.plot_1, "Data")
        legend1.addItem(self.plot_2, "Fit")
        legend1.setParentItem(self.custom_view_box)
        legend1.anchor((0, 0), (0.4, 0))
        # ===================

    def open_file(self):
        pass

    def save(self):
        pass

    def save_as(self):
        pass

    def export(self):
        pass

    def show_fullscreen(self):
        self.show_fullscreen_action.setVisible(False)
        self.exit_fullscreen_action.setVisible(True)
        self.showFullScreen()

    def exit_fullscreen(self):
        self.show_fullscreen_action.setVisible(True)
        self.exit_fullscreen_action.setVisible(False)
        self.showNormal()

    def show_sidebar(self):
        self.h_splitter.widget(1).setVisible(True)
        self.show_sidebar_action.setVisible(False)
        self.hide_sidebar_action.setVisible(True)

    def hide_sidebar(self):
        self.h_splitter.widget(1).setVisible(False)
        self.show_sidebar_action.setVisible(True)
        self.hide_sidebar_action.setVisible(False)

    def update(self, event):
        if event == Event.ENABLE_FIT_BUTTON:
            self.fit_btn.setEnabled(True)
        elif event == Event.DISABLE_FIT_BUTTON and self.fit_btn.isEnabled():
            self.fit_btn.setEnabled(False)
        elif event == Event.PLOT:
            file_data, fitted_data = self.controller.get_plot_data()
            self.plot_1.setData(**file_data)
            self.plot_2.setData(**fitted_data)
