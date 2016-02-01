# -*- coding: utf-8 -*-

import os
from PyQt4 import uic

from epipy.ui.controller.event import Event
from epipy.ui.controller.sidebarviewcontroller import SideBarController
from epipy.ui.view.aboutdialog import AboutDialog
from epipy.ui.view.helpwidget import HelpWidget
from epipy.ui.view.infogroupbox import InfoGroupBox
from epipy.ui.view.plotview import PlotView
from epipy.ui.view.sidebarwidget import SideBarWidget

dir_name = os.path.dirname
folder_path = os.path.join(dir_name(__file__), '')
MainWindowUI, MainWindowBase = uic.loadUiType(os.path.join(folder_path, "mainwindow.ui"))


class MainWindow(MainWindowBase, MainWindowUI):
    def __init__(self, controller):
        MainWindowBase.__init__(self)
        self.setupUi(self)
        self.controller = controller
        self.controller.attach(self)
        self.controller_service = self.controller.get_controller_service()

        # Menu
        self.about_dialog = AboutDialog()
        self.help_view = HelpWidget()
        self.exit_action.triggered.connect(self.close)
        self.show_fullscreen_action.triggered.connect(self.show_fullscreen)
        self.exit_fullscreen_action.triggered.connect(self.exit_fullscreen)
        self.exit_fullscreen_action.setVisible(False)
        self.show_sidebar_action.triggered.connect(self.show_sidebar)
        self.hide_sidebar_action.triggered.connect(self.hide_sidebar)
        self.show_sidebar_action.setVisible(False)
        self.clear_information_action.triggered.connect(self.controller.clear_information)
        self.help_action.triggered.connect(self.help_view.show)
        self.about_action.triggered.connect(self.about_dialog.show)

        # Top Left
        self.plot_view = PlotView(self)
        self.h_splitter.insertWidget(0, self.plot_view)

        # Top Right
        self.side_bar_controller = SideBarController(self.controller_service)
        self.side_bar = SideBarWidget(self.side_bar_controller)
        self.h_splitter.insertWidget(1, self.side_bar)

        # Bottom
        self.info_group_box = InfoGroupBox(self.controller)
        self.v_splitter.insertWidget(1, self.info_group_box)

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
        if event == Event.PLOT:
            file_data, fitted_data, forecast_data = self.side_bar_controller.get_plot_data()
            self.plot_view.plot(file_data, fitted_data, forecast_data)
            self.controller.set_side_bar_model(self.side_bar_controller.get_model())
